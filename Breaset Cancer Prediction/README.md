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

The following dependencies are required to run the Breast Cancer Prediction model:

**1. Python (3.x)**: Base programming language.

**2. Scikit-learn**: For data preprocessing, building the SVM model, and evaluation.

- **Installation**: `pip install scikit-learn`
  
**3. Pandas**: For data manipulation and analysis.

- **Installation**: `pip install pandas`
  
**4. NumPy**: For numerical computations.

- **Installation**: `pip install numpy`
  
**5. Matplotlib**: For visualizing the data.

- **Installation**: `pip install matplotlib`
  
**6. Seaborn**: For advanced data visualization.

- **Installation**: `pip install seaborn`

## 🧪 Prediction

The **Breast Cancer Prediction** model allows users to input medical data about their condition (e.g., characteristics of cell nuclei) and predicts whether the patient is likely to have **Benign** (non-cancerous) or **Malignant** (cancerous) cells. If cancer is detected, the model advises consulting a doctor immediately.

**✍️ Input**

The user is prompted to provide the following medical features derived from the patient's test reports:

- Mean Radius
- Mean Texture
- Mean Perimeter
- Mean Area
- Mean Smoothness
- Mean Compactness
- Mean Concavity
- Mean Concave Points
- Mean Symmetry
- Fractal Dimension

**📤 Output:**

Once the input is provided, the model returns:

- **Entered Details**: Displays the user-provided inputs for verification.
  
- **Prediction**: Indicates whether the diagnosis is Benign (No Cancer Detected) or Malignant (Cancer Detected).
  
- **Advice**: Offers guidance for the next steps, including a recommendation to consult a doctor if cancer is detected.

## 📝 Example Input/Output

      📋 Patient Details:  
         Mean Radius: 12.5  
         Mean Texture: 20.0  
         Mean Perimeter: 90.0  
         Mean Area: 600.0  
         Mean Smoothness: 0.12  
         Mean Compactness: 0.2  
         Mean Concavity: 0.3  
         Mean Concave Points: 0.15  
         Mean Symmetry: 0.1  
         Fractal Dimension: 0.06  

        🎯 Prediction: Malignant (Cancer Detected)  
        🩺 Advice: Consult a doctor and take immediate action.  

## 🔮 Conclusion

The Breast Cancer Prediction project applies machine learning techniques, including data preprocessing, feature scaling, and SVM classifier development, to provide a fast and reliable prediction tool. It aims to assist in early detection, enabling patients to seek timely medical intervention.

## 🌟 Future Enhancements

- **Hyperparameter Optimization**: Implement grid search or randomized search for tuning the SVM model.
  
- **Additional Features**: Incorporate other patient health metrics to improve predictive accuracy.

- **Deployment**: Create a web-based or mobile-friendly application for real-world use.

- **Explainability**: Introduce interpretable AI techniques to help patients and doctors understand predictions.
  
## 🚀 How to Run

**1. Dataset Preparation**: Ensure the dataset (`/content/BreastCancer.csv`) is uploaded to your working directory.

**2. Run the Code**: Paste the provided script into Python (IDE, Jupyter, or Colab) and execute.

**3. Provide Input**: Enter the patient's medical details when prompted.

**4. Get Prediction**: Review the diagnosis and follow the suggested advice.
