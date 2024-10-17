#!/bin/bash

# Define variables
LOCATION='us-east1'
JOB_NAME="pamap-sdk-job"
MACHINE_TYPE="n1-standard-4"
REPLICA_COUNT=1
CUSTOM_CONTAINER_IMAGE_URI="us-east1-docker.pkg.dev/hitachi-rail-gtsc/pamap-trainer/pamap-trainer-image:latest"

# Run the gcloud command to create a custom AI job
gcloud ai custom-jobs create \
  --region="$LOCATION" \
  --display-name="$JOB_NAME" \
  --worker-pool-spec=machine-type="$MACHINE_TYPE",replica-count="$REPLICA_COUNT",container-image-uri="$CUSTOM_CONTAINER_IMAGE_URI"

# Check the status of the command execution
if [ $? -eq 0 ]; then
    echo "Custom AI job created successfully!"
else
    echo "Failed to create custom AI job."
fi
