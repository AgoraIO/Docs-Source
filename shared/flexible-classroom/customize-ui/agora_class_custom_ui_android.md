---
title: "Customize the Classroom UI with UIKit"
weight: 12
type: docs
description: 

---

You can use the Agora Classroom SDK as it is to launch a flexible classroom. However, if you want to customize the UI of classrooms, such as changing colors, changing buttons, adjusting layouts, and adding logos, you can get the source code of the Agora Classroom SDK and build a Classroom SDK on your own.

This page shows you how to customize the user interfaces of Flexible Classroom by editing the the source code of the UIKit in the Agora Classroom SDK.

## Understand the tech

In the Agora Classroom SDK, the code of the user interfaces is separated from the code of core business logic. The Classroom SDK contains two libraries, UIKit and EduCore. These two libraries connect with each other through [Agora Edu Context](./edu_context_api_ref_android_overview?platform=Android). For example, for the text chat feature of Flexible Classroom, a user can click on a button to send a text message, and the user can receive messages sent by other users. In this case, you can call a method in the Chat Context to send a message and listen for the events in the Chat Context to receive messages.

![](https://web-cdn.agora.io/docs-files/1623761240753)

You can find the source code of UIKit in the `agoraui` folder in the [CloudClass-Android](https://github.com/AgoraIO-Community/CloudClass-Android/tree/release/apaas%2F1.1.5.1) repository on GitHub (Branch release/apaas/1.1.5.1). The project structure of UIKit is as follows:

| Folder | Description |
| :----------- | :----------------------------------------------------------- |
| `interfaces` | Defines the protocols and listeners of the  Flexible Classroom business logic. Do not need to edit the code under this directory. |
| `impl` | The default implementations of each protocol in Flexible Classroom, that is, the default UI components used by Flexible Classroom, including:<ul><li>`chat`: The UI code of the chat area.</li><li>`handsup`: The UI code related to students "raising their hands" to apply for speaking up.</li><li>`room`: The UI code related to the classroom states and navigation bar.</li><li>`screnshare`: The UI code related to screen sharing.</li><li>`tool`: The UI code related to the toolbar containing various teaching tools.</li><li>`users`: The UI code related to user states.</li><li>`video`: The UI code of the video area.</li><li>`whiterboard`: The UI code of the whiteboard area.</li><li>`container`: Show how the basic UI components are combined in a classroom.</ul> |
| `component` | The other public components used by Flexible Classroom. |

## UI customization example

This section provides examples of customizing the user interfaces of Flexible Classroom.

### Change the color of the navigation bar

The following example demonstrates how to modify the background color of the navigation bar component from white to gray by editing `agoraui/src/main/res/layout/agora_status_bar_layout.xml`.

<div class="alert info">The navigation bar component is implemented in <code>agoraui/src/main/kotlin/io/agora/uikit/impl/room/AgoraUIRoomStatus.kt</code>.</div>

#### Before

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
 android:layout_width="match_parent"
 android:layout_height="match_parent"
 android:background="@drawable/agora_class_room_rect_bg">
...
</RelativeLayout>
```

![](https://web-cdn.agora.io/docs-files/1622431132516)

#### After

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
 android:layout_width="match_parent"
 android:layout_height="match_parent"
 android:background="#BFBFBF">
...
</RelativeLayout>
```

![](https://web-cdn.agora.io/docs-files/1623327367108)

### Adjust the layout

The following example demonstrates how to switch the position of the leave room button and the network condition icon by editing `agoraui/src/main/res/layout/agora_status_bar_layout.xml`.

<div class="alert info">The navigation bar component is implemented in <code>agoraui/src/main/kotlin/io/agora/uikit/impl/room/AgoraUIRoomStatus.kt</code>.</div>

#### Before

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
  android:layout_width="match_parent"
  android:layout_height="match_parent"
  android:background="@drawable/agora_class_room_rect_bg">
  <androidx.appcompat.widget.AppCompatImageView
      android:id="@+id/agora_status_bar_network_state_icon"
      android:layout_width="@dimen/agora_status_bar_icon_size"
      android:layout_height="@dimen/agora_status_bar_icon_size"
      android:layout_centerVertical="true"
      android:layout_alignParentStart="true"
      android:layout_alignParentLeft="true"
      android:layout_marginStart="@dimen/margin_large"
      android:layout_marginLeft="@dimen/margin_large"/>
  <androidx.appcompat.widget.AppCompatImageView
      android:id="@+id/agora_status_bar_exit_icon"
      android:layout_width="@dimen/agora_status_bar_icon_size"
      android:layout_height="@dimen/agora_status_bar_icon_size"
      android:layout_centerVertical="true"
      android:layout_alignParentEnd="true"
      android:layout_alignParentRight="true"
      android:layout_marginEnd="@dimen/margin_large"
      android:layout_marginRight="@dimen/margin_large"
      android:src="@drawable/agora_room_icon_exit"/>
...
</RelativeLayout>
```

![](https://web-cdn.agora.io/docs-files/1622431132516)

#### After

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
  android:layout_width="match_parent"
  android:layout_height="match_parent"
  android:background="@drawable/agora_class_room_rect_bg">
  <androidx.appcompat.widget.AppCompatImageView
    android:id="@+id/agora_status_bar_network_state_icon"
    android:layout_width="@dimen/agora_status_bar_icon_size"
    android:layout_height="@dimen/agora_status_bar_icon_size"
    android:layout_centerVertical="true"
    android:layout_alignParentEnd="true"
    android:layout_alignParentRight="true"
    android:layout_marginEnd="@dimen/margin_large"
    android:layout_marginRight="@dimen/margin_large"/>
 <androidx.appcompat.widget.AppCompatImageView
    android:id="@+id/agora_status_bar_exit_icon"
    android:layout_width="@dimen/agora_status_bar_icon_size"
    android:layout_height="@dimen/agora_status_bar_icon_size"
    android:layout_centerVertical="true"
    android:layout_alignParentStart="true"
    android:layout_alignParentLeft="true"
    android:layout_marginStart="@dimen/margin_large"
    android:layout_marginLeft="@dimen/margin_large"
    android:src="@drawable/agora_room_icon_exit"/>
...
</RelativeLayout>
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

1. Add the text in `agoraui/src/main/res/values/strings.xml`.

```
   <!-- Custom -->
   <string name="custom_widget_text" translatable="false">Leave</string>
```

2. Add a `custom_widget_layout.xml` file under the `agoraui/src/main/res/layout` directory to define the style of the custom component.
   ```
   <?xml version="1.0" encoding="utf-8"?>
   <FrameLayout
   xmlns:android="http://schemas.android.com/apk/res/android"
   android:layout_width="match_parent"
   android:layout_height="match_parent">
   <TextView
   android:id="@+id/tv_custom_leave"
   android:layout_width="100dp"
   android:layout_height="100dp"
   android:background="#BFBFBF"
   android:textColor="@android:color/white"
   android:gravity="center"
   android:layout_gravity="center"
   android:text="@string/custom_widget_text"/>
   </FrameLayout>
   ```

3. Copy the following code to `agoraui/src/main/kotlin/io.agora.uikit/impl/container/AgoraUI1v1Container.kt` to add the custom component to the one-to-one classroom.

   ```kotlin
   class AgoraUI1v1Container : AbsUIContainer() {
     override fun init(layout: ViewGroup, left: Int, top: Int, width: Int, height: Int) {
     ...
       addCustomWidget(layout)
     }
     private fun addCustomWidget(layout: ViewGroup){
       val customLayout = LayoutInflater.from(layout.context).inflate(R.layout.custom_widget_layout, layout)
       customLayout.findViewById<TextView>    (R.id.tv_custom_leave).setOnClickListener {
   roomStatus?.showLeaveDialog()
       }
     }
   }
   ```

   You can see the following icon in the one-to-one classroom.

   ![](https://web-cdn.agora.io/docs-files/1623333238071)