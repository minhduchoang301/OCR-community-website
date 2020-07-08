import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt
import keras
import numpy as np
from mlxtend.data import loadlocal_mnist

class Model():
	def __init__(self, train_img, train_label, test_img, test_label):
		self.train_img = train_img
		self.train_label = train_label
		self.test_img = test_img
		self.test_label = test_label

	def load(self)
		x_train, y_train = loadlocal_mnist(images_path= self.train_img, labels_path= self.train_label)
		x_test, y_test = loadlocal_mnist(images_path=self.test_img, labels_path= 'self.test_label')
		return x_train, y_train, x_test, y_test

	def model()
		x_train, y_train, x_test, y_test = self.load()
		model = tf.keras.models.Sequential([
	    	# This is the first convolution
	    	tf.keras.layers.Reshape((28,28,1), input_shape=(784,)),
	    	tf.keras.layers.Conv2D(32, (5, 5), activation='relu', input_shape=(28, 28, 1)),
	    	tf.keras.layers.Dropout(0.5),
	    	#tf.keras.layers.MaxPooling2D(2, 2),
	    	# The second convolution
	    	tf.keras.layers.Conv2D(32, (5, 5), activation='relu'),
	    	#tf.keras.layers.MaxPooling2D(2, 2),
	    	# # The third convolution
	    	# tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
	    	# tf.keras.layers.MaxPooling2D(2, 2),
	    	# # The fourth convolution
	    	# tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
	    	# tf.keras.layers.MaxPooling2D(2, 2),
	    	# Flatten the results to feed into a DNN
	    	tf.keras.layers.Flatten(),
	    	tf.keras.layers.Dropout(0.5),
	    	# 512 neuron hidden layer
	    	tf.keras.layers.Dense(512, activation='relu'),
	    	tf.keras.layers.Dense(256, activation='relu'),    
	    	#tf.keras.layers.Dense(128, activation='relu'),
	    	tf.keras.layers.Dense(47, activation='softmax')
	    	])
		model.compile(loss= 'sparse_categorical_crossentropy', optimizer= 'Adam' , metrics=['accuracy'])
		print(model.summary())
		history = model.fit(train_images,y_train,validation_data=(test_images, y_test), batch_size= 128, epochs= 20)
		tf.keras.models.save(model, "/content/model")
