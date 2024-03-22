<div align="center">

[![Visit Visier](./header.png)](https://visier.com)

# Visier<a id="visier"></a>

Visier APIs for sending raw or untransformed source data to Visier


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`visierdataintake.data_intake.get_processing_jobs_by_parent_receiving_job_id`](#visierdataintakedata_intakeget_processing_jobs_by_parent_receiving_job_id)
  * [`visierdataintake.data_intake.get_sources`](#visierdataintakedata_intakeget_sources)
  * [`visierdataintake.data_intake.push_data`](#visierdataintakedata_intakepush_data)
  * [`visierdataintake.data_intake.push_data_cancel`](#visierdataintakedata_intakepush_data_cancel)
  * [`visierdataintake.data_intake.push_data_complete`](#visierdataintakedata_intakepush_data_complete)
  * [`visierdataintake.data_intake.receiving_job_status`](#visierdataintakedata_intakereceiving_job_status)
  * [`visierdataintake.data_intake.start_transfer`](#visierdataintakedata_intakestart_transfer)
  * [`visierdataintake.data_intake.upload_data`](#visierdataintakedata_intakeupload_data)
  * [`visierdataintake.data_upload.file_to_visier`](#visierdataintakedata_uploadfile_to_visier)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Visier&serviceName=DataIntake&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from visier_data_intake_python_sdk import VisierDataIntake, ApiException

visierdataintake = VisierDataIntake(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Retrieve processing job statuses by receiving job ID
    get_processing_jobs_by_parent_receiving_job_id_response = visierdataintake.data_intake.get_processing_jobs_by_parent_receiving_job_id(
        receiving_job_id="receivingJobId_example",
        tenant_code="string_example",
        limit=1,
        start=1,
    )
    print(get_processing_jobs_by_parent_receiving_job_id_response)
except ApiException as e:
    print("Exception when calling DataIntakeApi.get_processing_jobs_by_parent_receiving_job_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from visier_data_intake_python_sdk import VisierDataIntake, ApiException

visierdataintake = VisierDataIntake(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Retrieve processing job statuses by receiving job ID
        get_processing_jobs_by_parent_receiving_job_id_response = await visierdataintake.data_intake.aget_processing_jobs_by_parent_receiving_job_id(
            receiving_job_id="receivingJobId_example",
            tenant_code="string_example",
            limit=1,
            start=1,
        )
        print(get_processing_jobs_by_parent_receiving_job_id_response)
    except ApiException as e:
        print("Exception when calling DataIntakeApi.get_processing_jobs_by_parent_receiving_job_id: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from visier_data_intake_python_sdk import VisierDataIntake, ApiException

visierdataintake = VisierDataIntake(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Retrieve processing job statuses by receiving job ID
    get_processing_jobs_by_parent_receiving_job_id_response = visierdataintake.data_intake.raw.get_processing_jobs_by_parent_receiving_job_id(
        receiving_job_id="receivingJobId_example",
        tenant_code="string_example",
        limit=1,
        start=1,
    )
    pprint(get_processing_jobs_by_parent_receiving_job_id_response.body)
    pprint(get_processing_jobs_by_parent_receiving_job_id_response.body["parent_job_id"])
    pprint(get_processing_jobs_by_parent_receiving_job_id_response.body["parent_tenant_code"])
    pprint(get_processing_jobs_by_parent_receiving_job_id_response.body["limit"])
    pprint(get_processing_jobs_by_parent_receiving_job_id_response.body["start"])
    pprint(get_processing_jobs_by_parent_receiving_job_id_response.body["processing_jobs"])
    pprint(get_processing_jobs_by_parent_receiving_job_id_response.headers)
    pprint(get_processing_jobs_by_parent_receiving_job_id_response.status)
    pprint(get_processing_jobs_by_parent_receiving_job_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DataIntakeApi.get_processing_jobs_by_parent_receiving_job_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `visierdataintake.data_intake.get_processing_jobs_by_parent_receiving_job_id`<a id="visierdataintakedata_intakeget_processing_jobs_by_parent_receiving_job_id"></a>

Use this API to retrieve a list of statuses for all processing jobs associated with the given receiving job ID.

 Processing jobs deal with an individual analytic tenant's data load. A processing job is either triggered through
 the UI or is one of many processing jobs spawned from a receiving job. When a processing job is triggered as part
 of a set from an receiving job, it is associated to the receiving job through a Parent ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_processing_jobs_by_parent_receiving_job_id_response = visierdataintake.data_intake.get_processing_jobs_by_parent_receiving_job_id(
    receiving_job_id="receivingJobId_example",
    tenant_code="string_example",
    limit=1,
    start=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### receiving_job_id: `str`<a id="receiving_job_id-str"></a>

The receiving job ID.

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of the tenant you want to retrieve the processing jobs for. Use this if you are only interested in the results for one analytic tenant.

##### limit: `int`<a id="limit-int"></a>

The limit of processing jobs to retrieve per page.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

#### 🔄 Return<a id="🔄-return"></a>

[`GetProcessingJobsResponse`](./visier_data_intake_python_sdk/pydantic/get_processing_jobs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/jobs/processing-jobs/{receivingJobId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdataintake.data_intake.get_sources`<a id="visierdataintakedata_intakeget_sources"></a>

Prior to transferring data to Visier, you must identify the sources you want to target. Sources store data for
 the solution and are used to map data to Visier's data model.

 Note: To set up sources in your tenant, contact Visier Customer Success.
 This API allows you to query the list of available sources, and identify the source schema and required fields.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sources_response = visierdataintake.data_intake.get_sources()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PushDataSourceDefinitionsDTO`](./visier_data_intake_python_sdk/pydantic/push_data_source_definitions_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-sources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdataintake.data_intake.push_data`<a id="visierdataintakedata_intakepush_data"></a>

This API allows you to transfer data to Visier in batches of records. Each request includes a batch of records
 formatted as a comma separated array with the first row containing the column headers in the request body. Each
 subsequent request should also include the first row as a header.

 Each request transfers a batch of records to a single source. Transfer sessions may include one or more batches before completion.

 Each batch is identified by a sequence number. Sequence numbers help identify any batches  that were delivered incorrectly.

 Each batch is limited to the following request size:
 - Batch size limit: 10 MB
 - Record count limit: 300,000 rows

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
push_data_response = visierdataintake.data_intake.push_data(
    body="body_example",
    transfer_session_id="transferSessionId_example",
    source_id="string_example",
    sequence=1,
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transfer_session_id: `str`<a id="transfer_session_id-str"></a>

The transfer session ID returned after the data transfer session starts.

##### source_id: `str`<a id="source_id-str"></a>

The unique identifier associated with the source you want to transfer data to.

##### sequence: `int`<a id="sequence-int"></a>

The unique sequence number associated with a batch of records.

##### tenant_code: `str`<a id="tenant_code-str"></a>

The code of the tenant you want to transfer data to. For example, WFF_j1r or WFF_j1r~c7o.

##### requestBody: `str`<a id="requestbody-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PushDataResponse`](./visier_data_intake_python_sdk/pydantic/push_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-transfer-sessions/{transferSessionId}/add` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdataintake.data_intake.push_data_cancel`<a id="visierdataintakedata_intakepush_data_cancel"></a>

This API allows you to cancel a transfer session after starting it. If a transfer session is cancelled, all
 records within the transfer session do not persist in Visier’s data store.

 If you cancel a transfer session, please start a new transfer session and resend the complete data set.

 You might cancel a transfer session if:
 - A request to send a batch of records failed.
 - The original set of records is incomplete.
 - An infrastructure error occurs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
push_data_cancel_response = visierdataintake.data_intake.push_data_cancel(
    transfer_session_id="transferSessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transfer_session_id: `str`<a id="transfer_session_id-str"></a>

The transfer session ID to cancel.

#### 🔄 Return<a id="🔄-return"></a>

[`PushDataCancelResponse`](./visier_data_intake_python_sdk/pydantic/push_data_cancel_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-transfer-sessions/{transferSessionId}/cancel` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdataintake.data_intake.push_data_complete`<a id="visierdataintakedata_intakepush_data_complete"></a>

This API allows you to complete the specified transfer session by triggering a receiving job. A receiving job
 validates the transferred data and adds the transferred data to Visier’s data store.

 You can set an optional parameter to generate a data version through a processing job immediately after the receiving job completes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
push_data_complete_response = visierdataintake.data_intake.push_data_complete(
    transfer_session_id="string_example",
    processing_data=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transfer_session_id: `str`<a id="transfer_session_id-str"></a>

The unique identifier associated with the transfer session.

##### processing_data: `bool`<a id="processing_data-bool"></a>

If true, a processing job will be triggered after the receiving job successfully completes. This generates a new data version.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PushDataCompleteRequest`](./visier_data_intake_python_sdk/type/push_data_complete_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PushDataCompleteResponse`](./visier_data_intake_python_sdk/pydantic/push_data_complete_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/jobs/receiving-jobs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdataintake.data_intake.receiving_job_status`<a id="visierdataintakedata_intakereceiving_job_status"></a>

After completing a transfer session, you may want to know the status of the receiving job and the associated tenant
 receiving jobs. A receiving job validates the transferred data and adds the transferred data to Visier’s data store.

 Use this API to retrieve the receiving job status and summary of analytic tenant receiving jobs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
receiving_job_status_response = visierdataintake.data_intake.receiving_job_status(
    receiving_job_id="receivingJobId_example",
    jobs=True,
    tenant_code="string_example",
    start=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### receiving_job_id: `str`<a id="receiving_job_id-str"></a>

The **dataReceivingJobId** provided after a data transfer session completes. See **`/v1/op/jobs/receiving-jobs`**.

##### jobs: `bool`<a id="jobs-bool"></a>

If true, returns the status of receiving jobs spawned by the receiving job specified by receivingJobId.

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of the tenant you want to retrieve the receiving jobs for. Use this if you are only interested in the results for one analytic tenant.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

##### limit: `int`<a id="limit-int"></a>

The number of job statuses to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`ReceivingJobStatusResponse`](./visier_data_intake_python_sdk/pydantic/receiving_job_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/jobs/receiving-jobs/{receivingJobId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdataintake.data_intake.start_transfer`<a id="visierdataintakedata_intakestart_transfer"></a>

Use this API to start a new transfer session. A transfer session can include one or more batches of records to be
 sent to Visier. Batches of records may be transferred as JSON or file payloads.

 Recommended: For optimal performance, please include all batches of records in a single transfer session.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
start_transfer_response = visierdataintake.data_intake.start_transfer()
```

#### 🔄 Return<a id="🔄-return"></a>

[`StartTransferResponse`](./visier_data_intake_python_sdk/pydantic/start_transfer_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-transfer-sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdataintake.data_intake.upload_data`<a id="visierdataintakedata_intakeupload_data"></a>

This API allows you to upload data to Visier as CSV or ZIP files. Each request transfers a single file. If the
 data intended for Visier is stored in multiple files, you may compress them into a single ZIP file or make
 multiple requests within the same transfer session.

 File size limit: 3 GB

 Each file is identified by a sequence number. Sequence numbers help identify any batches that were delivered incorrectly.

 If you define a specific source in the request, all files within the request will target the declared source. If
 a source is not defined, the filenames are matched against the source regex to correctly assign each file to a
 source. To find out the source regex, please contact Visier Customer Success.

 Note: If you include files that should target multiple sources in one ZIP file, do not define a source in the request.

 Analytic tenants: For optimal transfer speed, provide one ZIP file per source.
 Administrating tenants: For optimal transfer speed, provide one ZIP file containing all the required data files for your analytic tenants.
 In the ZIP file, use one folder per analytic tenant. The ZIP file must adhere to the following file structure:

 File1.zip
 - Folder1: WFF_tenantCode1
    - Filename1.csv
    - Filename2.csv
 - Folder2: WFF_tenantCode2
    - Filename3.csv
    - Filename4.csv

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_data_response = visierdataintake.data_intake.upload_data(
    body=None,
    transfer_session_id="transferSessionId_example",
    source_id="string_example",
    sequence="string_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transfer_session_id: `str`<a id="transfer_session_id-str"></a>

The transfer session ID returned after the data transfer session starts.

##### source_id: `str`<a id="source_id-str"></a>

The unique identifier associated with the source you want to transfer data to.

##### sequence: `str`<a id="sequence-str"></a>

The unique sequence number associated with a batch of records.

##### tenant_code: `str`<a id="tenant_code-str"></a>

The code of the tenant you want to transfer data to. For example, WFF_j1r or WFF_j1r~c7o.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🔄 Return<a id="🔄-return"></a>

[`PushDataResponse`](./visier_data_intake_python_sdk/pydantic/push_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-transfer-sessions/{transferSessionId}/upload` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdataintake.data_upload.file_to_visier`<a id="visierdataintakedata_uploadfile_to_visier"></a>

Use this API to upload data files to Visier. You can upload ZIP, CSV, XLS, and XLSX filetypes in plaintext or encrypted with Visier's PGP key. The maximum file upload size is 5 GB.

 Use of this API requires client redirect. This API redirects requests directly to Visier's upload infrastructure to support long-running uploads. 
 To ensure efficient uploading, we recommend that you use an HTTP client that supports the 100 Continue status code.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
file_to_visier_response = visierdataintake.data_upload.file_to_visier(
    body=open('/path/to/file', 'rb'),
    filename="filename_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filename: `str`<a id="filename-str"></a>

The filename of the data file to upload, including the file extension (such as .zip or .csv).

##### requestBody: `IO`<a id="requestbody-io"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Status`](./visier_data_intake_python_sdk/pydantic/status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/data/upload/files/{filename}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
