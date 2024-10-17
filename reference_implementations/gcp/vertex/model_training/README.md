# Creating Model Training Pipeline

## Creating and Pushing Docker Repository to Artifact Registry
PROJECT_ID='hitachi-rail-gtsc'
REPO_NAME='pamap-trainer'

gcloud artifacts repositories create $REPO_NAME --repository-format=docker \
--location=us-east1 --description="Docker repository"

IMAGE_URI=us-east1-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/pamap_image:latest

gcloud auth configure-docker \
    us-east1-docker.pkg.dev

gcloud builds submit "~/Git/ai-deployment-bootcamp/reference_implementations/gcp/vertex/model_training/" --region=us-east1 --tag us-east1-docker.pkg.dev/hitachi-rail-gtsc/pamap-trainer/pamap-trainer-image:latest