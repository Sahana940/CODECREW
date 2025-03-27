import tensorflow as tf

# Load the saved model
model = tf.keras.models.load_model('waste_classifier_model.h5')

# Convert the model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the converted model
tflite_model_path = 'waste_classifier_model.tflite'
with open(tflite_model_path, 'wb') as f:
    f.write(tflite_model)

print(f"TFLite model saved at {tflite_model_path}.")
