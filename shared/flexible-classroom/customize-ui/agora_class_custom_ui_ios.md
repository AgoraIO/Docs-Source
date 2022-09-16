---
title: "Customize the Classroom UI with UIKit"
weight: 13
type: docs
description: 

---

You can use the Agora Classroom SDK as it is to launch a flexible classroom. However, if you want to customize the UI of classrooms, such as changing colors, changing buttons, adjusting layouts, and adding logos, you can get the source code of the Agora Classroom SDK and build a Classroom SDK on your own.

This page shows you how to customize the user interfaces of Flexible Classroom by editing the the source code of the UIKit in the Agora Classroom SDK.

## Understand the tech

In the Agora Classroom SDK, the code of the user interfaces is separated from the code of core business logic. The Classroom SDK contains two libraries, UIKit and EduCore. These two libraries connect with each other through [Agora Edu Context](./edu_context_api_ref_ios_overview?platform=iOS). For example, for the text chat feature of Flexible Classroom, a user can click on a button to send a text message, and the user can receive messages sent by other users. In this case, you can call a method in the Chat Context to send a message and listen for the events in the Chat Context to receive messages.

![](https://web-cdn.agora.io/docs-files/1623761240753)

UIKit provides all the code for the user interfaces of Flexible Classroom. You can find the source code of UIKit in the `Modules` folder in the [CloudClass-iOS](https://github.com/AgoraIO-Community/CloudClass-iOS/tree/release/apaas%2F1.1.5) repository on GitHub (Branch release/apaas/1.1.5). The project structure of UIKit is as follows:

| Folder | Description |
| :-------------------- | :---------------------------------------------------- |
| `AgoraUIBaseViews` | The source code of the basic UI components used by Flexible Classroom, including buttons and views. |
| `AgoraUIEduBaseViews` | The source code of the function-level UI components used by Flexible Classroom, such as the chat area. |
| `AgoraUIManager` | Assemble UI components in various classrooms. |

## UI customization example

This section provides examples of customizing the user interfaces of Flexible Classroom.

### Change the color of the navigation bar

The following example demonstrates how to change the background color of the navigation bar component from white to gray by modifying `AgoraUIEduBaseViews/AgoraUIEduBaseViews/AgoraUINavigationBar/AgoraUINavigationBar.swift`.

#### Before

```swift
func initView() {
        self.backgroundColor = UIColor.white
        ...
}
```

![](https://web-cdn.agora.io/docs-files/1622431132516)

#### After

```swift
func initView() {
        self.backgroundColor = UIColor.init(rgb: UInt32("BFBFBF", radix: 16) ?? 0)
        ...
}
```

![](https://web-cdn.agora.io/docs-files/1623327367108)

### Adjust the layout

The following example demonstrates how to change the position of the leave room button and the network status icon by modifying `AgoraUIEduBaseViews/AgoraUIEduBaseViews/AgoraUINavigationBar/AgoraUINavigationBar.swift`.

#### Before

```swift
func initLayout() {
        signalImgView.agora_safe_x = 10
        signalImgView.agora_width = 20
        signalImgView.agora_height = 20
        signalImgView.agora_center_y = 0

        leaveButton.agora_safe_right = 10
        leaveButton.agora_width = 24
        leaveButton.agora_height = 24
        leaveButton.agora_center_y = 0
        ...
}
```

![](https://web-cdn.agora.io/docs-files/1622431132516)

#### After

```swift
func initLayout() {
        signalImgView.agora_safe_right = 10
        signalImgView.agora_width = 20
        signalImgView.agora_height = 20
        signalImgView.agora_center_y = 0

        leaveButton.agora_safe_x = 10
        leaveButton.agora_width = 24
        leaveButton.agora_height = 24
        leaveButton.agora_center_y = 0
        ...
}
```

![](https://web-cdn.agora.io/docs-files/1623332519282)

### Add a basic UI component

The following example shows how to add a custom basic UI component and use it in Flexible Classroom:

Suppose the properties of the UI component are defined as follows:

- Size: 100*100
- Position: Centered
- Background color: #BFBFBF
- Text: Leave
- Text color: UIColor.white
- What happens when clicking the button: Leave the room

Add a basic UI component, as follows:

1. Copy the following code to `AgoraUIEduBaseViews/AgoraUIEduBaseViews/AgoraResources/en.lproj/Localizable.strings` to add the text.

   ```
DemoLeave = "Leave";
   ```
2. Copy the following code to `AgoraUIEduAppViews/AgoraUIEduAppViews/AgoraUIManager.swift` to add the properties of the component.

   ```swift
   weak var demoButton: AgoraBaseUIButton?
   ```
3. Copy the following code to `AgoraUIEduAppViews/AgoraUIEduAppViews/AgoraUIManager.swift`.

   ```swift
   func addContainerViews() {
   ···
   let demoBtn = AgoraBaseUIButton()
   demoBtn.setTitle(AgoraKitLocalizedString("DemoLeave"), for: UIControl.State.normal)
   demoBtn.titleLabel?.font = UIFont.systemFont(ofSize: 15)
   demoBtn.setTitleColor(UIColor.white, for: UIControl.State.normal)
   demoBtn.backgroundColor = UIColor(rgb: UInt32("BFBFBF",radix: 16) ?? 0)
   demoBtn.addTarget(self,
                     action: #selector(onTouchLeaveDemo(_:)),
                     for: UIControl.Event.touchUpInside)
   self.demoButton = demoBtn
   self.appView.addSubview(demoBtn)
   }
   
   /*
    * Function:
    *          initLayout
    * Operation:
    *          add code like below
    */
   func layoutContainerViews() {
        ···
        demoButton?.agora_center_x = self.agora_center_x
        demoButton?.agora_center_y = self.agora_center_y
        demoButton?.agora_width = 100
        demoButton?.agora_height = 100
   }
   /*
    * Operation:
    *          add a function like below
    */
   @objc func onTouchLeaveDemo(_ btn: AgoraBaseUIButton) {
       self.roomListener?.onLeaveRoom()
   }
   ```
   
   You can see the following icon in the one-to-one classroom.
   
   ![](https://web-cdn.agora.io/docs-files/1623333238071)