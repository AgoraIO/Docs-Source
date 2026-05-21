import re #Regular expressions
import os #Operating system
import shutil #Copy images
import argparse
import sys
import json
import yaml
import urllib.parse
import textwrap
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString

# Default value
platform = 'android'

# Create an ArgumentParser object
parser = argparse.ArgumentParser()
# Add named arguments
parser.add_argument('--platform', type=str, help='Target platform: android|electron|flutter|ios|macos|react-native|unity|web|windows')
parser.add_argument('--product', type=str, help='Agora product: video-calling|interactive-live-streaming|etc.')
parser.add_argument('--mdxPath', type=str, help='The absolute path to the mdx file')
parser.add_argument('--output-file', type=str, help='Explicit output filename (including .md)')
parser.add_argument('--docs-folder', type=str, help='Path to the Docs root folder')
parser.add_argument(
    '--images-dir',
    default=None,
    help='Directory to copy images into (default: output/images next to --output-file)'
)

# Access the values of the named arguments
args = parser.parse_args()
platform = args.platform if args.platform is not None else platform
product = args.product
mdxPath = args.mdxPath

# Get the Docs repository path
if mdxPath is None:
    print('usage: mdx2md.py [-h] [--platform PLATFORM] [--product PRODUCT] [--mdxPath MDXPATH]')
    sys.exit(-1)
docs_index = mdxPath.find(os.path.sep + 'docs')
if docs_index >= 0:
    repoPath = mdxPath[:docs_index]
else:
    print('Invalid mdx path!')
    sys.exit(-2)

siteBaseUrl = "https://docs.agora.io/en"
docsPath = repoPath + "/docs"
assetsPath = docsPath + "/assets"

if product is None:
    # Get the product name from the path
    dirname = os.path.dirname(mdxPath)
    # Normalize path separators to handle mixed separators
    dirname = dirname.replace('/', os.path.sep)
    # Split the directory path into parts
    parts = dirname.split(os.path.sep)
    # Find the index of the "docs" or "docs-help" folder
    try:
        if "docs-help" in parts:
            docs_index = parts.index("docs-help")
            # For help files, set a generic product name or skip product logic
            product = "help"  # or you could set product = None and handle it later
        else:
            docs_index = parts.index("docs")
            # product name is the name of the docs sub-folder
            if docs_index + 1 < len(parts):
                product = parts[docs_index + 1]
            else:
                print("Error: No product folder found after 'docs'")
                sys.exit(-4)
    except ValueError:
        print("Error: Neither 'docs' nor 'docs-help' folder found in path")
        print(f"Available parts: {parts}")
        sys.exit(-5)

# ----- Helper functions -------

def normalize_wrapper_attributes(text):
    """
    Normalize JSX array syntax in PlatformWrapper and ProductWrapper attributes
    to simple quoted strings before processing.
    
    Converts:
        platform={["ios","macos"]}  ->  platform="ios,macos"
        platform={['ios','macos']}  ->  platform="ios,macos"
        notAllowed={["web"]}        ->  notAllowed="web"
    """
    def strip_array_syntax(match):
        attr_name = match.group(1)
        values = match.group(2)
        # Remove all inner quotes and whitespace, then rejoin with comma
        cleaned = re.sub(r'[\'"\s]', '', values)
        return f'{attr_name}="{cleaned}"'
    
    # Match platform={[...]} or notAllowed={[...]} with any quote style inside
    pattern = re.compile(r'(platform|notAllowed)=\{?\[([^\]]+)\]\}?')
    return pattern.sub(strip_array_syntax, text)

# Functions to recursively resolve variables in global.js to create a dictionary
def read_variables(file_path):
    variables = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(r'export const (\w+)\s*=\s*(.+?)(?:;|$)', line)
            if match:
                variable_name, variable_value = match.groups()
                variables[variable_name] = variable_value.strip().strip("'\"`")
    return resolve_variables(variables)

def resolve_variables(variables):
    resolved_variables = {}
    for variable_name, variable_value in variables.items():
        resolved_value = resolve_value(variable_value, variables)
        resolved_variables[variable_name] = resolved_value
    return resolved_variables

def resolve_value(value, variables):
    match = re.search(r'\$\{(\w+)\}', value)
    while match:
        variable_name = match.group(1)
        variable_value = variables.get(variable_name, '')
        value = value.replace(f'${{{variable_name}}}', variable_value)
        match = re.search(r'\$\{(\w+)\}', value)
    return value

def load_product_platforms(products_file):
    """Parse products.js and return { productId: [platforms...] }"""
    with open(products_file, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r"id:\s*'([^']+)'.*?platforms:\s*{[^}]*latest:\s*\[([^\]]*)\]", re.DOTALL)
    mapping = {}
    for match in pattern.finditer(content):
        product_id = match.group(1)
        platforms_str = match.group(2)
        platforms = re.findall(r"'([^']+)'", platforms_str)
        mapping[product_id] = platforms
    return mapping

# Improved createDictionary function that handles JavaScript comments
def createDictionary(path):
    with open(path, 'r', encoding='utf-8') as f:
        data_file = f.read()

    # Extract the data from the file using regular expressions
    data_str = re.search(r'const data = {(.*?)};', data_file, re.DOTALL).group(1)
    data_str = '{' + data_str + '}'
    
    # Remove JavaScript comments before processing
    # Remove single-line comments (//)
    data_str = re.sub(r'//.*?$', '', data_str, flags=re.MULTILINE)
    # Remove multi-line comments (/* */)
    data_str = re.sub(r'/\*.*?\*/', '', data_str, flags=re.DOTALL)
    
    # Add quotes around keys (unquoted keys)
    data_str = re.sub(r'([A-Z_]+):', r'"\1":', data_str)
    
    # Convert single quotes to double quotes for JSON compatibility
    data_str = data_str.replace("'", '"')
    
    # Handle trailing commas (JSON doesn't allow them)
    data_str = re.sub(r',\s*}', '}', data_str)
    data_str = re.sub(r',\s*]', ']', data_str)
    
    try:
        # Parse as JSON (safer than eval)
        data = json.loads(data_str)
    except json.JSONDecodeError as e:
        print(f"Error parsing data from {path}: {e}")
        print(f"Problematic string portion: {data_str[max(0, e.pos-50):min(len(data_str), e.pos+50)]}")
        # Fallback to eval if JSON parsing fails (less safe but more flexible)
        try:
            import ast
            data = ast.literal_eval(data_str)
        except (ValueError, SyntaxError) as eval_error:
            print(f"Also failed with ast.literal_eval: {eval_error}")
            raise
    
    return data

def remove_react_comments(text):
    """
    Remove React-style comments {/* ... */} from MDX content.
    Handles both single-line and multi-line comments.
    """
    # Pattern to match {/* ... */} comments
    # Uses non-greedy matching to handle multiple comments on same line
    react_comment_pattern = re.compile(r'\{\s*/\*.*?\*/\s*\}', re.DOTALL)
    
    # Remove all React comments
    cleaned_text = react_comment_pattern.sub('', text)
    
    # Clean up any extra whitespace left behind
    # Remove empty lines that might have been created
    cleaned_text = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned_text)
    
    return cleaned_text

# Use the product and platform dictionaries to resolve <Vpd> and <Vpl> tags
def resolve_local_variables(text, product, productDictionary, platform, platformDictionary):
    text = re.sub(r'<Vpd\s+k="(\w+)"\s*/>', lambda match: productDictionary[product].get(match.group(1), match.group(0)), text)
    text = re.sub(r'<Vpl\s+k="(\w+)"\s*/>', lambda match: platformDictionary[platform].get(match.group(1), match.group(0)), text)
    return text

# ===== EXTRACTED HELPER FUNCTIONS FOR PARAMETER LIST PROCESSING =====
# These functions are used by both standalone ParameterList and RestAPILayout

def normalize_tags_for_parsing(content):
    """Convert tag names to lowercase for BeautifulSoup parsing"""
    tag_mappings = {
        'LeftColumn': 'leftcolumn',
        'RightColumn': 'rightcolumn',
        'ParameterList': 'parameterlist',
        'Parameter': 'parameter', 
        'PathParameter': 'pathparameter',
        'Section': 'section',
        'Tabs': 'tabs',
        'TabItem': 'tabitem'
    }
    
    for original, normalized in tag_mappings.items():
        content = re.sub(f'<{original}(\\s[^>]*?)?>', f'<{normalized}\\1>', content)
        content = re.sub(f'</{original}>', f'</{normalized}>', content)
    
    return content


def process_list_element(list_element):
    """Convert HTML lists to markdown format with proper spacing"""
    items = []
    for li in list_element.find_all('li', recursive=False):  # Only direct children
        item_text = li.get_text(strip=True)
        items.append(f"    - {item_text}")  # 4 spaces for proper indentation
    
    if items:
        return '\n' + '\n'.join(items)  # Start with newline, separate each item
    return ''


def process_mixed_content_with_lists(element):
    """Process elements that contain both text and lists"""
    result_parts = []
    
    for child in element.children:
        if isinstance(child, NavigableString):
            text = str(child).strip()
            if text:
                result_parts.append(text)
        elif isinstance(child, type(element)):  # Tag type
            if child.name in ['ul', 'ol']:
                list_content = process_list_element(child)
                result_parts.append(list_content)
            else:
                child_text = child.get_text(strip=True)
                if child_text:
                    result_parts.append(child_text)
    
    return ' '.join(result_parts)


