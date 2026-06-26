import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
import os

# ======================================
# PAGE CONFIGURATION
# ======================================

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# ======================================
# LOAD CSS
# ======================================

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ======================================
# SIDEBAR
# ======================================

st.sidebar.title("📌 About Project")

st.sidebar.success(
"""
**Model Used:** Random Forest Regressor
"""
)

st.sidebar.markdown("### 📊 Model Performance")

st.sidebar.metric("R² Score", "0.56")
st.sidebar.metric("MAE", "₹1.32 Lakh")

st.sidebar.markdown("### Features Used")

st.sidebar.markdown("""
- 🚘 Car Name
- 🏢 Company
- ⛽ Fuel Type
- 🛣️ Kilometers Driven
- 📅 Car Age
""")

st.sidebar.markdown("### Built Using")

st.sidebar.markdown("""
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
""")

# ======================================
# LOAD MODEL
# ======================================

try:
    with open("car_price_model.pkl", "rb") as file:
        model = pickle.load(file)

except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# ======================================
# LOAD DATASET
# ======================================

try:
    cars = pd.read_csv("Cleaned df.csv")

except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# ======================================
# HEADER IMAGE
# ======================================

if os.path.exists("car_banner.jpg"):
    st.image(
        "car_banner.jpg",
        use_container_width=True
    )

# ======================================
# TITLE
# ======================================

st.markdown(
    "<h1 class='main-title'>🚗 Car Price Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Predict the resale value of your car using Machine Learning</p>",
    unsafe_allow_html=True
)

st.divider()

# ======================================
# USER INPUTS
# ======================================

company = st.selectbox(
    "🏢 Select Company",
    sorted(cars["company"].dropna().unique())
)

name = st.selectbox(
    "🚘 Select Car Model",
    sorted(
        cars[cars["company"] == company]["name"].dropna().unique()
    )
)

year = st.number_input(
    "📅 Manufacturing Year",
    min_value=1990,
    max_value=datetime.now().year,
    value=2018
)

kms = st.number_input(
    "🛣️ Kilometers Driven",
    min_value=0,
    value=40000
)

fuel = st.selectbox(
    "⛽ Fuel Type",
    sorted(cars["fuel_type"].dropna().unique())
)

# ======================================
# PREDICTION
# ======================================

if st.button("🔍 Predict Price"):

    car_age = datetime.now().year - year

    input_df = pd.DataFrame(
        [[
            name,
            company,
            kms,
            fuel,
            car_age
        ]],
        columns=[
            "name",
            "company",
            "kms_driven",
            "fuel_type",
            "car_age"
        ]
    )

    try:

        prediction = model.predict(input_df)[0]

        # Avoid negative predictions
        prediction = max(prediction, 0)

        st.success("Prediction Generated Successfully!")

        # ==========================
        # VEHICLE DETAILS
        # ==========================

        st.subheader("🚘 Vehicle Details")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Car Model:** {name}")
            st.write(f"**Company:** {company}")
            st.write(f"**Fuel Type:** {fuel}")

        with col2:
            st.write(f"**Year:** {year}")
            st.write(f"**KM Driven:** {kms:,}")
            st.write(f"**Car Age:** {car_age} Years")

        st.divider()

        # ==========================
        # PRICE DISPLAY
        # ==========================

        prediction_lakh = prediction / 100000

        st.metric(
            "💰 Estimated Resale Value",
            f"₹ {prediction_lakh:.2f} Lakhs"
        )

        st.caption(
            f"Approximate Amount: ₹ {prediction:,.0f}"
        )

        # ==========================
        # PRICE RANGE
        # ==========================

        lower = prediction * 0.9
        upper = prediction * 1.1

        lower_lakh = lower / 100000
        upper_lakh = upper / 100000

        st.info(
            f"""
📊 **Estimated Price Range**

₹ {lower_lakh:.2f} Lakhs - ₹ {upper_lakh:.2f} Lakhs
"""
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# ======================================
# DISCLAIMER
# ======================================

st.warning(
"""
⚠️ **Disclaimer**

Predicted prices are estimates generated using a Machine Learning model trained on historical data.

Actual market prices may vary depending on:

- Vehicle condition
- Ownership history
- Accident history
- Service records
- Location

Please use these predictions as indicative values only.
"""
)

# ======================================
# FOOTER
# ======================================

st.divider()

st.caption(
    "🚗 Developed by Tanishka | Built with Streamlit, Scikit-Learn & Random Forest"
)

st.markdown("""
### 🔗 Connect

- GitHub: [tanishkagolya-tech](https://github.com/tanishkagolya-tech)

- LinkedIn: [Tanishka Golya](https://www.linkedin.com/in/tanishka-golya-8673b232a)
""")