from data_preprocessing import PreprocessingPipeline
from model import create_model

from constants import BUCKET_ROOT, DATA_DIR, MODEL_NAME, SEQUENCE_LENGTH, STEP_SIZE, EPOCHS, BATCH_SIZE, \
    OPTIMIZER, LOSS, VAL_SPLIT

# CREATE DATASETS
subject_ID = "subject102"
activity_type = "Protocol"
data_prep = PreprocessingPipeline(DATA_DIR, subject_ID=subject_ID, activity_type=activity_type)
_, dataset = data_prep.gather_data(loop_back=SEQUENCE_LENGTH, overlap=STEP_SIZE)

# CREATE/COMPILE MODEL
model = create_model(input_shape=dataset.shape)
model.compile(optimizer=OPTIMIZER,
              loss=LOSS,
              metrics=['accuracy'])

# TRAIN MODEL
history = model.fit(
        dataset,
        dataset,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        validation_split=VAL_SPLIT)

# SAVE MODEL
model.save(f'{BUCKET_ROOT}/{MODEL_NAME}')