def get_element_text_content(element):
    """Get all text content from element, including nested tags"""
    if isinstance(element, NavigableString):
        return str(element).strip()
    elif hasattr(element, 'name'):  # Tag object
        if element.name in ['ul', 'ol']:
            return process_list_element(element)
        elif element.name == 'li':
            # Handle individual list items
            return f"- {element.get_text(strip=True)}"
        else:
            # For other elements, check if they contain lists
            if element.find(['ul', 'ol']):
                return process_mixed_content_with_lists(element)
            else:
                return element.get_text(strip=True)
    else:
        return ''


def get_direct_text_content(param_element):
    """Get text content directly under element, excluding nested parameter tags"""
    text_parts = []
    
    for child in param_element.children:
        if isinstance(child, NavigableString):
            text_content = str(child).strip()
            if text_content:
                text_parts.append(text_content)
        elif hasattr(child, 'name') and child.name != 'parameter':  # Tag object, not a parameter
            if child.name in ['ul', 'ol']:
                # Process list specially for parameter descriptions
                list_content = process_list_element(child)
                if list_content:
                    text_parts.append(list_content)
            else:
                # Handle other tags normally
                child_text = get_element_text_content(child)
                if child_text:
                    text_parts.append(child_text)
    
    return ''.join(text_parts).strip()


def process_parameter_recursively(param_element, indent_level):
    """Recursively process Parameter elements maintaining hierarchy"""
    result_lines = []
    indent = '  ' * indent_level
    
    # Extract parameter attributes
    name = param_element.get('name', 'unknown')
    param_type = param_element.get('type', 'string')
    possible_values = param_element.get('possiblevalues', param_element.get('possibleValues'))
    
    # Get description (text content that's not in nested parameter tags)
    description = get_direct_text_content(param_element)
    
    # Build parameter type info with possible values if present
    type_info = f"({param_type}"
    if possible_values:
        # Split values and wrap each in backticks
        values_list = [f"`{val.strip()}`" for val in possible_values.split(',')]
        values_str = ', '.join(values_list)
        type_info += f", possible values: {values_str}"
    type_info += ")"
    
    # Build parameter line
    param_line = f"{indent}- **{name}** {type_info}: {description}"
    result_lines.append(param_line)
    
    # Process nested parameters
    nested_params = param_element.find_all('parameter', recursive=False)
    for nested_param in nested_params:
        nested_lines = process_parameter_recursively(nested_param, indent_level + 1)
        result_lines.extend(nested_lines)
    
    return result_lines

# ===== END OF EXTRACTED HELPER FUNCTIONS =====


def resolve_parameter_list(text):
    """
    Convert standalone ParameterList components to structured markdown.
    Handles ParameterList both inside and outside RestAPILayout.
    Uses BeautifulSoup for reliable parsing of nested structures.
    """
    try:
        from bs4 import BeautifulSoup, NavigableString, Tag
    except ImportError:
        print("Warning: BeautifulSoup not available for ParameterList processing")
        return text
    
    # Pattern to match ParameterList components
    parameterlist_pattern = re.compile(
        r'<ParameterList\s*([^>]*?)>(.*?)</ParameterList>',
        re.MULTILINE | re.DOTALL
    )
    
    def process_parameterlist(match):
        attributes_str = match.group(1)
        content = match.group(2).strip()
        
        # Normalize tags for parsing
        normalized_content = normalize_tags_for_parsing(content)
        wrapped_content = f"<root>{normalized_content}</root>"
        
        try:
            soup = BeautifulSoup(wrapped_content, 'html.parser')
            result_parts = []
            
            # Add title if present in attributes
            title_match = re.search(r'title\s*=\s*["\']([^"\']+)["\']', attributes_str)
            if title_match:
                result_parts.append(f"**{title_match.group(1)}**")
                result_parts.append('')
            
            # Process all parameter elements recursively
            root = soup.find('root')
            if root:
                for element in root.children:
                    if isinstance(element, Tag) and element.name == 'parameter':
                        param_lines = process_parameter_recursively(element, 0)
                        result_parts.extend(param_lines)
                    elif isinstance(element, NavigableString):
                        text_content = str(element).strip()
                        if text_content:
                            result_parts.append(text_content)
            
            return '\n'.join(result_parts) if result_parts else match.group(0)
            
        except Exception as e:
            print(f"Error processing ParameterList: {e}")
            return match.group(0)
    
    # Replace all ParameterList components
    return parameterlist_pattern.sub(process_parameterlist, text)


def resolve_rest_api_layout(text):
    """
    Convert RestAPILayout components to structured markdown using BeautifulSoup parser.
    This approach handles nested structures much more reliably than regex.
    """
    try:
        from bs4 import BeautifulSoup, NavigableString, Tag
    except ImportError:
        print("Warning: BeautifulSoup not available, falling back to regex approach")
        return resolve_rest_api_layout_regex_fallback(text)
    
    # Pattern to match the entire RestAPILayout component
    rest_api_pattern = re.compile(
        r'<RestAPILayout>(.*?)</RestAPILayout>',
        re.MULTILINE | re.DOTALL
    )
    
    def process_rest_api_layout(match):
        layout_content = match.group(1).strip()
        
        # Wrap in a root element and parse
        try:
            # BeautifulSoup expects lowercase tag names for HTML parsing
            # Convert to lowercase for parsing, but preserve original logic
            normalized_content = normalize_tags_for_parsing(layout_content)
            wrapped_content = f"<root>{normalized_content}</root>"
            
            soup = BeautifulSoup(wrapped_content, 'html.parser')
            result_parts = []
            
            # Process LeftColumn
            left_column = soup.find('leftcolumn')
            if left_column:
                method = left_column.get('method', '')
                endpoint = left_column.get('endpoint', '')
                
                if method:
                    result_parts.append(f"**Method:** {method}")
                if endpoint:
                    result_parts.append(f"**Endpoint:** `{endpoint}`")
                if method or endpoint:
                    result_parts.append('')
                
                processed_left = process_left_column_parsed(left_column)
                if processed_left:
                    result_parts.append(processed_left)
            
            # Process RightColumn
            right_column = soup.find('rightcolumn')
            if right_column:
                processed_right = process_right_column_parsed(right_column)
                if processed_right:
                    result_parts.append('')
                    result_parts.append(processed_right)
            
            return '\n'.join(result_parts)
            
        except Exception as e:
            print(f"Parser error: {e}")
            # Fallback to regex approach if parsing fails
            return resolve_rest_api_layout_regex_fallback(layout_content)
    
    def process_left_column_parsed(left_column):
        """Process LeftColumn content using parsed tree structure"""
        result_parts = []
        
        for element in left_column.children:
            if isinstance(element, NavigableString):
                text_content = str(element).strip()
                if text_content:
                    result_parts.append(text_content)
            elif isinstance(element, Tag):
                if element.name == 'pathparameter':
                    param_line = process_path_parameter_parsed(element)
                    result_parts.append(param_line)
                elif element.name == 'parameterlist':
                    # Use extracted helper function
                    param_section = process_parameter_list_parsed(element)
                    result_parts.append(param_section)
                else:
                    # Handle other elements (headings, text, etc.)
                    content = process_generic_element(element)
                    if content:
                        result_parts.append(content)
        
        # Join with proper spacing
        return format_content_with_spacing('\n'.join(result_parts))
    
    def process_path_parameter_parsed(param_element):
        """Process a single PathParameter element"""
        name = param_element.get('name', 'unknown')
        param_type = param_element.get('type', 'string')
        # Handle both string and boolean values for required
        required_attr = param_element.get('required', 'false')
        if required_attr in ['{true}', 'true', True]:
            required = True
        elif required_attr in ['{false}', 'false', False]:
            required = False
        else:
            required = False
            
        default_value = param_element.get('defaultvalue', param_element.get('defaultValue'))
        
        # Build type info
        status = 'required' if required else 'optional'
        type_info = f"({param_type}, {status}"
        if default_value:
            type_info += f", default: {default_value}"
        type_info += ")"
        
        # Get parameter description and handle lists specially
        description = get_direct_text_content(param_element)
        
        return f"- **{name}** {type_info}: {description}"
    
    def process_parameter_list_parsed(param_list):
        """Process a ParameterList element using extracted helpers"""
        result_parts = []
        
        # Add title if present
        title = param_list.get('title')
        if title:
            result_parts.append(f"**{title}**")
            result_parts.append('')
        
        # Process all parameter elements recursively
        for element in param_list.children:
            if isinstance(element, Tag) and element.name == 'parameter':
                param_lines = process_parameter_recursively(element, 0)
                result_parts.extend(param_lines)
            elif isinstance(element, NavigableString):
                text_content = str(element).strip()
                if text_content:
                    result_parts.append(text_content)
        
        return '\n'.join(result_parts)
    
    def process_right_column_parsed(right_column):
        """Process RightColumn content"""
        result_parts = []
        
        sections = right_column.find_all('section')
        for section in sections:
            title = section.get('title', 'Section')
            
            # Process section content
            if 'example' in title.lower():
                content = process_code_examples_parsed(section)
            else:
                content = get_element_text_content(section)
            
            result_parts.append(f"## {title}")
            result_parts.append('')
            result_parts.append(content)
        
        return '\n\n'.join(result_parts)
    
    def process_code_examples_parsed(section):
        """Process code examples in Tabs/TabItem structure"""
        result_lines = []
        
        tabs = section.find('tabs')
        if tabs:
            tab_items = tabs.find_all('tabitem')
            for tab_item in tab_items:
                label = tab_item.get('label', 'Example')
                
                result_lines.append(f"**{label}**")
                
                # Get code content and clean it up
                code_content = get_element_text_content(tab_item)
                cleaned_code = clean_code_content(code_content)
                result_lines.append(cleaned_code)
                result_lines.append('')
        else:
            # No tabs, just get section content
            content = get_element_text_content(section)
            result_lines.append(content)
        
        return '\n'.join(result_lines).rstrip()
    
    def clean_code_content(content):
        """Clean up code content while preserving structure"""
        lines = content.split('\n')
        result_lines = []
        
        for line in lines:
            # Preserve code block markers
            if line.strip().startswith('```'):
                result_lines.append(line.strip())
            elif line.strip():
                # Reduce excessive indentation but preserve some structure
                stripped = line.lstrip()
                original_indent = len(line) - len(stripped)
                
                if original_indent > 8:
                    result_lines.append('    ' + stripped)  # Max 4 spaces
                else:
                    result_lines.append(line.rstrip())
            else:
                result_lines.append('')
        
        return '\n'.join(result_lines)
    
    def process_generic_element(element):
        """Process generic elements like headings, paragraphs, etc."""
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            prefix = '#' * level
            return f"{prefix} {element.get_text(strip=True)}"
        else:
            return get_element_text_content(element)
    
    def format_content_with_spacing(content):
        """Add proper spacing around headers and sections"""
        lines = content.split('\n')
        result_lines = []
        
        for i, line in enumerate(lines):
            result_lines.append(line)
            
            # Add spacing after headers
            if line.startswith('#') and i < len(lines) - 1:
                next_line = lines[i + 1]
                if next_line.strip() and not next_line.startswith('#'):
                    result_lines.append('')
            
            # Add spacing before headers (except first line)
            if i > 0 and line.startswith('#'):
                prev_line = lines[i - 1]
                if prev_line.strip() and not prev_line.startswith('#'):
                    result_lines.insert(-1, '')
        
        # Clean up excessive blank lines
        cleaned_content = '\n'.join(result_lines)
        cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)
        
        return cleaned_content.strip()
    
    # Process all RestAPILayout components
    return rest_api_pattern.sub(process_rest_api_layout, text)


