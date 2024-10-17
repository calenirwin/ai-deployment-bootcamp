GOOGLE_CLOUD_PROJECT = 'hitachi-rail-gtsc'
GOOGLE_CLOUD_REGION = 'us-east1'
BUCKET_ROOT = '/gcs/pamap_dataset'
DATA_DIR = f'{BUCKET_ROOT}/flower_photos'

ENDPOINT_NAME = "pamap2_lstm_ae"

LR = 0.001
DROPOUT = 0.1
LSTM_UNITS = 90
SEQUENCE_LENGTH = 90
NUM_FEATURES = 28
LOSS = 'mse'
EPOCHS = 5
BATCH_SIZE = 16