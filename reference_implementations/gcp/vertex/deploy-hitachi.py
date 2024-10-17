from google.cloud import aiplatform, bigquery
from model_training.trainer.constants import BUCKET_ROOT, MODEL_NAME, GOOGLE_CLOUD_PROJECT, GOOGLE_CLOUD_REGION, SERVING_IMAGE

aiplatform.init(project=GOOGLE_CLOUD_PROJECT, location=GOOGLE_CLOUD_REGION)

project_prefix = GOOGLE_CLOUD_PROJECT.replace("-", "_")
endpoint_display_name = f"{project_prefix}_endpoint"
bq_logging_dataset = f"{endpoint_display_name}_monitoring"
bq_logging_table = f"bq://{GOOGLE_CLOUD_PROJECT}.{bq_logging_dataset}.req_resp"

gcs_path = BUCKET_ROOT.replace("/gcs/", "gs://")
model = aiplatform.Model.upload(
    display_name=MODEL_NAME,
    artifact_uri=f"{gcs_path}/{MODEL_NAME}",
    serving_container_image_uri=SERVING_IMAGE,
)

bq_client = bigquery.Client()
dataset_ids = [dataset.dataset_id for dataset in list(bq_client.list_datasets())]
if bq_logging_dataset not in dataset_ids:
    bq_dataset = bigquery.Dataset(f"{GOOGLE_CLOUD_PROJECT}.{bq_logging_dataset}")
    bq_dataset.location = "US"
    bq_dataset = bq_client.create_dataset(bq_dataset, timeout=30)

endpoint = aiplatform.Endpoint.create(
    display_name=endpoint_display_name,
    enable_request_response_logging=True,
    request_response_logging_sampling_rate=1.0,
    request_response_logging_bq_destination_table=bq_logging_table,
)

deployed_endpoint = model.deploy(
    endpoint=endpoint,
    machine_type="n1-standard-4",
    # auto-scaling
    max_replica_count=1,
)

print("Endpoint ID:", endpoint.name)
