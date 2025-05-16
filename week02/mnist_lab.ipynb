# MUSA 650 Homework 1: Basics of Machine Learning

In this assignment, you’ll explore fundamental machine learning concepts and techniques, with a focus on data preprocessing, image manipulation, and model evaluation. You are responsible for figuring out the code independently and may refer to tutorials, code examples, or use AI support, but **please cite all sources**.

Submit a single Jupyter Notebook containing code, narrative text, visualizations, and answers to each question. Open a pull request from your fork of this repository to the main repository for submission.

## Important Notes

- **Sample Size Considerations**: If experiments take too long with the complete dataset, start with a smaller sample for timely execution. For your final submission, use the full dataset if feasible, but if processing is still too intensive, note your sample sizes clearly. Sample size variations will not affect grading if documented appropriately.
- **Data Reshaping**: To switch between 2D and 1D representations, use functions like `numpy.flatten()` or `numpy.resize()` as needed.

## 1. Data Exploration

Load the mnist dataset using the following code, which contains all of the module imports needed for this assignment:

```
import pandas as pandas
import numpy as np
import matplotlib.pyplot as plt
import keras

from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
```

### 1.1 Dimensionality

What is the type of the training and testing datasets?

How many features are in the training dataset? The testing dataset? How many samples are in each dataset?

If an array has a shape of `(100, 28, 28)`, what does each number represent in the context of image data (i.e., which number represents the number of images, and which represent the number of pixels?), and how would it change if you flattened it to a 2D array?

How would you convert a 3D array into a 2D array without changing the total number of elements? Describe how `flatten()` and `reshape()` can be used for this purpose.

Explain why it’s necessary to reshape data when transitioning from raw images to model input, particularly in neural networks. What are the implications of reshaping an image array into a vector (1D array) for each sample? (Feel free to turn to Google for this, as long as you cite your sources.)

### 1.2 Visualization

Select one random example from each category in the testing set, display each 2D image, and label it with the corresponding category name.

## 2. Data Processing

### 2.1 Subsetting

Create a 10% random subset of each training and testing set. What is the distribution of each label in the initial train data? What is the distribution of each label in the reduced train data?

Now subset the **first** 10% of each training and testing set. What is the distribution of each label in the initial train data? What is the distribution of each label in the reduced train data?

When reducing dataset size, what differences might you expect to see in results between randomly selecting samples versus selecting the first portion of the dataset? Is this borne out by the subsets you just created? How does the distribution of the labels in the various subsampled datasets compare to the distribution of the full datasets?

Why might subsampling a dataset be beneficial when developing machine learning models? Discuss the trade-offs.

### 2.2 Feature Engineering

What are the features versus the output in this assignment? Why is it important to distinguish between features (inputs) and outputs (labels) in a machine learning model?

Select all train images labeled "3". Create a single, pixel-wise average image of all of these images. Plot the 2D mean and standard deviation images for category 3 in both the training and testing sets. Comment on the differences between the mean and standard deviation images between the training and testing datasets. Plot the 2D mean and standard deviation images for category "3" in the training and testing sets for the binarized images.

Now repeat this for a new label (e.g., "7"). Comment on the differences between the mean and standard deviation images between the training and testing datasets for the binarized images.

Binarize both of the images from the previous question by setting pixel values equal to 1 if they are greater than the mean value for that pixel and equal to 0 if they are less than the mean value for that pixel.

In plain English, what are we actually **doing** when we binarize an image? How does the new pixel value relate to the pixel value of the original image and the mean value for that pixel across all images with that label?

What is the index of the most **dissimilar** image in category "3" in the training set for the regular images? What about the most **similar** image? Does this change for the binarized images? If so, why? Make sure to plot all four images with approproate labels.

What do you think the effect of binarizing these images is from a machine learning perspective? How does binarization of images (converting pixel values to 0 or 1 based on a threshold) affect the representation of features, and what might be the benefits and limitations of this approach?

How does what you've just done relate to the idea of standardizing data? Why might it be important to standardize our data before using it to train a model?

Describe how calculating a pixel-wise mean or standard deviation for a set of images can help you understand variations within a category. What does a high standard deviation indicate in this context?

## 3. Model Training, Validation, and Intepretation

### 3.1 Support Vector Machine

From the training dataset, select only images from categories "3" and "9".Subdivide the data into Set1 and Set2, with 60% of the data in Set1 and 40% in Set2. Replace category labels with 0 for 3 and 1 for 9.
Use Set1 to train a linear support vector machine classifier with default parameters and predict the class labels for Set2. What is the prediction accuracy using the model trained on the training set? What is the prediction accuracy using the model trained on the testing set?

### 3.2 Modeling with Engineered Data

We describe each image by using a reduced set of features (compared to n = 784 initial features for each pixel value) as follows:

- Binarize the image by setting the pixel values to 1 if they are greater than 128 and 0 otherwise.
- For each image row i, find n_i, the sum of 1's in the row (28 features).
- For each image column j, find n_j, the sum of 1's in the column (28 features).
- Concatenate these features to form a feature vector of 56 features.

What is the prediction accuracy using an SVM model trained on the training set? What is the prediction accuracy using an SVM model trained on the testing set? How about the prediction accuracy of a KNN model trained on the training set? And on the testing set? What does this tell you about the potential impacts of feature engineering?

### 3.3 K-Nearest Neighbors

In the training and testing datasets, select images in the categories 1, 3, 5, 7, and 9. Train a k-NN classifier using 4 to 40 nearest neighbors, with a step size of 4.

For k = 4, what is the label that was predicted with lowest accuracy?

For k = 20, what is the label that was predicted with lowest accuracy?

What is the label pair that was confused most often (i.e., class A is labeled as B, and vice versa)?

Visualize 5 mislabeled samples with their actual and predicted labels.

Based on the patterns in the pixel values for each category, which labels (numbers) do you think the model might struggle to identify or distinguish from one another? Explain why certain labels might be more challenging to separate, considering the similarity in pixel patterns or shapes.

### 3.4 Comprehension Questions

Why is it important to have separate training and testing datasets? What potential issues arise if you use the same data for both training and evaluation?

If you achieve a high accuracy on the training set but a lower accuracy on the testing set, what might this indicate about your model’s performance and generalization?
