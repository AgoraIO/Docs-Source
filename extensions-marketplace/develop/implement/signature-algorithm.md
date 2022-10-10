---
title: "Encrypted signature"
sidebar_position: 4
type: docs
description: >
  How to generate the signature that allows vendors to verify HTTP requests sent by Agora.
---

export const toc = [{}];

The Provisioning, Usage, and Billing APIs have a request parameter named `signature`. This parameter is an encrypted string shared between vendors and Agora. It allows vendors to verify HTTP requests sent by Agora.

This page explains how to generate a signature.


## Overview

The signature combines the source string (`SourceString`) and your secret key (`apiSecret&`) using an encryption algorithm, as follows:
- GET methods:

  ```
  signature = URLEncode(Base64( HMAC-SHA1( apiSecret&, SourceString) ), "UTF-8")
  ```

- POST and PUT methods:

  ```
  signature = Base64( HMAC-SHA1( apiSecret&, SourceString) )
  ```

After receiving the request, you need to apply the encryption algorithm to generate a signature on your own. If the generated signature is the same as the one you receive, you can verify that the request is sent by Agora.


## Generate a signature (GET)

Take the [Usage API](usage) for example, Agora sends the following request to query usage information:

```text
https://[host]/usage?fromTs=1619913600&toTs=1619917200&pageNum=1&apiKey=pzD5XinRSlmA64tZx81fL92YcBsJK0gd&signature={signature}
```

For this example, the parameters used in the encryption algorithm are as follows:

| Parameter         | Value                                                           |
| :----------- | :----------------------------------------------------------- |
| `SourceString` | `GET&%2Fusage&apiKey%3DpzD5XinRSlmA64tZx81fL92YcBsJK0gd%26fromTs%3D1619913600%26pageNum%3D1%26toTs%3D1619917200` |
| `apiSecret`    | `U1SXE6k57vxVRjTomgquwC2F3tH8ziOB` (This is for demonstration only. Your actual `apiSecret` should be different.) |
| `signature`    | `SFVnCVlRbrZcjMPGTWVxAE4QWZ8%3D`                             |

This section shows how to generate the signature step-by-step.

### Step 1: Construct the source string

To construct `SourceString`, follow these steps:

1. Get the type of the HTTP request and add an "&":

   ```
   GET&
   ```

2. In the request URL, leave only the path after `[host]` and before `?` (if any), URL-encode the resulting string (that is, `/usage`), and add an "&". The source string now looks like:


   ```
   GET&%2Fusage&
   ```

3. Sequence the query parameters in the request URL except `signature` (that is, `fromTs`, `toTs`, and `apiKey`) in alphabetical ascending order in the form of `key=value`, and combine them using "&":

   ```text
   apiKey=pzD5XinRSlmA64tZx81fL92YcBsJK0gd&fromTs=1619913600&pageNum=1&toTs=1619917200
   ```

   URL-encode the string above and add it to the source string:

   ```text
   GET&%2Fusage&apiKey%3DpzD5XinRSlmA64tZx81fL92YcBsJK0gd%26fromTs%3D1619913600%26pageNum%3D1%26toTs%3D1619917200
   ```

### Step 2: Construct your secret key

To construct the secret key, add an “&” to the end of your apiSecret string.

For example, if the apiSecret you provide when applying to become a vendor is U1SXE6k57vxVRjTomgquwC2F3tH8ziOB, the secret key should be `U1SXE6k57vxVRjTomgquwC2F3tH8ziOB&`.


### Step 3: Generate the signature

The encryption algorithm for GET methods is as follows:

```
signature = URLEncode(Base64( HMAC-SHA1( apiSecret&, SourceString) ), "UTF-8")
```

Using the `SourceString` and `apiSecret&` from previous steps, you get this signature:

```text
SFVnCVlRbrZcjMPGTWVxAE4QWZ8%3D
```

## Generate a signature (POST and PUT)

Take the [Provisioning API](provisioning) for example, Agora sends the following request body:

```json
{
    "projectId": "430892",
    "apiKey": "pzD5XinRSlmA64tZx81fL92YcBsJK0gd",
    "signature": "To be generated"
}
```

And the request URL is:

```text
https://[host]/customers/123456/projects/new
```

For this example, the parameters used in the encryption algorithm are as follows:

| Parameter          | Value                                                     |
| :----------- | :----------------------------------------------------------- |
| `SourceString` | `POST&%2Fcustomers%2F123456%2Fprojects%2Fnew&apiKey%3DpzD5XinRSlmA64tZx81fL92YcBsJK0gd%26projectId%3D430892` |
| `apiSecret`    | `U1SXE6k57vxVRjTomgquwC2F3tH8ziOB`  (This is for demonstration only. Your actual `apiSecret` should be different.) |
| `signature`    | `YZOl2v5q3I7o0x3F13tpnkq5aDI=`                               |

This section shows how to generate the signature step-by-step.

### Step 1: Construct the source string

To construct `SourceString`, follow these steps:

1. Get the type of the HTTP request and add an "&":

   ```
   POST&
   ```

2. In the request URL, leave only the path after `[host]` and before `?` (if any), URL-encode the resulting string (that is, `/usage`), and add an "&". The source string now looks like:

   ```text
   POST&%2Fcustomers%2F123456%2Fprojects%2Fnew&
   ```

3. Sequence the query parameters in the request body except `signature` (that is, `projectId` and `apiKey`) in alphabetical ascending order in the form of `key=value`, and combine them using "&":

   ```text
   apiKey=pzD5XinRSlmA64tZx81fL92YcBsJK0gd&projectId=430892
   ```

   URL-encode the string above and add it to the source string:

   ```text
   POST&%2Fcustomers%2F123456%2Fprojects%2Fnew&apiKey%3DpzD5XinRSlmA64tZx81fL92YcBsJK0gd%26projectId%3D430892
   ```

### Step 2: Construct your secret key

To construct the secret key, add an “&” to the end of your apiSecret string.

For example, if the apiSecret you provide when applying to become a vendor is U1SXE6k57vxVRjTomgquwC2F3tH8ziOB, the secret key should be `U1SXE6k57vxVRjTomgquwC2F3tH8ziOB&`.

### Step 3: Generate the signature

The encryption algorithm for POST and PUT methods is as follows:

```
signature = Base64( HMAC-SHA1( apiSecret&, SourceString) )
```

Using the `SourceString` and `apiSecret&` from previous steps, you get this signature:

```text
YZOl2v5q3I7o0x3F13tpnkq5aDI=
```

