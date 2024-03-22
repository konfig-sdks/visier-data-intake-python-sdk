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


class RequiredProcessingJob(TypedDict):
    pass

class OptionalProcessingJob(TypedDict, total=False):
    # The job ID of the processing job for the analytic tenant.
    jobId: str

    # The analytic tenant code.
    tenantCode: str

    # The data version associated with the processing job.
    dataVersion: str

    # The status of the receiving job for the analytic tenant.
    status: str

    # A meaningful message about the processing job.
    message: str

class ProcessingJob(RequiredProcessingJob, OptionalProcessingJob):
    pass
