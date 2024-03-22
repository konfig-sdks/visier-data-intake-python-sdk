import typing_extensions

from visier_data_intake_python_sdk.apis.tags import TagValues
from visier_data_intake_python_sdk.apis.tags.data_intake_api import DataIntakeApi
from visier_data_intake_python_sdk.apis.tags.data_upload_api import DataUploadApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DATA_INTAKE: DataIntakeApi,
        TagValues.DATA_UPLOAD: DataUploadApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DATA_INTAKE: DataIntakeApi,
        TagValues.DATA_UPLOAD: DataUploadApi,
    }
)
