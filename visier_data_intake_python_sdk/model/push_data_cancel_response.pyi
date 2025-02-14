# coding: utf-8

"""
    Visier Data Intake APIs

    Visier APIs for sending raw or untransformed source data to Visier

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

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


class PushDataCancelResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            message = schemas.StrSchema
            transferSessionId = schemas.StrSchema
            
            
            class dataTransferResultDetails(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DataTransferResultDetail']:
                        return DataTransferResultDetail
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DataTransferResultDetail'], typing.List['DataTransferResultDetail']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dataTransferResultDetails':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DataTransferResultDetail':
                    return super().__getitem__(i)
            status = schemas.StrSchema
            __annotations__ = {
                "message": message,
                "transferSessionId": transferSessionId,
                "dataTransferResultDetails": dataTransferResultDetails,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transferSessionId"]) -> MetaOapg.properties.transferSessionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataTransferResultDetails"]) -> MetaOapg.properties.dataTransferResultDetails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "transferSessionId", "dataTransferResultDetails", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transferSessionId"]) -> typing.Union[MetaOapg.properties.transferSessionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataTransferResultDetails"]) -> typing.Union[MetaOapg.properties.dataTransferResultDetails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "transferSessionId", "dataTransferResultDetails", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        transferSessionId: typing.Union[MetaOapg.properties.transferSessionId, str, schemas.Unset] = schemas.unset,
        dataTransferResultDetails: typing.Union[MetaOapg.properties.dataTransferResultDetails, list, tuple, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PushDataCancelResponse':
        return super().__new__(
            cls,
            *args,
            message=message,
            transferSessionId=transferSessionId,
            dataTransferResultDetails=dataTransferResultDetails,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from visier_data_intake_python_sdk.model.data_transfer_result_detail import DataTransferResultDetail
