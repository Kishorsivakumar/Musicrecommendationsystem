import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ReduceLROnPlateau
from sklearn.metrics import classification_report, confusion_matrix


train_dir = 'C:/Users/Kishor/Miniproject/fer2013/train_dir'
test_dir = 'C:/Users/Kishor/Miniproject/fer2013/validation_dir'


train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(48, 48),
    batch_size=128,          
    color_mode='grayscale',
    class_mode='categorical'
)

test_data = test_datagen.flow_from_directory(
    test_dir,
    target_size=(48, 48),
    batch_size=128,
    color_mode='grayscale',
    class_mode='categorical'
)


model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(64, activation='relu'),  
    Dropout(0.4),
    Dense(7, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


callbacks = [
    ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3)
]


history = model.fit(
    train_data,
    epochs=15,
    validation_data=test_data,
    callbacks=callbacks
)


plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.show()


model.save('emotion_model.h5')
print('Model trained and saved successfully as emotion_model.h5')
