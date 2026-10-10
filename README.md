# Traffic Volume Forecasting System

A machine learning web application built with **Streamlit** that predicts traffic volume based on the selected hour and day of the week. It includes a demo login page, model evaluation metrics, a visualization of actual versus predicted traffic volume, and traffic-level guidance.

## Features

- **Demo login system** to access the dashboard.
- **Synthetic traffic data generation** for demonstration and testing.
- **Data preview** to inspect sample records.
- **Linear Regression model** trained using the hour and day of the week.
- **Model evaluation** using Mean Absolute Error (MAE) and Mean Squared Error (MSE).
- **Actual vs. predicted visualization** using a scatter plot.
- **Interactive prediction** based on a user-selected hour and day.
- **Traffic-level messages** for low, average, and high predicted traffic.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Linear Regression

## Project Workflow

1. The user logs in to the application.
2. The application generates synthetic traffic data.
3. The `Hour` and `Day` columns are used as input features, and `Traffic_Volume` is the target.
4. The data is split into training and testing sets.
5. A Linear Regression model is trained on the training data.
6. The model predicts traffic volume for the test set.
7. MAE and MSE are calculated to evaluate prediction errors.
8. The dashboard displays a scatter plot comparing actual and predicted values.
9. The user enters an hour (0–23) and a day (0–6) to obtain a traffic-volume prediction and a corresponding traffic-level message.

## Requirements

- Python 3.9 or a compatible version supported by the selected package releases
- pip

## Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

Replace the placeholders with your Git repository URL and project folder name. If you already have the project files locally, open a terminal in the project directory instead.

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Linux or macOS:

```bash
source venv/bin/activate
```

On Windows Command Prompt:

```bat
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install streamlit pandas numpy matplotlib scikit-learn
```

To save the installed package versions for later:

```bash
pip freeze > requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Replace `app.py` with the actual Python filename if yours is different. Streamlit will provide a local URL, usually `http://localhost:8501`, to open in your browser.

## Demo Login

The current source code contains these demonstration credentials:

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `admin123` |

**Security note:** These credentials are hard-coded for demonstration only. Do not use this login implementation as production authentication. For a deployed application, use secure authentication and store secrets outside the source code.

## How to Use

1. Start the Streamlit application.
2. Enter the demo username and password.
3. Review the generated synthetic traffic data.
4. Check the MAE and MSE values in the Model Evaluation section.
5. Review the Actual vs Predicted Traffic Volume scatter plot.
6. Enter an hour from `0` to `23`.
7. Enter a day from `0` to `6`.
8. Read the predicted traffic volume and the displayed traffic-level guidance.
9. Select **Logout** to return to the login page.

### Day Input Convention

The code generates day values from `0` through `6`, but it does not assign weekday names. You can interpret them consistently as:

- `0` — Monday
- `1` — Tuesday
- `2` — Wednesday
- `3` — Thursday
- `4` — Friday
- `5` — Saturday
- `6` — Sunday

This is a suggested convention; the model itself only receives numeric values.

## Traffic-Level Interpretation

The application uses the following rules for its predicted traffic volume:

| Predicted volume | Classification | Dashboard guidance |
|---|---|---|
| Below 100 | Low | Road may be relatively clear |
| 100 to below 150 | Average | Moderate traffic; a slight delay may occur |
| 150 to 190, inclusive | High | Heavy traffic; consider alternatives where appropriate |
| Above 190 | Out of expected range | Displays a warning message |

These thresholds are application-defined demonstration rules, not validated real-world traffic standards.

## Important Limitations

- **Synthetic data:** The application creates random demonstration data instead of using live traffic data or a real-world traffic dataset.
- **Random data on reruns:** The generated records can change when Streamlit reruns the script, so model metrics and predictions may vary.
- **Limited input features:** The model uses only hour and day; it does not account for weather, road conditions, holidays, accidents, or special events.
- **Demonstration accuracy:** MAE and MSE describe errors on the generated test split only. They do not establish real-world forecasting accuracy.
- **Demo authentication:** The login is hard-coded and is not suitable for production security.
- **No live routing:** Traffic guidance is based only on predicted volume; the app does not retrieve live congestion or recommend a verified alternative route.

## Future Enhancements

- Train and evaluate the model using a real traffic dataset.
- Add weather, holiday, road, and event-related features.
- Compare Linear Regression with other regression models.
- Add additional evaluation metrics such as RMSE and R².
- Store traffic records in a database such as MySQL or PostgreSQL.
- Implement secure user authentication.
- Add time-series forecasting and historical trend charts.
- Integrate a live traffic API, if available, for real-time data.

## Project Structure

```text
traffic-volume-forecasting/
├── app.py
├── requirements.txt
└── README.md
```

The structure above is a suggested layout. Adjust the filenames to match your actual project.

## Disclaimer

This project is intended for learning, demonstration, and academic purposes. Predictions are based on synthetic data and should not be used as the sole basis for real-world travel or traffic-management decisions.

## Author

Add your name here.
