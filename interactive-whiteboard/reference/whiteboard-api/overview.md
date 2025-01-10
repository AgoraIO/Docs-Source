---
title: 'Overview'
sidebar_position: 1
type: docs
description: >
    Basic information about the Interactive Whiteboard API.
---

This article provides basic information about the <Vg k="WHITE_SDK" /> RESTful API.

## Domain

All requests are sent to the domain named `api.netless.link`.

## Data format

The `Content-Type` field in all HTTP request headers is `application/json`. All requests and responses are in JSON format. All request URLs and request bodies are case-sensitive.

<div class="alert note">Agora's server for the whiteboard service will allow more data formats but cannot guarantee full compatibility. If all request parameters are filled in correctly, but the request still fails, please check the data format of the request.</div>

## Core features

The <Vg k="WHITE_SDK" /> RESTful API provides the following features:

- [Token generation](../../whiteboard-sdk/develop/generate-token-rest)
- [Room management](room-management)
- [Screenshot management](screenshots)
- [Scene management](scene-management)
- [File conversion](file-conversion)

## Status codes

All possible response status codes are listed in the table below:

- If the status code is `200` or `201`, the request is successful.

- If the status code is not `200` or `201`, the request fails. The response body includes a `message` field that describes the reason for the failure.

| Response status code | Status | Description |
| :-------------- | :-------------------- | :--------------------------------------------------------- |
| `200` | OK | The request is successful, and the server returns the requested data. |
| `201` | Created | The request is successful, and the server creates or modifies the requested data. |
| `400` | Invalid request | The user's request has an error, and the server does not create or modify any data. |
| `401` | Unauthorized | The user does not have permission (the token is incorrect). |
| `403` | Forbidden | The user has permission (contrary to 401), but is denied access to perform the requested operation. |
| `404` | Not found | The server cannot find the requested resource. |
| `500` | Internal server error | The server encounters an error and cannot process the request. |