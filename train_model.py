import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from cnn_model import create_model

# Directories
train_data_dir = '../data/train'
validation_data_dir = '../data/validation'

# Image dimensions
img_width, img_height = 150, 150

# Parameters
batch_size = 32
epochs = 10

# Data augmentation for training
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

# Normalization for validation
validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

# Data generators
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

# Create model
input_shape = (img_width, img_height, 3)
num_classes = len(train_generator.class_indices)
model = create_model(input_shape, num_classes)

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)

# Save the trained model
model_save_path = 'waste_classifier_model.h5'
model.save(model_save_path)
print(f"Model saved at {model_save_path}.")
