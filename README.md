# 🚗 Car Price Predictor

A Machine Learning web application that predicts the resale price of used cars based on various features such as car model, company, fuel type, kilometers driven, and car age.

## 📌 Project Overview

Buying and selling used cars can be challenging because determining the correct resale price is difficult. This project uses Machine Learning to estimate the resale value of a used car based on historical car data.

The application provides an easy-to-use web interface built with Streamlit, where users can enter car details and instantly get an estimated resale price.


## ✨ Features

* Predicts used car prices instantly.
* User-friendly web interface built with Streamlit.
* Supports multiple car brands and models.
* Displays estimated price along with a price range.
* Responsive and attractive UI.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-Learn**
* **Streamlit**
* **Pickle**

---

##  Machine Learning Model

Several regression algorithms were evaluated during experimentation:

* Linear Regression
* Random Forest Regressor
* Gradient Boosting Regressor

After comparing performance metrics, **Random Forest Regressor** was selected as the final model for deployment.

### Model Performance

* **R² Score:** 0.56
* **Mean Absolute Error (MAE):** ₹1.32 Lakh



## Features Used

* Car Name
* Company
* Fuel Type
* Kilometers Driven
* Car Age



## 📁 Project Structure


car_price_prediction/
│
├── app.py
├── style.css
├── requirements.txt
├── car_price_model.pkl
├── Cleaned df.csv
├── car_banner.jpg
├── README.md
```

## 🚀 How to Run Locally

### Clone the repository

git clone https://github.com/tanishkagolya-tech/car_price_prediction.git


### Navigate to project folder

cd car_price_prediction


### Install dependencies

pip install -r requirements.txt


### Run the Streamlit application


streamlit run app.py


## 📸 Application Preview

<img width="809" height="427" alt="image" src="https://github.com/user-attachments/assets/8be4568a-ede6-46f5-b730-6b9def34421e" />



## 🔮 Future Improvements

* Add dynamic car images.
* Improve model accuracy using more data.
* Deploy the application on Streamlit Cloud.
* Add advanced price analysis and visualizations.


## 👩‍💻 Author

**Tanishka Golya**

* GitHub: https://github.com/tanishkagolya-tech
* LinkedIn: https://www.linkedin.com/in/tanishka-golya-8673b232a



⭐ If you found this project useful, consider giving it a star on GitHub.
