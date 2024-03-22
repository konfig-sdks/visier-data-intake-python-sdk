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

from visier_data_intake_python_sdk.pydantic.processing_job import ProcessingJob

class GetProcessingJobsResponse(BaseModel):
    # The job ID of the receiving job that spawned this job.
    parent_job_id: typing.Optional[str] = Field(None, alias='parentJobId')

    # The tenant code of the receiving job that spawned this job.
    parent_tenant_code: typing.Optional[str] = Field(None, alias='parentTenantCode')

    # The limit of processing jobs to retrieve per page.
    limit: typing.Optional[int] = Field(None, alias='limit')

    # The index to start retrieving results from, also known as offset. The index begins at 0.
    start: typing.Optional[int] = Field(None, alias='start')

    # A list of objects representing the processing jobs to retrieve.
    processing_jobs: typing.Optional[typing.List[ProcessingJob]] = Field(None, alias='processingJobs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
