import tensorflow as tensorflow
from tensorflow import keras
from tensorflow.keras.layers import Dense, Embedding, Bidirectional, LSTM

num_words = 10000 # nombre de mots à utiliser
maxlen = 100 # longueur maximale de chaque avis
