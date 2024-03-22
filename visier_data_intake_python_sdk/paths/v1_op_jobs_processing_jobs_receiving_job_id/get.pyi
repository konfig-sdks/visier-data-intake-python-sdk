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

from visier_data_intake_python_sdk.model.status import Status as StatusSchema
from visier_data_intake_python_sdk.model.get_processing_jobs_response import GetProcessingJobsResponse as GetProcessingJobsResponseSchema

from visier_data_intake_python_sdk.type.get_processing_jobs_response import GetProcessingJobsResponse
from visier_data_intake_python_sdk.type.status import Status

from ...api_client import Dictionary
from visier_data_intake_python_sdk.pydantic.status import Status as StatusPydantic
from visier_data_intake_python_sdk.pydantic.get_processing_jobs_response import GetProcessingJobsResponse as GetProcessingJobsResponsePydantic

# Query params
TenantCodeSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
StartSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'tenantCode': typing.Union[TenantCodeSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'start': typing.Union[StartSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_tenant_code = api_client.QueryParameter(
    name="tenantCode",
    style=api_client.ParameterStyle.FORM,
    schema=TenantCodeSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_start = api_client.QueryParameter(
    name="start",
    style=api_client.ParameterStyle.FORM,
    schema=StartSchema,
    explode=True,
)
# Path params
ReceivingJobIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'receivingJobId': typing.Union[ReceivingJobIdSchema, str, ],
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


request_path_receiving_job_id = api_client.PathParameter(
    name="receivingJobId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ReceivingJobIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = GetProcessingJobsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GetProcessingJobsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GetProcessingJobsResponse


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

    def _get_processing_jobs_by_parent_receiving_job_id_mapped_args(
        self,
        receiving_job_id: str,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if tenant_code is not None:
            _query_params["tenantCode"] = tenant_code
        if limit is not None:
            _query_params["limit"] = limit
        if start is not None:
            _query_params["start"] = start
        if receiving_job_id is not None:
            _path_params["receivingJobId"] = receiving_job_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_processing_jobs_by_parent_receiving_job_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Retrieve processing job statuses by receiving job ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_receiving_job_id,
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
            request_query_tenant_code,
            request_query_limit,
            request_query_start,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/op/jobs/processing-jobs/{receivingJobId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_processing_jobs_by_parent_receiving_job_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve processing job statuses by receiving job ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_receiving_job_id,
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
            request_query_tenant_code,
            request_query_limit,
            request_query_start,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/op/jobs/processing-jobs/{receivingJobId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetProcessingJobsByParentReceivingJobIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_processing_jobs_by_parent_receiving_job_id(
        self,
        receiving_job_id: str,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_processing_jobs_by_parent_receiving_job_id_mapped_args(
            receiving_job_id=receiving_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
        )
        return await self._aget_processing_jobs_by_parent_receiving_job_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_processing_jobs_by_parent_receiving_job_id(
        self,
        receiving_job_id: str,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_processing_jobs_by_parent_receiving_job_id_mapped_args(
            receiving_job_id=receiving_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
        )
        return self._get_processing_jobs_by_parent_receiving_job_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetProcessingJobsByParentReceivingJobId(BaseApi):

    async def aget_processing_jobs_by_parent_receiving_job_id(
        self,
        receiving_job_id: str,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> GetProcessingJobsResponsePydantic:
        raw_response = await self.raw.aget_processing_jobs_by_parent_receiving_job_id(
            receiving_job_id=receiving_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
            **kwargs,
        )
        if validate:
            return GetProcessingJobsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GetProcessingJobsResponsePydantic, raw_response.body)
    
    
    def get_processing_jobs_by_parent_receiving_job_id(
        self,
        receiving_job_id: str,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        validate: bool = False,
    ) -> GetProcessingJobsResponsePydantic:
        raw_response = self.raw.get_processing_jobs_by_parent_receiving_job_id(
            receiving_job_id=receiving_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
        )
        if validate:
            return GetProcessingJobsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GetProcessingJobsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        receiving_job_id: str,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_processing_jobs_by_parent_receiving_job_id_mapped_args(
            receiving_job_id=receiving_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
        )
        return await self._aget_processing_jobs_by_parent_receiving_job_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        receiving_job_id: str,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_processing_jobs_by_parent_receiving_job_id_mapped_args(
            receiving_job_id=receiving_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
        )
        return self._get_processing_jobs_by_parent_receiving_job_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

