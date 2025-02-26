# Indian Restaurant Ratings Map

## 📌 Project Overview
This project visualizes the **top-rated restaurants in India** on an interactive map using **Folium**. The map categorizes restaurants based on their ratings:

- **🟢 High Rating (4.0 - 5.0)** → Green markers
- **🟡 Medium Rating (2.5 - 3.9)** → Yellow markers
- **🔴 Low Rating (0 - 2.4)** → Red markers

The top **20 restaurants** from each category are displayed on the map.

---

## 📂 Dataset
The dataset should contain:
- **Latitude & Longitude** of restaurants
- **Aggregate rating** of restaurants
- **Country Code** (India = `1`)

---

## ⚙️ Installation
Make sure you have Python installed. Then, install the required libraries:

```bash
pip install pandas folium
```

---

## 🚀 Usage
1. Clone this repository:
```bash
git clone https://github.com/yourusername/restaurant-map-india.git
cd restaurant-map-india
```

2. Run the script:
```bash
python restaurant_map.py
```

3. The map will be generated and saved as an HTML file or displayed in a Jupyter Notebook.

---

## 🗺️ How It Works
1. **Filters Indian restaurants** (`Country Code = 1`).
2. **Removes unrated restaurants** (`Aggregate rating > 0`).
3. **Selects top 20 restaurants** in each rating category (High, Medium, Low).
4. **Pins them on an interactive Folium map** with color-coded markers.
5. **Click on a marker** to see the restaurant name and rating.

---

## 📜 License
This project is open-source and available under the MIT License.

---

## 🔗 Author
Developed by Gopi. Contributions are welcome!

