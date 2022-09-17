
## Migrate from v1.1.5 to v2.1.0

In v2.1.0, Agora fully optimizes the internal architecture of the Agora Classroom SDK and refactors the Agora Edu Context APIs.

This section lists the major changes of the Edu Context API between v2.1.0 and v1.1.5.

<div class="alert info">To learn more about the Agora Edu Context API v2.1.0, see the <a href="/en/agora-class/API%20Reference/edu_context_kotlin/v2.1.0/API/edu_context_api_overview.html" target="_blank">API reference</a>.</div>

### Chat context

Remove `ChatContext` and `IChatHandler`.

### Whiteboard context

Remove `WhiteboardContext` and `IWhiteboardHandler`. In v2.1.0, the whiteboard feature is implemented in `AgoraUIKit`.

### Device context

Remove `DeviceContext` and `IDeviceHandler`. Use methods and callbacks in `MediaContext` and `IMediaHandler` instead, as follows:

- Remove `getDeviceConfig`. Use `getLocalDeviceState` instead.
- Remove `setCameraDeviceEnable`, `switchCameraFacing`, `setMicDeviceEnable`, and `setSpeakerEnable`. Use `openSystemDevice` and `closeSystemDevice` instead.
- Remove `setDeviceLifecycle`. In v2.1.0, the SDK does not maintain the device state.
- Remove `onCameraDeviceEnableChanged`, `onCameraFacingChanged`, `onMicDeviceEnabledChanged`, and `onSpeakerEnabledChanged`. Use `onLocalDeviceStateUpdated` instead.
- Remove `onDeviceTips`.

### Hands-up context

Remove `HandsUpContext` and `IHandsUpHandler`. Use methods and callbacks in `UserContext` and `IUserHandler` instead, as follows:

- Remove `performHandsUp`. Use `handsWave` and `handsDown` instead.
- Remove `onHandsUpEnabled`. Use `onHandsWaveEnabled` instead.
- Remove `onHandsUpStateUpdated`and `onHandsUpStateResultUpdated`. Use `onUserHandsWave` and `onUserHandsDown` instead.
- Remove `onHandsUpTips`.

### Room context

- Remove `roomInfo`. Use `getRoomInfo` instead.
- Remove `leave`. Use `leaveRoom` instead.
- Move `uploadLog` to `MonitorContext`.
- Remove `updateFlexRoomProps`. Use `updateRoomProperties` and `deleteRoomProperties` instead.
- Rename `joinClassroom` as `joinRoom`.
- Remove `onClassroomName`. You can call `getRoomInfo` to get the room name.
- Rename `onClassState` as `onClassStateUpdated`.
- Remove `onClassTime`.
- Remove `onNetworkStateChanged`. Use `onLocalNetworkQualityUpdated` in `IMonitorHandler` instead.
- Remove `onLogUploaded`. You can get the log `serailNumber` with the callback function in the `uploadLog` method in` MonitorContext`.
- Remove `onConnectionStateChanged`. Use `onLocalConnectionUpdated` in `IMonitorHandler` instead.
- Remove `onClassTip`.
- Remove `onFlexRoomPropsInitialized`. To get room custom properties after joining the room, you can call `getRoomProperties`.
- Remove `onFlexRoomPropsChanged`. Use `onRoomPropertiesUpdated` and `onRoomPropertiesDeleted` instead.
- Remove `onError`.
- Remove `onClassroomJoinSuccess` and `onClassroomJoinFail`. Use `callback` in `joinRoom` instead.
- Remove `onClassroomLeft`. Use `onRoomClosed` instead.

### Screen-sharing context

- Remove `ScreenShareContext`. Use `StreamContext` instead. When `videoSourceType` in `AgoraEduContextStreamInfo` is `Screen`, you can regard this stream as a screen-sharing video stream.
- Remove `IScreenShareHandler`. Use `IStreamHandler` instead. Remove `onUpdateScreenShareState`. Use `onStreamJoined`, `onStreamLeft`, and `onStreamUpdated` in `IStreamHandler` instead.

### User context

- Remove `localUserInfo`. Use `getLocalUserInfo` instead.
- Remove `muteVideo` and `muteAudio`. Use `muteStreams` in `StreamContext` instead.
- Remove `renderVideo`. Use `startRenderLocalVideo` and `startRenderRemoteVideo` in `MediaContext` instead.
- Remove `updateFlexUserProps`. Use `updateUserProperties` and `deleteUserProperties` instead.
- Remove `setVideoEncoderConfig`.  Use `setLocalVideoConfig` in `StreamContext` instead.
- Remove `onUserListUpdated`. Us `getAllUserList` and `getUserList` in `UserContext` and `onRemoteUserJoined`, `onRemoteUserLeft`, and `onUserUpdated ` in `UserHandler` instead.
- Remove `onCoHostListUpdated`. Use `onCoHostUserListAdded` and `onCoHostUserListRemoved` instead. You can also get the information of all on-stage users through `getCoHostList` in `UserContext`.
- Rename `onUserReward` to `onUserRewarded`.
- Rename `onKickOut` as `onLocalUserKickedOut`.
- Remove `onUserTip` and `onRoster`.
- Remove `onFlexUserPropsChanged`. Use `onUserPropertiesUpdated` and `onUserPropertiesDeleted` in `IUserHandler` instead. You can also get custom user properties through `getUserProperties` in `UserContext`.