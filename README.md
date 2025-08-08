# Electric-Motor-Temperature-Prediction

## Data Analysis

### 📌 Project Overview

This project performs **exploratory data analysis (EDA)** on a dataset containing parameters from a Permanent Magnet Synchronous Motor (PMSM). The goal is to understand relationships between motor parameters and prepare insights that could be used for **temperature prediction modeling**.

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

## 🚀 How to Run

1. Clone the repository.
2. Place your dataset file (`Dataset.csv`) in the appropriate path.
3. Open the Jupyter Notebook:

   ```python
   jupyter notebook Data_analysis.ipynb
   ```
4. Run cells sequentially to view the analysis.



