import React from 'react';
import VoiceCall from '@site/static/img/product-icons/v2/voice-calling.svg';
import VideoCall from '@site/static/img/product-icons/v2/video-calling.svg';
import InteractiveLiveStreaming from '@site/static/img/product-icons/v2/interactive-live-streaming.svg';
import BroadcastStreaming from '@site/static/img/product-icons/v2/broadcast-streaming.svg';
import Chat from '@site/static/img/product-icons/v2/agora-chat.svg';
import Signaling from '@site/static/img/product-icons/v2/signaling.svg';
import InteractiveWhiteboard from '@site/static/img/product-icons/v2/interactive-whiteboard.svg';
import IoT from '@site/static/img/product-icons/v2/iot.svg';
import ConversationalAI from '@site/static/img/product-icons/v2/conversational-ai.svg';
import FutureOfWork from '@site/static/img/product-icons/v2/future-of-work.svg';
import Telehealth from '@site/static/img/product-icons/v2/telehealth.svg';
import MediaEntertainment from '@site/static/img/product-icons/v2/media-entertainment.svg';
import HeartSocial from '@site/static/img/product-icons/v2/heart-social.svg';
import Gaming from '@site/static/img/product-icons/v2/gaming.svg';
import Metaverse from '@site/static/img/product-icons/v2/metaverse.svg';
import AgoraAnalytics from '@site/static/img/product-icons/v2/agora-analytics.svg';
import CloudRecording from '@site/static/img/product-icons/v2/cloud-recording.svg';
import CloudTranscoding from '@site/static/img/product-icons/v2/cloud-transcoding.svg';
import OnPremiseRecording from '@site/static/img/product-icons/v2/on-premise-recording.svg';
import ServerGateway from '@site/static/img/product-icons/v2/server-gateway.svg';
import MediaGateway from '@site/static/img/product-icons/v2/media-gateway.svg';
import FlexibleClassroom from '@site/static/img/product-icons/v2/flexible-classroom.svg';
import MediaPush from '@site/static/img/product-icons/v2/media-push.svg';
import MediaPull from '@site/static/img/product-icons/v2/media-pull.svg';
import RealTimeSTT from '@site/static/img/product-icons/v2/real-time-stt.svg';
import OpenAIIntegration from '@site/static/img/product-icons/v2/open-ai-integration.svg';
import Ten from '@site/static/img/product-icons/v2/ten.svg';
import ConvoAIDeviceKit from '@site/static/img/product-icons/convo-ai-device-kit.svg';