def resolve_rest_api_layout_regex_fallback(text):
    """
    Fallback regex-based implementation for when BeautifulSoup is not available
    """
    # This would contain the previous regex implementation
    # For now, just return the text unchanged with a warning
    print("Warning: Using regex fallback - install BeautifulSoup for better parsing")
    return text

def resolve_product_overview(text):
    """
    Convert ProductOverview components to structured markdown.
    Handles all component attributes and generates organized sections.
    """

    # Standard pattern fails when JSX fragments (<> ... </>) appear inside
    # attributes because the [^>]*? stops at the first > inside a fragment.
    # Instead we locate the component manually using tag depth tracking.

    result_parts_outer = []
    last_end = 0

    # Find each <ProductOverview occurrence
    for open_match in re.finditer(r'<ProductOverview\s*', text):
        component_start = open_match.start()

        # Walk forward from end of '<ProductOverview' to find where the
        # opening tag ends — that is, the '>' that is NOT inside a JSX
        # fragment or string literal.
        # We track:
        #   - paren depth  (for JSX expressions like description={( <> ... </> )} )
        #   - brace depth  (for JS objects/arrays)
        #   - whether we are inside a string
        pos = open_match.end()
        paren_depth = 0
        brace_depth = 0
        in_string = None  # None, '"', or "'"

        opening_tag_end = None
        while pos < len(text):
            ch = text[pos]

            if in_string:
                if ch == in_string and text[pos - 1] != '\\':
                    in_string = None
            else:
                if ch in ('"', "'"):
                    in_string = ch
                elif ch == '(':
                    paren_depth += 1
                elif ch == ')':
                    paren_depth -= 1
                elif ch == '{':
                    brace_depth += 1
                elif ch == '}':
                    brace_depth -= 1
                elif ch == '>' and paren_depth == 0 and brace_depth == 0:
                    # This '>' closes the opening tag
                    opening_tag_end = pos + 1
                    break
            pos += 1

        if opening_tag_end is None:
            continue

        attributes_str = text[open_match.end():opening_tag_end - 1]

        # Now find the matching </ProductOverview>
        close_tag = '</ProductOverview>'
        close_pos = text.find(close_tag, opening_tag_end)
        if close_pos == -1:
            continue

        inner_content = text[opening_tag_end:close_pos].strip()
        component_end = close_pos + len(close_tag)

        # Preserve text before this component
        result_parts_outer.append(text[last_end:component_start])
        last_end = component_end

        # ----------------------------------------------------------------
        # Extract attributes
        # ----------------------------------------------------------------
        attributes = {}

        simple_attrs = [
            'title', 'img', 'quickStartLink', 'uiQuickStartLink',
            'uiSamplesQuickStartLink', 'fastboardQuickStartLink',
            'apiReferenceLink', 'authenticationLink', 'samplesLink'
        ]
        for attr in simple_attrs:
            m = re.search(f'{attr}\\s*=\\s*["\']([^"\']*)["\']', attributes_str)
            if m:
                attributes[attr] = m.group(1)

        # ----------------------------------------------------------------
        # Extract productFeatures array
        # ----------------------------------------------------------------
        features = []
        features_match = re.search(
            r'productFeatures\s*=\s*\{?\[\s*(.*?)\s*\]\}?',
            attributes_str, re.DOTALL
        )
        if features_match:
            features_str = features_match.group(1)
            feature_objects = re.findall(r'\{([^}]*)\}', features_str)

            for feature_obj in feature_objects:
                feature = {}
                title_match = re.search(r'title:\s*["\']([^"\']*)["\']', feature_obj)
                if title_match:
                    feature['title'] = title_match.group(1)

                content_match = re.search(
                    r'content:\s*"([^"]*(?:\s*\+\s*"[^"]*")*)"',
                    feature_obj, re.DOTALL
                )
                if not content_match:
                    content_match = re.search(
                        r"content:\s*'([^']*(?:\s*\+\s*'[^']*')*)'",
                        feature_obj, re.DOTALL
                    )
                if content_match:
                    content = content_match.group(1)
                    content = re.sub(r'"\s*\+\s*"', '', content)
                    content = re.sub(r"'\s*\+\s*'", '', content)
                    feature['content'] = content.strip()

                link_match = re.search(r'link:\s*["\']([^"\']*)["\']', feature_obj)
                if link_match:
                    feature['link'] = link_match.group(1)

                if feature:
                    features.append(feature)

        # ----------------------------------------------------------------
        # Extract linkButtons array using bracket-depth tracking
        # Regex fails here because JSX fragments contain > and ) chars
        # ----------------------------------------------------------------
        link_buttons = []
        lb_start_match = re.search(r'linkButtons\s*=\s*\{?\[', attributes_str)

        if lb_start_match:
            search_start = lb_start_match.end()
            depth = 1
            i = search_start
            while i < len(attributes_str) and depth > 0:
                if attributes_str[i] == '[':
                    depth += 1
                elif attributes_str[i] == ']':
                    depth -= 1
                i += 1
            buttons_str = attributes_str[search_start:i - 1]

            # Extract individual { ... } button objects using brace tracking
            button_objects = []
            depth = 0
            start = None
            for i, ch in enumerate(buttons_str):
                if ch == '{':
                    if depth == 0:
                        start = i + 1
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0 and start is not None:
                        button_objects.append(buttons_str[start:i])
                        start = None

            for btn_obj in button_objects:
                label_match = re.search(r'label:\s*["\']([^"\']+)["\']', btn_obj)
                link_match = re.search(r'link:\s*["\']([^"\']*)["\']', btn_obj)
                desc_match = re.search(r'<>\s*(.*?)\s*</>', btn_obj, re.DOTALL)

                if label_match:
                    label = label_match.group(1)
                    link = link_match.group(1) if link_match else ''
                    description = (
                        ' '.join(desc_match.group(1).split()) if desc_match else ''
                    )
                    link_buttons.append({
                        'label': label,
                        'description': description,
                        'link': link,
                        'type': 'primary'
                    })

        # ----------------------------------------------------------------
        # Build markdown output
        # ----------------------------------------------------------------
        result_parts = []

        if attributes.get('title'):
            result_parts.append(f"# {attributes['title']}")
            result_parts.append('')

        # Inner content — resolve variables
        if inner_content:
            processed_content = inner_content
            global_pattern = r'<Vg\s+k\s*=\s*"(\w+)"\s*\/?>'
            processed_content = re.sub(
                global_pattern,
                lambda m: globalVariables.get(m.group(1), m.group(0)),
                processed_content
            )
            processed_content = resolve_local_variables(
                processed_content, product, productDict, platform, platformDict
            )
            result_parts.append(processed_content)
            result_parts.append('')

        # Buttons — prefer linkButtons, fall back to string attributes
        if link_buttons:
            buttons = link_buttons
        else:
            buttons = []
            if attributes.get('quickStartLink'):
                buttons.append({
                    'label': 'SDK quickstart',
                    'link': attributes['quickStartLink'],
                    'description': 'Customize your experience from the start with our flexible Video SDK.',
                    'type': 'primary'
                })
            if attributes.get('uiQuickStartLink'):
                buttons.append({
                    'label': 'UI Kit quickstart',
                    'link': attributes['uiQuickStartLink'],
                    'description': 'Start with a pre-built video UI and video calling logic - customize as you go.',
                    'type': 'primary'
                })
            if attributes.get('authenticationLink'):
                buttons.append({
                    'label': 'Authentication',
                    'link': attributes['authenticationLink'],
                    'type': 'secondary'
                })
            if attributes.get('apiReferenceLink'):
                buttons.append({
                    'label': 'API reference',
                    'link': attributes['apiReferenceLink'],
                    'type': 'secondary'
                })
            if attributes.get('samplesLink'):
                buttons.append({
                    'label': 'Samples',
                    'link': attributes['samplesLink'],
                    'type': 'secondary'
                })

        if buttons:
            result_parts.append('## Start building with')
            result_parts.append('')
            for button in buttons:
                link = button['link']
                if link.startswith('/') and not link.startswith('http'):
                    # linkButtons use relative paths without .md extension —
                    # resolve to docs.agora.io and append .md
                    if not link.endswith('.md'):
                        link = f"https://docs.agora.io/en{link}.md"
                    else:
                        link = f"https://docs.agora.io/en{link}"
                if button.get('description'):
                    result_parts.append(
                        f"- [{button['label']}]({link}) - {button['description']}"
                    )
                else:
                    result_parts.append(f"- [{button['label']}]({link})")
            result_parts.append('')

        if features:
            result_parts.append('## Product Features')
            result_parts.append('')
            for feature in features:
                if feature.get('title'):
                    if feature.get('link'):
                        link = feature['link']
                        if link.startswith('/en/'):
                            link = f"{siteBaseUrl}{link}"
                        elif link.startswith('/') and not link.startswith('http'):
                            link = f"{siteBaseUrl}/en{link}"
                        feature_line = f"- [**{feature['title']}**]({link})"
                    else:
                        feature_line = f"- **{feature['title']}**"
                    if feature.get('content'):
                        feature_line += f" - {feature['content']}"
                    result_parts.append(feature_line)
            result_parts.append('')

        result_parts_outer.append('\n'.join(result_parts).rstrip())

    # Append any text after the last component
    result_parts_outer.append(text[last_end:])
    return ''.join(result_parts_outer)

