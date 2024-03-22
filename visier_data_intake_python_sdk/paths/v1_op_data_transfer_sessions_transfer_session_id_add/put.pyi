# coding: utf-8

"""
    Visier Data Intake APIs

    Visier APIs for sending raw or untransformed source data to Visier

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from visier_data_intake_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from visier_data_intake_python_sdk.api_response import AsyncGeneratorResponse
from visier_data_intake_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_data_intake_python_sdk import schemas  # noqa: F401

from visier_data_intake_python_sdk.model.push_data_response import PushDataResponse as PushDataResponseSchema
from visier_data_intake_python_sdk.model.status import Status as StatusSchema

from visier_data_intake_python_sdk.type.push_data_response import PushDataResponse
from visier_data_intake_python_sdk.type.status import Status

from ...api_client import Dictionary
from visier_data_intake_python_sdk.pydantic.push_data_response import PushDataResponse as PushDataResponsePydantic
from visier_data_intake_python_sdk.pydantic.status import Status as StatusPydantic

# Query params
SourceIdSchema = schemas.StrSchema
SequenceSchema = schemas.IntSchema
TenantCodeSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'sourceId': typing.Union[SourceIdSchema, str, ],
        'sequence': typing.Union[SequenceSchema, decimal.Decimal, int, ],
        'tenantCode': typing.Union[TenantCodeSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_source_id = api_client.QueryParameter(
    name="sourceId",
    style=api_client.ParameterStyle.FORM,
    schema=SourceIdSchema,
    explode=True,
)
request_query_sequence = api_client.QueryParameter(
    name="sequence",
    style=api_client.ParameterStyle.FORM,
    schema=SequenceSchema,
    explode=True,
)
request_query_tenant_code = api_client.QueryParameter(
    name="tenantCode",
    style=api_client.ParameterStyle.FORM,
    schema=TenantCodeSchema,
    explode=True,
)
# Path params
TransferSessionIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'transferSessionId': typing.Union[TransferSessionIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_transfer_session_id = api_client.PathParameter(
    name="transferSessionId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TransferSessionIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = schemas.StrSchema


request_body_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = PushDataResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PushDataResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PushDataResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = StatusSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Status


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Status


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _push_data_mapped_args(
        self,
        body: str,
        transfer_session_id: str,
        source_id: typing.Optional[str] = None,
        sequence: typing.Optional[int] = None,
        tenant_code: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        args.body = body if body is not None else _body
        if source_id is not None:
            _query_params["sourceId"] = source_id
        if sequence is not None:
            _query_params["sequence"] = sequence
        if tenant_code is not None:
            _query_params["tenantCode"] = tenant_code
        if transfer_session_id is not None:
            _path_params["transferSessionId"] = transfer_session_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _apush_data_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Transfer data to sources via JSON
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_transfer_session_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_source_id,
            request_query_sequence,
            request_query_tenant_code,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/op/data-transfer-sessions/{transferSessionId}/add',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_body.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _push_data_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Transfer data to sources via JSON
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_transfer_session_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_source_id,
            request_query_sequence,
            request_query_tenant_code,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/op/data-transfer-sessions/{transferSessionId}/add',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_body.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class PushDataRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def apush_data(
        self,
        body: str,
        transfer_session_id: str,
        source_id: typing.Optional[str] = None,
        sequence: typing.Optional[int] = None,
        tenant_code: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._push_data_mapped_args(
            body=body,
            transfer_session_id=transfer_session_id,
            source_id=source_id,
            sequence=sequence,
            tenant_code=tenant_code,
        )
        return await self._apush_data_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def push_data(
        self,
        body: str,
        transfer_session_id: str,
        source_id: typing.Optional[str] = None,
        sequence: typing.Optional[int] = None,
        tenant_code: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._push_data_mapped_args(
            body=body,
            transfer_session_id=transfer_session_id,
            source_id=source_id,
            sequence=sequence,
            tenant_code=tenant_code,
        )
        return self._push_data_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class PushData(BaseApi):

    async def apush_data(
        self,
        body: str,
        transfer_session_id: str,
        source_id: typing.Optional[str] = None,
        sequence: typing.Optional[int] = None,
        tenant_code: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PushDataResponsePydantic:
        raw_response = await self.raw.apush_data(
            body=body,
            transfer_session_id=transfer_session_id,
            source_id=source_id,
            sequence=sequence,
            tenant_code=tenant_code,
            **kwargs,
        )
        if validate:
            return PushDataResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PushDataResponsePydantic, raw_response.body)
    
    
    def push_data(
        self,
        body: str,
        transfer_session_id: str,
        source_id: typing.Optional[str] = None,
        sequence: typing.Optional[int] = None,
        tenant_code: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PushDataResponsePydantic:
        raw_response = self.raw.push_data(
            body=body,
            transfer_session_id=transfer_session_id,
            source_id=source_id,
            sequence=sequence,
            tenant_code=tenant_code,
        )
        if validate:
            return PushDataResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PushDataResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        body: str,
        transfer_session_id: str,
        source_id: typing.Optional[str] = None,
        sequence: typing.Optional[int] = None,
        tenant_code: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._push_data_mapped_args(
            body=body,
            transfer_session_id=transfer_session_id,
            source_id=source_id,
            sequence=sequence,
            tenant_code=tenant_code,
        )
        return await self._apush_data_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        body: str,
        transfer_session_id: str,
        source_id: typing.Optional[str] = None,
        sequence: typing.Optional[int] = None,
        tenant_code: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._push_data_mapped_args(
            body=body,
            transfer_session_id=transfer_session_id,
            source_id=source_id,
            sequence=sequence,
            tenant_code=tenant_code,
        )
        return self._push_data_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

