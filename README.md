# SSOReady Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

The SSOReady Python Library provides convenient access to the SSOReady API from
applications written in Python.

The library includes type definitions for all request and response fields, and
offers both synchronous and asynchronous clients powered by `httpx`.

## Installation

Add this dependency to your project's build file:

```bash
pip install ssoready
# or
poetry add ssoready
```

## Usage

Simply import `SSOReady` and start making calls to our API.

```python
from ssoready.client import SSOReady

client = SSOReady(
    api_key="YOUR_API_KEY", # defaults to SSOREADY_API_KEY
)

client.saml.redeem_access_code(
    saml_access_code="saml_access_code_94d90b43a2027a9084bfc792",
)
```

## Async Client

The SDK also exports an async client so that you can make non-blocking
calls to our API.

```python
from ssoready.client import AsyncSSOReady

client = AsyncSSOReady(
    api_key="YOUR_API_KEY",
)

async def main() -> None:
    await client.saml.redeem_access_code(
        saml_access_code="saml_access_code_94d90b43a2027a9084bfc792",
    )
asyncio.run(main())
```

## Exception Handling

All errors thrown by the SDK will be subclasses of [`ApiError`](./src/schematic/core/api_error.py).

```python
import ssoready

try:
    client.saml.redeem_access_code(
        saml_access_code="saml_access_code_94d90b43a2027a9084bfc792",
    )
except ssoready.core.ApiError as e: # Handle all errors
    print(e.status_code)
    print(e.body)
```

## Advanced

### Timeouts

By default, requests time out after 60 seconds. You can configure this with a
timeout option at the client or request level.

```python
from ssoready.client import SSOReady

client = SSOReady(
    ...,
    # All timeouts are 20 seconds
    timeout=20.0,
)

# Override timeout for a specific method
client.saml.redeem_access_code(..., {
    timeout_in_seconds=20.0
})
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be
retried as long as the request is deemed retriable and the number of retry attempts has not grown larger
than the configured retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.saml.redeem_access_code(..., {
    max_retries=1
})
```

### Custom HTTP client

You can override the httpx client to customize it for your use-case. Some common use-cases
include support for proxies and transports.

```python
import httpx

from ssoready.client import SSOReady

client = SSOReady(...,
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update.
Therefore, we recommend pinning the package version to a specific version in your package.json file.
This way, you can install the same version each time without breaking changes unless you are
intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a
PR as a proof of concept, but know that we will not be able to merge it as-is.
