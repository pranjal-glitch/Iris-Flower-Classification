# 🌸 Iris Flower Classification

A Machine Learning project that classifies Iris flowers into three different species based on sepal and petal measurements. The project includes data analysis, model training, evaluation, and deployment through an interactive Streamlit web application.

---

## 📌 Project Overview

The Iris dataset is one of the most popular datasets in Machine Learning and pattern recognition.

This project predicts the species of an Iris flower using the following features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Predicted Species

* Iris Setosa
* Iris Versicolor
* Iris Virginica

---

## 🎯 Objectives

* Perform data preprocessing and exploration.
* Visualize feature relationships.
* Train a Machine Learning classification model.
* Evaluate model performance.
* Deploy the trained model using Streamlit.
* Create a user-friendly interface for real-time predictions.

---

## 📂 Project Structure

```text

Iris-Flower-Classification/
│
├── dataset/
│   └── Iris.csv
│
├── notebooks/
│   └── iris_classification.ipynb
│
├── models/
│   └── iris_model.pkl
│
├── images/
│   ├── pairplot.png
│   ├── correlation_heatmap.png
│   ├── confusion_matrix.png
│   ├── homepage.png
│   └── prediction_result.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset Information

Dataset: Iris Flower Dataset

Total Samples: 150

Features:

| Feature       | Description     |
| ------------- | --------------- |
| SepalLengthCm | Length of sepal |
| SepalWidthCm  | Width of sepal  |
| PetalLengthCm | Length of petal |
| PetalWidthCm  | Width of petal  |

Target Variable:

* Species

Classes:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

---

## 🔍 Exploratory Data Analysis

The following visualizations were used:

* Species Distribution
* Pair Plot
* Correlation Heatmap
* Confusion Matrix

These visualizations helped understand feature relationships and class separability.

---

## 🤖 Machine Learning Model

Algorithm Used:

### K-Nearest Neighbors (KNN)

KNN classifies a flower based on the similarity of its measurements to previously observed flowers.

---

## 📈 Model Performance

Evaluation Metrics:

* Accuracy Score
* Classification Report
* Confusion Matrix

### Result

The model achieved high classification accuracy on the test dataset.

---

## 🌐 Streamlit Web Application

The project includes a modern Streamlit-based user interface where users can:

* Enter flower measurements.
* Predict Iris species instantly.
* View prediction confidence.
* Interact with the trained Machine Learning model.

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Iris-Flower-Classification.git
```

### Move Into Project Folder

```bash
cd Iris-Flower-Classification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Application Screenshots

### Home Page

Add screenshot:

```text
images/homepage.png
```

### Prediction Result

Add screenshot:

```text
images/prediction_result.png
```

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit

---

## 🔮 Future Improvements

* Compare multiple classification algorithms.
* Deploy online using Streamlit Cloud.
* Add additional model evaluation metrics.
* Improve UI with advanced analytics.

---

## 👨‍💻 Author

Pranjal Srivastava

B.Tech Computer Science & Engineering

JECRC University, Jaipur

---

⭐ If you found this project useful, consider giving it a star.
