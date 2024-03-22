import typing_extensions

from visier_data_intake_python_sdk.paths import PathValues
from visier_data_intake_python_sdk.apis.paths.v1_op_data_sources import V1OpDataSources
from visier_data_intake_python_sdk.apis.paths.v1_op_data_transfer_sessions import V1OpDataTransferSessions
from visier_data_intake_python_sdk.apis.paths.v1_op_data_transfer_sessions_transfer_session_id_add import V1OpDataTransferSessionsTransferSessionIdAdd
from visier_data_intake_python_sdk.apis.paths.v1_op_data_transfer_sessions_transfer_session_id_cancel import V1OpDataTransferSessionsTransferSessionIdCancel
from visier_data_intake_python_sdk.apis.paths.v1_op_data_transfer_sessions_transfer_session_id_upload import V1OpDataTransferSessionsTransferSessionIdUpload
from visier_data_intake_python_sdk.apis.paths.v1_op_jobs_processing_jobs_receiving_job_id import V1OpJobsProcessingJobsReceivingJobId
from visier_data_intake_python_sdk.apis.paths.v1_op_jobs_receiving_jobs import V1OpJobsReceivingJobs
from visier_data_intake_python_sdk.apis.paths.v1_op_jobs_receiving_jobs_receiving_job_id import V1OpJobsReceivingJobsReceivingJobId
from visier_data_intake_python_sdk.apis.paths.v1alpha_data_upload_files_filename import V1alphaDataUploadFilesFilename

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_OP_DATASOURCES: V1OpDataSources,
        PathValues.V1_OP_DATATRANSFERSESSIONS: V1OpDataTransferSessions,
        PathValues.V1_OP_DATATRANSFERSESSIONS_TRANSFER_SESSION_ID_ADD: V1OpDataTransferSessionsTransferSessionIdAdd,
        PathValues.V1_OP_DATATRANSFERSESSIONS_TRANSFER_SESSION_ID_CANCEL: V1OpDataTransferSessionsTransferSessionIdCancel,
        PathValues.V1_OP_DATATRANSFERSESSIONS_TRANSFER_SESSION_ID_UPLOAD: V1OpDataTransferSessionsTransferSessionIdUpload,
        PathValues.V1_OP_JOBS_PROCESSINGJOBS_RECEIVING_JOB_ID: V1OpJobsProcessingJobsReceivingJobId,
        PathValues.V1_OP_JOBS_RECEIVINGJOBS: V1OpJobsReceivingJobs,
        PathValues.V1_OP_JOBS_RECEIVINGJOBS_RECEIVING_JOB_ID: V1OpJobsReceivingJobsReceivingJobId,
        PathValues.V1ALPHA_DATA_UPLOAD_FILES_FILENAME: V1alphaDataUploadFilesFilename,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_OP_DATASOURCES: V1OpDataSources,
        PathValues.V1_OP_DATATRANSFERSESSIONS: V1OpDataTransferSessions,
        PathValues.V1_OP_DATATRANSFERSESSIONS_TRANSFER_SESSION_ID_ADD: V1OpDataTransferSessionsTransferSessionIdAdd,
        PathValues.V1_OP_DATATRANSFERSESSIONS_TRANSFER_SESSION_ID_CANCEL: V1OpDataTransferSessionsTransferSessionIdCancel,
        PathValues.V1_OP_DATATRANSFERSESSIONS_TRANSFER_SESSION_ID_UPLOAD: V1OpDataTransferSessionsTransferSessionIdUpload,
        PathValues.V1_OP_JOBS_PROCESSINGJOBS_RECEIVING_JOB_ID: V1OpJobsProcessingJobsReceivingJobId,
        PathValues.V1_OP_JOBS_RECEIVINGJOBS: V1OpJobsReceivingJobs,
        PathValues.V1_OP_JOBS_RECEIVINGJOBS_RECEIVING_JOB_ID: V1OpJobsReceivingJobsReceivingJobId,
        PathValues.V1ALPHA_DATA_UPLOAD_FILES_FILENAME: V1alphaDataUploadFilesFilename,
    }
)
