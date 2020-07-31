import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import numpy as np
import matplotlib.pyplot as plt

train_dir = os.path.join(os.path.curdir, "data/train")
validation_dir = os.path.join(os.path.curdir, "data/validate")

train_cima_dir  = os.path.join(train_dir, "cima")
train_baixo_dir = os.path.join(train_dir, "baixo")
train_esq_dir   = os.path.join(train_dir, "esq")
train_dir_dir   = os.path.join(train_dir, "dir")
validation_cima_dir  = os.path.join(validation_dir, "cima")
validation_baixo_dir = os.path.join(validation_dir, "baixo")
validation_esq_dir   = os.path.join(validation_dir, "esq")
validation_dir_dir   = os.path.join(validation_dir, "dir")

num_cima_tr  = len(os.listdir(train_cima_dir))
num_baixo_tr = len(os.listdir(train_baixo_dir))
num_esq_tr   = len(os.listdir(train_esq_dir))
num_dir_tr   = len(os.listdir(train_dir_dir))
num_cima_val  = len(os.listdir(validation_cima_dir))
num_baixo_val = len(os.listdir(validation_baixo_dir))
num_esq_val   = len(os.listdir(validation_esq_dir))
num_dir_val   = len(os.listdir(validation_dir_dir))

total_train = num_cima_tr + num_baixo_tr + num_esq_tr + num_dir_tr
total_val   = num_cima_val + num_baixo_val + num_esq_val + num_dir_val

print("TREINO")
print("Total de imagens cima:  ", num_cima_tr)
print("Total de imagens baixo: ", num_baixo_tr)
print("Total de imagens esq:   ", num_esq_tr)
print("Total de imagens dir:   ", num_dir_tr)
print("VALIDAÇÃO")
print("Total de imagens cima:  ", num_cima_val)
print("Total de imagens baixo: ", num_baixo_val)
print("Total de imagens esq:   ", num_esq_val)
print("Total de imagens dir:   ", num_dir_val)
print("----")
print("Total de amostras do treinamento: ", total_train)
print("Total de amostras da validação:   ", total_val)

# definindo parametros de pre-processamento
batch_size = 5
epochs     = 10
IMG_HEIGHT = 60
IMG_WIDTH  = 60

# utilizando ImageDataGenerator para
# - Ler imagens do disco.
# - Decodificar o conteúdo da imagem e converter num formato de GRID com seus valores RGB.
# - Convertê-los em floating point tensors.
# - Reescalonar os tensores de valores entre 0-255 a 0-1

# define o gerador de imagem para treinamento
train_image_generator = ImageDataGenerator(rescale=1./255)
validation_image_generator = ImageDataGenerator(rescale=1./255)
#
## gera os dados necessários para o treinamento
train_data_gen = train_image_generator.flow_from_directory(batch_size=batch_size,
                                                           directory=train_dir,
                                                           shuffle=True,
                                                           class_mode='categorical')

validation_data_gen = train_image_generator.flow_from_directory(batch_size=batch_size,
                                                           directory=validation_dir,
                                                           shuffle=True,
                                                           class_mode='categorical')

#print(train_data_gen.labels)
#print(validation_data_gen.labels)

# criando o modelo
num_classes = 4

#model = Sequential()
#model.add(Dense(400, input_dim=IMG_HEIGHT*IMG_WIDTH, activation='relu'))
#model.add(Dense(250, activation='relu'))
#model.add(Dense(num_classes, activation='softmax'))
#model.compile(tf.keras.optimizers.Adam(lr=0.01), loss='categorical_crossentropy', metrics=['accuracy'])

model = Sequential([
    Conv2D(16, 1, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH ,1)),
    MaxPooling2D(),
    Conv2D(32, 1, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 1, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

print(model.summary())

#history =  model.fit(train_data_gen, epochs=5, batch_size = 200, verbose = 1, shuffle = 1, validation_data=validation_data_gen, validation_steps=total_val / batch_size)
history = model.fit(train_data_gen, 
                    steps_per_epoch=total_train / batch_size, 
                    epochs=epochs,
                    #validation_data=validation_data_gen,
                    #validation_steps=total_val / batch_size
                    )
