const data = {
  'web': {
    NAME: 'Web',
    PATH: 'web',
    CLIENT: 'app'
  },

  'android': {
    NAME: 'Android',
    PATH: 'android',
    CLIENT: 'app',
    RTC_EVENT_HANDLER_CLASS: 'IRtcEngineEventHandler',
    RTC_CONNECTION: 'RtcConnection',
    RTC_ENGINE: 'RtcEngine',
    RTC_ENGINE_EX: 'RtcEngineEx',
    RTC_JOIN_CHANNEL_EX: 'joinChannelEx',
    RTC_EVENT_HANDLER_PARAMETER: 'eventHandler' // In joinChannel API
  },

  'ios': {
    NAME: 'iOS',
    PATH: 'ios',
    CLIENT: 'app',
    PACKAGE_NAME: 'AgoraRtcEngine_iOS',
    PACKAGE_PRODUCT_NAME: 'RtcBasic',
    RTC_EVENT_HANDLER_CLASS: 'AgoraRtcEngineDelegate',
    RTC_CONNECTION: 'AgoraRtcConnection',
    RTC_ENGINE: 'AgoraRtcEngineKit',
    RTC_ENGINE_EX: 'AgoraRtcEngineKit(Ex)',
    RTC_JOIN_CHANNEL_EX: 'joinChannelExByToken',
    RTC_EVENT_HANDLER_PARAMETER: 'delegate' // In joinChannel API
  },

  'macos': {
    NAME: 'macOS',
    PATH: 'macos',
    CLIENT: 'app',
    PACKAGE_NAME: 'AgoraRtcEngine_macOS',
    PACKAGE_PRODUCT_NAME: 'RtcBasic',
    RTC_EVENT_HANDLER_CLASS: 'AgoraRtcEngineDelegate',
    RTC_CONNECTION: 'AgoraRtcConnection',
    RTC_ENGINE: 'AgoraRtcEngineKit',
    RTC_ENGINE_EX: 'AgoraRtcEngineKit(Ex)',
    RTC_JOIN_CHANNEL_EX: 'joinChannelExByToken',
    RTC_EVENT_HANDLER_PARAMETER: 'delegate' // In joinChannel API
  },
  

  'react-native': {
    NAME: 'React Native',
    PATH: 'react-native',
    CLIENT: 'app'
  },
  'react-js': {
    NAME: 'ReactJS',
    PATH: 'react-js',
    CLIENT: 'app'
  },
  'electron': {
    NAME: 'Electron',
    PATH: 'electron',
    CLIENT: 'app'
  },

  
  'unity': {
    NAME: 'Unity',
    PATH: 'unity',
    CLIENT: 'game',
    RTC_EVENT_HANDLER_CLASS: 'IRtcEngineEventHandler',
    RTC_CONNECTION: 'RtcConnection',
    RTC_ENGINE: 'RtcEngine',
    RTC_ENGINE_EX: 'IRtcEngineEx',
    RTC_JOIN_CHANNEL_EX: 'JoinChannelEx',
  },

  'windows': {
    NAME: 'Windows',
    PATH: 'windows',
    CLIENT: 'app',
    RTC_EVENT_HANDLER_CLASS: 'IRtcEngineEventHandler',
    RTC_CONNECTION: 'RtcConnection',
    RTC_ENGINE: 'IRtcEngine',
    RTC_ENGINE_EX: 'IRtcEngineEx',
    RTC_JOIN_CHANNEL_EX: 'joinChannelEx',
    RTC_EVENT_HANDLER_PARAMETER: 'eventHandler' // In joinChannel API
  },

  'flutter': {
    NAME: 'Flutter',
    PATH: 'flutter',
    CLIENT: 'app'
  },

  'linux-cpp': {
    NAME: 'Linux C++',
    PATH: 'linux-cpp',
    CLIENT: 'app'
  },

  'linux-c': {
    NAME: 'Linux C',
    PATH: 'linux-c',
    CLIENT: 'app'
  },

  'unreal': {
    NAME: 'Unreal Engine',
    PATH: 'unreal',
    CLIENT: 'game'
  },

  'blueprint': {
    NAME: 'Unreal (Blueprint)',
    PATH: 'blueprint',
    CLIENT: 'game'
  },

  'python': {
    NAME: 'Python',
    PATH: 'python',
    CLIENT: 'app'
  }

};

export default data;