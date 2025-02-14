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

from visier_data_intake_python_sdk.type.data_transfer_result_detail_source_names import DataTransferResultDetailSourceNames

class RequiredDataTransferResultDetail(TypedDict):
    pass

class OptionalDataTransferResultDetail(TypedDict, total=False):
    # The code of the tenant that data was transferred to. For example, WFF_j1r or WFF_j1r~c7o.
    tenantCode: str

    sourceNames: DataTransferResultDetailSourceNames

    # The total size of the transfer session in bytes.
    dataSize: str

    # The total number of rows transferred during the transfer session.
    rows: str

class DataTransferResultDetail(RequiredDataTransferResultDetail, OptionalDataTransferResultDetail):
    pass
