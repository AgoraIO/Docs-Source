<PlatformWrapper platform="android">
This page provides the Kotlin API reference of the Agora Classroom SDK for Android.

## AgoraClassSdk

`AgoraClassSdk` is the basic interface of the Agora Classroom SDK and provides the main methods that can be invoked by your app.

### version

```java
public static String version();
```

Gets the SDK version.

**Returns**

The SDK version.



### setConfig

```java
public static void setConfig(AgoraEduSDKConfig agoraEduSDKConfig);
```

Globally configures the SDK.

**Sample code**

```java
/** Global Configuration */
// Agora App ID
String appId = "XXX";
// Whether to enable eye care mode
boolean eyeCare = false;
AgoraClassSdk.setConfig(new AgoraClassSdkConfig(appId, eyeCare));
```

**Parameter**

| Parameter | Description |
| :------------------ | :----------------------------------------------------------- |
| `agoraEduSDKConfig` | The SDK global configuration. See [AgoraClassSdkConfig](#agoraclasssdkconfig). |

### launch

```java
public static AgoraEduClassRoom launch(@NotNull Context context,
                                       @NotNull AgoraEduLaunchConfig config,
                                       @NotNull AgoraEduLaunchCallback callback);
```

Launches a flexible classroom.

**Sample code**

```java
/** Classroom launching configuration */
// The user name
String userName = "XXX";
// The user ID. Must be the same as the user ID that you use for generating an <Vg k="MESS" /> token.
String userUuid = "XXX";
// The classroom name
String roomName = "XXX";
// The classroom ID
String roomUuid = "XXX";
// The user role
int roleType = AgoraEduRoleType.AgoraEduRoleTypeStudent.getValue();
// The classroom type
int roomType = AgoraEduRoomType.AgoraEduRoomType1V1.getValue()/AgoraEduRoomType.AgoraEduRoomTypeSmall.getValue()/AgoraEduRoomType.AgoraEduRoomTypeBig.getValue();
// The <Vg k="MESS" /> token
String rtmToken = "";
// The start time (ms) of the class, determined by the first user joining the classroom.
long startTime = System.currentTimeMillis() + 100;
// The duration (ms) of the class, determined by the first user joining the classroom.
long duration = 310L;
// The region where the classroom is located. All clients must set the same region, otherwise, they may fail to communicate with each other.
String region = AgoraEduRegion.cn;

AgoraEduLaunchConfig agoraEduLaunchConfig = new AgoraEduLaunchConfignew AgoraEduLaunchConfig(
    userName, userUuid, roomName, roomUuid, roleType,
    roomType, rtmToken, startTime, duration, region, null, null,
    AgoraBoardFitMode.Retain, streamState, AgoraEduLatencyLevel.AgoraEduLatencyLevelUltraLow,
    null, null);
AgoraClassSdk.launch(MainActivity2.this, agoraEduLaunchConfig, (state) -> {
    Log.e(TAG, "launch-classroom-state:" + state.name());
});
```

**Parameter**

| Parameter | Description |
| :--------- | :----------------------------------------------------------- |
| `context` | The context of the app. |
| `config` | The classroom launching configuration. See [AgoraEduLaunchConfig](#agoraedulaunchconfig). |
| `callback` | The SDK uses the [AgoraEduLaunchCallback](#agoraedulaunchcallback) class to report events related to classroom launching to the app. |

**Returns**

The `AgoraEduClassRoom` class.



### configCourseWare

```java
public static void configCourseWare(@NotNull List<AgoraEduCourseware> coursewares);
```

Configures courseware downloading.

**Sample code**

```java
/** Construct and configure courseware */
// Configure the courseware
String taskUuid = "xxxxx";
// The courseware download address
String resourceUrl = String.formate("https://convertcdn.netless.link/dynamicConvert/{taskUuid}.zip", taskUuid);
// The courseware name
String resourceName = "xxxxxxx"
// The list of courseware pages
List<SceneInfo> sceneInfos = new ArrayList();
// The link of a converted page
String src = "http://xxxxxxx";
Ppt ppt = new Ppt(src, 360, 640);
SceneInfo sceneInfo = new SceneInfo(1, ppt, "ppt-file-name");
List<SceneInfo> sceneInfos = new ArrayList();
sceneInfos.add(sceneInfo);
// The path for storing the courseware
String scenePath = resourceName + "/" + sceneInfos.get(0).name;
AgoraEduCourseware courseware = new AgoraEduCourseware(resourceName, scenePath, sceneInfos, resourceUrl);
List<AgoraEduCourseware> wares = new ArrayList();
wares.add(courseware);
// Configure the courseware pre-downloading
configCoursewares(wares);
```

**Parameter**

| Parameter | Description |
| :------ | :----------------------------------------------------------- |
| `wares` | The courseware pre-download configuration. See [AgoraEduCourseware](#agoraeducourseware). |

### downloadCourseWare

```java
public static void downloadCourseWare(@NotNull Context context, @Nullable AgoraEduCoursewarePreloadListener listener)
        throws Exception;
```

Pre-downloads the courseware.

**Sample code**

```java
// Download the configured courseware
downloadCoursewares(activityContext, new AgoraEduCoursewarePreloadListener() {
    @Override
    public void onStartDownload(@NotNull AgoraEduCourseware ware) {
    }
    @Override
    public void onProgress(@NotNull AgoraEduCourseware ware, double progress) {
    }
    @Override
    public void onComplete(@NotNull AgoraEduCourseware ware) {
    }
    @Override
    public void onFailed(@NotNull AgoraEduCourseware ware) {
    }
});
```

**Parameter**

| Parameter | Description |
| :--------- | :----------------------------------------------------------- |
| `context` | The context of the app. |
| `listener` | The SDK reports events related to courseware preloading to the app through the [AgoraEduCoursewarePreloadListener](#agoraeducoursewarepreloadlistener) class. |


### registerExtensionApp

```java
public static void registerExtensionApp(List<AgoraExtAppConfiguration> apps);
```

Register an extension application by using the ExtApp tool. ExtApp is a tool for embedding extension applications in Flexible Classroom. For details, see [Customize Flexible Classroom with ExtApp](/flexible-classroom/develop/customize-ui/).

## AgoraEduLaunchCallback

The `AgoraEduLaunchCallback` class reports events related to classroom launching to the app.

### onCallback

```java
void onCallback(AgoraEduEvent state);
```

Reports classroom events.

| Parameter | Description |
| :------ | :----------------------------------------------- |
| `state` | The classroom events. See [AgoraEduEvent](#agoraeduevent). |

## AgoraEduCoursewarePreloadListener

The `AgoraEduCoursewarePreloadListener` class reports events related to courseware preloading to the app.

### onStartDownload

```java
void onStartDownload(@NotNull AgoraEduCourseware ware);
```

Indicates that the SDK starts downloading the courseware.

| Parameter | Description |
| :----- | :----------------------------------------------------------- |
| `ware` | The courseware pre-download configuration. See [AgoraEduCourseware](#agoraeducourseware). |

### onProgress

```java
void onProgress(@NotNull AgoraEduCourseware ware, double progress);
```

Indicates the progress of courseware pre-downloading.

| Parameter | Description |
| :--------- | :----------------------------------------------------------- |
| `ware` | The courseware pre-download configuration. See [AgoraEduCourseware](#agoraeducourseware). |
| `progress` | Indicates the progress of courseware pre-downloading. |

### onComplete

```java
void onComplete(@NotNull AgoraEduCourseware ware);
```

Indicates that the courseware pre-downloading completes.

| Parameter | Description |
| :----- | :----------------------------------------------------------- |
| `ware` | The courseware pre-download configuration. See [AgoraEduCourseware](#agoraeducourseware). |



### onFailed

```java
void onFailed(@NotNull AgoraEduCourseware ware);
```

The courseware pre-downloading fails.

| Parameter | Description |
| :----- | :----------------------------------------------------------- |
| `ware` | The courseware pre-download configuration. See [AgoraEduCourseware](#agoraeducourseware). |

## Type definition

### AgoraClassSdkConfig

```java
public class AgoraClassSdkConfig {
    @NotNull
    private String appId;
    private int eyeCare;
}
```

The SDK global configuration. Used in [setConfig](#setconfig).

| Attributes | Description |
| :-------- | :----------------------------------------------------------- |
| `appId` | The Agora App ID. See [Get the Agora App ID](../reference/manage-agora-account#get-the-app-id). |
| `eyeCare` | Whether to enable eye care mode:<li>`0`: (Default) Disable eye care mode.</li><li>`1`: Enable eye care mode.</li> |

### AgoraEduLaunchConfig

```kotlin
class AgoraEduLaunchConfig(val userName: String,
                           val userUuid: String,
                           val roomName: String,
                           val roomUuid: String,
                           val roleType: Int = AgoraEduRoleType.AgoraEduRoleTypeStudent.value,
                           val roomType: Int,
                           val rtmToken: String,
                           val startTime: Long?,
                           val duration: Long?,
                           val region: String,
                           var videoEncoderConfig: EduVideoEncoderConfig? = null,
                           val mediaOptions: AgoraEduMediaOptions?,
                           val boardFitMode: AgoraBoardFitMode,
                           val streamState: StreamState?,
                           val latencyLevel: AgoraEduLatencyLevel? = AgoraEduLatencyLevel.AgoraEduLatencyLevelUltraLow,
                           val userProperties: MutableMap<String, String>? = null,
                           val widgetConfigs: MutableList<UiWidgetConfig>? = null) : Parcelable
```

The classroom launching configuration. Used in [launch](#launch).

| Attributes | Description |
| :------------------- | :----------------------------------------------------------- |
| `userName` | The user name for display in the classroom. The string length must be less than 64 bytes. |
| `userUuid` | The user ID. This is the globally unique identifier of a user. **Must be the same as the User ID that you use for generating an <Vg k="MESS" /> token**. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  " {", "}",  "\|",  "~", "," </li>  |
| `roomName` | The room name for display in the classroom. The string length must be less than 64 bytes. |
| `roomUuid` | The room ID. This is the globally unique identifier of a classroom. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  " {", "}",  "\|",  "~", "," </li>   |
| `roleType` | The role of the user in the classroom. See  [AgoraEduRoleType](#agoraeduroletype). |
| `roomType` | The classroom type. See [AgoraEduRoomType](#agoraeduroomtype). |
| `rtmToken` | The <Vg k="MESS" /> token used for authentication. For details, see [Generate an <Vg k="MESS" /> Token](/flexible-classroom/develop/authentication-workflow/). |
| `startTime` | The start time (ms) of the class, determined by the first user joining the classroom. |
| `duration` | The duration (ms) of the class, determined by the first user joining the classroom. |
| `region` | The region where the classrooms is located. All clients must use the same region, otherwise, they may fail to communicate with each other. See [AgoraEduRegionStr](#agoraeduregionstr). |
| `videoEncoderConfig` | Video encoding configurations, including the width and height, frame rate, and bitrate. See [EduVideoEncoderConfig](#eduvideoencoderconfig) |
| `mediaOptions` | The media options, including media encryption configurations. See [AgoraEduMediaOptions](#agoraedumediaoptions). |
| `boardFitMode` | The PPT display mode. See [AgoraBoardFitMode](#agoraboardfitmode). |
| `streamState` | Controls whether students automatically send audio or video streams after they go onto the "stage". See [StreamState](#streamstate). |
| `latencyLevel` | The latency level of an audience member. See [AgoraEduLatencyLevel](#agoraedulatencylevel). |
| `userProperties` | User properties customized by the developer. For details, see [How can I set user properties? ](/help/integration-issues/agora_class_custom_properties) |


### AgoraEduEvent

```java
public enum AgoraEduEvent {
    AgoraEduEventFailed(0),
    AgoraEduEventReady(1),
    AgoraEduEventDestroyed(2),
    AgoraEduEventForbidden(3);
}
```

Classroom events. Reported in [onCallback](#oncallback).

| Attributes | Description |
| :----------------------- | :------------------------ |
| `AgoraEduEventFailed` | `0`: The user fails to enter the classroom. |
| `AgoraEduEventReady` | `1`: The classroom is ready. |
| `AgoraEduEventDestroyed` | `2`: The classroom has been destroyed. |
| `AgoraEduEventForbidden` | `3`: The user is forbidden by the Flexible Classroom cloud service and not allowed to enter the classroom. |

### AgoraEduRoleType

```java
public enum AgoraEduRoleType {
   AgoraEduRoleTypeStudent(2);
}
```

The role of the user in the classroom. Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Attributes | Description |
| :------------------------ | :---------- |
| `AgoraEduRoleTypeStudent` | `2`: A student. |



### AgoraEduRoomType

```java
public enum AgoraEduRoomType {
   AgoraEduRoomType1V1(0),
   AgoraEduRoomTypeSmall(4),
   AgoraEduRoomTypeBig(2);
}
```

The classroom type. Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Attributes | Description |
| :---------------------- | :----------------------------------------------------------- |
| `AgoraEduRoomType1V1` | `0`: One-to-one Classroom. An online teacher gives an exclusive lesson to only one student. |
| `AgoraEduRoomTypeBig` | `2`: Lecture Hall. A teacher gives an online lesson to multiple students. Students do not send their audio and video by default. There is no upper limit on the number of students. During the class, students can "raise their hands" to apply for speaking up. Once the teacher approves, the student can send their audio and video to interact with the teacher. |
| `AgoraEduRoomTypeSmall` | `4`: Small Classroom. A teacher gives an online lesson to multiple students. Students do not send their audio and video by default. The maximum number of users in a classroom is 500. During the class, the teacher can invite students to speak up "on stage" and have real-time audio and video interactions with the teacher. |

### AgoraBoardFitMode

```java
public enum AgoraBoardFitMode {
    Auto,
    Retain;
}
```

The PPT display mode on the whiteboard. Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Parameter | Description |
| :------- | :----------------------------------------------------------- |
| `Auto` | (Default) The PPT display mode is fit, which means uniformly scaling the PPT until one of its dimensions fits the boundary. |
| `Retain` | In this mode, if the student manually adjusts the PPT size, the client maintains this size no matter what class the student joins. |

### StreamState

```java
data class StreamState (
        var videoState:Int,
        var audioState:Int
)
```

Controls whether students automatically send audio or video streams after they go onto the "stage". Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Parameter | Description |
| :----------- | :----------------------------------------------------------- |
| `videoState` | Whether to send the video stream:<li>`0`: (Default) Do not send the video stream.</li><li>`1`: Send the video stream.</li> |
| `audioState` | Whether to send the audio stream:<li>`0`: (Default) Do not send the audio stream.</li><li>`1`: Send the audio stream.</li> |

### AgoraEduLatencyLevel

```java
enum class AgoraEduLatencyLevel(val value: Int) {
    AgoraEduLatencyLevelLow(1),
    AgoraEduLatencyLevelUltraLow(2);
}
```

The latency level of an audience member. Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Parameter | Description |
| :----------------------------- | :--------------------------------------------------------- |
| `AgoraEduLatencyLevelLow` | Low latency. The latency from the sender to the receiver is 1500 ms to 2000 ms. |
| `AgoraEduLatencyLevelUltraLow` | (Default) Ultra-low latency. The latency from the sender to the receiver is 400 ms to 800 ms. |

### AgoraEduMediaOptions

```kotlin
class AgoraEduMediaOptions(val encryptionConfigs: AgoraEduMediaEncryptionConfigs?)
```

Media options. Set in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

| Parameter | Description |
| :----------------- | :----------------------------------------------------------- |
| `encryptionConfig` | The media stream encryption configuration. See [AgoraEduMediaEncryptionConfig](#agoraedumediaencryptionconfig) for details. |

### AgoraEduMediaEncryptionConfig

```kotlin
data class AgoraEduMediaEncryptionConfigs(
        val encryptionKey: String?,
        val encryptionMode: Int
)
```

The media stream encryption configuration. Used in [AgoraEduMediaOptions](#agoraedumediaoptions).

| Parameter | Description |
| :----- | :------------------------------------- |
| `mode` | The encryption mode. See `AgoraEduEncryptMode`. |
| `key` | The encryption key. |

### AgoraEduEncryptMode

```kotlin
enum class AgoraEduEncryptMode(val value: Int) {
    NONE(0),
    AES_128_XTS(1),
    AES_128_ECB(2),
    AES_256_XTS(3),
    SM4_128_ECB(4),
    AES_128_GCM(5),
    AES_256_GCM(6);
}
```

The media stream encryption configuration. See [AgoraEduMediaEncryptionConfig](#agoraedumediaencryptionconfig) for details.

| Parameter | Description |
| :------------ | :-------------------------- |
| `NONE` | No encryption. |
| `AES_128_XTS` | 128-bit AES encryption, XTS mode. |
| `AES_128_ECB` | 128-bit AES encryption, ECB mode. |
| `AES_256_XTS` | 256-bit AES encryption, XTS mode. |
| `SM4_128_ECB` | 128-bit ECB encryption, SM4 mode. |
| `AES_128_GCM` | 128-bit AES encryption, GCM mode. |
| `AES_256_GCM` | 256-bit AES encryption, GCM mode. |

### AgoraEduCourseware

```java
data class AgoraEduCourseware(
        val resourceName: String?,
        val scenePath: String?,
        val scenes: List<SceneInfo>?,
        val resourceUrl: String?
) {
}
```

The courseware pre-download configuration. Used in [configCoursewares](#configcoursewares).

| Attributes | Description |
| :------------- | :----------------------------------------------------------- |
| `resourceName` | The file name. |
| `scenePath` | The local path for storing the file. Agora recommends setting this parameter as the combination of `resourceName` and `name` of the first `SceneInfo` object in `scenes`, such as, `resourceName + "/" + sceneInfos.get(0).name`. |
| `scenes` | A list of converted file pages, an array of `SceneInfo` objects. Flexible Classroom automatically converts files with the suffixes of `"ppt"`, `"pptx"`, `"doc"`, `"docx"`, and `"pdf"` to formats that can be displayed on the whiteboard in the classroom and then display the file on the whiteboard in pages. Each `SceneInfo` object represents one page. |
| `resourceUrl` | The URL address of the file, such as `"https://convertcdn.netless.link/dynamicConvert/{taskUuid}.zip"`. |

### SceneInfo

```java
public class SceneInfo {
    private int componentCount;
    private Ppt ppt;
    private String name;
}
```

The detailed information of a page. Set in [AgoraEduCourseware](#agoraeducourseware).

| Attributes | Description |
| :--------------- | :-------------------------------------------------------- |
| `componentCount` | The number of pages. |
| `ppt` | The detailed information of a converted page. See [Ppt](#ppt). |
| `name` | The page name. |

### Ppt

```java
public class Ppt {
    private String src;
    private double width;
    private double height;
}
```

The detailed information of a page displayed on the whiteboard. Set in [SceneInfo](#sceneinfo).

| Attributes | Description |
| :------- | :------------------------------ |
| `src` | The URL address of the converted page. |
| `width` | The width (pixel) of the page. |
| `height` | The height (pixel) of the page. |

### AgoraEduRegion

```java
object AgoraEduRegion {
    const val default = "CN"
    const val cn = "CN"
    const val na = "NA"
    const val eu = "EU"
    const val ap = "AP"
}
```

Regions.

| Attributes | Description |
| :--- | :----------------- |
| `CN` | Mainland China. |
| `NA` | North America. |
| `EU` | Europe. |
| `AP` | Asia Pacific. |

### EduVideoEncoderConfig

```java
data class EduVideoEncoderConfig(
        var videoDimensionWidth: Int = 320,
        var videoDimensionHeight: Int = 240,
        var frameRate: Int = 15,
        var bitrate: Int = 200,
        var mirrorMode: Int = EduMirrorMode.AUTO.value
)
```

The video encoder configuration. Used in [AgoraEduLaunchConfig](#agoraedulaunchconfig).

> - In the Small Classroom scenario, the default resolution is 120p (160*120).
- In the One-to-one Classroom and Lecture Hall scenarios, the default resolution is 240p (320*240).

| Parameter | Description |
| :----------- | :----------------------------------- |
| `width` | Width (pixel) of the video frame. |
| `height` | Height (pixel) of the video frame. |
| `frameRate` | The frame rate (fps) of the video. The default value is 15. |
| `bitrate` | The bitrate (Kbps) of the video. The default value is 200. |
| `mirrorMode` | Video mirror modes. See `EduMirrorMode`. |



### EduMirrorMode

```kotlin
enum class EduMirrorMode(val value: Int) {
    AUTO(0),
    ENABLED(1),
    DISABLED(2)
}
```

Whether to enable mirror mode. Used in [EduVideoEncoderConfig](#eduvideoencoderconfig).

| Parameter | Description |
| :--------- | :--------------------- |
| `AUTO` | The SDK disables mirror mode by default. |
| `ENABLED` | Enable mirror mode. |
| `DISABLED` | Disable mirror mode. |

</PlatformWrapper>