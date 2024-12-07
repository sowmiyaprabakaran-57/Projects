# Breast Cancer Prediction

## 📊 Project Overview

This project aims to predict whether a tumor is malignant or benign based on various statistical features extracted from imaging data. The machine learning model uses Random Forest Classifier to classify the diagnosis based on historical patient data. The project involves data preprocessing, feature selection, model training, and evaluation.

## 🛠️ Tools and Libraries Used

The following libraries and tools are used in this project:

- **Google Colab** : Platform for running the code in a cloud environment.
- **Pandas** : Data manipulation and analysis library.
- **NumPy**: Library for numerical computations.
- **Matplotlib & Seaborn**: Visualization libraries used for plotting graphs and exploring data.
- **Scikit-learn**: Machine learning library used for preprocessing, model training, and evaluation.
- **RandomForestClassifier**: The machine learning model used for binary classification (malignant vs benign).
- **LabelEncoder**: For encoding categorical data into numerical values.
- **RobustScaler**: Used to scale features while handling outliers.

## 📂 Dataset

The dataset used in this project is the "breast_cancer_data.csv" file, which contains details about various features related to breast cancer diagnosis, including:

- `id` : Unique identifier for the patient.
- `diagnosis`: Target variable indicating whether the tumor is malignant (M) or benign (B).
- `radius_mean`: Mean of the distances from the center to the points on the perimeter.
- `texture_mean`: Mean of the texture measurement.
- `perimeter_mean`: Mean of the perimeter measurements.
- `area_mean`: Mean of the area measurements.
- `smoothness_mean`: Mean smoothness value.
- `compactness_mean`: Mean compactness measurement.
- `concavity_mean`: Mean concavity value.
- `concave points_mean`: Mean of concave points.

## 🛠️ Data Preprocessing

The following preprocessing steps were carried out:

**1. Handling Missing Data:** Ensured there were no missing values in the features and target variables.

**2. Encoding the Target Variable:** The 'diagnosis' column was encoded into numeric values:

            'M' → 1 (malignant)

            'B' → 0 (benign)

**3. Scaling Data:** Scaled numerical features using RobustScaler to manage outliers.

**4. Train-Test Split:** Split the data into training and testing sets with a test size of 20%.

## 🔧 Model Development

**1. Train-Test Split:** Data was split into training and testing subsets for model evaluation.

**2. Feature Scaling:** Scaled features using RobustScaler to handle potential outliers.

**3. Random Forest Classifier:** The RandomForestClassifier was trained on preprocessed data to classify tumors as malignant or benign.

## 📊 Exploratory Data Analysis (EDA)

**1. Correlation analysis:** Correlation analysis was performed to identify key features affecting prediction accuracy.

**2. Visualization:**  Visualizations like heatmaps were plotted to better understand relationships between features and target variable.

## 📊 Model Evaluation Metrics

The trained model was evaluated using metrics like:

- **Accuracy**: The overall correctness of the model.
  
- **Precision**: The ratio of correctly predicted malignant cases to all predicted as malignant.
  
- **Recall**: The ability of the model to identify all actual malignant cases.
  
- **F1 Score**: The balance between precision and recall.

## 📜 Dependencies

The required libraries are listed. They include:

    pandas
    scikit-learn
    matplotlib
    seaborn

