import keras
from keras.layers import LSTM, RepeatVector, TimeDistributed, Dense, Dropout, Bidirectional

from constants import DROPOUT, LSTM_UNITS, NUM_FEATURES, SEQUENCE_LENGTH, LR, LOSS, EPOCHS, BATCH_SIZE
from data_preprocessing import PreprocessingPipeline


def create_model(input_shape):
    """ Create an LSTM-AE

    @return Sequential model
    """
    model = keras.Sequential()

    # encoder
    model.add(Bidirectional(LSTM(units=LSTM_UNITS,
                                 activation="relu",
                                 input_shape=(input_shape[1], input_shape[2]))))
    model.add(Dropout(rate=DROPOUT))
    model.add(RepeatVector(n=input_shape[1]))

    # decoder
    model.add(Bidirectional(LSTM(units=LSTM_UNITS,
                                 activation="relu",
                                 return_sequences=True)))
    model.add(Dropout(rate=DROPOUT))
    model.add(TimeDistributed(Dense(units=input_shape[2])))

    opt = keras.optimizers.Adam(learning_rate=LR)
    model.compile(optimizer=opt, loss=LOSS)

    return model


if __name__ == "__main__":
    folder_data = "data/"
    subject_ID = "subject102"
    activity_type = "Protocol"
    data_prep = PreprocessingPipeline(folder_data, subject_ID=subject_ID, activity_type=activity_type)
    data_dict, dataset = data_prep.gather_data(loop_back=90, overlap=30)

    model = create_model(input_shape=dataset.shape)
    model.compile(optimizer="adam",
                  loss="mse",
                  metrics=['accuracy'])

    history = model.fit(
        dataset,
        dataset,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        validation_split=0.1)

    model.summary()
