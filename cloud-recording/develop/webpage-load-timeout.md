---
title: "Web page load timeout detection"
sidebar_position: 10
type: docs
platform_selector: false
description: >
  Call the specified interface to notify the browser that the web page has been loaded
---

## Introduction

During web page recording,  poor network performance may cause the following issues:

- The web page takes a long time to load, and the load time is not fixed. It is impossible to know the time when the effective recording starts, and important content may be lost.
- The web page fails to load. Because there is no error reporting mechanism, the browser does not reload the page, resulting in page content inconsistent with expectations.

In order to solve these issues, the web page recording service supports **web page load timeout detection**. During the web page recording, you need to call the specified interface to notify the browser that the web page has been loaded to achieve the following functions:

- If the browser receives a notification that the web page is loaded before the timeout limit, the browser starts recording the web page.
- If the browser does not receive a notification that the web page is loaded before the timeout limit, the browser automatically reloads the web page and notify the developer in time as an event message. If the web page fails to load before the timeout limit for a second time, the recording service stops to avoid recording wrong content.

The Agora web page load timeout detection function can only ensure that page elements are loaded correctly. If you need more comprehensive protection for web page recording, please refer to [Best Practices in Integrating Web Page Recording](../best-practices/webpage-best-practices).

## Implementation

You need to implement the web page load timeout detection function in two steps:

1. When calling the [`start`](../reference/restful-api#start) method, set the web page load timeout limit through the `readyTimeout` parameter.
2. Judge for yourself whether the web page is loaded, and call the specified interface of the browser to notify the browser when the web page is loaded.
 - If the web page loads before the set timeout limit, call the specified interface of the browser to notify the browser that the web page has been loaded.
 - If the web page fails to load completely before the set timeout limit, the browser reloads the web page. The `reason` field received in the [`web_recorder_reload`](../reference/rest-api-overview#73-web_recorder_reload) callback is `page_load_timeout`.
 - If the web page fails to load before the timeout limit for a second time, it means the web page has failed to load. The recording service stops. The `code` field received in the [`web_recorder_stopped`](../reference/rest-api-overview#71-web_recorder_stopped-web_recorder_stopped) callback is `4`, and the `message` field is `page_load_timeout`.

### Set the web page load timeout limit

You need to set the web page load timeout limit through the `readyTimeout` parameter when calling the [`start`](../reference/restful-api#start) method. The parameter settings are as follows:

`readyTimeout`: (optional) Number, set the web page loading timeout limit, in seconds.The value range is [0,60].

- 0 or null, which means the web page loading status is not detected.
- An integer greater than or equal to 1, which sets the web page load timeout limit.

If you set `readyTimeout` to less than 0 or a non-integer, an error code `2` is received.

### Set the web page loading completion notification interface

You need to call the `notifyReady()` interface on the recording web page to notify the browser that the web page has been loaded successfully.

Sample code:

```
<script>
function notifyReady() {
    if (typeof window.navigator.notifyReady === 'function')
        window.navigator.notifyReady();
}
</script>
```
If you record other URL pages, you need to set the `notifyReady` interface on the page to be recorded.

### API reference

- [`start`](../reference/restful-api#start) 
- [`web_recorder_started`](../reference/rest-api-overview#70-web_recorder_started-web_recorder_started)
- [`web_recorder_reload`](../reference/rest-api-overview#73-web_recorder_reload)

