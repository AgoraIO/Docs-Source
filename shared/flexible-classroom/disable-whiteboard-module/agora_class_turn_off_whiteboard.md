---
title: "Turn the Whiteboard on or off in the Classroom"
weight: 5
type: docs
description: 

---

The whiteboard module in Flexible Classroom is implemented based on AgoraWidget. You can turn the whiteboard module on or off in the classroom by setting the widget state as active or inactive.

<div class="alert info">After disabling the whiteboard module, the drawing tools, including pencils, text boxes, shapes, and erasers will no longer be available. Users can neither display class files on the whiteboard. Other features, such as uploading or deleting class files, pop-up quiz, count-down timer, and screen sharing will not be affected.</div>

INCLUDE HERE




## Reference

### AgoraWidgetContext

#### create

```swift
AgoraBaseWidget create(AgoraWidgetConfig config)
```

Creates a widget object.

Parameter:

- config: The initialization configurations of the widget object.

Return: An AgoraBaseWidget object.

#### setWidgetActive

```swift
void setWidgetActive(String widgetId,
                     String ownerUuid,
                     Map<String: Any> roomProperties,
                     AgoraWidgetFrame syncFrame,
                     Callback<Void> success,
                     Callback<Error> failure)
```

Sets the widget state as active.

Parameter:

- widgetId: The widget ID.
- ownerUuid: (Nullable) The ID of the user to whom the widget belongs. When the user goes offline, the `onWidgetInactive` callback will be triggered for the widgets owned by this user.
- roomProperties: (Nullable) The room properties related to the widget.
- syncFrame: (Nullable) The size and position of the widget.
- success: The method call succeeds.
- failure: The method call fails, the SDK returns an error.

#### setWidgetInactive

```swift
void setWidgetInactive(String widgetId,
                       Callback<Void> success,
                       Callback<Error> failure)
```

Sets the widget state as inactive.

Parameter:

- widgetId: The widget ID.
- roomProperties: (Nullable) The room properties related to the widget.
- success: The method call succeeds.
- failure: The method call fails, the SDK returns an error.

#### getWidgetActivity

```swift
Bool getWidgetActivity(String widgetId)
```

Gets the state of a specified widget.

Parameter:

- widgetId: The widget ID.

Return: Whether the widget is active or not.

#### getWidgetConfigs

```swift
Array<AgoraWidgetConfig> getWidgetConfigs()
```

Gets the configurations of all widgets.

Return: An array of the AgoraWidgetConfig objects.

#### getWidgetConfig

```swift
AgoraWidgetConfig getWidgetConfig(String widgetId)
```

Gets the configurations of a specified widget.

Parameter:

- widgetId: The widget ID.

Return: An AgoraWidgetConfig object.

#### addWidgetActiveObserver

```swift
AgoraWidgetError addWidgetActiveObserver(AgoraWidgetActiveObserver observer,
                                         String widgetId)
```

Registers an observer to observe the state of a specified widget. When the state of the widget changes, the SDK triggers a callback.

Parameter:

- observer: See AgoraWidgetActiveObserver.
- widgetId: The widget ID.

Return: When the widget ID is not valid, the SDK returns an error.

#### removeWidgetActiveObserver

```swift
AgoraWidgetError removeWidgetActiveObserver(AgoraWidgetActiveObserver observer,
                                            String widgetId)
```

Registers the observer of a specified widget.

Parameter:

- observer: See AgoraWidgetActiveObserver.
- widgetId: The widget ID.

Return: When the widget ID is not valid, the SDK returns an error.

### AgoraWidgetActiveObserver

#### onWidgetActive

```swift
void onWidgetActive(String widgetId)
```

Occurs when the widget state changes to active.

Parameter:

- widgetId: The widget ID.

#### onWidgetInactive

```swift
void onWidgetInactive(String widgetId)
```

Occurs when the widget state changes to inactive.

Parameter:

- widgetId: The widget ID.