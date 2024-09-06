# SSOReady-Python

`ssoready` is a Python SDK for the [SSOReady](https://ssoready.com) API. 

SSOReady is a set of open-source dev tools for implementing Enterprise SSO. You
can use SSOReady to add SAML support to your product this afternoon, for free,
forever. You can think of us as an open source alternative to products like
Auth0 or WorkOS.

This library includes type definitions for all request and response fields, and
offers both synchronous and asynchronous clients powered by `httpx`.

## Installation

Add this dependency to your project's build file:

```bash
pip install ssoready
# or
poetry add ssoready
```

## Usage

For full documentation, check out https://ssoready.com/docs.

At a super high level, all it takes to add SAML to your product is to:

1. Sign up on [app.ssoready.com](https://app.ssoready.com) for free
2. From your login page, call `get_saml_redirect_url` when you want a user to sign in with SAML
3. Your user gets redirected back to a callback page you choose, e.g. `your-app.com/ssoready-callback?saml_access_code=...`. You
   call `redeem_saml_access_code` with the `saml_access_code` and log them in.

Import and construct a SSOReady client like this:

```python
from ssoready.client import SSOReady

client = SSOReady() # loads your API key from the env var SSOREADY_API_KEY
# or
client = SSOReady(api_key="ssoready_sk_...")
```

Calling the `get_saml_redirect_url` endpoint looks like this:

```python
# this is how you implement a "Sign in with SSO" button
redirect_url = client.saml.get_saml_redirect_url(
    # the ID of the organization/workspace/team (whatever you call it)
    # you want to log the user into
    organization_external_id="..."
).redirect_url

# redirect the user to `redirect_url`...
```

And using `redeem_saml_access_code` looks like this:

```python
# this goes in your handler for POST /ssoready-callback
redeem_result = client.saml.redeem_saml_access_code(saml_access_code="saml_access_code_...")

email = redeem_result.email
organization_external_id = redeem_result.organization_external_id

# log the user in as `email` inside `organizationExternalId`...
```

Check out [the quickstart](https://ssoready.com/docs) for the details spelled
out more concretely. The whole point of SSOReady is to make enterprise SSO super
obvious and easy.

## Async Client

You an also use asyncio with this SDK. Do so by using `AsyncSSOReady` instead of
`SSOReady`.

```python
from ssoready.client import AsyncSSOReady

client = AsyncSSOReady()

async def main() -> None:
    await client.saml.get_redirect_url(organization_external_id="...")
    
asyncio.run(main())
```

All methods available on the sync `SSOReady` client are also available on
`AsyncSSOReady`.

## Contributing

Issues and PRs are more than welcome. Be advised that this library is largely
autogenerated from
[`ssoready/fern-config`](https://github.com/ssoready/fern-config). Most code
changes ultimately need to be made there, not on this repo.
