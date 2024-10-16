import keras
from keras import layers

from . import DROPOUT, LSTM_UNITS, LOOK_BACK, LR, LOSS


def create_model():
    """ Create an LSTM-AE

    @return Sequential model
    """
    model = keras.Sequential()

    # encoder
    model.add(layers.Bidirectional(layers.LSTM(units=LSTM_UNITS)))
    model.add(layers.Dropout(rate=DROPOUT))
    model.add(layers.RepeatVector(n=LOOK_BACK))

    # decoder
    model.add(layers.Bidirectional(layers.LSTM(units=LSTM_UNITS, return_sequences=True)))
    model.add(layers.Dropout(rate=DROPOUT))
    model.add(layers.TimeDistributed(layers.Dense()))

    opt = keras.optimizers.Adam(learning_rate=LR)
    model.compile(optimizer=opt, loss=LOSS)

    return model
