# 🌦️ Weather Data Analysis Application – Python Tkinter Mini Project  

## 🧠 Project Overview  
A comprehensive **Weather Data Analysis Application** built using **Python 🐍 Tkinter** for GUI and **Pandas 🧮** for data analysis.  
Easily **load weather data**, visualize **temperature trends 🌡️**, and perform **statistical analysis 📊** — all in one place!  

---

## ✨ Features  

### 🗂️ 1. Data Management  
📁 Load data from CSV files  
🧾 Display in an interactive table (first 100 rows)  
📂 File dialog for easy file selection  
⚡ Handles large datasets smoothly  

### 📊 2. Statistical Analysis  
📈 Complete summary of weather parameters  
🔥 Identify hottest & ❄️ coldest days  
🌧️ Total and average rainfall  
💨 Wind speed analysis  
☁️ Weather condition frequency distribution  

### 🌈 3. Data Visualization  
📅 **Temperature Trend** – Line chart with date axis  
🌧️ **Rainfall Analysis** – Bar chart for daily rainfall  
🌤️ **Weather Conditions** – Pie chart of conditions  
🧮 **Correlation Matrix** – Heatmap of relationships  

### 💻 4. User Interface  
🎨 Modern Tkinter GUI  
🎛️ Color-coded buttons for actions  
📊 Split layout for table & chart views  
🟢 Status bar for messages  

---

## ⚙️ Requirements  

### 📦 Python Libraries  
```
tkinter  # built-in
pandas
matplotlib
numpy
```

### 🧰 Installation  
```bash
pip install pandas matplotlib numpy
```

---

## 📁 Project Structure  
```
weather-data-analysis/
│
├── weather_analysis_app.py     # 🖥️ Main application
├── weather_data.csv            # 🌤️ Sample dataset
└── README.md                   # 📘 Documentation
```

---

## ▶️ How to Run  

1. 📂 Place all files in one folder  
2. ⚙️ Install dependencies:  
   ```bash
   pip install pandas matplotlib numpy
   ```  
3. ▶️ Run the app:  
   ```bash
   python weather_analysis_app.py
   ```  
4. 🖱️ Use buttons to:  
   - 📁 Load CSV File  
   - 📊 Show Statistics  
   - 🌡️ Temperature Trend  
   - 🌧️ Rainfall Analysis  
   - ☁️ Weather Conditions  
   - 🧮 Correlation Matrix  

---

## 🧾 Dataset Format  

| 📅 Column Name | 🔢 Type | 📝 Description |
|----------------|---------|----------------|
| Date | String | Date in YYYY-MM-DD format |
| Temperature_C | Float | Temperature in °C |
| Humidity_% | Float | Humidity percentage |
| Wind_Speed_kmh | Float | Wind speed (km/h) |
| Pressure_hPa | Float | Atmospheric pressure |
| Visibility_km | Float | Visibility (km) |
| Rainfall_mm | Float | Rainfall (mm) |
| Weather_Condition | String | Weather description |

---

## 📊 Key Functionalities  

✅ **Load CSV File** – Select, validate, and display data  
✅ **Show Statistics** – Summary with key insights  
✅ **Visual Charts** – Explore patterns interactively  
✅ **Correlation Matrix** – Understand parameter relationships  

---

## 🧰 Technical Stack  

🔹 **GUI Framework:** Tkinter  
🔹 **Data Analysis:** Pandas, NumPy  
🔹 **Visualization:** Matplotlib  
🔹 **Chart Embedding:** FigureCanvasTkAgg  
🔹 **Primary Color:** #2c3e50 (Dark Blue-Gray)  

---

## 🧱 Error Handling  

⚠️ Handles:  
- 🚫 Missing or invalid CSV files  
- 📄 Empty datasets  
- ❌ Wrong file types  
- 🔒 Permission errors  
- 🧮 Type mismatches  

---

## 🧩 Customization  

🎨 **Add New Charts:**  
1️⃣ Create a new Tkinter button  
2️⃣ Add a plotting function  
3️⃣ Use `clear_canvas()` before embedding a new chart  

🌈 **Change Colors:**  
Modify button, chart, or background color settings directly in the code!  

---

## 🎓 Learning Outcomes  

📚 You’ll learn:  
1. 🖥️ GUI development with Tkinter  
2. 🧮 Data analysis using Pandas  
3. 📊 Visualization using Matplotlib  
4. 💾 File handling (CSV import/export)  
5. 🚨 Exception handling  
6. 🧱 Object-oriented design principles  
7. 🔗 Integration of multiple libraries  

---

## 🔮 Future Enhancements  

🚀 Planned updates:  
- 🧾 Export reports to PDF  
- 🗓️ Filter data by date range  
- 🔁 Compare multiple datasets  
- 📈 Forecasting trends  
- 🖼️ Save charts as images  
- 💽 Database integration  
- ☁️ Real-time weather API  

---

## 🧩 Troubleshooting  

| ⚠️ Issue | 💡 Solution |
|----------|--------------|
| "File not found" | Ensure CSV is in the same folder |
| "Module not found" | Run `pip install pandas matplotlib numpy` |
| Charts not displaying | Check if `matplotlib` is installed |
| App not starting | Use Python 3.6+ and verify Tkinter installation |

---

## 👨‍💻 Author Information  

**👤 Name:** Arpit Soni  
**🎓 Class:** MCA (Data Science)  
**🏷️ UID:** 25MCD10053  
**📚 Course:** Advanced Python Mini Project  

---

## 📜 License  

🆓 This project is free to use and modify for educational purposes.  
Created with ❤️ for learning **Python + Data Analysis + GUI Development**.  

---

✨ *“Turning data into insights, one chart at a time!”* 🌦️📊  
