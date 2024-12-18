# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ssoready.core.http_client import AsyncHttpClient, HttpClient

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.query_encoder import encode_query
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..types.get_saml_redirect_url_response import GetSamlRedirectUrlResponse
from ..types.redeem_saml_access_code_response import RedeemSamlAccessCodeResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SamlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper: SyncClientWrapper = client_wrapper

    def redeem_saml_access_code(
        self, *, saml_access_code: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> RedeemSamlAccessCodeResponse:
        """
        Parameters
        ----------
        saml_access_code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedeemSamlAccessCodeResponse
            OK

        Examples
        --------
        from ssoready.client import SSOReady

        client = SSOReady(
            api_key="YOUR_API_KEY",
        )
        client.saml.redeem_saml_access_code(
            saml_access_code="saml_access_code_...",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if saml_access_code is not OMIT:
            _request["samlAccessCode"] = saml_access_code
        _response = HttpClient.request(
            self._client_wrapper.httpx_client,
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/saml/redeem"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries", 0) if request_options is not None else 0,  
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedeemSamlAccessCodeResponse, _response.json()) 
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_saml_redirect_url(
        self,
        *,
        saml_connection_id: typing.Optional[str] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        organization_external_id: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSamlRedirectUrlResponse:
        """
        Parameters
        ----------
        saml_connection_id : typing.Optional[str]

        organization_id : typing.Optional[str]

        organization_external_id : typing.Optional[str]

        state : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSamlRedirectUrlResponse
            OK

        Examples
        --------
        from ssoready.client import SSOReady

        client = SSOReady(
            api_key="YOUR_API_KEY",
        )
        client.saml.get_saml_redirect_url(
            organization_external_id="my_custom_external_id",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if saml_connection_id is not OMIT:
            _request["samlConnectionId"] = saml_connection_id
        if organization_id is not OMIT:
            _request["organizationId"] = organization_id
        if organization_external_id is not OMIT:
            _request["organizationExternalId"] = organization_external_id
        if state is not OMIT:
            _request["state"] = state
        _response = HttpClient.request(
            self._client_wrapper.httpx_client,
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/saml/redirect"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries", 0) if request_options is not None else 0,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(GetSamlRedirectUrlResponse, _response.json())
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSamlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper: AsyncClientWrapper = client_wrapper

    async def redeem_saml_access_code(
        self, *, saml_access_code: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> RedeemSamlAccessCodeResponse:
        """
        Parameters
        ----------
        saml_access_code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedeemSamlAccessCodeResponse
            OK

        Examples
        --------
        from ssoready.client import AsyncSSOReady

        client = AsyncSSOReady(
            api_key="YOUR_API_KEY",
        )
        await client.saml.redeem_saml_access_code(
            saml_access_code="saml_access_code_...",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if saml_access_code is not OMIT:
            _request["samlAccessCode"] = saml_access_code
        _response = await AsyncHttpClient.request(
            self._client_wrapper.httpx_client,
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/saml/redeem"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries", 0) if request_options is not None else 0,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedeemSamlAccessCodeResponse, _response.json())
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_saml_redirect_url(
        self,
        *,
        saml_connection_id: typing.Optional[str] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        organization_external_id: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSamlRedirectUrlResponse:
        """
        Parameters
        ----------
        saml_connection_id : typing.Optional[str]

        organization_id : typing.Optional[str]

        organization_external_id : typing.Optional[str]

        state : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSamlRedirectUrlResponse
            OK

        Examples
        --------
        from ssoready.client import AsyncSSOReady

        client = AsyncSSOReady(
            api_key="YOUR_API_KEY",
        )
        await client.saml.get_saml_redirect_url(
            organization_external_id="my_custom_external_id",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if saml_connection_id is not OMIT:
            _request["samlConnectionId"] = saml_connection_id
        if organization_id is not OMIT:
            _request["organizationId"] = organization_id
        if organization_external_id is not OMIT:
            _request["organizationExternalId"] = organization_external_id
        if state is not OMIT:
            _request["state"] = state
        _response = await AsyncHttpClient.request(
            self._client_wrapper.httpx_client,
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/saml/redirect"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries", 0) if request_options is not None else 0, 
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(GetSamlRedirectUrlResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