# New comprehensive platform tag resolver
def resolve_all_platform_tags(text, platform):
    """
    Resolve all PlatformWrapper tags in the text for the given platform.
    This handles both standard and notAllowed attributes.
    Properly handles nested PlatformWrapper tags.
    """
    
    text = normalize_wrapper_attributes(text)

    # Keep processing until no more PlatformWrapper tags are found
    max_iterations = 100  # Prevent infinite loops
    iteration = 0
    
    while '<PlatformWrapper' in text and iteration < max_iterations:
        iteration += 1
        
        # Find the first opening PlatformWrapper tag
        start_match = re.search(r'<PlatformWrapper\s+([^>]*?)>', text)
        if not start_match:
            break
            
        start_pos = start_match.start()
        end_pos = start_match.end()
        attributes = start_match.group(1)
        
        # Now find the matching closing tag, accounting for nested tags
        depth = 1
        search_pos = end_pos
        
        while depth > 0 and search_pos < len(text):
            # Look for the next opening or closing tag
            opening = text.find('<PlatformWrapper', search_pos)
            closing = text.find('</PlatformWrapper>', search_pos)
            
            if closing == -1:
                # No closing tag found, malformed structure
                print(f"Warning: Unclosed PlatformWrapper tag found")
                text = text[:start_pos] + text[end_pos:]
                break
            
            if opening != -1 and opening < closing:
                # Found another opening tag before the closing tag (nested)
                depth += 1
                search_pos = opening + 1
            else:
                # Found a closing tag
                depth -= 1
                if depth == 0:
                    # This is our matching closing tag
                    closing_end = closing + len('</PlatformWrapper>')
                    content = text[end_pos:closing]
                    
                    # Determine if we should include this content
                    platform_match = re.search(r'platform\s*=\s*["\']([^"\']+)["\']', attributes)
                    notallowed_match = re.search(r'notAllowed\s*=\s*["\']([^"\']+)["\']', attributes)
                    
                    include_content = False
                    
                    if platform_match:
                        platforms_str = platform_match.group(1)
                        platforms_str = platforms_str.strip('[]').replace(' ', '')
                        allowed_platforms = [p.strip() for p in platforms_str.split(',')]
                        include_content = platform in allowed_platforms
                    elif notallowed_match:
                        excluded_str = notallowed_match.group(1)
                        excluded_str = excluded_str.strip('[]').replace(' ', '')
                        excluded_platforms = [p.strip() for p in excluded_str.split(',')]
                        include_content = platform not in excluded_platforms
                    
                    # Replace the entire wrapper with content or nothing
                    if include_content:
                        # Process nested PlatformWrapper tags in the content first
                        content = resolve_all_platform_tags(content, platform)
                        text = text[:start_pos] + content + text[closing_end:]
                    else:
                        text = text[:start_pos] + text[closing_end:]
                    
                    break
                else:
                    search_pos = closing + 1
    
    # Final cleanup of any orphaned closing tags
    text = re.sub(r'</PlatformWrapper>', '', text)
    
    return text

# Similar function for ProductWrapper tags
def resolve_all_product_tags(text, product):
    """
    Resolve all ProductWrapper tags in the text for the given product.
    This handles both standard and notAllowed attributes.
    Properly handles nested ProductWrapper tags.
    """
    
    text = normalize_wrapper_attributes(text)
    
    # Keep processing until no more ProductWrapper tags are found
    max_iterations = 100  # Prevent infinite loops
    iteration = 0
    
    while '<ProductWrapper' in text and iteration < max_iterations:
        iteration += 1
        
        # Find the first opening ProductWrapper tag
        start_match = re.search(r'<ProductWrapper\s+([^>]*?)>', text)
        if not start_match:
            break
            
        start_pos = start_match.start()
        end_pos = start_match.end()
        attributes = start_match.group(1)
        
        # Now find the matching closing tag, accounting for nested tags
        depth = 1
        search_pos = end_pos
        
        while depth > 0 and search_pos < len(text):
            # Look for the next opening or closing tag
            opening = text.find('<ProductWrapper', search_pos)
            closing = text.find('</ProductWrapper>', search_pos)
            
            if closing == -1:
                # No closing tag found, malformed structure
                print(f"Warning: Unclosed ProductWrapper tag found")
                text = text[:start_pos] + text[end_pos:]
                break
            
            if opening != -1 and opening < closing:
                # Found another opening tag before the closing tag (nested)
                depth += 1
                search_pos = opening + 1
            else:
                # Found a closing tag
                depth -= 1
                if depth == 0:
                    # This is our matching closing tag
                    closing_end = closing + len('</ProductWrapper>')
                    content = text[end_pos:closing]
                    
                    # Determine if we should include this content
                    product_match = re.search(r'product\s*=\s*["\']([^"\']+)["\']', attributes)
                    notallowed_match = re.search(r'notAllowed\s*=\s*["\']([^"\']+)["\']', attributes)
                    
                    include_content = False
                    
                    if product_match:
                        products_str = product_match.group(1)
                        products_str = products_str.strip('[]').replace(' ', '')
                        allowed_products = [p.strip() for p in products_str.split(',')]
                        include_content = product in allowed_products
                    elif notallowed_match:
                        excluded_str = notallowed_match.group(1)
                        excluded_str = excluded_str.strip('[]').replace(' ', '')
                        excluded_products = [p.strip() for p in excluded_str.split(',')]
                        include_content = product not in excluded_products
                    
                    # Replace the entire wrapper with content or nothing
                    if include_content:
                        # Process nested ProductWrapper tags in the content first
                        content = resolve_all_product_tags(content, product)
                        text = text[:start_pos] + content + text[closing_end:]
                    else:
                        text = text[:start_pos] + text[closing_end:]
                    
                    break
                else:
                    search_pos = closing + 1
    
    # Final cleanup of any orphaned closing tags
    text = re.sub(r'</ProductWrapper>', '', text)
    
    return text

