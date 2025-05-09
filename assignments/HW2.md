# MUSA 650 Homework 2: Supervised Land Use Classification with Google Earth Engine

In this assignment, you will use Google Earth Engine via Python to implement multi-class land cover classification. You will hand-label Landsat 8 satellite images which you will then use to train a random forest model. Along the way, you will consider practical remote sensing issues like cloud cover, class imbalances, and feature selection.

## Important Note on Google Earth Engine

**Google Earth Engine Scaling:** If you encounter scaling issues with GEE, this typically indicates something wrong with your code rather than limitations of the platform. GEE is built to handle this type of task efficiently at scale by running computations on the server side. If you experience scaling problems, review your code structure and consult the provided resources. While GEE has a bit of a steep learning curve, mastering its approach to large-scale data processing is valuable for remote sensing work.

**This assignment requires you to work in groups of 2-3 students. No individual assignments will be accepted. One member of the group should submit on behalf of everyone, making sure to include all group members' names at the top of the notebook.**

You are responsible for figuring out the code independently and may refer to tutorials, code examples, or use AI support, but **please cite all sources**.

In particular, we encourage you to consult the [official Python Google Earth Engine `geemap` package](https://geemap.org/), the online course [Spatial Thoughts](https://spatialthoughts.com/courses/google-earth-engine/), and the [Google Earth Engine Tutorials book](https://google-earth-engine.com/).

## Submission Guidelines

Submit your work via a Pull Request to the main branch of this repository with the following structure:

```
assignments/
  submissions/
    HW2/
      HW2.ipynb
      classification.tif
      accuracy.csv
      map-visualization.gif
```

Your Jupyter notebook must:

- Include the assignment number in the filename
- Contain all instructions from this markdown, followed by the relevant code chunks
- Include your names and submission date
- Be well-formatted with appropriate code chunks (no overly long code blocks)
- Be linted and formatted using [`ruff`](https://docs.astral.sh/ruff/) before submission

Code quality will be factored into your grade. Break your code into logical chunks rather than having dozens of lines in a single cell.

Since interactive embeds (e.g., `geemap`) do not render properly in static Jupyter notebooks, please include a .gif of you clicking through each layer in your map. Embed this .gif in your notebook and include it in your submission folder.

## 1. Setup

For this assignment, you will define the region of interest (ROI) of your choice, _provided that it is in a country outside of the United States._ We recommend picking an urban area large enough that you will have a sufficient sample size but not so large that it will take an excessively long time to process.

You'll also use Landsat 8 satellite imagery from USGS for this assignment. Choose images from 2023, filtering for images with minimal cloud cover. Because we'll be includeing NDVI in our calculations, you'll likely want to choose images from the greenest time of year in your region of choice (summer/rainy season). Be mindful of the differences between the northern and southern hemisphere.

## 2. Data Collection and Feature Engineering

### 2.1 Collecting and Labeling Training Data

Using the [interactive `geemap` interface](https://www.youtube.com/watch?v=VWh5PxXPZw0) or another approach (e.g., QGIS, ArcGIS, a GeoJSON file, etc.), create at least 100 samples (points or polygons) for each of the following four classes: urban, bare, water, and vegetation. (Again, we encourage you to work in pairs or groups of three to generate these hand labels.) Use visual cues and manual inspection to ensure that the samples are accurate. Assign each class a unique label (e.g., 0 for urban, 1 for bare, 2 for water, and 3 for vegetation) and merge the labeled samples into a single dataset.

If you choose to base your labels on an existing land cover dataset, be aware that this means you're training a model on another model's outputs. This can lead to compounded inaccuracies, as your model will inherit the errors of the original dataset. To mitigate this, consider using only the most certain labels from the original dataset (e.g., those with a high probability score) or look for agreement between multiple datasets.

**Note:** Everything from here on out (feature engineering, model training and evaluation, accuracy assessment) **must** be done in Earth Engine, not scikit-learn or other platforms. The goal is specifically to learn how to use Earth Engine.

### 2.2 Feature Engineering

For possible use in the model, calculate and add the following spectral indices:

- **NDVI** (Normalized Difference Vegetation Index)
- **NDBI** (Normalized Difference Built-up Index)
- **MNDWI** (Modified Normalized Difference Water Index)

Calculate [kernel filters](https://google-earth-engine.com/Advanced-Image-Processing/Neighborhood-based-Image-Transformation/) (e.g., edge detection, smoothing) based on the RGB imagery. Add elevation and slope data from a DEM. Normalize all image bands to a 0 to 1 scale for consistent model input.

## 3. Model Training and Evaluation

### 3.1 Model Training

Split your data into a training dataset (70%) and a validation dataset (30%). Train and evaluate a random forest model using the training set with all engineered features.

After training, analyze [variable importance scores](https://stackoverflow.com/questions/74519767/interpreting-variable-importance-from-random-forest-in-gee) to justify each feature's inclusion.

Discuss which features are most important. Based on your understanding of the task at hand, why do you think this is? Which features are least important, and why? What might the role of multicolinearity be in this context, and how might it contribute to overfitting (e.g., if two features are highly correlated, they may provide redundant information to the model)? Again, how does this relate to your understanding of what each feature actually represents?

Compare at least two different feature sets (e.g., one with all features and one with only the most important features) to see if there is a difference in model performance. Report the final features that you keep in your model.

### 3.2 Accuracy Assessment

Use the trained model to classify the Landsat 8 image, creating a land cover classification map with your chosen classes.

Using the validation data, generate a confusion matrix. Calculate appropriate validation metrics for the class at hand (a multi-class classification problem). Explain how you selected these validation metrics and what they indicate about the quality of your model.

Visually compare your landcover data for your ROI with the corresponding [landcover data from the European Space Agency](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCover_v200). Do your classifications agree? If not, do you notice any patterns in the types of landcover where they differ, or any particular features in the imagery that are hard for your model to recognize (e.g., sand, water, or asphalt)? Why might this be the case?

Export the classified image as a GeoTIFF and the confusion matrix and accuracy metrics to a CSV file for documentation.

## 4. Reflection Questions

What limitations did you run into when completing this assignment? What might you do differently if you repeated it, or what might you change if you had more time and/or resources?

What was the impact of feature engineering? Which layers most contributed to the model? Did you expect this? Why or why not?

Did you find it difficult to create the training data by hand? Did you notice any issues with class imbalance? If so, how might you resolve this in the future (hint: consider a different sampling technique).

Did your model perform better on one class than another? Why? Can you think of a reason that this might be good or bad depending on the context?

How did you handle overfitting in the model? Where do you think it came from (e.g., too many features, too few samples, a model with too many trees, etc.)?

# MUSA 650 Homework 2 Rubric (10 points)

| Category                                        | Weight | Excellent                                                                                                                           | Satisfactory                                              | Unsatisfactory                                     |
| ----------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------- |
| **Conceptual Understanding & Discussion (70%)** |
| Feature Engineering Analysis                    | 1.5    | In-depth discussion of feature selection rationale; critical analysis of how each feature contributes                               | Adequate discussion of features with some analytical gaps | Minimal or no discussion of feature choices        |
| Model Training & Feature Importance Discussion  | 2.0    | Comprehensive discussion of model decisions; insightful analysis of feature importance; thoughtful handling of statistical concerns | Adequate discussion with basic analysis of results        | Limited or incorrect analysis of model choices     |
| Accuracy Assessment & Interpretation            | 1.5    | Insightful discussion of metric selection, interpretation of results; thoughtful comparative analysis with ESA data                 | Sound discussion with competent interpretation            | Minimal or incorrect interpretation of results     |
| Reflection & Critical Thinking                  | 2.0    | Thoughtful critical analysis of limitations and implications, connections to theory                                                 | Adequate reflection with some theoretical connections     | Superficial or missing reflection                  |
| **Technical Implementation (30%)**              |
| Code Functionality & Execution                  | 1.0    | Fully functional code with well-considered implementation                                                                           | Working code with minor issues                            | Non-functional or severely flawed code             |
| Code Organization & Documentation               | 1.0    | Logically structured; well-commented; follows best practices                                                                        | Generally organized with adequate documentation           | Poor organization or insufficient documentation    |
| Formatting & Best Practices                     | 0.5    | Properly formatted with ruff; consistent style                                                                                      | Minor formatting issues                                   | No evidence of code quality standards              |
| Submission Requirements                         | 0.5    | All requirements met professional presentation                                                                                      | Minor issues but complete                                 | Incomplete submission or major formatting problems |
