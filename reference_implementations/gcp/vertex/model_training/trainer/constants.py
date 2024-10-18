GOOGLE_CLOUD_PROJECT = 'hitachi-rail-gtsc'
GOOGLE_CLOUD_REGION = 'us-east1'
BUCKET_ROOT = '/gcs/pamap_dataset'
DATA_DIR = f'{BUCKET_ROOT}/'
MODEL_NAME = "pamap_lstmae"

TRAINER_URI = "us-east1-docker.pkg.dev/hitachi-rail-gtsc/pamap-trainer/pamap-trainer-image:latest"

SERVING_IMAGE="us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-13:latest"

LR = 0.001
DROPOUT = 0.1
LSTM_UNITS = 90
SEQUENCE_LENGTH = 90
STEP_SIZE = 30
NUM_FEATURES = 28
LOSS = 'mse'
OPTIMIZER = 'adam'
EPOCHS = 5
BATCH_SIZE = 16
VAL_SPLIT = 0.1
