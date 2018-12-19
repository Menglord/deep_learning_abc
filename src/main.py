import network2
import mnist_loader
import matplotlib.pyplot as plt
import numpy as np

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = network2.Network([784,30,10],cost=network2.CrossEntropyCost)
    
net.large_weight_initializer()

epoches = 400

evaluation_cost, \
evaluation_accuracy, \
training_cost, \
training_accuracy = net.SGD(training_data[:1000], epoches, 10, 0.5, lmbda=0.3,\
                         evaluation_data=test_data, \
                         monitor_evaluation_cost=True,\
                         monitor_evaluation_accuracy=True,\
                         monitor_training_cost=True,\
                         monitor_training_accuracy=True)


