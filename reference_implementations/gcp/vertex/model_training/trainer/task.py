import tensorflow as tf
import keras
import numpy as np
import os

from model import create_model
from . import EPOCHS, ENDPOINT_NAME

BUCKET_ROOT = '/gcs/pamap2'
DATA_DIR = f'{BUCKET_ROOT}/training'


def create_datasets(data_dir):
    """ Create train and validation dataset
    """
    raise NotImplementedError

# CREATE DATASETS
train_dataset, validation_dataset = create_datasets(DATA_DIR)

# CREATE/COMPILE MODEL
model = create_model()
model.compile(optimizer=keras.optimizers.Adam(),
              loss=keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

# TRAIN MODEL
history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=EPOCHS
)

# SAVE MODEL
model.save(f'{BUCKET_ROOT}/{ENDPOINT_NAME}')
