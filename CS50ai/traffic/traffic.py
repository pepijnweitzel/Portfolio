import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    # Set variables
    images = []
    labels = []

    # Iterate over directories in data_dir
    for i in range(NUM_CATEGORIES):

        # Iterate over every image in directory
        for filename in os.listdir(os.path.join(data_dir, str(i))):

            # Read image as numpy.ndarray
            image = cv2.imread(os.path.join(data_dir, str(i), filename))

            # Resize image to IMG_WIDTH and IMG_HEIGHT
            resized_image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))

            # Append numpy.ndarray to list of images
            images.append(resized_image)

            # Label is name of directory for corresponding images aka 'i', so add to labels list
            labels.append(i)

    return images, labels


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    # Create neural network model
    model = tf.keras.models.Sequential([

        # Add an input layer
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),

        # Convolutional layer. Learn 32 filters using a 3x3 kernel
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),

        # Average-pooling layer, using 3x3 pool size
        tf.keras.layers.AveragePooling2D(pool_size=(3, 3)),

        # Flatten units
        tf.keras.layers.Flatten(),

        # Add a hidden layer
        tf.keras.layers.Dense(256, activation="relu"),

        # Add second hidden layer
        tf.keras.layers.Dense(256, activation="relu"),

        # Add dropout to hidden layer (dropout of 50%) to prevent overfitting
        tf.keras.layers.Dropout(0.5),

        # Add an output layer of NUM_CATERGORIES number
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    # Train neural network model
    model.compile(
        # Adam is easy default choice
        optimizer='adam',
        # Categorical_crossentropy for vector usage
        loss='categorical_crossentropy',
        # Accuracy is easy default choice
        metrics=['accuracy'
    ])

    return model
su
if __name__ == "__main__":
    main()
