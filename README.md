# Electric-Motor-Temperature-Prediction

## Data Analysis

### 📌 Project Overview

This project performs **exploratory data analysis (EDA)** on a dataset containing parameters from a Permanent Magnet Synchronous Motor (PMSM) and predicts the **Permanent Magnet (PM) temperature** of an electric motor using various machine learning models. It uses features such as current, voltage, ambient temperature, motor speed, and coolant temperature to make predictions.

### 📂 Dataset

Dataset link: https://www.kaggle.com/wkirgsn/electric-motor-temperature

The dataset contains various electrical, thermal, and operational measurements of the motor.

**Key Features:**

* `u_q` – Voltage in q-axis
* `coolant` – Coolant temperature
* `stator_winding` – Stator winding temperature
* `u_d` – Voltage in d-axis
* `stator_tooth` – Stator tooth temperature
* `motor_speed` – Motor speed
* `i_d` – Current in d-axis
* `i_q` – Current in q-axis
* `pm` – Permanent magnet surface temperature
* `stator_yoke` – Stator yoke temperature
* `ambient` – Ambient temperature
* `torque` – Motor torque
* `profile_id` – Profile identifier for operating conditions

### 📊 Analysis Steps

1. **Import Libraries**

   * `numpy`, `pandas`, `matplotlib`, `seaborn`, `plotly`

2. **Load Dataset**

   * Reads CSV data into a Pandas DataFrame.

3. **Data Exploration**

   * View basic statistics and dataset shape.
   * Check for missing values.
   * Identify value ranges for each feature.

4. **Visualization**

   * **Bar plot** to find out the profile id with most observations.
   * **Box plot** to check outliers in our dataset.
   * **Correlation heatmaps** to identify relationships between variables.
   * **Line plots** for time series trends.
   * **Scatter plots** for feature relationships.
   * **Distribution plots** to analyze value spread.

### 📦 Requirements

Install dependencies with:

```python
pip install numpy pandas matplotlib seaborn plotly
```

### 🚀 How to Run

1. Clone the repository.
2. Place your dataset file (`Dataset.csv`) in the appropriate path.
3. Open the Jupyter Notebook:

   ```python
   jupyter notebook Data_analysis.ipynb
   ```
4. Run cells sequentially to view the analysis.

## Model Building

### 📌 Features

* Data preprocessing using **MinMaxScaler**
* Models implemented:

  * Linear Regression
  * Decision Tree Regressor
  * Random Forest Regressor *(optional – large size and slow to train)*
  * Support Vector Regressor *(optional because of time consuming)*
    
* Model evaluation using:

  * R² Score
  * Mean Squared Error (MSE)
  * Mean Absolute Error (MAE)
    
* Model saving using `joblib`

### 🛠 Requirements

* Python 3.8+
* pandas
* scikit-learn
* joblib
* jupyter (if using the notebook)

Install dependencies:

```python
pip install pandas scikit-learn joblib jupyter
```

The dataset should contain the following columns:

* `i_q` – q-axis current
* `i_d` – d-axis current
* `u_q` – q-axis voltage
* `u_d` – d-axis voltage
* `ambient` – ambient temperature
* `motor_speed` – motor speed
* `coolant` – coolant temperature
* `pm` – permanent magnet temperature (target)

Place the dataset in the working directory and update the file path in the code:

```python
Dataframe = pd.read_csv("path/to/Dataset.csv") # update the file path with your dataset path
```

### 📈 Model Performance

From testing:

* Decision Tree achieved 98% accuracy with much faster training compared to Random Forest.
* Random Forest can be used for slightly better accuracy, but the model file is **3GB+**.
* Random Forest and SVR take significantly longer to train.

## 📂 Project Structure
```
ELECTRIC-MOTOR-TEMPERATURE-PREDICTION/
│
├── 📁 Data Collection and Analysis
│    ├── Data_analysis.ipynb
│    ├── dataset_download_script.py
│
├── 📁 Flask Application
│    ├── 📁 static
│    │    ├── body_background.webp
│    │    ├── Manual_predict.css
│    │    ├── motor_image.webp
│    │    ├── result.css
│    │
│    ├── 📁 templates
│    │    ├── Manual_predict.html
│    │    ├── result.html
│    │
│    ├── app.py
│
├── 📁 Model Building
│    ├── decision_tree_model.save
│    ├── decision_tree_model.zip  # unzip this model and after that load in app.py
│    ├── linear_model.save  # i saved this folder for just future usecase if you want to use this model instead of decidion_tree_model then load this model in app.py file 
│    ├── mm_scaler_x.joblib  # scaler for input data
│    ├── mm_scaler_y.joblib  # scaler for output data
│    ├── model_building.ipynb  
│
├── Dataset.csv  # copy the path of this dataset and paste it at the time of loading of data.
├── README.md
```


