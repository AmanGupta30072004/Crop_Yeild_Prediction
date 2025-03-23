# Crop Yield Prediction
![Dashboard](images/image.png)

## 📌 Overview
This project predicts crop yield based on factors such as rainfall, pesticide usage, temperature, and geographical region. The model helps in making informed agricultural decisions by analyzing historical data and forecasting future yields.

## 📂 Dataset
The dataset consists of agricultural data with the following key columns:
- **Year** – Year of observation
- **average_rain_fall_mm_per_year** – Average annual rainfall (in mm)
- **pesticides_tonnes** – Amount of pesticides used (in tonnes)
- **avg_temp** – Average annual temperature (in °C)
- **Area** – Geographical region (Country)
- **Item** – Type of crop
- **Yield** – Crop yield in tons per hectare (Target variable)

## 🔍 Data Preprocessing
- **Handling Categorical Data**: Used `OneHotEncoder` to convert categorical features (`Area` and `Item`) into numerical format.
- **Feature Scaling**: Applied `StandardScaler` to normalize numerical features (`Year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, `avg_temp`).
- **Train-Test Split**: Data was split into training (80%) and testing (20%) sets.

## 📊 Models Used
### 1️⃣ Decision Tree Regressor (DTR)
- **Algorithm**: A tree-based model that splits data at different feature values to predict the target variable.
- **Advantages**: Handles non-linearity and works well with categorical data.

## 🎯 Model Evaluation
- **Mean Absolute Error (MAE)**: Measures average absolute errors between predicted and actual values.
- **Root Mean Squared Error (RMSE)**: Evaluates model performance by penalizing large errors.
- **R² Score**: Measures how well the model explains the variance in the target variable.

## 🚀 Deployment with Streamlit
The trained model is deployed as a web application using **Streamlit**.
- Users input features (Year, rainfall, temperature, etc.).
- The model processes the data and predicts crop yield.
- Displays results dynamically on the web app.

## 🛠 How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/AmanGupta30072004/Crop_Yeild_Prediction.git
   cd Crop_Yeild_Prediction
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## 📌 Future Improvements
- Implement more advanced models like Random Forest, XGBoost, or Neural Networks.
- Collect more diverse datasets for better generalization.
- Add interactive visualizations for better analysis.

---
**Author:** Aman Gupta 🚀
