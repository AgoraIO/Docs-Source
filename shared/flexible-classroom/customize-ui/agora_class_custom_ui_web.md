---
title: "Customize the UI of Flexible Classroom with UIKit"
weight: 11
type: docs
description: 

---

You can use the Agora Classroom SDK as it is to launch a flexible classroom. However, if you want to customize the UI of classrooms, such as changing colors, changing buttons, adjusting layouts, and adding logos, you can get the source code of the Agora Classroom SDK and build a Classroom SDK on your own.

This page shows you how to customize the user interfaces of Flexible Classroom by editing the the source code of the UIKit in the Agora Classroom SDK.

## Understand the tech

In the Agora Classroom SDK, the code of the user interfaces is separated from the code of core business logic. The Classroom SDK contains two libraries, UIKit and EduCore. These two libraries connect with each other through [Agora Edu Context](./edu_context_api_ref_web_overview?platform=Web). For example, for the text chat feature of Flexible Classroom, a user can click on a button to send a text message, and the user can receive messages sent by other users. In this case, you can call a method in the Chat Context to send a message and listen for the events in the Chat Context to receive messages.

![](https://web-cdn.agora.io/docs-files/1623761240753)

You can find the source code of UIKit in the [CloudClass-Desktop](https://github.com/AgoraIO-Community/CloudClass-Desktop/tree/release/apaas-1.1.0.1-ga) repository on GitHub (Branch release/apaas/1.1.5). The UIKit contains the following two parts:

- `packages/agora-scenario-ui-kit/src/components`: The source code of the basic UI components used by Flexible Classroom. You can use the open-source tool [Storybook](https://storybook.js.org/docs/react/get-started/introduction) to develop and manage all UI components. A UI component generally contains the following files:
  - `.css`: Define the style of the component.
  - `.stories.tsx`: Define the display of components in Storybook.
  - `.tsx`: Define the detailed design of the component.
- `package /agora-classroom-sdk/src/ui-kit`:
  - `containers`: The source code of function-level UI components used by Flexible Classroom.
  - `scenarios`: The source code of the classroom-level UI components used by Flexible Classroom.

## Implementation

### Set up development environment

- Install [Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

   ```shell
   # Install Node.js and npm globally
   npm install -g npm
   # Check Node.js version
	 node -v
	 # Check npm version
   npm -v
   ```

- Install yarn

   ```shell
   # Install yarn
   npm install yarn -g
   # Check yarn version
   yarn -v
   ```

### Procedure

Modify the UI of Flexible Classroom, as follows:

1. Run the folllowing command to clone the CloudClass-Desktop project:

   ```bash
   git clone https://github.com/AgoraIO-Community/CloudClass-Desktop.git
   ```
   
2. Navigate to the root directory of the CloudClass-Desktop project, check out the release/apaas/1.1.5 branch, and then run the following command to install the dependencies.

   ```shell
   # Install global dev dependencies
   yarn
   # Install all dependencies via lerna and yarn
   yarn bootstrap
   ```

3. Run the following command to open Storybook to quickly adjust the UI.

   ```shell
   # Open storybook
   yarn dev:ui-kit
   ```

   You can see all the basic UI components used by Flexible Classroom in Storybook.

   ![storybook-example](https://web-cdn.agora.io/docs-files/1617714921810)

   You can directly edit the source code of a component in the `packages/agora-classroom-sdk/src/ui-kit/components` folder and see the changed UI in Storybook. If the existing basic UI components of Flexible Classroom cannot meet your needs, you can add a new UI component in the `packages/agora-classroom-sdk/src/ui-kit/components` directory, and then edit the code of classroom-level UI components in the `packages/agora-classroom-sdk/src/ui-kit/capabilities` to apply the UI component that you add to Flexible Classroom. For details, see the [UI customization examples](#example).

4. The user interfaces in Storybook are all based on Mock data, which can help you quickly view the UI display based on component properties. If you need to adjust the UI for the real scene, Agora recommends adjusting the UI in the development mode of the Agora Classroom SDK.

   1. Rename the `env.example` file in the `packages/Agora-classroom-sdk` folder to `.env`, then pass in your Agora App ID and App Certificate in the `.env` file.

   2. Run the following command in the root directory to launch a flexible classroom.

      ```shell
      yarn dev
      ```


<a name="example"></a>

## UI customization examples

This section provides examples of customizing the user interfaces of Flexible Classroom.

### Change the color of the navigation bar

The following example shows how to change the background color of the navigation bar component BizHeader from white to red by editing the `agora-scenario-ui-kit/src/components/biz-header/index.css` file.

#### Before

```css
.biz-header {
  @apply bg-white;
  padding: 0 15px 0 8px;
}
```

![biz-header-before](https://web-cdn.agora.io/docs-files/1617714984066)

#### After

```css
.biz-header {
  padding: 0 15px 0 8px;
  background: red;
}
```

![biz-header-after](https://web-cdn.agora.io/docs-files/1617715004882)

After the change, the background color of all the BizHeader components used in the Flexible Classroom becomes red.

![biz-header-after-fx](https://web-cdn.agora.io/docs-files/1617715029659)

### Change the classroom layout

The following example demonstrates how to switch the video and chat area in the Flexible Classroom. This adjustment involves multiple components. Therefore, you need to modify the parent container of these two components, which is the `packages/agora-classroom-sdk/src/ui-kit/capabilities/scenarios/1v1/index.tsx` file.

#### Before

```tsx
export const OneToOneScenario = observer(() => {
  ...
  return (
    <Layout
      className={cls}
      direction="col"
      style={{
        height: '100vh'
      }}
    >
      <NavigationBar />
      <Layout className="bg-white" style={{ height: '100%' }}>
        <Content>
          <ScreenSharePlayerContainer />
          <WhiteboardContainer />
        </Content>
        <Aside className={fullscreenCls}>
          <VideoList />
          <RoomChat />
        </Aside>
      </Layout>
      <DialogContainer />
      <LoadingContainer />
    </Layout>
  )
})
```

![](https://web-cdn.agora.io/docs-files/1620289086480)

#### After

```tsx
export const OneToOneScenario = observer(() => {
  ...
  return (
    <Layout
      className={cls}
      direction="col"
      style={{
        height: '100vh'
      }}
    >
      <NavigationBar />
      <Layout className="bg-white" style={{ height: '100%' }}>
        /** Change the order of Content and Aside in Layout. */
        <Aside className={fullscreenCls}>
          <VideoList />
          <RoomChat />
        </Aside>
        <Content>
          <ScreenSharePlayerContainer />
          <WhiteboardContainer />
        </Content>
      </Layout>
      <DialogContainer />
      <LoadingContainer />
    </Layout>
  )
})
```

![](https://web-cdn.agora.io/docs-files/1620289100529)

### Add a basic UI component

The following example shows how to add a custom basic UI component and use it in the Flexible Classroom:

1. Create a `custom` folder under the `packages/agora-classroom-sdk/src/ui-kit/components` directory and create the following files:

   - `index.css`

     ```css
     .custom {
       display: inline-block;
       padding: 10px;
       background: #efebe9;
       border: 5px solid #B4A078;
       outline: #B4A078 dashed 1px;
       outline-offset: -10px;
     }
     ```

   - `index.tsx`
   
     ```tsx
     import React, { FC } from 'react';
     import classnames from 'classnames';
     import { BaseProps } from '~components/interface/base-props';
     import './index.css';
     
     export interface CustomProps extends BaseProps {
         width?: number;
         height?: number;
         children?: React.ReactNode;
     }
     
     export const Custom: FC<CustomProps> = ({
         width = 90,
         height = 90,
         children,
         className,
         ...restProps
     }) => {
         const cls = classnames({
             [`custom`]: 1,
             [`${className}`]: !!className,
         });
         return (
             <div
                 className={cls}
                 style={{
                     width,
                     height,
                 }}
                 {...restProps}
             >
                 {children}
             </div>
         )
     }
     ```
   
   - `index.stories.tsx`
   
     ```tsx
     import React from 'react'
     import { Meta } from '@storybook/react';
     import { Custom } from '~components/custom'
     
     const meta: Meta = {
         title: 'Components/Custom',
         component: Custom,
     }
     
     type DocsProps = {
         width: number;
         height: number;
     }
     
     export const Docs = ({width, height}: DocsProps) => (
         <>
             <div className="mt-4">
                 <Custom
                     width={width}
                     height={height}
                 >
                     <h3>Custom UI component</h3>
                 </Custom>
             </div>
         </>
     )
     
     Docs.args = {
         width: 250,
         height: 200,
     }
     
     export default meta;
     ```
   
   The custom component is a div element with a two-layer border and renders a children element. You can see the custom component in Storybook.
   
   ![](https://web-cdn.agora.io/docs-files/1622777338261)

2. To export the custom component, add the following code to `packages/agora-scenario-ui-kit/src/components/index.ts` .

   ```ts
   export * from './custom'
   ```

3. Apply the custom component on the whiteboard of a one-to-one classroom, as follows:

   1. Import the custom component in `packages/agora-classroom-sdk/src/ui-kit/capabilities/containers/board/index.tsx`:

      ```ts
      import { Custom } from '~ui-kit'
      ```

   2. Use the custom component in `WhiteboardContainer`:

      ```tsx
      export const WhiteboardContainer = observer(() => {
      return (
         <div className="whiteboard">
           ...... 
           {showZoomControl ? <ZoomController
           className='zoom-position'
           zoomValue={zoomValue}
           currentPage={currentPage}
           totalPage={totalPage}
           maximum={!isFullScreen}
           clickHandler={handleZoomControllerChange}
           /> : null}
           <Custom className='custom-position' width={200} height={200}>
             <div>Use the custom component</div>
           </Custom>
           </div>
      )
    })
     ```
     
   3. Define the `custom-position` style in `packages/agora-classroom-sdk/src/ui-kit/capabilities/scenarios/1v1/style.css`:
   
      ```
      .custom-position{
       position: absolute;
       left: 100px;
       bottom: 200px;
      }
      ```
   4. Check the custom component in the flexible classroom.
   
         ![custom-ui-compnent-fx](https://web-cdn.agora.io/docs-files/1617715517511)

### Connect UI components with the app business logic

The following example shows how to display the class time in the custom component we added in the previous section.

1. To ensure the custom component supports displaying time, edit the `index.tsx` file of the custom component .

   ```tsx
   import React, { FC } from 'react';
   import classnames from 'classnames';
   import { BaseProps } from '~components/interface/base-props';
   import './index.css';
   /** Add the time property. */
   export interface CustomProps extends BaseProps {
       width?: number;
       height?: number;
       children?: React.ReactNode;
       time: number;
   }
   /** Render time. */
   export const Custom: FC<CustomProps> = ({
       width = 90,
       height = 90,
       children,
       className,
       time,
       ...restProps
   }) => {
       const cls = classnames({
           [`custom`]: 1,
           [`${className}`]: !!className,
       })
       return (
           <div
               className={cls}
               style={{
                   width,
                   height,
               }}
               {...restProps}
           >
               {time}
               {children}
           </div>
       )
   }
   ```

2. Add a property to the custom component in `packages/agora-classroom-sdk/src/ui-kit/capabilities/containers/board/index.tsx`.

   ```tsx
   ...
    return (
    <div className="whiteboard">
      {
        ready ?
        <div id="netless" style={{position: 'absolute', top: 0, left: 0, height: '100%', width: '100%'}} ref={mountToDOM} ></div> : null
      }
      {showTab ?
      <TabsContainer /> : null}
      {showToolBar ?
        <Toolbar active={currentSelector} activeMap={activeMap} tools={tools} onClick={handleToolClick} className="toolbar-biz" />
      : null}
      {showZoomControl ? <ZoomController
        className='zoom-position'
        zoomValue={zoomValue}
        currentPage={currentPage}
        totalPage={totalPage}
        maximum={!isFullScreen}
        clickHandler={handleZoomControllerChange}
      /> : null}
      /** Add the time property. */
      <Custom time={5000} className='custom-position' width={200} height={200}>
        <div>Use the custom component</div>
      </Custom>
    </div>
    )
})
   ```

   After the modification, run the project, and you can see that the time is displayed on the custom component.

   ![](https://web-cdn.agora.io/docs-files/1622779701958)

3. We need to import real class time. In this example, we use the [liveClassStatus](https://docs.agora.io/en/agora-class/edu_context_api_ref_wev_room?platform=Web#liveclassstatus) property of the RoomContext in the Agora Edu Context to get the class time. Edit `packages/agora-classroom-sdk/src/ui-kit/capabilities/containers/board/index.tsx` to get the class time and set it as a property in the custom component .

   <div class="alter note">Agora does not recommend directly referencing the Agora Edu Context in basic UI components, because basic UI components may be reused in different scenarios.</div>

   ```tsx
   ...
export const WhiteboardContainer = observer(() => {
     ...
     const {
       liveClassStatus
     } = useRoomContext()

     return (
       <div className="whiteboard">
         {
           ready ?
           <div id="netless" style={{position: 'absolute', top: 0, left: 0, height: '100%', width: '100%'}} ref={mountToDOM} ></div> : null
         }
         {showTab ?
         <TabsContainer /> : null}
         {showToolBar ?
           <Toolbar active={currentSelector} activeMap={activeMap} tools={tools} onClick={handleToolClick} className="toolbar-biz" />
         : null}
         {showZoomControl ? <ZoomController
           className='zoom-position'
           zoomValue={zoomValue}
           currentPage={currentPage}
           totalPage={totalPage}
           maximum={!isFullScreen}
           clickHandler={handleZoomControllerChange}
         /> : null}
         <Custom time={liveClassStatus.duration} className='custom-position' width={200} height={200}>
           <div>Use the custom component</div>
         </Custom>
       </div>
     )
})
   ```

   After the modification, run the project, and you can see that the class time is automatically updated on the user interface in milliseconds. We can then modify the `index.tsx` file of the custom component, fine-tune the style of the custom component, and then format the time.

   ```tsx
   ...
export const Custom: FC<CustomProps> = ({
    width = 90,
    height = 90,
    children,
    className,
    time,
    ...restProps
}) => {
    const cls = classnames({
        [`custom`]: 1,
        [`${className}`]: !!className,
    })
    return (
        <div
            className={cls}
            style={{
                width,
                height,
            }}
            {...restProps}
        >
            The class has lasted for {Math.floor(time/1000)} seconds
            {children}
        </div>
    )
}
   ```

   The final user interface is as follows:

   ![](https://web-cdn.agora.io/docs-files/1622780228732)

### Change the global style of basic UI components

The following example shows how to modify the global style of basic UI components.

1. Define global styles in `packages/agora-classroom-sdk/src/ui-kit/styles/global.css`:

   ```css
   .fixed-container {
 display: flex;
 justify-content: center;
 align-items: center;
 flex: 1;
 "height": 360
 position: fixed;
 width: 480,
 z-index: 99;
}
   ```

2. Add the following code to the `.stories.tsx` and `.tsx` files of the basic UI components to apply this global style:

   ```ts
   export const DialogContainer: React.FC<any> = observer(() => {
    const { dialogQueue } = useDialogContext()
    return (
    <div>
     {
        dialogQueue.map(({ id, component: Component, props }: DialogType) => (
          <div key={id} className="fixed-container">
            <Component {...props} id={id} />
          </div>
       ))
     }
    </div>
 )
})
   ```