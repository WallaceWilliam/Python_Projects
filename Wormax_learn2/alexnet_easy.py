# alexnet.py

""" AlexNet.
References:
    - Alex Krizhevsky, Ilya Sutskever & Geoffrey E. Hinton. ImageNet
    Classification with Deep Convolutional Neural Networks. NIPS, 2012.
Links:
    - [AlexNet Paper](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
"""

# 142 samples per second

import tflearn
import numpy as np
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization

def modified_alexnet(width, height, channels, lr, output=3):
    network = input_data(shape=[None, width, height, channels], name='input')
    network = conv_2d(network, 64, 16, strides=4, activation='relu')
    network = conv_2d(network, 128, 8, activation='relu')
    network = conv_2d(network, 256, 4, activation='relu')
    network = max_pool_2d(network, 8, strides=2)
    network = local_response_normalization(network)
    network = fully_connected(network, 256, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 256, activation='tanh')
    network = fully_connected(network, output, activation='sigmoid')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')
    model = tflearn.DNN(network, checkpoint_path='model_alexnet',
                        max_checkpoints=1, tensorboard_verbose=0, tensorboard_dir='log')

    return model

