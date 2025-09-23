---
title: 'Technical architecture'
sidebar_position: 2
type: docs
platform_selector: false
description: >
  Overview of the components in Flexible Classroom. 
---


The following figure shows the overall technical architecture of Flexible Classroom:

![](https://web-cdn.agora.io/docs-files/1653557375318)

## Module description

### Agora Classroom SDK

- This module includes the source code of Agora's online education solutions. It supports three types of classrooms: One-to-one Classroom, Small Classroom, and Lecture Hall. Customized classroom types are also supported.
- Developers can integrate the Classroom SDK into their own project as a third-party package, inherit the classroom types provided by Agora and make custom modifications.
- The Classroom SDK consists of the Edu UI layer, the Edu Context or UI Store layer, and the Edu Core layer.

### Pluggable widgets

- Pluggable widgets are independent of the Classroom SDK.
- Agora provides several ready-to-use widgets, including Interactive Whiteboard, Instant Messaging, Polle, Pop-up Quiz, and Countdown Timer.
- Developers are free to customize pluggable widgets based on their own business requirements.

### The Edu UI layer

- This module provides UI templates for three types of classrooms: One-to-one Classroom, Small Classroom, and Lecture Hall.
- This layer is open-sourced and available on GitHub. Developers can edit the source code to add customized classroom types.

### Edu Context (Native)

- This module is for native clients, including Android and iOS.
- It connects the Edu UI layer with the Edu Core layer and enables developers to quickly launch a flexible classroom with a small amount of code.
- This layer is open-sourced and provides APIs for modules such as users, rooms, streams, and widgets.

### Edu UI Store (Web/Electron)

- This module is for the Web and Electron clients.
- It implements business logic for the containers in the Edu UI layer and defines states and APIs used by the Edu UI layer.
- This module is open-sourced and available on GitHub. Developers are free to edit the source code based on their own UI requirements.

### The Edu Core layer

- This layer provides core business abilities and data support for the upper layers.
- This layer is closed source and provides modular interfaces for the user, room, stream, device, and widget management. With these abilities and API methods, developers can control operations and behaviors in classrooms.