# 🚗 Car Purchasing Data Analysis

A data analytics & predictive modeling project for car purchase data to help sellers and buyers make informed decisions about car pricing and features.

---

## 📌 Project Description

This project explores the dataset of used car sales (or car buying habits) to:
- Understand major factors affecting car prices  
- Build predictive models to estimate car sale price  
- Visualize key relationships (e.g. mileage vs price, age vs price)  

---

## 📂 Repository Structure

```
Car-Purchasing-Data/
│
├── data/          
├── notebooks/     
├── src/           
├── models/        
├── images/        
├── output/        
├── requirements.txt
└── README.md
```

---

## 📊 Data Description

- **Source**: (e.g. CSV from Kaggle or private dataset)  
- **Main Columns**:
  - `price`
  - `make`
  - `model`
  - `year`
  - `mileage`
  - `condition`
  - `fuel_type`

---

## 🔎 Exploratory Data Analysis (EDA)

In `notebooks/EDA.ipynb`:
- Handle missing & duplicate values  
- Analyze distributions (histograms)  
- Relationships between variables (scatter plots)  
- Heatmap for correlations  

📷 Example plot:  
![Mileage vs Price](./images/mileage_price.png)

---

## 🤖 Predictive Modeling

- Models used: **Linear Regression**, **Random Forest**, **XGBoost**  
- Best model: **Random Forest**  
- Performance:
  - **MAE**: 1500  
  - **RMSE**: 2500  
  - **R² Score**: 0.78  

---

## 🧪 How to Run

```bash
# clone repo
git clone https://github.com/Omayma-ali/Car-Purchasing-Data.git
cd Car-Purchasing-Data

# install dependencies
pip install -r requirements.txt

# run notebook or script
jupyter notebook notebooks/EDA.ipynb
python src/train_model.py
```

---

## 📂 Project Structure Explained

- `data/`: raw & cleaned datasets  
- `notebooks/`: Jupyter notebooks for EDA & experiments  
- `src/`: training, prediction scripts  
- `models/`: saved models  
- `images/`: plots, screenshots  
- `output/`: reports & results  
- `requirements.txt`: dependencies list  
- `README.md`: documentation  

---

## 🔮 Future Work

- Try advanced models (Gradient Boosting, Neural Networks)  
- Add classification task (e.g., High / Medium / Low price category)  


---

## 👩‍💻 Author / Contact

**Omayma Ali** — Data Analyst / Data Scientist  
- [GitHub](https://github.com/Omayma-ali)
- [LinkedIn](www.linkedin.com/in/omayma-ali)  
- [Fiverr](https://www.fiverr.com/users/omaymaaa)
- [Khamsat](https://khamsat.com/user/omayma_ali) 