export const products = {
  core: [
    {
      visible: true,
      id: 'conversational-ai',
      label: 'Conversational AI ',
      description: 'Build real-time voice AI agents',
      previousLabel: '',
      link: 'conversational-ai/overview/product-overview',
      icon: <ConversationalAI />,
      beta: false,
      platforms: {
        latest: [],
      },
    },
    {
      visible: true,
      id: 'convo-ai-device-kit',
      label: 'Convo AI Device Kit R1',
      description: 'A turnkey solution for adding voice AI to any device',
      previousLabel: '',
      link: 'convo-ai-device-kit/overview/product-overview',
      icon: <ConvoAIDeviceKit />,
      beta: true,
      platforms: {
        latest: [],
      },
    },
    {
      visible: true,
      id: 'open-ai-integration',
      label: 'OpenAI Realtime API',
      previousLabel: '',
      link: 'open-ai-integration/overview/product-overview',
      icon: <OpenAIIntegration />,
      beta: false,
      platforms: {
        latest: ['python'],
      },
      buildWith: ['SDK'],
    },
    {
      visible: true,
      id: 'voice-calling',
      label: 'Voice Calling',
      description: 'Embed real-time voice chat into any app',
      previousLabel: '',
      link: 'voice-calling/overview/product-overview',
      icon: <VoiceCall />,
      latestVersion: '4.x',
      versionedPaths: {
        '3.x': '3.x/voice-calling/introduction/product-overview',
      },
      beta: false,
      platforms: {
        latest: [
          'android',
          'ios',
          'macos',
          'web',
          'windows',
          'electron',
          'flutter',
          'react-native',
          'python',
          'react-js',
          'unity',
          'unreal',
          `blueprint`,
        ],
        '3.x': [
          'android',
          'ios',
          'macos',
          'windows-cpp',
          'windows-csharp',
          'unity',
          'flutter',
          'react-native',
          'electron',
          'cocos-creator',
          'cocos-2d-x',
        ],
      },
      buildWith: ['SDK', 'NO CODE'],
    },
    {
      visible: true,
      id: 'video-calling',
      label: 'Video Calling',
      description: 'Embed real-time video calling anywhere',
      previousLabel: '',
      link: 'video-calling/overview/product-overview',
      icon: <VideoCall />,
      latestVersion: '4.x',
      versionedPaths: {
        '3.x': '3.x/video-calling/introduction/product-overview',
      },
      beta: false,
      platforms: {
        latest: [
          'android',
          'ios',
          'macos',
          'web',
          'windows',
          'electron',
          'flutter',
          'react-native',
          'react-js',
          'unity',
          'unreal',
          'blueprint',
        ],
        '3.x': [
          'android',
          'ios',
          'macos',
          'windows-cpp',
          'windows-csharp',
          'unity',
          'flutter',
          'react-native',
          'electron',
          'cocos-creator',
          'cocos-2d-x',
        ],
      },
      buildWith: ['SDK', 'NO CODE'],
    },
    {
      visible: true,
      id: 'interactive-live-streaming',
      label: 'Interactive Live Streaming',
      description: 'Ultra-low latency live streaming',
      previousLabel: '',
      link: 'interactive-live-streaming/overview/product-overview',
      icon: <InteractiveLiveStreaming />,
      latestVersion: '4.x',
      versionedPaths: {
        '3.x': '3.x/interactive-live-streaming/introduction/product-overview',
      },
      beta: false,
      platforms: {
        latest: [
          'android',
          'ios',
          'macos',
          'web',
          'windows',
          'electron',
          'flutter',
          'react-native',
          'react-js',
          'unity',
          'unreal',
          'blueprint',
        ],
        '3.x': [
          'android',
          'ios',
          'macos',
          'windows-cpp',
          'windows-csharp',
          'unity',
          'flutter',
          'react-native',
          'electron',
          'cocos-creator',
          'cocos-2d-x',
        ],
      },
      buildWith: ['SDK', 'NO CODE'],
    },
    {
      visible: true,
      id: 'broadcast-streaming',
      label: 'Broadcast Streaming',
      description: 'Live stream to large global audiences',
      previousLabel: '',
      link: 'broadcast-streaming/overview/product-overview',
      icon: <BroadcastStreaming />,
      beta: false,
      platforms: {
        latest: [
          'android',
          'ios',
          'macos',
          'web',
          'windows',
          'electron',
          'flutter',
          'react-native',
          'react-js',
          'unity',
          'unreal',
          'blueprint',
        ],
      },
      buildWith: ['SDK', 'NO CODE'],
    },
    {
      visible: true,
      id: 'agora-chat',
      label: 'Chat',
      description: 'Create customized messaging experiences',
      previousLabel: '',
      link: 'agora-chat/overview/product-overview',
      icon: <Chat />,
      beta: false,
      platforms: {
        latest: [
          'android',
          'ios',
          'web',
          'windows',
          'unity',
          'flutter',
          'react-native',
        ],
      },
      buildWith: ['SDK'],
    },
    {
      visible: true,
      id: 'signaling',
      label: 'Signaling',
      description: 'Synchronize metadata in real time',
      previousLabel: '',
      link: 'signaling/overview/product-overview',
      icon: <Signaling />,
      latestVersion: '2.x',
      versionedPaths: {
        '1.x': '1.x/signaling/overview/product-overview',
      },
      beta: false,
      platforms: {
        latest: [
          'android',
          'ios',
          'macos',
          'web',
          'windows',
          'flutter',
          `react-native`,
          'linux-cpp',
          'unity',
        ],
        '1.x': [
          'android',
          'ios',
          'web',
          'macos',
          'windows',
          'linux-cpp',
          'linux-java',
          'unity',
        ],
      },
      buildWith: ['SDK', 'NO CODE'],
    },
    {
      visible: true,
      id: 'interactive-whiteboard',
      label: 'Interactive Whiteboard',
      description: 'Custom real-time digital whiteboard',
      previousLabel: '',
      link: 'interactive-whiteboard/overview/product-overview',
      icon: <InteractiveWhiteboard />,
      beta: false,
      platforms: {
        latest: ['android', 'ios', 'web'],
      },
      buildWith: ['SDK', 'NO CODE'],
    },
    {
      visible: true,
      id: 'iot',
      label: 'IoT SDK',
      description: 'Real-time engagement for smart devices',
      previousLabel: '',
      link: 'iot/overview/product-overview',
      icon: <IoT />,
      beta: false,
      platforms: {
        latest: ['android', 'linux-c'],
      },
      buildWith: ['SDK'],
    },
  ],
  openSource: [
    {
      visible: true,
      id: 'ten-framework',
      label: 'TEN Framework',
      previousLabel: '',
      description: 'A powerful framework for building a wide range of applications and services',
      link: 'ten-framework/overview/product-overview',
      icon: <Ten />,
      beta: false,
      platforms: {
        latest: [],
      },
    },
    {
      visible: true,
      id: 'ten-agent',
      label: 'TEN Agent',
      previousLabel: '',
      description: 'A conversational AI agent powered by the TEN Framework.',
      link: 'ten-agent/overview/product-overview',
      icon: <Ten />,
      beta: false,
      platforms: {
        latest: [],
      },
    },
  ],  
  addOns: [
    {
      visible: true,
      id: 'agora-analytics',
      icon: <AgoraAnalytics />,
      label: 'Analytics',
      previousLabel: '',
      description: 'Track quality, performance, and usage',
      link: 'agora-analytics/overview/product-overview',
      beta: false,
      platforms: {
        latest: [],
      },
    },
    {
      visible: true,
      id: 'cloud-recording',
      icon: <CloudRecording />,
      label: 'Cloud Recording',
      previousLabel: '',
      description: 'Record voice or video calls to the cloud',
      link: 'cloud-recording/overview/product-overview',
      beta: false,
      platforms: {
        latest: [],
      },
    },
    {
      visible: true,
      id: 'cloud-transcoding',
      icon: <CloudTranscoding />,
      label: 'Cloud Transcoding',
      description: 'Transcode real-time audio and video streams for audience subscription.',
      previousLabel: '',
      link: 'cloud-transcoding/overview/product-overview',
      beta: true,
      platforms: {
        latest: [],
      },
    },
    {
      visible: true,
      id: 'on-premise-recording',
      icon: <OnPremiseRecording />,
      label: 'On-Premise Recording',
      previousLabel: '',
      description: 'Record voice or video calls to your local server',
      link: 'on-premise-recording/overview/product-overview',
      latestVersion: '4.x',
      versionedPaths: {
        '3.x': '3.x/on-premise-recording/overview/product-overview',
      },
      beta: false,
      platforms: {
        latest: ['linux-cpp', 'linux-java'],
        '3.x': ['linux-cpp', 'linux-java'],
      },
    },
    {
      visible: true,
      id: 'server-gateway',
      icon: <ServerGateway />,
      label: 'Server Gateway',
      previousLabel: '',
      description: 'Transmit Video SDK streams via a Linux server',
      link: 'server-gateway/overview/product-overview',
      beta: false,
      latestVersion: '4.x',
      versionedPaths: {
        '3.x': '3.x/server-gateway/overview/product-overview',
      },
      platforms: {
        latest: ['linux-cpp', 'linux-java', 'python', 'go'],
      },
    },
    {
      visible: true,
      id: 'media-gateway',
      icon: <MediaGateway />,
      label: 'Media Gateway',
      previousLabel: '',
      description:
        'Stream directly with RTMP/SRT protocol to Agora RTC channels',
      link: 'media-gateway/overview/product-overview',
      beta: false,
      platforms: {
        latest: [],
      },
    },
    {
      visible: true,
      id: 'flexible-classroom',
      label: 'Flexible Classroom',
      icon: <FlexibleClassroom />,
      previousLabel: '',
      description: 'Build scalable online classrooms of any size',
      link: 'flexible-classroom/overview/product-overview',
      beta: false,
      platforms: {
        latest: ['android', 'ios', 'web', 'electron'],
      },
    },
    {
      visible: true,
      id: 'media-push',
      icon: <MediaPush />,
      label: 'Media Push',
      previousLabel: '',
      description: 'Push stream to CDN to reach a larger audience',
      link: 'media-push/overview/product-overview',
      beta: false,
      platforms: {
        latest: [],
      },
    },
    {
      visible: true,
      id: 'media-pull',
      icon: <MediaPull />,
      label: 'Media Pull',
      previousLabel: '',
      description: 'Add an external stream to a live-broadcast',
      link: 'media-pull/overview/product-overview',
      beta: false,
      platforms: {
        latest: [],
      },
    },
    {
      visible: true,
      id: 'real-time-stt',
      icon: <RealTimeSTT />,
      label: 'Real-Time Speech-To-Text',
      previousLabel: '',
      description: 'Transcribe a media stream into text in real time',
      link: 'real-time-stt/overview/product-overview',
      beta: false,
      platforms: {
        latest: [],
      },
    },
  ],
  extensions: {
    marketplace: {
      visible: true,
      id: 'extensions-marketplace',
      label: 'Extensions Marketplace',
      img: '/home-page/home-extension-marketplace.png',
      previousLabel: '',
      description:
        'Discover, enable, and manage extensions to enhance your real-time experience with video and audio modifiers, transcriptions, and content moderation.',
      link: 'extensions-marketplace/overview/product-overview',
      beta: false,
      platforms: {
        latest: [
          'android',
          'ios',
          'web',
          'macos',
          'windows',
          'flutter',
          'react-native',
        ],
      },
    },
    gallery: [
      {
        id: 'video-modifiers',
        label: 'Video Modifiers',
        description:
          'Add video functionality like face filters and background removal',
        link: 'https://www.agora.io/en/agora-extensions-marketplace/',
      },
      {
        id: 'audio-modifiers',
        label: 'Audio Modifiers',
        description:
          'Add audio functionality like noise reduction and voice filters',
        link: 'https://www.agora.io/en/agora-extensions-marketplace/',
      },
      {
        id: 'transcriptions',
        label: 'Transcriptions',
        description:
          'Process speech data with transcription and conversation insights',
        link: 'https://www.agora.io/en/agora-extensions-marketplace/',
      },
      {
        id: 'content-moderation',
        label: 'Content Moderation',
        description: 'Moderate content from audio, video, and messages',
        link: 'https://www.agora.io/en/agora-extensions-marketplace/',
      },
    ],
  },
  useCases: [
    {
      id: 'usecase-education',
      label: 'Education',
      link: 'https://www.agora.io/en/solutions/education/',
      icon: <FlexibleClassroom fill="currentColor" />,
      features: [
        {
          name: 'Video Calling',
          link: 'https://www.agora.io/en/products/video-call/',
        },
        { name: 'Chat', link: 'https://www.agora.io/en/products/chat/' },
        {
          name: 'Signaling',
          link: 'https://www.agora.io/en/products/signaling/',
        },
        {
          name: 'Conversational AI',
          link: 'https://www.agora.io/en/products/conversational-ai-engine/',
        },
        {
          name: 'Interactive Whiteboard',
          link: 'https://www.agora.io/en/products/interactive-whiteboard/',
        },
      ],
    },
    {
      id: 'usecase-live-streaming',
      label: 'Live Audio Streaming',
      link: 'https://www.agora.io/en/solutions/live-audio-streaming/',
      icon: <InteractiveLiveStreaming fill="currentColor" />,
      features: [
        { name: 'Voice Calling', link: '#' },
        { name: 'Chat', link: 'https://www.agora.io/en/products/chat/' },
        {
          name: 'Signaling',
          link: 'https://www.agora.io/en/products/signaling/',
        },
        {
          name: 'Conversational AI',
          link: 'https://www.agora.io/en/products/conversational-ai-engine/',
        },
      ],
    },
    {
      id: 'usecase-future-of-work',
      label: 'Future of Work',
      link: 'https://www.agora.io/en/solutions/future-of-work/',
      icon: <FutureOfWork fill="currentColor" />,
      features: [
        { name: 'Chat', link: 'https://www.agora.io/en/products/chat/' },
        {
          name: 'Voice Calling',
          link: 'https://www.agora.io/en/products/voice-call/',
        },
        {
          name: 'Video Calling',
          link: 'https://www.agora.io/en/products/video-call/',
        },
        {
          name: 'Signaling',
          link: 'https://www.agora.io/en/products/signaling/',
        },
        {
          name: 'Metaverse',
          link: 'https://www.agora.io/en/solutions/metaverse/',
        },
      ],
    },
    {
      id: 'usecase-telehealth',
      label: 'Telehealth',
      link: 'https://www.agora.io/en/solutions/telehealth/',
      icon: <Telehealth fill="currentColor" />,
      features: [
        {
          name: 'Video Calling',
          link: 'https://www.agora.io/en/products/video-call/',
        },
        {
          name: 'Signaling',
          link: 'https://www.agora.io/en/products/signaling/',
        },
        {
          name: 'Interactive Whiteboard',
          link: 'https://www.agora.io/en/products/interactive-whiteboard/',
        },
        { name: 'Chat', link: 'https://www.agora.io/en/products/chat/' },
      ],
    },
    {
      id: 'usecase-live-shopping',
      label: 'Live Shopping',
      link: 'https://www.agora.io/en/solutions/live-shopping/',
      icon: <InteractiveLiveStreaming fill="currentColor" />,
      features: [
        {
          name: 'Voice Calling',
          link: 'https://www.agora.io/en/products/voice-call/',
        },
        { name: 'Chat', link: 'https://www.agora.io/en/products/chat/' },
        {
          name: 'Conversational AI',
          link: 'https://www.agora.io/en/products/conversational-ai-engine/',
        },
      ],
    },
    {
      id: 'usecase-media-entertainment',
      label: 'Media & Entertainment',
      link: 'https://www.agora.io/en/solutions/media-and-entertainment/',
      icon: <MediaEntertainment fill="currentColor" />,
      features: [
        {
          name: 'Live Streaming',
          link: 'https://www.agora.io/en/products/interactive-live-streaming/',
        },
        { name: 'Chat', link: 'https://www.agora.io/en/products/chat/' },
        {
          name: 'Signaling',
          link: 'https://www.agora.io/en/products/signaling/',
        },
      ],
    },
    {
      id: 'usecase-social',
      label: 'Social',
      link: 'https://www.agora.io/en/solutions/social/',
      icon: <HeartSocial fill="currentColor" />,
      features: [
        {
          name: 'Live Streaming',
          link: 'https://www.agora.io/en/products/interactive-live-streaming/',
        },
        { name: 'Chat', link: 'https://www.agora.io/en/products/chat/' },
        {
          name: 'Signaling',
          link: 'https://www.agora.io/en/products/signaling/',
        },
      ],
    },
    {
      id: 'usecase-gaming',
      label: 'Gaming',
      link: 'https://www.agora.io/en/solutions/gaming/',
      icon: <Gaming fill="currentColor" />,
      features: [
        { name: 'Chat', link: 'https://www.agora.io/en/products/chat/' },
        {
          name: 'Signaling',
          link: 'https://www.agora.io/en/products/signaling/',
        },
        {
          name: 'Live Streaming',
          link: 'https://www.agora.io/en/products/interactive-live-streaming/',
        },
      ],
    },
    {
      id: 'usecase-metaverse',
      label: 'Metaverse',
      link: 'https://www.agora.io/en/solutions/metaverse/',
      icon: <Metaverse fill="currentColor" />,
      features: [
        { name: 'Chat', link: 'https://www.agora.io/en/products/chat/' },
        {
          name: 'Voice Calling',
          link: 'https://www.agora.io/en/products/voice-call/',
        },
        {
          name: 'Video Calling',
          link: 'https://www.agora.io/en/products/video-call/',
        },
      ],
    },
    {
      id: 'usecase-conversational-ai',
      label: 'Conversational AI',
      link: 'https://www.agora.io/en/solutions/conversational-ai/',
      icon: <ConversationalAI fill="currentColor" />,
      features: [
        {
          name: 'Agora x Open AI',
          link: 'https://www.agora.io/en/products/agora-openai-realtime-api/',
        },
        {
          name: 'Conversational AI Engine',
          link: 'https://www.agora.io/en/products/conversational-ai-engine/',
        },
        {
          name: 'Voice Calling',
          link: 'https://www.agora.io/en/products/voice-call/',
        },
      ],
    },
  ],
};
