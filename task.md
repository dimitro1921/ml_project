# Introduction to Machine Learning (KSE) Group Project Guidelines

**Instructor:** Oleh Nivievskyi

## 1. Objective
The purpose of the group project is to apply machine learning methods learned during the course to a real-world problem. Students are expected to formulate a research question, obtain and prepare data (focused on Ukraine), develop and compare machine learning models, evaluate their performance, and communicate findings effectively. The project should demonstrate both technical competence and the ability to interpret results in an applied context.

## 2. Team Composition
* Teams of 2 students.
* All team members are expected to contribute actively.
* Each team member must present during the final project presentation.
* Teams must submit a short contribution statement describing each member's role.

## 3. Topic Selection
Projects should address a meaningful prediction or classification problem. Possible domains include:
* Agriculture and food systems
* Remote sensing and land use
* Transportation and mobility
* Environmental and climate applications
* Finance and business analytics
* Public policy and governance
* Health and social sciences
* Sports analytics
* Education and labor markets
* Medicine

Students are encouraged to use Ukrainian data whenever possible. 

Examples:
* Crop classification from satellite imagery
* Predicting agricultural yields
* House price prediction
* Loan default prediction
* Customer churn prediction
* Traffic congestion forecasting
* Local government performance classification
* Detection of damaged infrastructure from imagery

Projects may involve:
* Regression
* Classification
* Unsupervised learning
* Deep learning

## 4. Project Requirements
Each project must include the following components.

### 4.1 Problem Definition
Clearly explain:
* The practical problem.
* Why it matters.
* The prediction/classification target (dependent variable).
* The predictors (features).

### 4.2 Data
Describe:
* Data source(s).
* Sample size.
* Variables used.
* Data cleaning procedures.
* Missing value treatment.
* Feature engineering steps.
* Provide descriptive statistics and visualizations.

### 4.3 Exploratory Data Analysis (EDA)
Conduct exploratory analysis to understand:
* Variable distributions.
* Relationships among variables.
* Potential outliers.
* Class imbalance (if applicable).
* Data quality issues.
* Include meaningful visualizations and discussion.

### 4.4 Model Development
**A. Supervised Learning Projects**
Students must implement at least two different models. The project must include:
(1) At least one interpretable model, such as:
* Linear Regression
* Logistic Regression
* Ridge Regression
* Lasso Regression
* Single Decision Tree

(2) At least one advanced machine learning model, such as:
* Random Forest
* Gradient Boosting
* XGBoost
* Support Vector Machine (SVM)
* Neural Network

Students should discuss the trade-off between:
* predictive accuracy,
* model complexity,
* interpretability.

A model that performs slightly worse but is substantially easier to interpret may sometimes be preferable in practice.

**B. Unsupervised Learning Projects**
Projects based primarily on unsupervised learning might be focused on:
* Customer segmentation
* Farm typology classification
* Community profiling
* Land-use clustering
* Gene expression clustering
* Topic modeling
* Dimensionality reduction of high-dimensional datasets

Students must apply at least two unsupervised learning techniques, for example:
* K-Means Clustering
* Hierarchical Clustering
* Principal Component Analysis (PCA)

(You might want to include only methods that are covered in the course slides).

The project should include:
1. Clear motivation for using unsupervised learning.
2. Justification of the chosen number of clusters or dimensions.
3. Interpretation and profiling of clusters/components.
4. Visualization of results.
5. Comparison of alternative methods.
6. Discussion of practical implications.

Where appropriate, students should use appropriate evaluation metrics.

### 4.5 Model Evaluation
Use appropriate train-test splitting and/or cross-validation.

For supervised learning projects:
* For regression problems report metrics such as: RMSE, MAE, $R^{2}$
* For classification problems report metrics such as: Accuracy, Precision, ROC-AUC
* Compare model performance systematically.

For unsupervised learning projects:
* Internal validation metrics
* Cluster stability
* Visualization quality
* Practical interpretability

### 4.6 Model Interpretation
Interpretation is a required component of every project. Students should discuss:
* Important variables or patterns.
* Practical meaning of results.
* Whether findings are consistent with domain knowledge.
* Limitations of the analysis.

Simply reporting performance metrics is not sufficient.

### 4.7 Conclusions
Summarize:
* Main findings.
* Best-performing model.
* Practical implications.
* Limitations.
* Suggestions for future improvements.

## 5. Reproducibility Requirements
All projects must be fully reproducible. Submit:
* 7. Final report (in .ipynb or .qmd formats; very well documented and commented on essentially every step of the code)
* 8. HTML output
* 9. Source code
* 10. Data (or clear instructions for accessing the data)
* 11. Presentation slides

The project should run from start to finish without manual intervention.

## 6. Deliverables
**A. Written Report (70%)**
Maximum length: 5 pages (excluding appendix).
Suggested structure:
1. Introduction
2. Problem Statement
3. Data Description
4. Exploratory Data Analysis
5. Methodology
6. Model Development
7. Results
8. Discussion
9. Conclusions
10. References

**B. Presentation (30%)**
* 10-15 minutes presentation
* 5 minutes Q&A
* Every team member must present.
* Presentation should focus on: Motivation, Data, Methods, Results, Lessons learned

## 7. Evaluation Criteria
| Criterion | Weight |
| :--- | :--- |
| Problem formulation | 5% |
| Data preparation and EDA | 10% |
| Appropriate use of ML methods | 15% |
| Model evaluation and comparison | 20% |
| Interpretation and discussion | 10% |
| Reproducibility and code quality | 10% |
| Presentation | 30% |

## 8. Academic Integrity
Students may use:
* Course materials
* Official documentation
* Open-source libraries
* Generative/agentic AI tools (ChatGPT, Claude, Gemini, etc.)

However:
* Students remain fully responsible for understanding and explaining every aspect of their work.
* Plagiarism, fabricated results, or submission of work that cannot be explained during the presentation will result in penalties.

## 9. Recommended Workflow
1. Define a practical problem.
2. Obtain and understand the data.
3. Conduct exploratory analysis.
4. Establish a baseline model.
5. Develop and compare more advanced models.
6. Evaluate performance using cross-validation.
7. Interpret results.
8. Communicate findings clearly.
9. Ensure full reproducibility.
10. Prepare a professional presentation.

The best projects will combine technical rigor with clear practical relevance and insightful interpretation of results.