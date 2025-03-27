import tensorflow as tf
from tensorflow.keras import layers, models

def create_waste_classification_model(input_shape=(150, 150, 3), num_classes=4):
    """
    Creates a convolutional neural network (CNN) model for waste classification.

    Args:
        input_shape: Tuple representing the shape of the input images (height, width, channels).
        num_classes: Number of waste categories to classify.

    Returns:
        A compiled Keras model.
    """

    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5), # Add dropout to reduce overfitting.
        layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model

if _name_ == '_main_':
    # Example usage:
    model = create_waste_classification_model()
    model.summary()