# Recursively resolve import statements
def parse_exported_variables(file_path):
    """
    Parse exported JavaScript variables from an MDX file.
    Returns a dictionary of variable names and their values.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        variables = {}
        
        # Find export const statements
        export_pattern = r'export\s+const\s+(\w+)\s*=\s*{([^}]*)};'
        matches = re.findall(export_pattern, content, re.MULTILINE | re.DOTALL)
        
        for var_name, var_content in matches:
            # Parse the object content
            obj_dict = {}
            
            # Find key-value pairs in the object
            # Handle both "key": "value" and key: "value" formats
            prop_pattern = r'(?:(?:"([^"]+)")|(\w+))\s*:\s*(?:(?:"([^"]+)")|{([^}]*)})'
            prop_matches = re.findall(prop_pattern, var_content)
            
            for match in prop_matches:
                key = match[0] or match[1]  # quoted or unquoted key
                
                if match[2]:  # string value
                    obj_dict[key] = match[2]
                elif match[3]:  # object value
                    # Parse nested object
                    nested_dict = {}
                    nested_pattern = r'(?:(?:"([^"]+)")|(\w+))\s*:\s*"([^"]+)"'
                    nested_matches = re.findall(nested_pattern, match[3])
                    
                    for nested_match in nested_matches:
                        nested_key = nested_match[0] or nested_match[1]
                        nested_value = nested_match[2]
                        nested_dict[nested_key] = nested_value
                    
                    obj_dict[key] = nested_dict
            
            variables[var_name] = obj_dict
        
        return variables
        
    except Exception as e:
        print(f"Warning: Could not parse variables from {file_path}: {e}")
        return {}


def has_variable_imports(content):
    """
    Check if the content contains 'import * as' patterns.
    Returns True if variable imports are detected.
    """
    pattern = r'import\s+\*\s+as\s+\w+\s+from\s+[\'"][^\'\"]+[\'"]'
    return bool(re.search(pattern, content))


def resolve_variable_expressions(content, variables, platform, ag_platform=None):
    """
    Resolve variable expressions like {variable.property[props.ag_platform]} in content.
    """
    if not variables:
        return content
    
    # Pattern to match {variable.property[props.ag_platform]} or {variable.property['platform']}
    pattern = r'\{(\w+)\.(\w+)\[(?:props\.ag_platform|[\'"]([^\'"]+)[\'"])\]\}'
    
    def replace_expression(match):
        var_name = match.group(1)
        prop_name = match.group(2)
        explicit_platform = match.group(3)
        
        # Use explicit platform if provided, 
        # otherwise use ag_platform for props.ag_platform, 
        # otherwise fall back to general platform
        if explicit_platform:
            target_platform = explicit_platform
        elif ag_platform and 'props.ag_platform' in match.group(0):
            target_platform = ag_platform
        else:
            target_platform = platform
        
        if var_name in variables and prop_name in variables[var_name]:
            prop_obj = variables[var_name][prop_name]
            if isinstance(prop_obj, dict) and target_platform in prop_obj:
                return prop_obj[target_platform]
        
        # Return original expression if not found
        return match.group(0)
    
    return re.sub(pattern, replace_expression, content)


# Enhanced resolve_imports function
def resolve_imports(mdxFilePath, ag_platform_override=None):
    """
    Enhanced import resolution that handles both component imports and variable imports.
    Also handles ag_platform attribute for component-specific platform resolution.
    """
    base_dir = os.path.dirname(mdxFilePath)
    with open(rf'{mdxFilePath}', 'r', encoding='utf-8') as file:
        mdxFileContents = file.read()
        # Use the comprehensive tag resolvers
        mdxFileContents = resolve_all_platform_tags(mdxFileContents, platform)
        mdxFileContents = resolve_all_product_tags(mdxFileContents, product)

    # Check if this file has variable imports - early detection
    has_var_imports = has_variable_imports(mdxFileContents)
    
    # Read import statements - handle both component and variable imports
    component_pattern = r'import\s+(\w+?)\s+from\s+\'(.+?md[x]*)\';?\n*'
    variable_pattern = r'import\s+\*\s+as\s+(\w+)\s+from\s+\'(.+?md[x]*)\';?\n*'
    
    component_matches = re.findall(component_pattern, mdxFileContents)
    variable_matches = re.findall(variable_pattern, mdxFileContents) if has_var_imports else []
    
    # If no imports found, return content as-is
    if not component_matches and not variable_matches:
        return mdxFileContents
    
    # Store parsed variables for resolution
    all_variables = {}
    
    # Process variable imports first
    if variable_matches:
        print(f"Processing variable imports in {os.path.basename(mdxFilePath)}")
        
        for var_name, filepath in variable_matches:
            filepath = filepath.replace('@docs', docsPath)
            if not os.path.isabs(filepath):
                filepath = os.path.abspath(os.path.join(base_dir, filepath))
            
            # Parse variables from the imported file
            file_variables = parse_exported_variables(filepath)
            if file_variables:
                # Store with the alias name
                all_variables[var_name] = file_variables
                print(f"  Loaded variables from {os.path.basename(filepath)}: {list(file_variables.keys())}")
    
    # Remove all import statements (both component and variable)
    import_pattern = r'import\s+(?:\*[\s\w]*as\s+\w+|\w+?)\s+from\s+\'[^\']+\';?\n*'
    mdxFileContents = re.sub(import_pattern, '', mdxFileContents)
    
    # Resolve variable expressions if we have variables
    if all_variables:
        # Flatten the nested structure for easier access
        flattened_vars = {}
        for alias, vars_dict in all_variables.items():
            flattened_vars[alias] = vars_dict
        
        mdxFileContents = resolve_variable_expressions(mdxFileContents, flattened_vars, platform, ag_platform_override)
    
    # Process component imports (existing logic)
    for tag, filepath in component_matches:
        filepath = filepath.replace('@docs', docsPath)
        if '/data/variables' in filepath:
            continue
        if not os.path.isabs(filepath):
            filepath = os.path.abspath(os.path.join(base_dir, filepath))

        # Replace component tags with content, checking for ag_platform attribute
        rgx = r'<{}([\s\S]*?)/>'.format(tag)
        
        def replace_component(match):
            tag_attributes = match.group(1)
            
            # Check for ag_platform attribute in the component tag
            ag_platform_match = re.search(r'ag_platform\s*=\s*[\'"]([^\'"]+)[\'"]', tag_attributes)
            component_ag_platform = ag_platform_match.group(1) if ag_platform_match else ag_platform_override
            
            # Recursively resolve the imported file with ag_platform context
            processed_content = resolve_imports(filepath, component_ag_platform)
            # Use general platform for PlatformWrapper and ProductWrapper tags
            processed_content = resolve_all_platform_tags(processed_content, platform)
            processed_content = resolve_all_product_tags(processed_content, product)
            
            return processed_content
        
        mdxFileContents = re.sub(rgx, replace_component, mdxFileContents)

    return mdxFileContents

def resolve_header(content):
    """
    - Removes 'export const ...' blocks
    - Adds '# title' heading at the top if frontmatter has a title
    """
    # Remove export statements
    content = re.sub(r"^export\s+const\s+.*$", "", content, flags=re.MULTILINE).strip()

    # Check for frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", content, re.DOTALL)
    if fm_match:
        fm_dict = yaml.safe_load(fm_match.group(1)) or {}
        body = content[fm_match.end():]
    else:
        fm_dict = {}
        body = content

    # Add heading if title exists
    if "title" in fm_dict:
        heading = f"# {fm_dict['title']}\n\n"
        if not body.startswith("# "):  # avoid duplicate heading
            body = heading + body

    return content[:fm_match.end()] + body if fm_match else body

def resolve_recipes(text):
    """
    Convert Recipes components to a markdown list.
    Format: * [title](link): description
    Internal links are resolved to full https://docs.agora.io/en/ URLs.
    """
    if '<Recipes' not in text:
        return text
    
    recipes_pattern = re.compile(
        r'<Recipes\s*([\s\S]*?)>\s*</Recipes>',
        re.MULTILINE | re.DOTALL
    )

    def process_recipes(match):
        attributes_str = match.group(1)
        result_parts = []

        # Extract optional description attribute
        desc_match = re.search(r'description\s*=\s*["\']([^"\']+)["\']', attributes_str)
        if desc_match:
            result_parts.append(desc_match.group(1))
            result_parts.append('')

        # Extract recipes array using bracket-depth tracking
        recipes_start = re.search(r'recipes\s*=\s*\{?\[', attributes_str)
        if not recipes_start:
            return match.group(0)

        search_start = recipes_start.end()
        depth = 1
        i = search_start
        while i < len(attributes_str) and depth > 0:
            if attributes_str[i] == '[':
                depth += 1
            elif attributes_str[i] == ']':
                depth -= 1
            i += 1
        recipes_str = attributes_str[search_start:i - 1]

        # Extract individual { ... } recipe objects using brace tracking
        recipe_objects = []
        depth = 0
        start = None
        for i, ch in enumerate(recipes_str):
            if ch == '{':
                if depth == 0:
                    start = i + 1
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0 and start is not None:
                    recipe_objects.append(recipes_str[start:i])
                    start = None

        for obj in recipe_objects:
            title_match = re.search(r'title\s*:\s*["\']([^"\']+)["\']', obj)
            link_match = re.search(r'link\s*:\s*["\']([^"\']+)["\']', obj)
            item_desc_match = re.search(r'description\s*:\s*["\']([^"\']+)["\']', obj)

            if not title_match or not link_match:
                continue

            title = title_match.group(1)
            link = link_match.group(1)
            item_desc = item_desc_match.group(1) if item_desc_match else ''

            # Resolve internal links to full URLs
            if link.startswith('/en/'):
                link = f"https://docs.agora.io{link}"
            elif link.startswith('/') and not link.startswith('//'):
                link = f"https://docs.agora.io/en{link}"

            line = f"* [{title}]({link})"
            if item_desc:
                line += f": {item_desc}"
            result_parts.append(line)

        return '\n'.join(result_parts)

    return recipes_pattern.sub(process_recipes, text)

def resolve_tabs(text):
    """
    Convert Tabs and TabItem components to markdown format.
    Ensures tab headers align properly with the Tabs block indentation.
    """

    def find_tabs_base_indent(match):
        """Find the base indentation of the Tabs block"""
        match_start = match.start()
        line_start = text.rfind('\n', 0, match_start) + 1
        tabs_line = text[line_start:match_start]
        indent_match = re.match(r'^(\s*)', tabs_line)
        return indent_match.group(1) if indent_match else ''

    def normalize_tabitem_to_tabs_level(content, base_indent):
        """If TabItem content is more indented than Tabs, bring it back to Tabs level"""
        lines = content.split('\n')
        if not lines:
            return content

        # Find first non-empty line indent
        tabitem_indent = ''
        for line in lines:
            if line.strip():
                tabitem_indent = re.match(r'^(\s*)', line).group(1)
                break

        # Normalize indentation if deeper than Tabs
        if len(tabitem_indent) > len(base_indent):
            excess_indent = len(tabitem_indent) - len(base_indent)
            normalized_lines = []
            for line in lines:
                if line.startswith(' ' * excess_indent):
                    normalized_lines.append(line[excess_indent:])
                else:
                    normalized_lines.append(line.lstrip())
            return '\n'.join(normalized_lines)
        return content

    while '<Tabs' in text:
        tabs_pattern = re.compile(r'<Tabs[^>]*?>(.*?)</Tabs>', re.DOTALL)
        match = tabs_pattern.search(text)
        if not match:
            break

        tabs_content = match.group(1)
        base_indent = find_tabs_base_indent(match)

        tabitem_pattern = re.compile(r'<TabItem\s+([^>]*?)>(.*?)</TabItem>', re.DOTALL)
        tabitems = tabitem_pattern.findall(tabs_content)

        result = []
        for i, (attributes, content) in enumerate(tabitems):
            value = re.search(r'value\s*=\s*["\']([^"\']*)["\']', attributes)
            label = re.search(r'label\s*=\s*["\']([^"\']*)["\']', attributes)
            header = (label.group(1) if label else (value.group(1) if value else 'Tab'))

            normalized_content = normalize_tabitem_to_tabs_level(content, base_indent)
            normalized_content = re.sub(r'^\s*\n', '', normalized_content)
            normalized_content = re.sub(r'\n\s*$', '', normalized_content)

            # First header: no indent, later headers: base_indent
            header_prefix = '' if i == 0 else base_indent

            result.append(f'{header_prefix}**{header}**')
            if normalized_content.strip():
                result.append(normalized_content)
            result.append('')

        replacement = '\n'.join(result).rstrip() + '\n'
        
        text = text[:match.start()] + replacement + text[match.end():]

    # Clean up any remaining tags
    text = re.sub(r'<TabItem\s+[^>]*?>', '', text)
    text = re.sub(r'</TabItem>', '', text)
    text = re.sub(r'<Tabs[^>]*?>', '', text)
    text = re.sub(r'</Tabs>', '', text)

    return text


def resolve_details(text):
    """
    Convert HTML details/summary tags to markdown format.
    <details>
      <summary>Summary text</summary>
      Content
    </details>
    becomes:
    **Summary text**
    
    Content
    """
    
    # Pattern to match details blocks with summary
    details_pattern = re.compile(
        r'<details[^>]*?>\s*<summary[^>]*?>(.*?)</summary>(.*?)</details>',
        re.MULTILINE | re.DOTALL
    )
    
    def process_details(match):
        summary_text = match.group(1).strip()
        content = match.group(2).strip()
        
        # Create markdown replacement
        result = f'**{summary_text}**\n\n{content}'
        return result
    
    # Replace all details blocks
    text = details_pattern.sub(process_details, text)
    
    # Clean up any orphaned details or summary tags
    text = re.sub(r'<details[^>]*?>', '', text)
    text = re.sub(r'</details>', '', text)
    text = re.sub(r'<summary[^>]*?>', '', text)
    text = re.sub(r'</summary>', '', text)
    
    return text

def resolve_admonitions(text):
    """
    Convert <Admonition> tags to markdown blockquotes.
    Removes blank lines so markdown renders cleanly.
    """

    admonition_types = {
        'note': ('📝', 'Note'),
        'tip': ('💡', 'Tip'),
        'info': ('ℹ️', 'Info'),
        'caution': ('⚠️', 'Caution'),
        'warning': ('⚠️', 'Warning'),
        'danger': ('🚨', 'Danger'),
        'important': ('❗', 'Important'),
        'success': ('✅', 'Success'),
    }

    admonition_pattern = re.compile(
        r'^(\s*)<Admonition\s+([^>]*?)>(.*?)</Admonition>',
        re.MULTILINE | re.DOTALL
    )

    def process_admonition(match):
        original_indent = match.group(1)
        attributes = match.group(2)
        raw_content = match.group(3)

        type_match = re.search(r'type\s*=\s*["\']([^"\']+)["\']', attributes)
        title_match = re.search(r'title\s*=\s*["\']([^"\']+)["\']', attributes)

        admonition_type = type_match.group(1).lower() if type_match else 'note'
        custom_title = title_match.group(1) if title_match else None

        emoji, default_title = admonition_types.get(admonition_type, ('📝', 'Note'))
        title = custom_title if custom_title else default_title

        content_lines = [line.rstrip() for line in raw_content.strip().splitlines()]

        result_lines = [f'{original_indent}> {emoji} **{title}**']
        for line in content_lines:
            result_lines.append(f'{original_indent}> {line}' if line.strip() else f'{original_indent}>')

        result = "\n".join(result_lines)

        # 🔑 cleanup: remove quote-only blank lines and stray empty lines
        result = re.sub(r'(?m)^>\s*$', '', result)         # remove ">" only lines
        result = re.sub(r"\n\s*\n", "\n", result)          # collapse blank lines

        return result

    return admonition_pattern.sub(process_admonition, text)

def remove_imports_outside_codeblocks(text):
    """
    Remove import statements that are outside of code blocks.
    Code blocks can be triple backticks (```) or <CodeBlock> tags.
    """
    
    # Store all code blocks with their positions
    protected_regions = []
    
    # Find all triple backtick code blocks
    for match in re.finditer(r'```[\s\S]*?```', text):
        protected_regions.append((match.start(), match.end()))
    
    # Find all CodeBlock tags
    for match in re.finditer(r'<CodeBlock[\s\S]*?</CodeBlock>', text):
        protected_regions.append((match.start(), match.end()))
    
    # Sort regions by start position
    protected_regions.sort()
    
    # Function to check if a position is inside a protected region
    def is_protected(pos):
        for start, end in protected_regions:
            if start <= pos < end:
                return True
        return False
    
    # Find and remove import statements that are not in protected regions
    lines = text.split('\n')
    result_lines = []
    current_pos = 0
    
    for line in lines:
        line_start = current_pos
        
        # Check if this line contains an import statement
        import_match = re.match(r'^\s*import\s+.*?\s+from\s+[\'"].*?[\'"];?\s*$', line)
        
        # If it's an import and not in a protected region, skip it
        if import_match and not is_protected(line_start):
            pass  # Skip this line
        else:
            result_lines.append(line)
        
        current_pos += len(line) + 1  # +1 for the newline character
    
    return '\n'.join(result_lines)

def resolve_hyperlinks(text, base_folder, http_url):
    # Find all links in the text
    pattern = r'(?<!\!)\[.*?\]\((.*?)\)'
    links = re.findall(pattern, text)

    # Loop through the links and resolve them
    for link in links:
        # Skip links that start with "http" or "https"
        if link.startswith('http') or link.startswith('#'):
            continue
        elif link.startswith('.'):
            # Resolve relative links with respect to the base folder
            resolved_link = os.path.abspath(os.path.join(base_folder, link))
            rel_path = os.path.relpath(resolved_link, docsPath)
        else: 
            # Resolve links with respect to the docs 'folder'
            rel_path = link

        # Create the new URL by adding the HTTP prefix
        new_url = '{}/{}'.format(http_url, rel_path.replace('\\','/'))
        new_url = new_url.replace('//','/')

        # Replace the link in the text
        text = text.replace(link, new_url)

    return text

def resolve_codeblocks(text):
    """
    Convert CodeBlock components to markdown code blocks with proper indentation and whitespace preservation.
    """
    
    # More precise patterns that preserve whitespace
    codeblock_pattern_wrapped = re.compile(
        r'<CodeBlock\s+([^>]*?)>\s*\{\`(.*?)\`\}\s*</CodeBlock>',
        re.MULTILINE | re.DOTALL
    )

    codeblock_pattern_raw = re.compile(
        r'<CodeBlock\s*([^>]*?)>(.*?)</CodeBlock>',
        re.MULTILINE | re.DOTALL
    )

    def replace_wrapped_codeblock(match):
        # Extract from wrapped pattern
        match_start = match.start()
        line_start = text.rfind('\n', 0, match_start) + 1
        line_before_match = text[line_start:match_start]
        
        attributes = match.group(1)
        code_content = match.group(2)  # This should preserve whitespace
        
        # Extract language
        language_match = re.search(r'language\s*=\s*["\']([^"\']*)["\']', attributes)
        language = language_match.group(1) if language_match else ''

        # Unescape characters but preserve whitespace structure
        code_content = code_content.replace('\\\\', '\\')
        code_content = code_content.replace('\\n', '\n')
        code_content = code_content.replace('\\t', '\t')
        code_content = code_content.replace('\\r', '\r')
        code_content = code_content.replace('\\"', '"')
        code_content = code_content.replace("\\'", "'")
        code_content = code_content.replace('\\`', '`')
        code_content = code_content.replace('\\{', '{')

        # Apply base indentation to each line while preserving internal indentation
        lines = code_content.split('\n')
        
        # Remove leading/trailing empty lines
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        
        # Add base indentation to each line
        indented_lines = []
        for line in lines:
            indented_lines.append(line_before_match + line)
        
        indented_content = '\n'.join(indented_lines)
        
        return f'```{language}\n{indented_content}\n{line_before_match}```'

    def replace_raw_codeblock(match):
        # Extract from raw pattern  
        match_start = match.start()
        line_start = text.rfind('\n', 0, match_start) + 1
        line_before_match = text[line_start:match_start]
        
        attributes = match.group(1)
        code_content = match.group(2)
        
        # Extract language and process similar to wrapped version
        language_match = re.search(r'language\s*=\s*["\']([^"\']*)["\']', attributes)
        language = language_match.group(1) if language_match else ''

        # Similar processing as wrapped version
        code_content = code_content.replace('\\\\', '\\')
        code_content = code_content.replace('\\n', '\n')
        code_content = code_content.replace('\\t', '\t')
        code_content = code_content.replace('\\r', '\r')
        code_content = code_content.replace('\\"', '"')
        code_content = code_content.replace("\\'", "'")
        code_content = code_content.replace('\\`', '`')

        lines = code_content.split('\n')
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        
        indented_lines = []
        for line in lines:
            indented_lines.append(line_before_match + line)
        
        indented_content = '\n'.join(indented_lines)
        
        return f'```{language}\n{indented_content}\n{line_before_match}```'

    # Apply both patterns
    text = codeblock_pattern_wrapped.sub(replace_wrapped_codeblock, text)
    text = codeblock_pattern_raw.sub(replace_raw_codeblock, text)

    return text

def resolve_links_and_images(text, base_folder, docs_folder, images_dir=None, original_base_url="https://docs.agora.io/en", new_base_url="https://docs-md.agora.io/en", assets_path="https://docs-md.agora.io"):
    """
    Consolidated function to process both images and links in markdown text.
    """

    # Derive images_dir from output file location if not explicitly provided
    if images_dir is None:
        images_dir = os.path.join(os.path.dirname(args.output_file), 'images')

    # Create images directory if it doesn't exist
    os.makedirs(images_dir, exist_ok=True)
      
    # Build path to docs assets folder using the docs_folder parameter
    docs_assets_path = os.path.join(docs_folder, 'docs', 'assets')
    
    # First, process <Link> tags with global variables
    link_tag_pattern = re.compile(r'<Link\s+to=\"\{\{(?:[Gg]lobal?|GLOBAL)\.([^\"]+)}}([^\"]*)\"\s*>(.*?)</Link>')

    def convert_internal_link(link_text, docs_url):
        """Convert internal docs.agora.io URLs to markdown file URLs"""
        try:
            parsed_url = urllib.parse.urlparse(docs_url)
            path = parsed_url.path
            if path.startswith('/en/'):
                path = path[4:]
            elif path.startswith('/en'):
                path = path[3:]
            
            query_params = urllib.parse.parse_qs(parsed_url.query)
            platform = None
            if 'platform' in query_params:
                platform = query_params['platform'][0]
            
            if platform:
                new_path = f"{path}_{platform}.md"
            else:
                new_path = f"{path}.md"
            
            if not new_path.startswith('/'):
                new_path = '/' + new_path
            
            final_url = f"{new_base_url}{new_path}"
            return f'[{link_text}]({final_url})'
            
        except Exception as e:
            print(f"Warning: Error converting internal link {docs_url}: {e}")
            return f'[{link_text}]({docs_url})'

    def process_link_tag(match):
        url_key = match.group(1)
        additional_path = match.group(2)
        name = match.group(3)
        
        base_url = globalVariables.get(url_key)
        if base_url is None:
            print(f"Warning: Unknown URL key: {url_key}")
            return match.group(0)
        
        if base_url and not base_url.startswith(('http://', 'https://')):
            if base_url.startswith('//'):
                base_url = 'https:' + base_url
            else:
                base_url = 'https://' + base_url
        
        full_url = f"{base_url}{additional_path}"
        
        if full_url.startswith(original_base_url):
            return convert_internal_link(name, full_url)
        else:
            return f'[{name}]({full_url})'

    # Process <Link> tags first
    text = link_tag_pattern.sub(process_link_tag, text)

    # Define helper functions for markdown links
    def process_image_link(alt_text, image_url):
        """Process image links - copy local images and update paths"""
        if image_url.startswith(('http://', 'https://', '#')):
            return f'![{alt_text}]({image_url})'
        
        try:
            clean_image_path = image_url.lstrip('/')
            
            destination_dir = os.path.join(images_dir, os.path.dirname(clean_image_path))
            os.makedirs(destination_dir, exist_ok=True)
            destination_path = os.path.join(images_dir, clean_image_path)
            
            source_path = docs_assets_path + image_url
            shutil.copyfile(source_path, destination_path)
            
            if assets_path == ".":
                image_url_output = clean_image_path
            else:
                image_url_output = f"{assets_path}/{clean_image_path}"
            
            return f'![{alt_text}]({image_url_output})'
            
        except FileNotFoundError:
            print(f"Warning: Image file not found: {source_path}")
            return f'![{alt_text}]({image_url})'
        except Exception as e:
            print(f"Warning: Error processing image {image_url}: {e}")
            return f'![{alt_text}]({image_url})'
    
    def process_text_link(link_text, link_url):
        """Process text links - convert internal docs links to markdown format"""
        if link_url.startswith('#'):
            return f'[{link_text}]({link_url})'
        
        if link_url.startswith('.'):
            resolved_path = os.path.abspath(os.path.join(base_folder, link_url))
            rel_path = os.path.relpath(resolved_path, docsPath)
            rel_path = rel_path.replace('\\', '/')
            link_url = f'{original_base_url}/{rel_path}'
        elif not link_url.startswith(('http://', 'https://')):
            link_url = f'{original_base_url}/{link_url}'
        
        link_url = re.sub(r'(?<!:)//+', '/', link_url)
        
        if link_url.startswith(original_base_url):
            return convert_internal_link(link_text, link_url)
        
        return f'[{link_text}]({link_url})'

    def process_link(match):
        is_image = match.group(1) == '!'
        alt_or_text = match.group(2)
        url = match.group(3)
        
        if is_image:
            return process_image_link(alt_or_text, url)
        else:
            return process_text_link(alt_or_text, url)
    
    # Process all markdown links and images
    link_pattern = r'(!?)\[([^\]]*)\]\(([^)]+)\)'
    processed_text = re.sub(link_pattern, process_link, text)
    
    return processed_text

def add_frontmatter(content, source_file, platform="flutter", exported_from=None, output_file=None):
    """
    Keeps original frontmatter (title, description, sidebar_position, etc.),
    and appends/updates platform, exported_from, and exported_on.
    Also adds a link to the HTML version at the top of the content.
    """
    exported_on = datetime.utcnow().isoformat() + "Z"

    # Match existing frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", content, re.DOTALL)
    if fm_match:
        original_fm = fm_match.group(1)
        body = content[fm_match.end():]
        fm_dict = yaml.safe_load(original_fm) or {}
    else:
        fm_dict = {}
        body = content

    # Update/add required fields
    fm_dict["platform"] = platform
    if exported_from:
        fm_dict["exported_from"] = exported_from
    fm_dict["exported_on"] = exported_on
    if output_file:
        fm_dict["exported_file"] = os.path.basename(output_file)

    # Only keep specific original fields, plus export-added fields
    allowed_original_keys = ["title", "description", "sidebar_position"]
    new_fm = {}

    # Add allowed original fields first (in order)
    for key in allowed_original_keys:
        if key in fm_dict:
            new_fm[key] = fm_dict[key]

    # Add export-added fields (platform, exported_from, exported_on, exported_file)
    export_keys = ["platform", "exported_from", "exported_on", "exported_file"]
    for key in export_keys:
        if key in fm_dict:
            new_fm[key] = fm_dict[key]

    new_frontmatter = "---\n" + yaml.safe_dump(new_fm, sort_keys=False).strip() + "\n---\n\n"
    
    # Build the AI navigation directive
    directive = "> For a complete site index fetch https://docs.agora.io/llms.txt."
    if exported_from and "/en/help/" not in exported_from:
        # Extract product slug from the exported_from URL
        # e.g. https://docs.agora.io/en/conversational-ai/overview/... -> conversational-ai
        path_after_en = exported_from.split("/en/", 1)[-1]
        product_slug = path_after_en.split("/")[0]
        if product_slug:
            overview_url = f"https://docs.agora.io/en/{product_slug}/overview/product-overview.md"
            directive += f" For all pages in this product fetch {overview_url}"
    
    # Add HTML version link if exported_from is available
    html_version_link = ""
    if exported_from:
        clean_url = re.sub(r'\.(mdx?|md)$', '', exported_from)
        html_version_link = f"[HTML Version]({clean_url})\n\n"

    return new_frontmatter + directive + "\n\n" + html_version_link + body

def cleanup_html_tags(text):
    """
    Clean up HTML tags in markdown content:
    - Replace <code></code> with backticks
    - Remove <span> tags but keep enclosed text
    - Remove <sup> and <sub> tags but keep enclosed text
    """
    
    # Replace <code></code> with backticks
    code_pattern = r'<code[^>]*>(.*?)</code>'
    text = re.sub(code_pattern, r'`\1`', text, flags=re.DOTALL)
    
    # Remove <span> tags but keep the text content
    span_pattern = r'<span[^>]*>(.*?)</span>'
    text = re.sub(span_pattern, r'\1', text, flags=re.DOTALL)
    
    # Also handle self-closing span tags
    span_self_closing = r'<span[^>]*/>'
    text = re.sub(span_self_closing, '', text)

    # Remove <sup> and <sub> tags but keep the text content
    text = re.sub(r'<sup[^>]*>(.*?)</sup>', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'<sub[^>]*>(.*?)</sub>', r'\1', text, flags=re.DOTALL)
    
    return text


def apply_final_cleanup(text):
    """
    Apply final cleanup operations to the converted markdown.
    """
    # Clean up HTML tags
    text = cleanup_html_tags(text)
    
    # Remove extra line breaks (existing logic)
    text = re.sub(r'\n([\s\t]*\n){3,}', r'\n\n', text)
    
    return text

# -----Main------

try:
    # Read the input file
    with open(mdxPath, 'r', encoding='utf-8') as file:
        contents = file.read()

    # Load global variables into a dictionary
    file_path = docsPath + '/shared/variables/global.js'
    if not os.path.exists(file_path):
        print(f"Warning: Global variables file not found at {file_path}")
        globalVariables = {}
    else:
        globalVariables = read_variables(file_path)

    # Create product and platform dictionaries to resolve <Vpl> and <Vpd> tags
    product_path = docsPath + '/shared/variables/product.js'
    platform_path = docsPath + '/shared/variables/platform.js'
    
    if not os.path.exists(product_path):
        print(f"Warning: Product dictionary file not found at {product_path}")
        productDict = {}
    else:
        productDict = createDictionary(product_path)
    
    if not os.path.exists(platform_path):
        print(f"Warning: Platform dictionary file not found at {platform_path}")
        platformDict = {}
    else:
        platformDict = createDictionary(platform_path)

    platform_selector = True
    has_platforms = False
    # Extract platform_selector before any processing modifies frontmatter
    original_fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", contents, re.DOTALL)
    platform_selector = True  # Default
    if original_fm_match:
        original_fm_dict = yaml.safe_load(original_fm_match.group(1)) or {}
        platform_selector = original_fm_dict.get("platform_selector", True)

    # Check if product has platforms defined
    is_help_file = "docs-help" in mdxPath
    if product and not is_help_file:
        products_file = os.path.join(args.docs_folder, "data", "v2", "products.js")
        if os.path.exists(products_file):
            product_platforms = load_product_platforms(products_file)
            has_platforms = bool(product_platforms.get(product, []))

    # Resolve import statements 
    # Also resolves PlatformWrapper and ProductWrapper tags
    mdxContents = resolve_imports(mdxPath)

    # Remove React comments
    mdxContents = remove_react_comments(mdxContents)

    # Replace global variables <Vg k="KEY" /> using the dictionary
    regex_pattern = r'<Vg\s+k\s*=\s*"(\w+)"\s*\/?>'
    mdxContents = re.sub(regex_pattern, lambda match: globalVariables.get(match.group(1), match.group(0)), mdxContents)

    # Replace product and platform variables <Vpd k="KEY" />, <Vpl k="KEY" />
    mdxContents = resolve_local_variables(mdxContents, product, productDict, platform, platformDict)

    # Check for ProductOverview component and handle specially
    if '<ProductOverview' in mdxContents:
        mdxContents = resolve_product_overview(mdxContents)

    # Process document header and add title
    mdxContents = resolve_header(mdxContents)

    # NEW: Process standalone ParameterList components BEFORE RestAPILayout
    # This ensures both standalone and nested ParameterList components are handled
    if '<ParameterList' in mdxContents:
        mdxContents = resolve_parameter_list(mdxContents)

    # Check for RestAPILayout component and handle specially
    if '<RestAPILayout' in mdxContents:
        print("RestAPILayout component detected - using specialized conversion")
        mdxContents = resolve_rest_api_layout(mdxContents)

    # Resolve Recipes components to markdown
    mdxContents = resolve_recipes(mdxContents)

    # Resolve Tabs components to markdown
    mdxContents = resolve_tabs(mdxContents)
    
    # Resolve CodeBlock components to markdown fenced code blocks
    mdxContents = resolve_codeblocks(mdxContents)

    # Resolve details/summary components to markdown
    mdxContents = resolve_details(mdxContents)
    
    # Resolve Admonition components to markdown blockquotes
    mdxContents = resolve_admonitions(mdxContents)

    # Remove import statements that are outside code blocks
    mdxContents = remove_imports_outside_codeblocks(mdxContents)

    # Apply final cleanup of platform and product tags (in case any were missed)
    mdxContents = resolve_all_platform_tags(mdxContents, platform)
    
    mdxContents = resolve_all_product_tags(mdxContents, product)
    
    # Remove extra line breaks
    mdxContents = re.sub(r'\n([\s\t]*\n){3,}', r'\n\n', mdxContents)

    # Update hyperlinks and images
    docFolder = os.path.dirname(mdxPath)
    mdxContents = resolve_links_and_images(mdxContents, docFolder, args.docs_folder, images_dir=args.images_dir)

    # Add frontmatter
    normalized_path = mdxPath.replace(os.sep, "/")

    # Check if this is a help file
    is_help_file = "/docs-help/" in normalized_path

    if is_help_file:
        # For help files, strip everything before "docs-help/"
        relative_path = normalized_path.split("/docs-help/", 1)[1]
        # Remove .mdx or .md extension if present
        if relative_path.endswith('.mdx'):
            relative_path = relative_path[:-4]
        elif relative_path.endswith('.md'):
            relative_path = relative_path[:-3]
        
        exported_from = f"https://docs.agora.io/en/help/{relative_path}"
    else:
        # Original docs processing
        if "/docs/" in normalized_path:
            relative_path = normalized_path.split("/docs/", 1)[1]
        else:
            relative_path = os.path.basename(normalized_path)

        # Remove .mdx extension if present
        if relative_path.endswith('.mdx'):
            relative_path = relative_path[:-4]
        elif relative_path.endswith('.md'):
            relative_path = relative_path[:-3]
        
        exported_from = f"https://docs.agora.io/en/{relative_path}"
        if platform and platform_selector and has_platforms:
            exported_from += f"?platform={platform}"

    # Cleanup HTML tags before adding frontmatter
    mdxContents = apply_final_cleanup(mdxContents)

    # Add frontmatter
    mdxContents = add_frontmatter(
        mdxContents,
        mdxPath,
        platform=platform,
        exported_from=exported_from,
        output_file=args.output_file
    )

    # Write the modified contents to a new md file
    if args.output_file:
        # Use exactly what the user provided
        output_path = os.path.abspath(args.output_file)
        output_dir = os.path.dirname(output_path)
        if output_dir:  # Only create directory if there is one
            os.makedirs(output_dir, exist_ok=True)
    else:
        if not os.path.exists('./output'):
            os.makedirs('./output')

        base_name = os.path.splitext(os.path.basename(mdxPath))[0]
        # Append platform unless explicitly disabled in frontmatter
        fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", mdxContents, re.DOTALL)
        if fm_match:
            fm_dict = yaml.safe_load(fm_match.group(1)) or {}
            platform_selector = fm_dict.get("platform_selector", True)
        else:
            platform_selector = True

        if platform_selector and platform:
            outputFilename = f"{base_name}_{platform}.md"
        else:
            outputFilename = f"{base_name}.md"

        output_path = os.path.join('./output', outputFilename)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(mdxContents)

    print(f"Successfully converted {output_path}")
    
except Exception as e:
    import traceback
    print(f"Error processing file: {e}")
    print("Full traceback:")
    traceback.print_exc()
    sys.exit(-3)