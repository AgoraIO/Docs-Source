---
title: 'Migration guide'
sidebar_position: 2
type: docs
description: >
  Upgrade to the latest version of <Vg k="WHITE" />.
---

Netless Whiteboard is acquired by Agora and now fully integrated into the Agora product suite. This guide shows how to migrate all the projects under your Netless account to <Vg k="CONSOLE" />. 

## Prerequisites

To follow the procedure in this document, you must have an existing Netless account.


- Before the migration completes, do not enable the whiteboard feature in <Vg k="CONSOLE" />; otherwise, the migration may fail.
- If you do not have a Netless account, you can skip the migration procedure and directly enable the whiteboard feature. See [Enable and Configure <Vg k="WHITE" />](../develop/enable-whiteboard).

## Migration procedure

To migrate the projects under your current Netless account to <Vg k="CONSOLE" />, follow the steps for the account case that matches your situation.

<a name="netlessaccount"></a>
### A Netless account only

  1. Log in to <Link to="{{Global.AGORA_CONSOLE_URL}}"><Vg k="CONSOLE" /></Link> using the email address linked with your Netless account.

  2. Click **Send Email**. 

  3. Follow the instructions in the email you receive to reset your password. 

The reset process automatically creates a new Agora account using the email address linked with your Netless account. Then you can use the following steps to migrate your projects:

  1. Log in to <Link to="{{Global.AGORA_CONSOLE_URL}}"><Vg k="CONSOLE" /></Link> again using your new password.

  2. Follow the on-screen instructions, then click **Migrate**. 

 Agora automatically migrates all your projects from Netless to <Vg k="CONSOLE" />.

### A Netless account and an Agora account that use the same email address

  1. Log in to <Link to="{{Global.AGORA_CONSOLE_URL}}"><Vg k="CONSOLE" /></Link> using the email address linked with both accounts.

  2. Follow the on-screen instructions, then click **Migrate**. 

Agora automatically migrates all your projects from Netless to <Vg k="CONSOLE" />.


### A Netless account and an Agora account that use different email addresses

To migrate to the existing Agora account, contact sales at support@agora.io.

To create a new Agora account and migrate Netless projects to that account, follow the steps in <a href="#netlessaccount">A Netless account only</a>.

## Reference

After a successful migration, you can refer to the following guides to enable and integrate the <Vg k="WHITE" /> into your app:

- [Enable and Configure <Vg k="WHITE" />](../develop/enable-whiteboard) 
- [Join an <Vg k="WHITE" /> Room](../get-started/get-started-sdk)
