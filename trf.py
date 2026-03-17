import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# -------------------------------
# Login Credentials (Demo)
# -------------------------------
USERNAME = "admin"
PASSWORD = "admin123"

def safe_rerun():
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()

# -------------------------------
# Session State
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------------
# Login Page
# -------------------------------
def login_page():
    st.title("🔐 Login Page")
    st.write("🚦 Traffic Volume Forecasting System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login Successful ✅")
            safe_rerun()
        else:
            st.error("Invalid Username or Password ❌")

# -------------------------------
# Main Application
# -------------------------------
def main_app():
    st.title("🚦 Traffic Volume Forecasting Dashboard")

    if st.button("Logout"):
        st.session_state.logged_in = False
        safe_rerun()

    # -------------------------------
    # Synthetic Data Generation
    # -------------------------------
    st.header("1️⃣ Synthetic Traffic Data")

    hours = np.arange(0, 24)
    days = np.random.randint(0, 7, 240)

    traffic_volume = (
        120
        + 30 * np.sin(np.tile(hours, 10))
        + np.random.randint(0, 40, 240)
    )

    data = pd.DataFrame({
        "Hour": np.tile(hours, 10),
        "Day": days,
        "Traffic_Volume": traffic_volume
    })

    st.dataframe(data.head(10))

    # -------------------------------
    # Preprocessing
    # -------------------------------
    X = data[["Hour", "Day"]]
    y = data["Traffic_Volume"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -------------------------------
    # Model Training
    # -------------------------------
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # -------------------------------
    # Model Evaluation
    # -------------------------------
    st.header("2️⃣ Model Evaluation")

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    st.write(f"**Mean Absolute Error (MAE):** {mae:.2f}")
    st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")

    # -------------------------------
    # Visualization
    # -------------------------------
    st.header("3️⃣ Visualization")

    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.set_xlabel("Actual Traffic Volume")
    ax.set_ylabel("Predicted Traffic Volume")
    ax.set_title("Actual vs Predicted Traffic Volume")

    st.pyplot(fig)

    # -------------------------------
    # User Prediction
    # -------------------------------
    st.header("4️⃣ Predict Traffic Volume")

    hour_input = st.number_input("Enter Hour (0–23)", min_value=0, max_value=23, value=8)
    day_input = st.number_input("Enter Day (0–6)", min_value=0, max_value=6, value=1)

    input_data = pd.DataFrame({
        "Hour": [hour_input],
        "Day": [day_input]
    })

    prediction = model.predict(input_data)
    predicted_value = int(round(prediction[0]))

    st.success(f"🚗 Predicted Traffic Volume: {predicted_value}")

    # Traffic Level Classification
    if predicted_value < 100:
        #st.info("🟢 Traffic Level: LOW (Below 100 vehicles)")
        st.info(
    "🟢 Traffic Level: LOW → Road is clear and traffic is smooth.\n\n"
    "You can continue on this route without any delay.\n\n"
    "HAPPY JOURNEY 🚗✨"
)
    elif 100 <= predicted_value < 150:
        #st.info("🟡 Traffic Level: AVERAGE (100–150 vehicles)")
        st.info(
    "🟡 Traffic Level: AVERAGE → Moderate traffic on this route.\n\n"
    "You may continue, but expect a slight delay.\n\n"
    "Drive safely and have a pleasant journey 😊"
)
    elif 150 <= predicted_value <= 190:
        #st.warning("🔴 Traffic Level: HIGH (150–190 vehicles)")
        st.warning(
    "🔴 Traffic Level: HIGH → Heavy traffic detected on this route.\n\n"
    "Consider choosing an alternative route to save time,\n"
    "or remain patient until traffic clears.\n\n"
    "Thank you for your patience 👍"
)
    else:
        st.error("🚨 Traffic volume exceeds expected range!")

# -------------------------------
# App Controller
# -------------------------------
if st.session_state.logged_in:
    main_app()
else:
    login_page()
