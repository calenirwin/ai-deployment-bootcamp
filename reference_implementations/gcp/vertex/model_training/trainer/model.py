import keras
from keras.layers import LSTM, RepeatVector, TimeDistributed, Dense, Dropout, Bidirectional

from constants import DROPOUT, LSTM_UNITS, LOSS, OPTIMIZER


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

    model.compile(optimizer=OPTIMIZER,
                  loss=LOSS)

    return model
