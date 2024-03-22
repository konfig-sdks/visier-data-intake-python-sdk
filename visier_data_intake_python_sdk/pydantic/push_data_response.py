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

from visier_data_intake_python_sdk.pydantic.tenant import Tenant

class PushDataResponse(BaseModel):
    # The unique identifier associated with the transfer session.
    transfer_session_id: typing.Optional[str] = Field(None, alias='transferSessionId')

    # The unique sequence number associated with a batch of records.
    sequence: typing.Optional[int] = Field(None, alias='sequence')

    # The status of the data transfer.
    status: typing.Optional[str] = Field(None, alias='status')

    # Any additional information about the data transfer.
    message: typing.Optional[str] = Field(None, alias='message')

    # A list of strings representing the tenants that data was pushed to and their data transfer results.
    tenants: typing.Optional[typing.List[Tenant]] = Field(None, alias='tenants')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
