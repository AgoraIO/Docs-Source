

<div class="alert note">This guide is provided by Bose PinPoint. Agora is planning a documentation upgrade program for all extensions on the marketplace. Please stay tuned. </div>

The Bose PinPoint extension reduces noise from the local microphone signal. To use our extension you just need to call the standard Agora-provided methods.

## Integrate Bose PinPoint extension

### Download and link to the extension

First, activate the extension in the Agora Developer Console on your project. Activate the extension by clicking **Activate** and agree to the prompt. Enable the extension on the projects you wish to integrate the PinPoint Extension with. Finally click **View**, under **Credentials**, on that project and make note of the API Key and API Secret.

Add the `Android Archive` file, `agora-pinpoint-release.aar` to your project, and note the directory. In this example the file `agora-pinpoint-release.aar` was added to the `app/libs` directory. Then add the dependency to the app's `build.gradle` by adding the line `implementation(files("libs/agora-pinpoint-release.aar"))` under dependencies

On iOS the `.framework` file has to be embedded in your project, on Android set up the `.aar` file as a dependency. 

### Getting started

To configure the extension, use the `setExtensionPropertyWithVendor` method. You need to set your API Key and API Secret values using this method. You can find these values for your project in the Agora Extensions Marketplace. 

Android:

You can also find the example app in the `android/example` directory in the extension package. Go to the section titled Using The Example Projects for more information about running the example projects. 

```java
mRtcEngine.setExtensionProperty("Bose", "PinPoint", "apiKey", "EXAMPLE_API_KEY"); mRtcEngine.setExtensionProperty("Bose", "PinPoint", "apiSecret", "EXAMPLE_API_SECRET");
```

iOS:

You can also find the example app in the `ios/example/` directories in the extension package. Go to the section titled Using The Example Projects for more information about running the example projects.

```objective-c
[self.agoraKit setExtensionPropertyWithVendor:@"Bose"
                                    extension:@"PinPoint"
                                          key:@"apiKey"
                                        value:@"EXAMPLE_API_KEY"];
[self.agoraKit setExtensionPropertyWithVendor:@"Bose"
                                    extension:@"PinPoint"
                                          key:@"apiSecret"
                                        value:@"EXAMPLE_API_SECRET"];
```

### Adding the extension

To add the extension to your instance of RtcEngine include the following call to addExtension when setting up your RtcEngineConfig

Android:

```java
RtcEngineConfig config = new RtcEngineConfig();
config.mContext = this;
config.mAppId = AppConfig.appId;
config.addExtension(ExtensionManager.EXTENSION_NAME);
config.mExtensionObserver = this;
config.mEventHandler = new IRtcEngineEventHandler() {
```

### Enabling the extension

Android:

```java
PinPoint.configure(getAssets());
mRtcEngine.enableExtension(“Bose”, ”PinPoint”, true);
```

iOS (Objective-C):

```objective-c
[self.agoraKit enableExtensionWithVendor:@"Bose"
                               extension:@"PinPoint"
                                 enabled:YES];
```

After the extension is enabled and the settings are validated, it starts reducing the noise from the local microphone signal automatically

## Run the demo

Download Agora Video SDK from Agora Extensions Marketplace and copy the zip file into the `libs/` directory and unzip them. You will need to have at least version 4.0.0 beta to use Extensions.

Android: 

Open `android/example/app/src/main/java/agoramarketplace/bose/pinpoint/AppConfig.java` 

Set your Agora appID and token (if using one) found in the Agora console

```java
final static String appId = "YOUR_APP_ID";
final static String apiKey = "YOUR_API_KEY";
final static String apiSecret = "YOUR_API_SECRET";
```

Set your Bose PinPoint Extension apiKey and apiSecret found in the Agora Extensions Marketplace.

If only one device is available to test with, you can join the channel by entering your App ID and channel name, which defaults to agora_extension using one of the [Agora Examples](https://webdemo.agora.io/agora-web-showcase/examples/Agora-Web-Tutorial-1to1-Web/)

iOS:

Open `AgoraWithPinPoint.xcodeproj` provided in the `ios/examples` directory.

Download Agora’s SDKs and copy `Agoraffmpeg.xcframework` and `AgoraRtcKit.xcframework` into the `libs/ directory`. Add the frameworks to your project by navigating to Project settings -> General -> Frameworks, Libraries and Embedded Content in XCode.

After creating an Agora App in the Agora console, open the file `ios/example/AgoraWithPinPoint/AppID.m`. Set your Agora appID and token (if using one) found in the Agora console

```objective-c
NSString *const appID = <#Your App Id#>;
NSString *const token = <#Temp Access Token#>;
```

Then open `ios/example/AgoraWithPinPoint/VideoChatViewController.m` Set your Bose PinPoint Extension apiKey and apiSecret found in the Agora console.

## Reference

### Troubleshooting

Android:

If the app crashes immediatly after setting the room name try these troubleshooting options: 

1. Confirm that apiKey, apiSecret, appID and token (if used) are set in the app and match the values present in the Agora Dev Console and Agora . 

iOS:

If `[self.agoraKit enableExtensionWithVendor:@"Bose" extension:@"PinPoint" enabled:YES]` is returning a negative number. Try these troubleshooting options: 

1. Confirm that apiKey, apiSecret, appID and token (if used) are set in the app and match the values present in the Agora Dev Console and Agora.
2. If it’s still returning a negative number, make sure the `.framework` has been manually added to the Xcode project by adding the Framework to, **Frameworks, Libraries, and Embedded Content**.
3. If while setting up the example app, you receive an error message stating dyld: library not loaded make sure the framework has been marked as, **Embed & Sign**, instead of the default, **Do not Embed**.