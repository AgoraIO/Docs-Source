

<div class="alert note">This guide is provided by Voicemod. Agora is planning a documentation upgrade program for all extensions on the marketplace. Please stay tuned. </div>

## Integrate Voicemod extension

### Download and link to the extension

You can download the libraries and example code from the Agora dashboard.

For Android, place the `aar` file into the libs folder of your project and link to the file, e.g., in `build.gradle` file:

```java
dependencies {
    implementation(name: 'voicemod-audio-filter-extension', ext: 'aar')
        ...
}
```

For iOS (Swift and Objective-C), place the framework package into your Frameworks folder and add the package to your project.

### Enable the extension

**Please note:** There is currently no callback that notifies the app when the extension has been enabled, and enabling the extension can take up to a few seconds.

Android:

```java
public void initializeAgoraEngine() {
    RtcEngineConfig config = new RtcEngineConfig();
    ...
    config.addExtension("VoicemodExtension");
    ...
    ...
    mRtcEngine = RtcEngine.create(config);
    ...
    mRtcEngine.enableExtension("Voicemod", "VoicemodExtension", true);
}
```

iOS (Swift)

```swift
func initializeAgoraEngine() {
    ...
    ...
    self.agoraKit.enableExtension(
        withVendor: "Voicemod", extension: "VoicemodExtension", enabled: true)
}
```

iOS (Objective-C):

```objective-c
- (void)initializeAgoraEngine {
    ...
    ...
    [self.agoraKit enableExtensionWithVendor:@"Voicemod"
                                   extension:@"VoicemodExtension"
                                     enabled:YES];
}
```

### Disable the extension

**Don’t forget to disable the extension when your app closes!** You will eventually be charged for usage, so it’s important that your app disables the extension when exiting the app.

Android:

```java
mRtcEngine.enableExtension("Voicemod", "VoicemodExtension", false);
```

iOS (Swift):

```swift
self.agoraKit.enableExtension(withVendor: "Voicemod", extension: "VoicemodExtension", enabled: false)
```

iOS (Objective-C):

```objective-c
[self.agoraKit enableExtensionWithVendor:@"Voicemod" extension:@"VoicemodExtension" enabled:NO];
```

### Initialize Voicemod

To start the extension, set your project’s API key and API secret

**Please note:** A request to initialise the Voicemod extension will fail unless the extension has been successfully enabled.

Android:

```java
public void initVoicemodSession(String userId) {
    String userData = "{" +
        "\"apiKey\": \"<your API key>\"," +
        "\"apiSecret\": \"<your API secret>\"" +
        "}";
    mRtcEngine.setExtensionProperty("Voicemod", "VoicemodExtension", "vcmd_user_data", userData);
}
```

iOS (Swift):

```swift
func initVoicemodSession() {
    let userData = [
        "apiKey": <your API key>,
        "apiSecret": <your API secret>]
    do {
        let jsonData = try JSONSerialization.data(withJSONObject: userData, options: [.prettyPrinted])
        let jsonString = String(data: jsonData, encoding: .utf8)!
        self.agoraKit.setExtensionPropertyWithVendor("Voicemod", extension: "VoicemodExtension", key: "vcmd_user_data", value: jsonString)
    }

    catch {
        print("JSON serialization failed")
    }

}
```

iOS (Objective-C):

```objective-c
- (void)initVoicemodSession:(NSString *)userId {
    NSDictionary *userData =
        @{@"apiKey" : @"<your API key>", @"apiSecret" : @"<your API secret>"};
    NSError *error;
    NSData *jsonData =
        [NSJSONSerialization dataWithJSONObject:userData
                                        options:NSJSONWritingPrettyPrinted
                                          error:&error];
    NSString *jsonString = [[NSString alloc] initWithData:jsonData
                                                 encoding:NSUTF8StringEncoding];
    [self.agoraKit setExtensionPropertyWithVendor:@"Voicemod"
                                        extension:@"VoicemodExtension"
                                              key:@"vcmd_user_data"
                                            value:jsonString];
}
```

### Enable a voice

**Please note:** A request to set the voice will fail unless the Voicemod extension has been successfully initialized.

Android:

```java
String voice = "\"titan\"";
mRtcEngine.setExtensionProperty("Voicemod", "VoicemodExtension", "vcmd_voice", voice);
```

iOS (Swift):

```swift
let voiceJson = String(format: "\"%@\"", vcmdVoices[row])
self.agoraKit.setExtensionPropertyWithVendor("Voicemod", extension: "VoicemodExtension", key: "vcmd_voice", value: voiceJson)
```

iOS (Objective-C):

```objective-c
NSString* voice = [NSString stringWithFormat:@"\"%@\"", @"titan"];
[self.agoraKit setExtensionPropertyWithVendor:@"Voicemod"
                                    extension:@"VoicemodExtension"
                                          key:@"vcmd_voice"
                                        value:voice];
```

### Disable voices

Android:

```java
String voice = "null";
mRtcEngine.setExtensionProperty("Voicemod", "VoicemodExtension", "vcmd_voice", voice);
```

iOS (Swift):

```swift
let voiceJson = "null"
self.agoraKit.setExtensionPropertyWithVendor("Voicemod", extension: "VoicemodExtension", key: "vcmd_voice", value: voiceJson)
```

iOS (Objective-C):

```objective-c
NSString* voice = @"null";
[self.agoraKit setExtensionPropertyWithVendor:@"Voicemod" extension:@"VoicemodExtension" key:@"vcmd_voice" value:voice];
```

## Reference

### Voicemod Properties

You can configure and control the Voicemod extension using the following properties.

Before you can use the extension, you must provide your API key and API secret by setting the `vcmd_user_data` property.

With the exception of `vcmd_user_data` and `vcmd_version`, the extension must be initialised for Voicemod property accessors to work.

| Property Key           | Property Value                                               | Access   | Description                                        |
| ---------------------- | ------------------------------------------------------------ | -------- | -------------------------------------------------- |
| vcmd_user_data         | object: { apiKey: “<project api key>”, apiSecret: “<project api secret>” } | set      | Set API key, API secret                            |
| vcmd_version           | string: “MAJOR.MINOR.PATCH”                                  | get      | Get Voicemod plugin version                        |
| vcmd_voice             | string                                                       | get, set | Set or get the current voice (“null” for no voice) |
| vcmd_presets           | array of strings: [“magic-chords”, “baby”, “cave”, “titan”, “robot”, “lost-soul”] | get      | Get list of existing voices                        |
| vcmd_background_sounds | boolean                                                      | set      | Toggle background sounds                           |
| vcmd_mute              | boolean                                                      | get, set | Toggle mute audio samples, get current setting     |

### FAQ

**How do I add the extension to my Agora Marketplace App?**

To use the extension, download the file(s) corresponding to your operating system(s) from our [releases repository](https://gitlab.com/voicemod/agora/releases), and follow the instructions in the [documentation page](https://voicemod.gitlab.io/agora/releases/).

**How large is the extension?**

The extension currently uses 14MB of storage space for Android and 32MB for iOS.

**What pricing plans are available?**

The extension is free for all until 31st December 2021, and will be charged at $1/1000 minutes after that.

**What are Voicemod’s Terms and Conditions?**

Please read our [End User License Agreement](https://voicemod.gitlab.io/agora/releases/EULA.html).

**Can I get more voices?**

We will be releasing an extended voice pack soon. Stay tuned!

**Can I use other Voicemod features such as Soundboard?**

We don’t currently support the use of Soundboard within an Agora Marketplace app, but we’re working on it. Stay tuned for v2 of our extension.