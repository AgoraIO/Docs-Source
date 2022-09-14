export const COMPANY = 'Agora';
export const URL_ROOT = 'https://docs.agora.io/en';
export const AGORA_BACKEND = `${COMPANY} SD-RTN`;
export const CLIENT = platform => (platform === 'unity' ? 'game' : 'app');

export const API_REF_ROOT = 'https://agora-api-reference.vercel.app/video-sdk';
export const API_REF_ROOT_VOICE_SDK = 'https://agora-api-reference.vercel.app/voice-sdk';
export const API_REF_OLD = 'https://docs.agora.io/en/Video/API%20Reference';
export const API_REF_WEB_ROOT = `${API_REF_ROOT}/web/4.13.0`;
export const API_REF_ANDROID_ROOT  = `${API_REF_ROOT}/java_ng/API`;
export const API_REF_IOS_ROOT = `${API_REF_ROOT}/ios/4.0.0-beta.2/API`;
export const API_REF_IOS_ROOT_VOICE_SDK = `${API_REF_ROOT_VOICE_SDK}/ios/4.0.0-beta.2/API`;
export const API_REF_MACOS_ROOT = `${API_REF_ROOT}/macos/4.0.0-beta.2/API`;
export const API_REF_IOS_MAC_VOICE_SDK = `${API_REF_ROOT_VOICE_SDK}/macos/4.0.0-beta.2/API`;
export const API_REF_RN_ROOT  = `${API_REF_ROOT}/rn_ng/API`;
export const API_REF_ROOT_VOICE = `${URL_ROOT}/voice-call-4.x-beta/API%20Reference`;
export const API_REF_RN_ROOT_VOICE = `${API_REF_ROOT_VOICE}/rn_ng/API`;
export const API_REF_FLUTTER_ROOT = `${API_REF_ROOT}/flutter/4.0.0-beta.2/API`;
export const API_REF_FLUTTER_ROOT_VOICE_SDK = `${API_REF_ROOT_VOICE_SDK}/flutter/4.0.0-beta.2/API`;
export const API_REF_UNITY_ROOT = `${API_REF_ROOT}/unity/4.0.0.beta-2/API`;
export const API_REF_UNITY_ROOT_VOICE_SDK = `${API_REF_ROOT_VOICE_SDK}/unity/4.0.0.beta-2/API`;
export const API_REF_ELECTRON_ROOT  = `${API_REF_ROOT}/electron_ng/API`;

export const CONSOLE = `${COMPANY} Console`;
export const TOKEN = 'token';

export const ENGINE = `${COMPANY} Engine`;
export const RTE = 'Real-Time Engagement';
export const RTEC = `${RTE} Core`;
export const RTES = `${RTE} SDK`;
export const APP_ID_LINK = `http://agora.io`;
export const AGORA_CONSOLE_URL = `http://console.agora.io`;
export const API_REF_ANDROID = `http://api.agora.io/android`;
export const LINK_APP_ID = `[Generate a temporary token](../reference/manage-agora-account#get-the-app-id)`;

export const PLATFORM = 'dummy';

export const VIDEO = 'Video Calling';
export const AUDIO = 'Voice Calling';
export const ASDK = 'Voice SDK';
export const ILS = 'Interactive Live Streaming';
export const ILSS = 'Interactive Live Streaming Standard';
export const ILSP = 'Interactive Live Streaming Premium';
export const VSDK = 'Video SDK';
export const VSDK_RELEASE = '4.x';
export const VSDK_PREVIOUS_RELEASE = '3.7.x';
export const VSDK_RELEASE_FOLDER = 'video-call-4.x-beta';

export const AV = 'Audio/Video';
export const AV_URL = `${URL_ROOT}/video`;

export const MESS = 'Signalling';
export const MESS_SDK = `${MESS} SDK`;
export const SIG = `${MESS}`;
export const CHAT = `Chat`;
export const PS = 'Pub-Sub';
export const PUSH = 'Push Notifications';

export const ACC = 'Acceleration';
export const ACCM = 'Media Accelerator';
export const ACCG = 'Global Accelerator';

export const TEMPL = 'Templates';

