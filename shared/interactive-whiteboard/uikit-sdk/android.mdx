<PlatformWrapper platform="android">

This page provides the API reference for the Fastboard SDK.

## FastboardView class

### getFastboard

```java
public Fastboard getFastboard()
```

Get the `Fastboard` object.

The Fastboard SDK does not support initializing a `Fastboard` instance directly. To get the `Fastboard` object, you need to add the `FastboardView` object to the app's layout, and then call the `getFastboard` method.

**Note**

Call this method to obtain the `Fastboard` object before calling other APIs.

**Returns**

The `Fastboard` object is returned when the method call is successful.

## Fastboard class

The Fastboard class provides methods for creating `FastRoom` objects.

### createFastRoom

```java
public FastRoom createFastRoom(FastRoomOptions roomOptions)
```
Create a `FastRoom` object.

**Note**

Call this method after obtaining the `Fastboard` object.

**Parameters**

- `roomOptions`: Configuration options for the whiteboard room. See <a href="#roomoptions">FastRoomOptions</a> for details.

**Returns**

A `FastRoom` object is returned when the method call is successful.

<a name="roomoptions"></a>
### FastRoomOptions

Whiteboard room configuration options.

```java
public class FastRoomOptions {
     private final String appId;
     private final String uuid;
     private final String token;
     private final String uid;
     private final boolean writable;

     private final FastRegion fastRegion;

     private Float containerSizeRatio;

     private FastUserPayload userPayload;

     public FastRoomOptions(String appId, String uuid, String token, String uid, FastRegion fastRegion) {
         this(appId, uuid, token, uid, fastRegion, true);
     }

     public FastRoomOptions(String appId, String uuid, String token, String uid, FastRegion fastRegion, boolean writable) {
         this.appId = appId;
         this.uuid = uuid;
         this.token = token;
         this.uid = uid;
         this.fastRegion = fastRegion;
         this.writable = writable;
     }
}
```

The `FastRoomOptions` class contains the following properties:

