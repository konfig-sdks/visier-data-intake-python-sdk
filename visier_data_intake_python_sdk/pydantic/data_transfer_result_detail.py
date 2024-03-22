# coding: utf-8

"""
    Visier Data Intake APIs

    Visier APIs for sending raw or untransformed source data to Visier

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from visier_data_intake_python_sdk.pydantic.data_transfer_result_detail_source_names import DataTransferResultDetailSourceNames

class DataTransferResultDetail(BaseModel):
    # The code of the tenant that data was transferred to. For example, WFF_j1r or WFF_j1r~c7o.
    tenant_code: typing.Optional[str] = Field(None, alias='tenantCode')

    source_names: typing.Optional[DataTransferResultDetailSourceNames] = Field(None, alias='sourceNames')

    # The total size of the transfer session in bytes.
    data_size: typing.Optional[str] = Field(None, alias='dataSize')

    # The total number of rows transferred during the transfer session.
    rows: typing.Optional[str] = Field(None, alias='rows')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