export const RTEE = 'Extensions';
export const AA = `${COMPANY} Analytics`;
export const WHITE = 'Interactive Whiteboard';
export const EM = `${RTEE} Marketplace`;
export const MS = 'Media Services';
export const MPUSH = 'Media Push';
export const MPULL = 'Media Pull';
export const REC = 'Recording';
export const MOD = 'Moderation';
export const CP = 'Cloud Proxy';
export const RTMPC = 'RTMP Converter';
export const TRANS = 'Transcoding';
export const OPREC = 'On-premise Recording';
export const CREC = 'Cloud Recording';

export const UCS = 'Use Cases';

export const AB = 'App Builder';
export const UIK = 'UI Kit';
export const vUIK = `Video ${UIK}`;
export const FC = 'Flexible Classroom';

export const WEB = 'Web';
export const IOS = 'iOS';
export const MAC = 'macOS';
export const AND = 'Android';
export const WIN = 'Windows';

export const ELE = 'Electron';
export const UNI = 'Unity';
export const FLU = 'Flutter';
export const REA = 'React Native';
export const COC = 'Cocos Creator';
export const CO2_AN = 'Cocos2d-x-Android';
export const SS = 'Server side';

export const ATW = 'Technical Writer';
export const ADR = 'DevReller';
export const ADEV = 'Developer';
export const AQA = 'Tester';
export const APO = 'Product Owner';

export const REPO_URL = 'https://gitlab.com/billy-the-fish/asciidoc-test';
export const AGORA_DOCS_URL = 'https://docs.agora.io/en';
export const DOWNLOAD_URL = 'https://download.agora.io/sdk/release';
export const AGORA_PLATFORM_FOLDER = 'Agora%20Platform';

export const API_REF_FOLDER = 'API%20Reference';
export const API_REF_WEB = 'https://docs.agora.io/en/Video/API%20Reference/web_ng';

export const APP_LINK = `${AGORA_DOCS_URL}/${AGORA_PLATFORM_FOLDER}/get_appid_token#get-the-app-id[App ID]`;

export const APP_CERTIFICATE_LINK =
"https://agoradocs.vercel.app/video-calling/reference/manage-agora-account/#get-the-app-certificate";

export const DEMO_BASIC_VIDEO_CALL_URL =
  'https://webdemo.agora.io/agora-websdk-api-example-4.x/basicVideoCall/index.html';

export const DEMO_PAGE_LINK = `<Link to="{{Global.DEMO_BASIC_VIDEO_CALL_URL}}"><Vg k="COMPANY" /> web demo</Link>`;

export const TOKEN_GENERATE_LINK = `<Link to="https://docs.agora.io/en/Agora%20Platform/get_appid_token?platform=All#generate-a-temporary-token">Generate a temporary token</Link>`;
export const TOKEN_GENERATE_URL = `https://docs.agora.io/en/Agora%20Platform/get_appid_token?platform=All#generate-an-rtc-temporary-token`;

export const AGORA_DYNAMIC_KEY_CODE_BASE_URL =
  'https://github.com/AgoraIO/Tools/tree/master/DynamicKey/AgoraDynamicKey';

export const ANDROID_UIKIT_VERSION = '4.0.1';
export const ANDROID_UIKIT_SDK = 'com.github.AgoraIO-Community.Android-UIKit:final';

export const WEB_UIKIT = 'Agora React Web UI Kit';

export const IOS_MI_PACKAGE_VERSION = '4.0.0-rc.1';
export const IOS_PACKAGE = 'NAME: AgoraRtcEngine_iOS';
export const IOS_VOICE_PACKAGE = 'AgoraRtcEngine_iOS_Voice_Beta';

export const UIKIT_GH_HUB = 'https://github.com/AgoraIO-Community/.github/wiki/Agora-Video-UIKit'
export const UIKIT_PACKAGE_IOS = 'https://github.com/AgoraIO-Community/VideoUIKit-iOS'
export const UIKIT_PACKAGE_ANDROID = 'https://github.com/AgoraIO-Community/Android-UIKit'
export const UIKIT_PACKAGE_MACOS = 'https://github.com/AgoraIO-Community/macOS-UIKit'
export const UIKIT_PACKAGE_FLUTTER = 'https://github.com/AgoraIO-Community/Flutter-UIKit'
export const UIKIT_PACKAGE_RN = 'https://github.com/AgoraIO-Community/ReactNative-UIKit'
export const UIKIT_PACKAGE_REACT_WEB = 'https://github.com/AgoraIO-Community/Web-React-UIKit'