# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from visier_data_intake_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_OP_DATASOURCES = "/v1/op/data-sources"
    V1_OP_DATATRANSFERSESSIONS = "/v1/op/data-transfer-sessions"
    V1_OP_DATATRANSFERSESSIONS_TRANSFER_SESSION_ID_ADD = "/v1/op/data-transfer-sessions/{transferSessionId}/add"
    V1_OP_DATATRANSFERSESSIONS_TRANSFER_SESSION_ID_CANCEL = "/v1/op/data-transfer-sessions/{transferSessionId}/cancel"
    V1_OP_DATATRANSFERSESSIONS_TRANSFER_SESSION_ID_UPLOAD = "/v1/op/data-transfer-sessions/{transferSessionId}/upload"
    V1_OP_JOBS_PROCESSINGJOBS_RECEIVING_JOB_ID = "/v1/op/jobs/processing-jobs/{receivingJobId}"
    V1_OP_JOBS_RECEIVINGJOBS = "/v1/op/jobs/receiving-jobs"
    V1_OP_JOBS_RECEIVINGJOBS_RECEIVING_JOB_ID = "/v1/op/jobs/receiving-jobs/{receivingJobId}"
    V1ALPHA_DATA_UPLOAD_FILES_FILENAME = "/v1alpha/data/upload/files/{filename}"