- `appId`: String. App Identifier for the interactive whiteboard project. For details, see [Get security credentials for your whiteboard project](../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).
- `uuid`: String. The UUID of the room, which is the unique identifier of the room. For details, see [Create a room (POST)](../reference/whiteboard-api/room-management#create-a-room-post) for the value of the `uuid` parameter in the response package body after the request is successful.
- `token`: String. Room Token of the room, used for user authentication when joining the room. It can be obtained in the following ways:
  - Call the [Generate a room token (POST)](../develop/generate-token-rest#generate-a-room-token-post) RESTful API.
    - Build a token generator at your app server. See [Generate a token at app server](../develop/generate-token-app-server).
  - `uid`: String. The unique identifier of a user in string format. The maximum length is 1,024 bytes. Ensure that the `uid` of each user in the same room is unique.
  - `writable`: boolean. Whether the user joins the whiteboard room in interactive mode:
    - `true`: Join the whiteboard room in interactive mode, that is, with read and write permissions.
    - `false`: Join the whiteboard room in subscription mode, that is, with read-only permission.
  - `fastRegion`: The data center, which must be the same as the data center you chose when [creating the whiteboard room](../reference/whiteboard-api/room-management#create-a-room-post). See <a href="#fastregion">FastRegion</a>.
- `containerSizeRatio`: Float. In the local display window, the aspect ratio of the content is `0.56` by default, which is `9:16`.
- `userPayload`: User information displayed by the user's cursor, including the user's nickname and avatar. See <a href="#fastuserpayload">`FastUserPayload`</a> for details.

<a name="fastregion"></a>
### FastRegion

Data center, containing the following enumeration values:

- `CN_HZ`: Hangzhou, China, the service area covers East Asia, Southeast Asia, and other areas not covered by the data center.

- `US_SV`: Silicon Valley, USA, the service area covers North America and South America.

- `SG`: Singapore, the service area covers Singapore, East Asia, and Southeast Asia.

- `IN_MUM`: Mumbai, India, the service area covers India.

- `EU`: London, UK, the service area covers Europe.

<a name="fastuserpayload"></a>
### FastUserPayload

```java
public class FastUserPayload {
     private final String nickName;
     private final String avatar;

     public FastUserPayload(String nickName) {
         this(nickName, null);
     }

     public FastUserPayload(String nickName, String avatar) {
         this.nickName = nickName;
         this.avatar = avatar;
     }
}
```

`FastUserPayload` object, used to store the user information displayed on the cursor, contains the following member variables:

- `nickName`: String. The user's nickname displayed on the user's cursor.

- `avatar`: String. (Optional) The user avatar displayed on the user cursor, the URL address corresponding to the avatar should be passed in.

## FastRoom class

The `FastRoom` class provides methods for managing interactive whiteboard real-time rooms.

### join [1/2]

```java
public void join()
```

Join a whiteboard room.

**Note**

This method needs to be called after the `FastRoom` object is successfully created.

### join [2/2]

```java
public void join(@Nullable OnRoomReadyCallback onRoomReadyCallback)
```

Join a whiteboard room.

**Note**

This method needs to be called after the `FastRoom` object is successfully created.

**Parameters**

- `onRoomReadyCallback`: <a href="#roomready">OnRoomReadyCallback</a> interface instance. Passing in `null` means not to register the interface.

<a name="roomready"></a>
### OnRoomReadyCallback

The `OnRoomReadyCallback` interface is used to send room event notifications to the app and includes the following member methods:

```java
void onRoomReady(FastRoom fastRoom);
```

Room ready callback.

**Parameters**

- `fastRoom`: `FastRoom` object.

### isReady

```java
public boolean isReady()
```

Get whether the room is ready.

After calling the `join` method, you need to call this method to get whether the room is ready. After the room is ready, other methods in the `FastRoom` class can be called to operate the whiteboard.

**Returns**

Is the room ready?

- `true`: ready.
- `false`: Not ready yet.

### isWritable

```java
public boolean isWritable()
```

Get whether the local user's current interactive whiteboard real-time room is in interactive mode.

**Returns**

Get whether the local user is in interactive mode:

- `true`: interactive mode, that is, with read and write permissions.
- `false`: Subscription mode, that is, with read-only permissions.

### redo

```java
public void redo()
```

Redo, that is, roll back the undo operation.

### setWritable [1/2]

```java
public void setWritable(boolean writable)
```

Set whether the user is in interactive mode in the room.

**Note**

This method needs to be called after the room is ready.

**Parameters**

- `writable`: whether the user is in interactive mode in the room:
   - `true`: interactive mode, that is, with read and write permissions.
   - `false`: Subscription mode, that is, with read-only permissions.

### setWritable [2/2]

```java
public void setWritable(boolean writable, FastResult<Boolean> result)
```

Set whether the user is in interactive mode in the room.

**Note**

This method needs to be called after the room is ready.

**Parameters**

- `writable`: whether the user is in interactive mode in the room:
   - `true`: interactive mode, that is, with read and write permissions.
   - `false`: Subscription mode, that is, with read-only permissions.
- `result`: The result of the `setWritable` method call. See <a href="#result">FastResult</a> for details. Passing in the `FastResult` instance, the SDK will trigger the callback implemented in the `FastResult` interface and report whether the `setWritable` method call is successful; passing in `null` means not to listen to the callback.


### undo

```java
public void undo()
```

Undo the previous operation.

### setStrokeColor

```java
public void setStrokeColor(@ColorInt int color)
```

Set the line color.

**Parameters**

- `color`: int. Line color, RGB format, for example `0x0000FF` means blue

### setAppliance

```java
public void setAppliance(FastAppliance fastAppliance)
```

Set the currently used whiteboard tool.

**Parameters**

- `fastAppliance`: Whiteboard tool. See <a href="#appliance">FastAppliance</a> for details.
<a name="appliance"></a>
### FastAppliance

Whiteboard tool, containing the following enumeration values:

- `CLICKER(Appliance.CLICKER)`: Click tool. Currently mainly used for clicking content on HTML5 files.

- `SELECTOR(Appliance.SELECTOR)`: Select tool.

- `PENCIL(Appliance.PENCIL)`: Pencil.

- `RECTANGLE(Appliance.RECTANGLE)`: Rectangle tool.

- `ELLIPSE(Appliance.ELLIPSE)`: Ellipse tool.

- `TEXT(Appliance.TEXT)`: text tool.

- `ERASER(Appliance.ERASER)`: Eraser tool.

- `LASER_POINTER(Appliance.LASER_POINTER)`: Laser pointer.

- `ARROW(Appliance.ARROW)`: Arrow.

- `STRAIGHT(Appliance.STRAIGHT)`: Straight line.

- `PENTAGRAM(Appliance.SHAPE, ShapeType.Pentagram)`: Pentagram.

- `RHOMBUS(Appliance.SHAPE, ShapeType.Rhombus)`: rhombus.

- `TRIANGLE(Appliance.SHAPE, ShapeType.Triangle)`: triangle.

- `BUBBLE(Appliance.SHAPE, ShapeType.SpeechBalloon)`: Speech bubble.

- `OTHER_CLEAR()`: Clear the whiteboard content.


### setStrokeWidth

```java
public void setStrokeWidth(int width)
```

Set the width of the line.

**Parameters**

- `width`: int. Line width (px).

### cleanScene

```java
public void cleanScene()
```

Clear the whiteboard content.

### setWritable

```java
public void setWritable(boolean writable)
```

Set whether the user is in interactive mode in the room.

**Parameters**

- `writable`: boolean. Whether the user is in interactive mode:
   - `true`: interactive mode, that is, with read and write permissions.
   - `false`: Subscription mode, that is, with read-only permissions.

### insertImage

```java
public void insertImage(String url, int width, int height)
```

Insert picture.

This method can insert and display the specified network image onto the current whiteboard page.

**Parameters**

- `url`: String. The URL address of the image. Please ensure that the app client can access the URL, otherwise the image will not be displayed properly.
- `width`: int. The width of the image (px).
- `height`: int. The height of the image (px).

### insertVideo

```java
public void insertVideo(String url, String title)
```

Insert and play audio and video in the whiteboard sub-window.

**Parameters**

- `url`: URL address of audio and video files. Please ensure that the app client can access the URL, otherwise the audio and video files cannot be loaded normally.
- `title`: window title.

### insertDocs

```java
public void insertDocs(FastInsertDocParams params, FastResult<String> result)
```

Insert and display documents in the whiteboard subwindow.

After successfully initiating the [document conversion task](whiteboard-api/file-conversion), you can call this method and pass in the relevant parameters of the converted document. The SDK will automatically create a sub-window, insert and display the converted document in pages.

**Parameters**

- `params`: Insert the parameter settings of the document. See <a href="#docparams">FastInsertDocParams</a> for details.
- `result`: `insertDocs` method call result. See <a href="#result">FastResult</a> for details. Passing in the `FastResult` instance, the SDK will trigger the callback implemented in the `FastResult` interface and report whether the `insertDocs` method call is successful; passing in `null` means not to listen to the callback.


<a name="docparams"></a>
### FastInsertDocParams

Document parameter settings.

```java
public class FastInsertDocParams {
     private String taskUUID;
     private String taskToken;
     private FastRegion region;
     private ConverterType converterType;
     private String fileType;
     private Boolean dynamicDoc;
     private String title;
}
```

The `FastInsertDocParams` class contains the following properties:

- `taskUUID`: String. Task UUID of the document conversion task, that is, [Initiate document conversion task API](whiteboard-api/file-conversion). When the request is successful, the uuid parameter in the response package body value.
- `taskToken`: String. The Task Token of the document conversion task must be consistent with the Task Token passed in when [Initiate document conversion task](whiteboard-api/file-conversion).
- `converterType`: enumeration. The version of the document conversion service, the values are as follows:
   - `Projector`: new version. For details, see [New version of document conversion service](../develop/file-conversion-overview).
   - `WhiteboardConverter`: legacy (default). For details, see [Old version of the document conversion service](file-conversion-overview-deprecated).
- `fileType`: String. Document type:
   - `pdf`: static document.
   - `pptx`: dynamic document.
- `dynamicDoc`: boolean. Whether the document conversion task type is a dynamic conversion task.
- `title`: String. Window title.


### setFastStyle

```java
public void setFastStyle(FastStyle style)
```

Style the whiteboard user interface.

**Parameters**

- `style`: The style of the whiteboard user interface. See <a href="#faststyle">FastStyle</a> for details.

<a name="faststyle"></a>
### FastStyle

Whiteboard user interface style.

```java
public class FastStyle {
     private int mainColor;
     private boolean darkMode;

     public FastStyle() {
     }

     public int getMainColor() {
         return mainColor;
     }

     public void setMainColor(@ColorInt int color) {
         this.mainColor = color;
     }

     public boolean isDarkMode() {
         return darkMode;
     }

     public void setDarkMode(boolean darkMode) {
         this.darkMode = darkMode;
     }

     public FastStyle copy() {
         FastStyle style = new FastStyle();
         style.mainColor = mainColor;
         style.darkMode = darkMode;
         return style;
     }
}
```

The `FastStyle` class contains the following member methods:

**getMainColor**

Gets the theme color of the whiteboard user interface.

**Returns**

The theme color for the whiteboard user interface.

**setMainColor**

Set the theme color of the whiteboard user interface.

This method can set the color of some button borders and prompt text when the whiteboard is loaded.

**Parameters**

- `color`: The theme color of the whiteboard user interface, RGB format, for example `0x0000FF` means blue.

**isDarkMode**

Gets whether the whiteboard user interface is in dark mode.

**Returns**

- `true`: Whiteboard user interface is in dark mode.
- `false`: The whiteboard user interface is in light mode.

**setDarkMode**

Set the whiteboard user interface to dark mode.

**Parameters**

- `darkMode`: whether to use dark mode:

  - `true`: dark mode.
  - `false`: light mode.


### setResource

```java
public void setResource(FastResource fastResource)
```

Set resources related to whiteboard color.

**Parameters**

- `fastResource`: Whiteboard color-related resources. See <a href="#fastresource">FastResource</a> for details.

<a name="fastresource"></a>
### FastResource

Resources related to whiteboard colors.

```java
public class FastResource {
     @ColorInt
     public int getBackgroundColor(boolean darkMode) {
         return color(darkMode
                 ? R.color.fast_dark_mode_bg
                 : R.color.fast_light_mode_bg
         );
     }

     @ColorInt
     public int getBoardBackgroundColor(boolean darkMode) {
         return getBackgroundColor(darkMode);
     }
}
```

Contains the following member methods, all of which can be overridden to customize colors:

**getBackgroundColor**

Get the background color of the whiteboard control.

**Parameters**

- `darkMode`: boolean. Whether the background color of the whiteboard control is dark mode:
   - `true`: dark mode.
   - `false`: light mode.

**Returns**

Hexadecimal color value.

**getBoardBackgroundColor**

Get the whiteboard background color.

**Note**

If you do not override this method, `getBackgroundColor` will be called by default.

**Parameters**

- `darkMode`: boolean. Whether the whiteboard background color is dark mode:
   - `true`: dark mode.
   - `false`: light mode.

**Returns**

Hexadecimal color value.


## FastUiSettings class

The `FastUiSettings` class provides methods for setting up the whiteboard user interface.

### showRoomController

```java
public void showRoomController(ControllerId... ids)
```

Demonstrates controls on a whiteboard user interface.

**Parameters**

- `ids`: The identifier of the control. See <a href="#controllerId">ControllerId</a> for details.

### hideRoomController

```java
public void hideRoomController(ControllerId... ids)
```

Hides controls on the whiteboard user interface.

**Parameters**

- `ids`: The identifier of the control. See <a href="#controllerId">ControllerId</a> for details.

<a name="controllerId"></a>
### ControllerId

Controls on the whiteboard user interface, including the following enumeration values:

- `RedoUndo`: redo and undo buttons.
- `ToolBox`: Toolbar.
- `PageIndicator`: Page indicator.

### setToolsExpandAppliances

```java
public static void setToolsExpandAppliances(List<List<FastAppliance>> toolsExpandAppliances)
```

Sets the tool set included in the toolbar in expanded mode.

If the default toolbar provided by Fastboard SDK cannot meet your needs, you can call this method to customize the tools contained in the toolbar and set the toolbar to expand mode. You can pass in a secondary tool list in this method. The elements in the primary list will be expanded and displayed on the toolbar, and the elements in the secondary list will be collapsed.

After successfully calling the `setToolsExpandAppliances` method, if you need to switch the toolbar to collapsed mode, you can call <a href="#settoolboxexpand">setToolboxExpand</a>.

**Note**

This method needs to be called before joining the whiteboard room.

**Parameters**

- `toolsExpandAppliances`: Tools included in the toolbar in expanded mode. See <a href="#appliance">FastAppliance</a> for details.

**Example**

```java
ArrayList<List<FastAppliance>> config = new ArrayList<>();
config.add(Arrays.asList(
         FastAppliance.CLICKER,
         FastAppliance.PENCIL,
         FastAppliance.TEXT,
         FastAppliance.SELECTOR,
         FastAppliance.ERASER
));
config.add(Arrays.asList(FastAppliance.SELECTOR));
config.add(Arrays.asList(FastAppliance.PENCIL));
config.add(Arrays.asList(FastAppliance.TEXT));
config.add(Arrays.asList(FastAppliance.ERASER));
config.add(Arrays.asList(
         FastAppliance.STRAIGHT,
         FastAppliance.ARROW,
         FastAppliance.RECTANGLE,
         FastAppliance.ELLIPSE,
         FastAppliance.PENTAGRAM,
         FastAppliance.RHOMBUS,
         FastAppliance.BUBBLE,
         FastAppliance.TRIANGLE
));
config.add(Arrays.asList(FastAppliance.OTHER_CLEAR));

FastUiSettings.setToolsExpandAppliances(config);
```

### setToolsCollapseAppliances

```java
public static void setToolsCollapseAppliances(List<FastAppliance> toolsCollapseAppliances)
```

Sets the tool set included in the toolbar in collapsed mode.

If the default toolbar provided by Fastboard SDK cannot meet your needs, you can call this method to customize the tools included in the toolbar and set the toolbar to fold mode. You can pass in a first-level tool list in this method, and the elements in the list will be collapsed on the toolbar by default.

After successfully calling the `setToolsCollapseAppliances` method, if you need to switch the toolbar to expanded mode, you can call <a href="#settoolboxexpand">setToolboxExpand</a>.

**Note**

This method needs to be called before joining the whiteboard room.

**Parameters**

- `toolsCollapseAppliances`: Tools included in the whiteboard toolbar. See <a href="#appliance">FastAppliance</a> for details.

**Example**

```java
ArrayList<FastAppliance> collapseAppliances = new ArrayList<>();
collapseAppliances.add(FastAppliance.PENCIL);
collapseAppliances.add(FastAppliance.ERASER);
collapseAppliances.add(FastAppliance.ARROW);
collapseAppliances.add(FastAppliance.SELECTOR);
collapseAppliances.add(FastAppliance.TEXT);
collapseAppliances.add(FastAppliance.OTHER_CLEAR);

FastUiSettings.setToolsCollapseAppliances(collapseAppliances);
```

### setToolsColors

```java
public static void setToolsColors(List<Integer> toolsColors)
```

Set the color used by the whiteboard tool.

This method sets the color of graphics, lines, or text drawn using the whiteboard tool.

**Note**

This method needs to be called before joining the whiteboard room.

**Parameters**

- `toolsColors`: Color of whiteboard tools, RGB format, for example `0x0000FF` means blue.

### setToolboxEdgeMargin

```java
public void setToolboxEdgeMargin(int margin)
```

Set the margins between the whiteboard toolbar and the sides.

The definition of the margin is determined by the toolbar position set in `setToolboxGravity`:

- The toolbar is located on the left side of the whiteboard: the margin refers to the distance between the left side of the toolbar and the left side of the whiteboard.
- The toolbar is located on the right side of the whiteboard: the margin refers to the distance between the right side of the toolbar and the right side of the whiteboard.

**Parameters**

- `margin`: int. The distance between the toolbar and the side of the whiteboard, in `px`.

### setToolboxGravity

```java
public void setToolboxGravity(int gravity)
```

Set the position of the toolbar on the whiteboard.

**Parameters**

- `gravity`: The position of the toolbar on the whiteboard:

  - `Gravity.LEFT`: left.
  - `Gravity.RIGHT`: Right.


<a name="settoolboxexpand"></a>
### setToolboxExpand

```java
public void setToolboxExpand(boolean expand)
```

Set whether to expand the toolbar.

The default display state of the toolbar is related to the device. It is expanded by default on tablets and collapsed by default on mobile phones. You can call this method to modify the display state of the toolbar.

**Parameters**

- `expand`: Whether to expand the toolbar:
   - `true`: expand.
   - `false`: fold.


<a name="result"></a>
## FastResult

The result of the method call.

```java
public interface FastResult<T> {
   void onSuccess(T value);
   void onError(Exception exception);
}
```

The `FastResult` interface reports the results of method calls and includes the following callback methods:

- `onSuccess`: callback when the method call is successful.
- `onError`: callback when an error occurs.

</PlatformWrapper>