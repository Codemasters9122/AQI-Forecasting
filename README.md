

# Time-series Forecasting Project

## Project Overview
Air pollution in Beijing is a serious health hazard, and PM2.5 (Particulate Matter with a diameter of less than 2.5 micrometers) is one of the most dangerous pollutants. This project aims to predict future PM2.5 levels in Beijing using machine learning models based on historical environmental and air quality data. Accurate forecasting can assist authorities in taking preventive measures and issuing timely warnings to protect public health.

## Dataset
The dataset used for this project is the **Beijing PM2.5 Dataset**, which contains hourly data from the U.S. Embassy in Beijing. The dataset includes several features influencing air quality.

### Dataset Features:
- **Date**: Timestamp of the measurement.
- **PM2.5**: Target variable representing PM2.5 concentration (μg/m³).
- **Dew Point**: Dew point in Celsius.
- **Temperature**: Ambient temperature in Celsius.
- **Pressure**: Atmospheric pressure in hPa.
- **Wind Direction**: Cardinal wind direction.
- **Wind Speed**: Wind speed in m/s.
- **Humidity**: Relative humidity in percentage.
- **Precipitation**: Precipitation in mm.
- **Season**: Season of the year (Winter, Spring, Summer, Autumn).

### Data Source
The dataset is sourced from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data).

## Modeling Approach
### 1. **Data Preprocessing**
   - Handling missing data using forward fill and interpolation methods.
   - Converting categorical variables (like wind direction) into numerical form using one-hot encoding.
   - Creating lag features and rolling averages to capture temporal dependencies.
   - Scaling numerical features for better performance in machine learning models.

### 2. **Model Selection**
   Several models were evaluated for their forecasting accuracy:
   - **Time Series Models**:
     - ARIMA
     - SARIMA
     - Prophet
   - **Machine Learning Models**:
     - Random Forest
     - Gradient Boosting (XGBoost, LightGBM)
     - Long Short-Term Memory (LSTM) Networks

### 3. **Evaluation Metrics**
   The performance of each model is evaluated using the following metrics:
   - Mean Absolute Error (MAE)
   - Root Mean Square Error (RMSE)
   - Mean Absolute Percentage Error (MAPE)

## Installation
To set up the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/pm2.5-forecasting.git
cd pm2.5-forecasting
```

### 2. Install dependencies
Ensure you have Python installed, then install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
Place the **Beijing PM2.5 Dataset** in the `data/` directory.

## Usage
### 1. Data Preprocessing
Run the script to preprocess the data and generate the required features:
```bash
python preprocess.py
```

### 2. Training the Model
To train the PM2.5 forecasting model, run the following command:
```bash
python train.py --model lgbm  # or 'arima', 'prophet', 'lstm', etc.
```

### 3. Making Predictions
After training, use the saved model to make PM2.5 predictions:
```bash
python predict.py --input "data/test_data.csv" --output "results/predictions.csv"
```

## Results
- **Model Performance**:
  - The LightGBM model performed the best, with an RMSE of 8.75 and MAE of 6.40 on the test set.
  - The LSTM model performed well with a lower RMSE on long-term predictions, capturing the temporal dependencies better.
  
- **Visualization**:
  - Predicted vs. Actual PM2.5 values are visualized as line charts.
  - Feature importance was plotted for non-time-series models (Random Forest and LightGBM).

## Future Work
- **Model Improvement**: Explore additional features, such as integrating external weather datasets and pollution sources (e.g., satellite data).
- **Deployment**: Set up an API or a dashboard for real-time PM2.5 forecasting.
- **Seasonality Adjustments**: Further work to refine seasonal components, especially during high-pollution periods like winter and holidays.
