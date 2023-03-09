# Manage Chat Room Attributes

This page shows how to manage custom attributes by calling Agora Chat RESTful APIs, including adding, removing, modifying, and retrieving attributes that are stored as key-value maps.

Before calling the following methods, ensure that you understand the call frequency limit of Agora Chat RESTful API calls described in [Limitations](./agora_chat_limitation).

<a name="param"></a>

## Common parameters

The following table lists common request and response parameters of the Agora Chat RESTful APIs:

### Request parameters

| Parameter | Type | Description | Required |
| :--------- | :----- | :---------------- | :------- |
| `host` | String | The domain name assigned by the Agora Chat service to access RESTful APIs. For how to get the domain name, see [Get the information of your project](./enable_agora_chat?platform=RESTful#get-the-information-of-the-agora-chat-project). | Yes |
| `org_name` | String | The unique identifier assigned to each company (organization) by the Agora Chat service.  For how to get the org name, see [Get the information of your project](./enable_agora_chat?platform=RESTful#get-the-information-of-the-agora-chat-project). | Yes |
| `app_name` | String | The unique identifier assigned to each app by the Agora Chat service. For how to get the app name, see [Get the information of your project](./enable_agora_chat?platform=RESTful#get-the-information-of-the-agora-chat-project). | Yes |
| `username` | String | The unique login account of the user. The username must be 64 characters or less and cannot be empty.  The following character sets are supported:<li>26 lowercase English letters (a-z)</li><li>26 uppercase English letters (A-Z)</li><li>10 numbers (0-9)</li><li>"\_", "-", "."</li><div class="alert note"><ul><li>The username is case insensitive, so `Aa` and `aa` are the same username. </li><li>Ensure that each username under the same app is unique.</li></ul></div> | Yes |


### Response parameters

| Parameter | Type | Description |
| :---------------- | :----- | :---------------------------------------------------------------- |
| `action` | String | The request method. |
| `organization` | String | The unique identifier assigned to each company (organization) by the Agora Chat service. This is the same as `org_name`. |
| `application` | String | A unique internal ID assigned to each app by the Agora Chat service. You can safely ignore this parameter. |
| `applicationName` | String | The unique identifier assigned to each app by the Agora Chat service. This is the same as `app_name`. |
| `uri` | String | The request URI. |
| `entities ` | JSON | The response entity. |
| `data` | JSON | The details of the response. |
| `timestamp` | Number | The Unix timestamp (ms) of the HTTP response. |
| `duration` | Number | The duration (ms) from when the HTTP request is sent to the time the response is received. |


## Authorization

Chat RESTful APIs require Bearer HTTP authentication. Every time an HTTP request is sent, the following `Authorization` field must be filled in the request header:

```http
Authorization: Bearer ${YourAppToken}
```

In order to improve the security of the project, Agora uses a token (dynamic key) to authenticate users before they log in to the chat system. Chat RESTful APIs only support authenticating users using app tokens. For details, see [Authentication using App Token](./generate_app_tokens?platform=RESTful).


## Set custom attributes

Adds new custom chat room attributes or modifies existing ones set by the current user.

<div class="alert note">This method is only used to modify the existing key-value pairs set by the current user. To perform the overwrite operation, see <a href="overwrite">Forcibly set custom attributes</a>.</div>

### HTTP request

```http
PUT https://{host}/{org_name}/{app_name}/metadata/chatroom/{chatroom_id}/user/{username}
```

#### Path parameter

For the parameters and detailed descriptions, see [Common parameters](#param).

#### Request header

| Parameter | Type | Description | Required |
| :-------------- | :----- | :--------------------- | :------- |
| `Accept` | String | `application/json` | Yes |
| `Content-Type` | String | `application/json` | Yes |
| `Authorization` | String | The authentication token of the user or administrator, in the format of `Bearer ${token}`, where `Bearer` is a fixed character, followed by an English space, and then the obtained token value. | Yes |

#### Request body

| Parameter | Type   | Required | Description                          |
| :------------ | :----- | :------- | :------ |
| `metaData`  | JSON | Yes  | The custom attributes that are stored as a collection of key-value pairs in the format `Map<String,String>`. Keys in a map are unique attribute names that map to the corresponding attribute values. Note the following limitations: <ul><li>Each chat room can have a maximum of 100 custom attributes.</li><li>The size of all custom attributes in an app can be a maximum of 10 GB.</li><li>Each map can contain a maximum of 10 key-value pairs.</li><li>Each key can contain a maximum of 128 characters.</li><li>Each value can contain a maximum of 4,086 characters.</li></ul> The following character sets are supported:<ul><li>26 lowercase English letters (a-z)</li><li>26 uppercase English letters (A-Z)</li><li>10 numbers (0-9)</li><li>"_", "-", "."</li></ul> |
| `autoDelete` | String | No  | Whether to automatically delete the custom attributes set by a chat room member when this member leaves the chat room:<li>(Default) <code>DELETE</code>: Delete the custom attributes.</li> <li><code>NO_DELETE</code>: Do not delete the custom attributes.</li> |

### HTTP response

#### Response body

| Field | Type | Description  |
| :----- | :------ | :------ |
| `data.successKeys` | Array | The keys of the custom attributes that are successfully set. |
| `data.errorKeys` | Object | The keys of the custom attributes that fail to be set paired with the corresponding error descriptions. |

For other fields and detailed descriptions, see [Common parameters](#param).

### Example

#### Request example

```shell
# Replaces <YourAppToken> with the app token generated from your token server.
curl -X PUT -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer <YourAppToken> ' -d '{
    "metaData": {
        "key1": "value1",
		    "key2": "value2"
      },
    "autoDelete": "DELETE"
 }' 'http://XXXX/XXXX/XXXX/metadata/chatroom/662XXXX13/user/user1'
```

#### Response example

```json
{
  "data":
  {
    "successKeys": ["key1"],
	  "errorKeys": {"key2":"errorDesc"},
  }
}
```


## Retrieve custom attributes

Retrieves the specified custom attributes of a chat room.

### HTTP request

```http
POST https://{host}/{org_name}/{app_name}/metadata/chatroom/{chatroom_id}
```

#### Path parameter

For the parameters and detailed descriptions, see [Common parameters](#param).

#### Request header

| Parameter | Type | Description | Required |
| :-------------- | :----- | :--------------------- | :------- |
| `Accept` | String | `application/json` | Yes |
| `Content-Type` | String | `application/json` | Yes |
| `Authorization` | String | The authentication token of the user or administrator, in the format of `Bearer ${token}`, where `Bearer` is a fixed character, followed by an English space, and then the obtained token value. | Yes |

#### Request body

| Parameter | Type   | Required | Description                          |
| :------------ | :----- | :------- | :------ |
| `keys`        | Array | No    | The keys of the custom attributes to retrieve. If you pass an empty array to this parameter, all custom attributes of the specified chat room are returned.  |

### HTTP response

#### Response body

| Field | Type | Description  |
| :----- | :------ | :------ |
| `data`   | Object | The key-value pairs of the retrieved custom attributes. |

For other fields and detailed descriptions, see [Common parameters](#param).

### Example

#### Request example

```shell
# Replaces <YourAppToken> with the app token generated from your token server.
curl -X POST -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer <YourAppToken> ' -d '{
    "keys": ["key1","key2"]
 }' 'http://XXXX/XXXX/XXXX/metadata/chatroom/662XXXX13'
```

#### Response example

```json
{
  "data":
  {
    "key1": "value1",
		"key2": "value2"
  }
}
```


## Remove custom attributes

Removes custom attributes set by the current user.

<div class="alert note">This method is only used to remove the key-value pairs set by the current user. To remove the key-value pairs set by others, see <a href="#force">Forcibly remove custom attributes</a>.</div>

### HTTP request

```http
DELETE https://{host}/{org_name}/{app_name}/metadata/chatroom/{chatroom_id}/user/{username}
```

#### Path parameter

For the parameters and detailed descriptions, see [Common parameters](#param).

#### Request header

| Parameter | Type | Description | Required |
| :-------------- | :----- | :--------------------- | :------- |
| `Accept` | String | `application/json` | Yes |
| `Content-Type` | String | `application/json` | Yes |
| `Authorization` | String | The authentication token of the user or administrator, in the format of `Bearer ${token}`, where `Bearer` is a fixed character, followed by an English space, and then the obtained token value. | Yes |

#### Request body

| Parameter | Type   | Required | Description                          |
| :------------ | :----- | :------- | :------ |
| `keys`        | Array | No    | The keys of the custom attributes to remove.      |

### HTTP response

#### Response body

| Field | Type | Description  |
| :----- | :------ | :------ |
| `data.successKeys`   | Array | The keys of the custom attributes that are successfully removed.  |
| `data.errorKeys` | Object | The keys of the custom attributes that fail to be removed paired with the corresponding error descriptions. |

For other fields and detailed descriptions, see [Common parameters](#param).

### Example

#### Request example

```shell
# Replaces <YourAppToken> with the app token generated from your token server.
DELETE -X POST -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer <YourAppToken> ' -d '{
    "keys": ["key1","key2"]
 }' 'http://XXXX/XXXX/XXXX/metadata/chatroom/662XXXX13/user/user1'
```

#### Response example

```json
{
  "data":
  {
    "successKeys": ["key1"],
	  "errorKeys": {"key2":"errorDesc"}
  }
}
```

<a name="overwrite"></a>

## Forcibly set custom attributes

In addition to adding new custom attributes or modifying the existing ones set by the current user, this method can also be used to overwrite the custom attributes set by others.

### HTTP request

```http
PUT https://{host}/{org_name}/{app_name}/metadata/chatroom/{chatroom_id}/user/{username}/forced
```

#### Path parameter

For the parameters and detailed descriptions, see [Common parameters](#param).

#### Request header

| Parameter | Type | Description | Required |
| :-------------- | :----- | :--------------------- | :------- |
| `Accept` | String | `application/json` | Yes |
| `Content-Type` | String | `application/json` | Yes |
| `Authorization` | String | The authentication token of the user or administrator, in the format of `Bearer ${token}`, where `Bearer` is a fixed character, followed by an English space, and then the obtained token value. | Yes |

#### Request body

| Parameter | Type   | Required | Description                          |
| :------------ | :----- | :------- | :------ |
| `metaData`  | JSON | Yes  | The custom attributes that are stored as a collection of key-value pairs in the format `Map<String,String>`. Keys in a map are unique attribute names that map to the corresponding attribute values. Note the following limitations: <ul><li>Each chat room can have a maximum of 100 custom attributes.</li><li>The size of all custom attributes in an app can be a maximum of 10 GB.</li><li>Each map can contain a maximum of 10 key-value pairs.</li><li>Each key can contain a maximum of 128 characters.</li><li>Each value can contain a maximum of 4,086 characters.</li></ul> The following character sets are supported:<ul><li>26 lowercase English letters (a-z)</li><li>26 uppercase English letters (A-Z)</li><li>10 numbers (0-9)</li><li>"_", "-", "."</li></ul> |
| `autoDelete` | String | No  | Whether to automatically delete the custom attributes set by a chat room member when this member leaves the chat room:<li>(Default) <code>DELETE</code>: Delete the custom attributes.</li> <li><code>NO_DELETE</code>: Do not delete the custom attributes.</li> |

### HTTP response

#### Response body

| Field | Type | Description  |
| :----- | :------ | :------ |
| `data.successKeys`   | Array | The keys of the custom attributes that are successfully set. |
| `data.errorKeys` | Object | The keys of the custom attributes that fail to be set paired with the corresponding error descriptions. |

For other fields and detailed descriptions, see [Common parameters](#param).

### Example

#### Request example

```shell
# Replaces <YourAppToken> with the app token generated from your token server.
curl -X PUT -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer <YourAppToken> ' -d '{
    "metaData": {
        "key1": "value1",
		    "key2": "value2"
      },
    "autoDelete": "DELETE"
 }' 'http://XXXX/XXXX/XXXX/metadata/chatroom/662XXXX13/user/user1/forced'
```

#### Response example

```json
{
  "data":
  {
    "successKeys": ["key1"],
	  "errorKeys": {"key2":"errorDesc"}
  }
}
```

<a name="force"></a>

## Forcibly remove custom attributes

In addition to removing the custom attributes set by the current user, this method can also be used to remove custom attributes set by others.

### HTTP request

```http
DELETE https://{host}/{org_name}/{app_name}/metadata/chatroom/{chatroom_id}/user/{username}/forced
```

#### Path parameter

For the parameters and detailed descriptions, see [Common parameters](#param).

#### Request header

| Parameter | Type | Description | Required |
| :-------------- | :----- | :--------------------- | :------- |
| `Accept` | String | `application/json` | Yes |
| `Content-Type` | String | `application/json` | Yes |
| `Authorization` | String | The authentication token of the user or administrator, in the format of `Bearer ${token}`, where `Bearer` is a fixed character, followed by an English space, and then the obtained token value. | Yes |

#### Request body

| Parameter | Type   | Required | Description                          |
| :------------ | :----- | :------- | :------ |
| `keys`        | Array | No    | The keys of the custom attributes to remove.      |

### HTTP response

#### Response body

| Field | Type | Description  |
| :----- | :------ | :------ |
| `data.successKeys`   | Array | The keys of the custom attributes that are successfully removed.  |
| `data.errorKeys` | Object | The keys of the custom attributes that fail to be removed paired with the corresponding error descriptions. |

For other fields and detailed descriptions, see [Common parameters](#param).

### Example

#### Request example

```shell
# Replaces <YourAppToken> with the app token generated from your token server.
DELETE -X POST -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer <YourAppToken> ' -d '{
    "keys": ["key1","key2"]
 }' 'http://XXXX/XXXX/XXXX/metadata/chatroom/662XXXX13/user/user1/forced'
```

#### Response example

```json
{
  "data":
  {
    "successKeys": ["key1"],
	"errorKeys": {"key2":"errorDesc"}
  }
}
```


<a name="code"></code>

## Status codes

For details, see [HTTP Status Codes](./agora_chat_status_code).