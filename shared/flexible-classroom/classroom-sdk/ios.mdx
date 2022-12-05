<PlatformWrapper platform="ios">
This page provides the Swift API reference of the Agora Classroom SDK for iOS.

## AgoraClassroomSDK

`AgoraClassroomSDK` is the basic interface of the Agora Classroom SDK and provides the main methods that can be invoked by your app.

### version

```swift
(NSString *)version;
```

Gets the SDK version.

**Returns**

The SDK version.

### setConfig

```swift
+ (BOOL)setConfig:(AgoraClassroomSDKConfig *)config;
```

Globally configures the SDK.

**Sample code**

```swift
/** Global configuration **/
@interface AgoraClassroomSDKConfig : NSObject
// Agora App ID
@property (nonatomic, copy) NSString *appId;
// Whether to enable eye care mode
@property (nonatomic, assign) BOOL eyeCare;
@end
AgoraClassroomSDKConfig *defaultConfig = [[AgoraClassroomSDKConfig alloc] initWithAppId:appId eyeCare:eyeCare];
[AgoraClassroomSDK setConfig:defaultConfig];
```

**Parameter**

| Parameter | Description |
| :------- | :----------------------------------------------------------- |
| `config` | The SDK global configuration. See [AgoraClassroomSDKConfig](#agoraclassroomsdkconfig). |

### launch

```swift
+ (AgoraEduClassroom * _Nullable)launch:(AgoraEduLaunchConfig *)config
                               delegate:(id<AgoraEduClassroomDelegate> _Nullable)delegate;
```

Launches a flexible classroom.

**Sample code**

```swift
/** Classroom launching configuration */
// The user name
NSString *userName = @"XXX";
// The user ID. Must be the same as the user ID that you use for generating an <Vg k="MESS" /> token.
NSString *userUUid = @"XXX";
// The classroom name
NSString *roomName = @"XXX";
// The classroom ID
NSString *roomUuid = @"XXX";
// The user role
AgoraEduRoleType roleType = AgoraEduRoleTypeStudent;
// The classroom type
AgoraEduRoomType roomType = AgoraEduRoomType1V1;
// The <Vg k="MESS" /> token
NSString *rtmToken = "";
// The start time (ms) of the class, determined by the first user joining the classroom.
NSNumber *startTime = @(XXX);
// The duration (ms) of the class, determined by the first user joining the classroom.
NSNumber *duration = @(1800);

AgoraEduLaunchConfig *config = [[AgoraEduLaunchConfig alloc] initWithUserName:userName userUuid:userUuid roleType:roleType roomName:roomName roomUuid:roomUuid roomType:roomType token:rtmToken startTime:startTime duration:duration];
[AgoraClassroomSDK launch:config delegate:self];
```

**Parameter**

| Parameter | Description |
| :--------- | :----------------------------------------------------------- |
| `config` | The classroom launching configuration. See [AgoraEduLaunchConfig](#agoraedulaunchconfig). |
| `delegate` | The SDK uses the [AgoraEduClassroomDelegate](#agoraeduclassroomdelegate) class to report events related to classroom launching to the app. |

**Returns**

The `AgoraEduClassroom` class.

### configCoursewares

```swift
+ (void)configCoursewares:(NSArray<AgoraEduCourseware *> *)config;
```

Configures courseware downloading.

**Sample code**

```swift
/** Construct, configure, and download the courseware */
// The ID of the courseware conversion task
NSString *taskUuid = @"xxxx";
// The courseware download address
NSString *resourceUrl = [NSString stringWithFormat:@"https://convertcdn.netless.link/dynamicConvert/%@/.zip", taskUuid];
// The courseware name
NSString *resourceName = @"XXX";
// The list of courseware pages
NSArray<WhiteScene*> *convertedFileList = @[];
// The path for storing the courseware
// Agora recommends setting this parameter as the combination of resourceName and name of the first object in convertedFileList
NSString *scenePath = [NSString stringWithFormat:@"%@/%@", resourceName, [convertedFileList.firstObject name]];

AgoraEduCourseware *courseware = [[AgoraEduCourseware alloc] initWithResourceName:resourceName scenePath:scenePath scenes:convertedFileList resourceUrl:resourceUrl];
// Configure the courseware pre-downloading
[AgoraClassroomSDK configCoursewares:@[courseware]];
```

**Parameter**

| Parameter | Description |
| :------- | :----------------------------------------------------------- |
| `config` | The courseware pre-download configuration. See [AgoraEduCourseware](#agoraeducourseware). |

### downloadCoursewares

```
+ (void)downloadCoursewares:(id<AgoraEduCoursewareDelegate> _Nullable)delegate;
```

Pre-downloads the courseware.

**Sample code**

```swift
// Download the configured courseware
[AgoraClassroomSDK downloadCoursewares:self];
```

**Parameter**

| Parameter | Description |
| :--------- | :----------------------------------------------------------- |
| `delegate` | The SDK reports events related to courseware preloading to the app through the [AgoraEduCoursewareDelegate](#agoraeducoursewaredelegate) class. |

### registerExtApps

```swift
+ (void)registerExtApps:(NSArray<AgoraExtAppConfiguration *> *)apps;
```

Register an extension application by using the ExtApp tool. ExtApp is a tool for embedding extension applications in Flexible Classroom. For details, see [Customize Flexible Classroom with ExtApp](/flexible-classroom/develop/customize-ui/).

## AgoraEduClassroom

### destroy

```swift
- (void)destroy;
```

Release the resources occupied by the` AgoraEduClassroom` object.

## AgoraEduClassroomDelegate

The `AgoraEduLaunchCallback` class reports events related to classroom launching to your app.

### didReceivedEvent

```swift
- (void)classroom:(AgoraEduClassroom *)classroom didReceivedEvent:(AgoraEduEvent)event;
```

Reports classroom events.

**Parameter**

| Parameter | Description |
| :------ | :----------------------------------------------- |
| `event` | The classroom events. See [AgoraEduEvent](#agoraeduevent). |

## AgoraEduCoursewareDelegate

The `AgoraEduCoursewareDelegate` class reports events related to courseware preloading to your app.

### didProcessChanged

```swift
- (void)courseware:(AgoraEduCourseware *)courseware didProcessChanged:(float)process;
```

Indicates the progress of courseware pre-downloading.

| Parameter | Description |
| :--------- | :--------------- |
| `progress` | Indicates the progress of courseware pre-downloading. |

### didCompleted

```swift
- (void)courseware:(AgoraEduCourseware *)courseware idCompleted:(NSError * _Nullable)error;
```

Indicates that the courseware pre-downloading completes.

| Parameter | Description |
| :------ | :------- |
| `error` | The error code. |

## Type definition

### AgoraEduEvent

```swift
typedef NS_ENUM(NSInteger, AgoraEduEvent) {
    AgoraEduEventFailed = 0,
    AgoraEduEventReady = 1,
    AgoraEduEventDestroyed =2,
};
```

Classroom events. Reported in the [didReceivedEvent](#didreceivedevent) callback.

| Attributes | Description |
| :----------------------- | :------------------ |
| `AgoraEduEventFailed` | `0`: The user fails to enter the classroom. |
| `AgoraEduEventReady` | `1`: The classroom is ready. |
| `AgoraEduEventDestroyed` | `2`: The classroom has been destroyed. |

### AgoraEduRoleType

```swift
typedef NS_ENUM(NSInteger, AgoraEduRoleType) {
    AgoraEduRoleTypeStudent = 2,
};
```

The role of the user in the classroom. Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Attributes | Description |
| :------------------------ | :---------- |
| `AgoraEduRoleTypeStudent` | `2`: A student. |

### AgoraEduRoomType

```swift
typedef NS_ENUM(NSInteger, AgoraEduRoomType) {
    AgoraEduRoomType1V1 = 0,
    AgoraEduRoomTypeSmall = 4,
    AgoraEduRoomTypeBig = 2,
};
```

The classroom type. Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Attributes | Description |
| :---------------------- | :----------------------------------------------------------- |
| `AgoraEduRoomType1V1` | `0`: One-to-one Classroom. An online teacher gives an exclusive lesson to only one student. |
| `AgoraEduRoomTypeBig` | `2`: Lecture Hall. A teacher gives an online lesson to multiple students. Students do not send their audio and video by default. There is no upper limit on the number of students. During the class, students can "raise their hands" to apply for speaking up. Once the teacher approves, the student can send their audio and video to interact with the teacher. |
| `AgoraEduRoomTypeSmall` | `4`: Small Classroom. A teacher gives an online lesson to multiple students. Students do not send their audio and video by default. The maximum number of users in a classroom is 500. During the class, the teacher can invite students to speak up "on stage" and have real-time audio and video interactions with the teacher. |

### AgoraClassroomSDKConfig

```swift
@interface AgoraClassroomSDKConfig : NSObject
@property (nonatomic, copy) NSString *appId;
@property (nonatomic, assign) BOOL eyeCare;
- (instancetype)initWithAppId:(NSString *)appId;
- (instancetype)initWithAppId:(NSString *)appId
                      eyeCare:(BOOL)eyeCare;
@end
```

The SDK global configuration. Used in [setConfig](#setconfig).

| Attributes | Description |
| :-------- | :----------------------------------------------------------- |
| `appId` | The Agora App ID. See [Get the Agora App ID](../reference/manage-agora-account#get-the-app-id). |
| `eyeCare` | Whether to enable eye care mode:<li>`false`: (Default) Disable eye care mode.</li><li>`true`: Enable eye care mode.</li> |

### AgoraEduLaunchConfig

```swift
@interface AgoraEduLaunchConfig : NSObject
@property (nonatomic, copy) NSString *userName;
@property (nonatomic, copy) NSString *userUuid;
@property (nonatomic, assign) AgoraEduRoleType roleType;
@property (nonatomic, copy) NSString *roomName;
@property (nonatomic, copy) NSString *roomUuid;
@property (nonatomic, assign) AgoraEduRoomType roomType;
@property (nonatomic, copy) NSString *token;
@property (nonatomic, copy) NSNumber *startTime;
@property (nonatomic, copy, nullable) NSNumber *duration;
@property (nonatomic, copy) NSString *region;
@property (nonatomic, strong, nullable) AgoraEduMediaOptions *mediaOptions;
@property (nonatomic, copy, nullable) NSDictionary<NSString *, NSString *> * userProperties;
@property (nonatomic, assign) AgoraEduStreamState videoState;
@property (nonatomic, assign) AgoraEduStreamState audioState;
@property (nonatomic, strong, nullable) AgoraEduVideoEncoderConfiguration *cameraEncoderConfiguration;
@property (nonatomic, assign) AgoraEduLatencyLevel latencyLevel;
@property (nonatomic, assign) AgoraBoardFitMode boardFitMode;

- (instancetype)initWithUserName:(NSString *)userName
                        userUuid:(NSString *)userUuid
                        roleType:(AgoraEduRoleType)roleType
                        roomName:(NSString *)roomName
                        roomUuid:(NSString *)roomUuid
                        roomType:(AgoraEduRoomType)roomType
                           token:(NSString *)token
                       startTime:(NSNumber * _Nullable)startTime
                        duration:(NSNumber * _Nullable)duration
                  userProperties:(NSDictionary<NSString *, NSString *> * _Nullable)userProperties;
@end
```

The classroom launching configuration. Used in [launch](#launch).

| Attributes | Description |
| :--------------------------- | :----------------------------------------------------------- |
| `userName` | The user name for display in the classroom. The string length must be less than 64 bytes. |
| `userUuid` | The user ID. This is the globally unique identifier of a user. **Must be the same as the User ID that you use for generating an <Vg k="MESS" /> token**. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  " {", "}",  "\|",  "~", "," </li>  |
| `roomName` | The room name for display in the classroom. The string length must be less than 64 bytes. |
| `roomUuid` | The room ID. This is the globally unique identifier of a classroom. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  " {", "}",  "\|",  "~", "," </li>  |
| `roleType` | The user's role in the classroom. See `AgoraEduRoleType`. |
| `roomType` | The classroom type. See `AgoraEduRoomType`. |
| `token` | The <Vg k="MESS" /> token used for authentication. For details, see [Generate an <Vg k="MESS" /> Token](/signaling/develop/authentication). |
| `startTime` | The start time (ms) of the class, determined by the first user joining the classroom. |
| `duration` | The duration (ms) of the class, determined by the first user joining the classroom. |
| `region` | The region where the classrooms is located. All clients must use the same region, otherwise, they may fail to communicate with each other. Supported regions are:<li>`CN`: Mainland China</li><li>`AP`: Asia Pacific</li><li>`EU`: Europe</li><li>`NA`: North America</li> |
| `mediaOptions` | Media options, including the media stream encryption configuration. See `AgoraEduMediaOptions` for details. |
| `userProperties` | User properties customized by the developer. For details, see [How can I set user properties? ](/help/integration-issues/agora_class_custom_properties) |
| `videoState` | Controls whether students automatically send audio or video streams after they go onto the "stage". See  `AgoraEduStreamState`. |
| `audioState` | Controls whether students automatically send audio or video streams after they go onto the "stage". See  `AgoraEduStreamState`. |
| `cameraEncoderConfiguration` | The encoding configurations of the video stream captured by the camera, including the width and height, frame rate, and bitrate. For details, see `AgoraEduVideoEncoderConfiguration`. |
| `latencyLevel` | The latency level of an audience member. See `AgoraEduLatencyLevel`. |
| `boardFitMode` | The PPT display mode on the whiteboard. See `AgoraBoardFitMode`. |

### AgoraBoardFitMode

```swift
@objc public enum AgoraBoardFitMode: Int {
    case auto, retain
}
```

The PPT display mode on the whiteboard. Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Parameter | Description |
| :------- | :----------------------------------------------------------- |
| `auto` | (Default) The PPT display mode is fit, which means uniformly scaling the PPT until one of its dimensions fits the boundary. |
| `retain` | In this mode, if the student manually adjusts the PPT size, the client maintains this size no matter what class the student joins. |

### StreamState

```swift
@objc public enum AgoraEduStreamState: Int {
    case off = 0, on, `default`
}
```

Controls whether students automatically send audio or video streams after they go onto the "stage". Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Parameter | Description |
| :---- | :--------------- |
| `off` | (Default) Students do not automatically send audio and video streams after they go onto the "stage". |
| `on` | Students automatically send audio and video streams after they go onto the "stage". |

### AgoraEduLatencyLevel

```java
@objc public enum AgoraEduLatencyLevel: Int {
    case low = 0
    case ultraLow
}
```

The latency level of an audience member. Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Parameter | Description |
| :--------- | :--------------------------------------------------------- |
| `low` | Low latency. The latency from the sender to the receiver is 1500 ms to 2000 ms. |
| `ultraLow` | (Default) Ultra-low latency. The latency from the sender to the receiver is 400 ms to 800 ms. |

### AgoraEduMediaOptions

```swift
@interface AgoraEduMediaOptions : NSObject
@property (nonatomic, strong) AgoraEduMediaEncryptionConfig *encryptionConfig;

- (instancetype)initWithConfig:(AgoraEduMediaEncryptionConfig *)encryptionConfig;
@end
```

Media options. Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Parameter | Description |
| :----------------- | :----------------------------------------------------------- |
| `encryptionConfig` | The media stream encryption configuration. See [AgoraEduMediaEncryptionConfig](#agoraedumediaencryptionconfig) for details. |

### AgoraEduVideoEncoderConfiguration

```swift
@interface AgoraEduVideoEncoderConfiguration : NSObject
@property (nonatomic, assign) NSUInteger width;
@property (nonatomic, assign) NSUInteger height;
@property (nonatomic, assign) NSUInteger frameRate;
@property (nonatomic, assign) NSUInteger bitrate;
@property (nonatomic, assign) AgoraEduCoreMirrorMode mirrorMode;

- (instancetype)initWithWidth:(NSUInteger)width
                       height:(NSUInteger)height
                    frameRate:(NSUInteger)frameRate
                      bitrate:(NSUInteger)bitrate
                   mirrorMode:(AgoraEduCoreMirrorMode)mirrorMode;
@end
```

The classroom launching configuration. See `AgoraEduLaunchConfig`.

> - In the Small Classroom scenario, the default resolution is 120p (160*120).
> - In the One-to-one Classroom and Lecture Hall scenarios, the default resolution is 240p (320*240).

| Parameter | Description |
| :----------- | :-------------------------------------------- |
| `width` | Width (pixel) of the video frame. |
| `height` | Height (pixel) of the video frame. |
| `frameRate` | The frame rate (fps) of the video. The default value is 15. |
| `bitrate` | The bitrate (Kbps) of the video. The default value is 200. |
| `mirrorMode` | Video mirror modes. See `EduMirrorMode`. |

### AgoraEduMediaEncryptionConfig

```swift
@interface AgoraEduMediaEncryptionConfig : NSObject
@property (nonatomic, assign) AgoraEduMediaEncryptionMode mode;
@property (nonatomic, copy) NSString *key;

- (instancetype)initWithMode:(AgoraEduMediaEncryptionMode)mode key:(NSString *)key;
@end
```

The media stream encryption configuration. Used in [AgoraEduMediaOptions](#agoraedumediaoptions).

| Parameter | Description |
| :----- | :----------------------------------------------------------- |
| `mode` | Encryption mode. See [AgoraEduMediaEncryptionMode](#agoraedumediaencryptionmode). |
| `key` | The encryption key. |

### AgoraEduMediaEncryptionMode

```swift
typedef NS_ENUM(NSInteger, AgoraEduMediaEncryptionMode) {
    AgoraEduMediaEncryptionModeAES128XTS = 1,
    AgoraEduMediaEncryptionModeAES128ECB = 2,
    AgoraEduMediaEncryptionModeAES256XTS = 3,
    AgoraEduMediaEncryptionModeAES128GCM = 5,
    AgoraEduMediaEncryptionModeAES256GCM = 6,
};
```

Media stream encryption mode. Set in [AgoraEduMediaEncryptionConfig](#agoraedumediaencryptionconfigs).

| Parameter | Description |
| :------------------------------------- | :-------------------------- |
| `AgoraEduMediaEncryptionModeAES128XTS` | 128-bit AES encryption, XTS mode. |
| `AgoraEduMediaEncryptionModeAES128ECB` | 128-bit AES encryption, ECB mode. |
| `AgoraEduMediaEncryptionModeAES256XTS` | 256-bit AES encryption, XTS mode. |
| `AgoraEduMediaEncryptionModeAES128GCM` | 128-bit AES encryption, GCM mode. |
| `AgoraEduMediaEncryptionModeAES256GCM` | 256-bit AES encryption, GCM mode. |

### AgoraEduCoreMirrorMode

```swift
@objc public enum AgoraEduCoreMirrorMode: Int {
    case auto = 0, enabled, disabled
}
```

Whether to enable mirror mode.

| Parameter | Description |
| :--------- | :--------------------- |
| `auto` | The SDK disables mirror mode by default. |
| `enabled` | Enable mirror mode. |
| `disabled` | Disable mirror mode. |

### AgoraEduCourseware

```swift
@interface AgoraEduCourseware : NSObject
@property (nonatomic, copy) NSString *resourceName;
@property (nonatomic, copy) NSString *scenePath;
@property (nonatomic, copy) NSString *resourceUrl;
@property (nonatomic, strong) NSArray<WhiteScene *> *scenes;
- (instancetype)initWithResourceName:(NSString *)resourceName
                           scenePath:(NSString *)scenePath
                              scenes:(NSArray<WhiteScene *> *)scenes
                         resourceUrl:(NSString *)resourceUrl;
@end
```

The courseware pre-download configuration. Used in [configCoursewares](#configcoursewares).

| Attributes | Description |
| :------------- | :----------------------------------------------------------- |
| `resourceName` | The file name. |
| `scenePath` | The local path for storing the file. Agora recommends setting this parameter as the combination of `resourceName` and the `name` of the first `SceneInfo` object in `scenes`. |
| `resourceUrl` | The URL address of the file, such as `"https://convertcdn.netless.link/dynamicConvert/{taskUuid}.zip".` |
| `scenes` | A list of converted file pages, an array of `WhiteScene` objects. Flexible Classroom automatically converts files with the suffixes of `"ppt"`, `"pptx"`, `"doc"`, `"docx"`, and `"pdf"` to formats that can be displayed on the whiteboard in the classroom and then display the file on the whiteboard in pages. Each `WhiteScene` object represents one page. |

### WhiteObject

```swift
@interface WhiteScene : WhiteObject

- (instancetype)init;
- (instancetype)initWithName:(nullable NSString *)name ppt:(nullable WhitePptPage *)ppt;

@property (nonatomic, copy, readonly) NSString *name;
@property (nonatomic, assign, readonly) NSInteger componentsCount;
@property (nonatomic, strong, readonly, nullable) WhitePptPage *ppt;

@end
```

The detailed information of a page. Set in [AgoraEduCourseware](#agoraeducourseware).

| Attributes | Description |
| :---------------- | :--------------------------------------------------------- |
| `componentsCount` | The number of pages. |
| `ppt` | The detailed information of a converted page. See `WhitePptPage`. |
| `name` | The page name. |

### WhitePptPage

```swift
@interface WhitePptPage : WhiteObject

- (instancetype)initWithSrc:(NSString *)src size:(CGSize)size;
- (instancetype)initWithSrc:(NSString *)src preview:(NSString *)url size:(CGSize)size;

@property (nonatomic, copy) NSString *src;
@property (nonatomic, assign) CGFloat width;
@property (nonatomic, assign) CGFloat height;
@property (nonatomic, copy, readonly) NSString *previewURL;
@end
```

The detailed information of a converted page. Set in [SceneInfo](#sceneinfo).

| Attributes | Description |
| :----------- | :------------------------------------------ |
| `src` | The URL address of the converted page. |
| `width` | The width (pixel) of the page. |
| `height` | The height (pixel) of the page. |
| `previewURL` | The URL address of the preview image generated after the dynamic file conversion. |

</PlatformWrapper>