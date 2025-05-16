# MUSA 650 Final Assignment: Remote Sensing Solution for Urban Planning

## Assignment Overview

For this final assignment in MUSA 650, you will design and implement a machine learning-based remote sensing solution to address a specific problem in urban planning. Your goal is to clearly identify the problem, define your target users, and develop a solution that uses Python-based remote sensing and machine learning techniques. This project will evaluate both your technical approach (50%) and a polished, five-minute lightning talk (50%) geared toward professional audiences.

## Submission Guidelines

Please follow the [general submission guidelines](../../README.md#submission-guidelines) in the course README. For this assignment, you must include the following files in your submission:

```
assignments/
  submissions/
    FINAL_PROJECT/
      FINAL_PROJECT.ipynb
      FINAL_PROJECT_presentation.pdf (or other format as specified in Lightning Talk section)
```

## Objectives

- Identify an urban planning problem and define your target user.
- Develop a solution using remote sensing data and machine learning techniques in Python.
- Provide a comprehensive analysis of the solution, including data sources, model architecture, preprocessing steps, feature engineering, and validation.
- Evaluate the solution's quantitative performance and discuss qualitative aspects like constraints, limitations, and improvements.
- Present a professional-grade, portfolio-ready summary of your work.

## Problem Scope

### 1. Problem Identification

- Identify a specific urban planning problem to address. Possible topics include:
  - Urban sprawl analysis
  - Flood identification
  - Heat risk mapping
  - Green corridor identification
- Explain **why this is a problem**, its **impacts**, and its relevance to urban planning.

### 2. Target User(s)

- Define a hypothetical user such as a national think tank, a city or regional government, or a research institution (e.g., USGS).
- Describe why this user would value your solution and the insights they hope to gain.

## Solution Development

### 3. Data and Model

- **Data Source**: Specify the data source(s) you will use, for example:
  - **NLCD** (National Land Cover Database) for land cover classification
  - **Sentinel-1** or **Sentinel-2** for radar and optical data
  - **Landsat** for multi-decadal change detection
  - **Proprietary datasets** that are accessible through open access licenses
- **Model Architecture**: Describe your model architecture, including:
  - Algorithms and libraries you plan to use (e.g., Google Earth Engine, TorchGeo, Keras).
  - Preprocessing steps and feature engineering.
  - Alternative approaches you considered and your rationale for the final model selection.
- **Scaling Considerations**: Discuss hardware and software considerations, such as:
  - **Data Augmentation**: When and why data augmentation may be necessary.
  - **Cloud Computing and GPUs**: Whether cloud computing (e.g., Google Cloud Platform, AWS) or GPUs are required to handle large datasets or speed up training.
  - **Training Constraints**: Describe any constraints on model training (e.g., speed limitations with local machines versus cloud environments) and how they influenced your model selection.

### 4. Relevant Research

- Summarize relevant research papers that informed your approach in brief paragraphs.
- Highlight key insights and how they influenced your design.

## Evaluation

### 5. Quantitative and Qualitative Analysis

- **Evaluation Metrics**: Describe and justify the evaluation metrics you used (e.g., accuracy, precision, recall, F1-score, Intersection over Union).
- **Quantitative Evaluation**: Report your model's performance based on these metrics.
- **Qualitative Analysis**: Describe strengths and limitations of your solution. Consider:
  - **Labeled Data Availability**: Was there enough labeled data, and did this affect the model's accuracy?
  - **Data Augmentation**: Discuss if data augmentation was used to improve performance.
  - **Computation Requirements**: Describe how computation requirements (e.g., using a local machine vs. cloud computing) impacted your solution.
  - **Scalability**: Address the feasibility of scaling this solution and the resources needed.

### 6. Future Steps

- Identify steps for improvement or expansion, such as enhancing model architecture, integrating additional data sources, or adjusting parameters.

## Lightning Talk Presentation

### Requirements

- Prepare a five-minute lightning talk that professionally summarizes your problem, solution, and key findings.
- Your presentation should be **polished and concise**, suitable for inclusion in a professional portfolio.
- Suggested formats include:
  - A video demonstration
  - A blog post
  - A LinkedIn article or post
  - A slide deck with speaker notes
- Your talk should clearly define the problem, outline your approach, present evaluation results, and discuss key insights or takeaways.

### Submission and Grading

- **Code and Analysis** (50%): Evaluation based on the technical depth, workflow, and rigor of your code, analysis, and evaluation.
- **Lightning Talk** (50%): Grading will focus on clarity, professionalism, presentation quality, and alignment with a professional portfolio.

## Rubric (40 points total)

| Category                          | Weight | Excellent                                                                 | Satisfactory                                 | Unsatisfactory                           |
| --------------------------------- | ------ | ------------------------------------------------------------------------- | -------------------------------------------- | ---------------------------------------- |
| **Code and Analysis (30 points)** |
| Problem Definition & Research     | 7.5    | Clear problem statement; thorough literature review; strong justification | Adequate problem definition and research     | Unclear problem or insufficient research |
| Data & Model Implementation       | 7.5    | Well-designed architecture; thorough preprocessing; clear documentation   | Functional implementation with minor issues  | Poor implementation or missing elements  |
| Evaluation & Analysis             | 7.5    | Comprehensive metrics; thorough analysis; clear limitations discussion    | Basic evaluation with some analysis          | Limited or missing evaluation            |
| Technical Depth                   | 7.5    | Advanced techniques; novel approaches; clear rationale for choices        | Standard approaches with basic justification | Basic or inappropriate techniques        |
| **Presentation (10 points)**      |
| Content & Structure               | 7.5    | Clear narrative; logical flow; professional format; compelling story      | Adequate structure with minor issues         | Poor organization or unclear content     |
| Design & Delivery                 | 2.5    | Professional visuals; engaging delivery; clear information hierarchy      | Basic visuals with adequate presentation     | Poor visuals or unprofessional delivery  |
