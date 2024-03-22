# coding: utf-8

"""
    Visier Data Intake APIs

    Visier APIs for sending raw or untransformed source data to Visier

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import visier_data_intake_python_sdk
from visier_data_intake_python_sdk.paths.v1alpha_data_upload_files_filename import put
from visier_data_intake_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1alphaDataUploadFilesFilename(ApiTestMixin, unittest.TestCase):
    """
    V1alphaDataUploadFilesFilename unit test stubs
        Upload a data file to Visier
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 307
    response_body = ''


if __name__ == '__main__':
    unittest.main()
