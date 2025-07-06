# celebeltech-internship

### Mini Project Added 
# 🖋️ MNIST-to-Delta Lake Pipeline

A Python-based pipeline that downloads the original [MNIST dataset](http://yann.lecun.com/exdb/mnist/), converts images to PNG format, and stores them in a **Delta Lake table** using **Apache Spark**.

This project demonstrates:
- Downloading and parsing raw MNIST `.gz` files.
- Converting image data to PNGs.
- Using PySpark and Delta Lake for structured data storage with ACID guarantees.

---

## 🧩 Project Structure

```
Mini Project/
│
├── main.py                 # Entry point of the pipeline  
├── config.py               # Configuration constants (paths, URLs)
├── downloader.py           # Downloads and parses MNIST data
├── spark_utils.py          # Creates Spark session with Delta support
├── data_processor.py       # Loads and processes MNIST data
├── get_mnist.py            # Parses MNIST binary files
├── utils.py                # Helper functions
├── flat_files/mnist_png/   # Folder containing generated PNG images
└── artifacts/              # Output directory for Delta tables
```

---

## 🔧 Prerequisites

Before running this project, ensure you have:

- ✅ **Python 3.8+**
- ✅ **Virtual Environment** (recommended)
- ✅ **Java Development Kit (JDK)** installed (Recommended: **JDK 11**)
- ✅ Installed Python packages:

```bash
pip install pyspark delta-spark numpy pillow requests
```

⚠️ **Mac M1/M2 users**: Some issues may occur with JDK 17+. Use JDK 11 if possible.

---

## 🛠️ How It Works

### 1. 📥 Downloading MNIST Data

The pipeline uses a GitHub mirror to download the official MNIST `.gz` files:

- Training images and labels  
- Test images and labels  

These are parsed manually without relying on third-party libraries like `python-mnist`.

---

### 2. 🖼️ Converting Images to PNG

Each image is:

- Converted from raw byte data to NumPy arrays
- Reshaped to 28x28 pixels
- Saved as grayscale PNG files in labeled folders (0, 1, ..., 9)

---

### 3. 📊 Creating Delta Lake Table

Using Apache Spark:

- The PNG file paths and corresponding labels are loaded into a DataFrame.
- Images are read as binary using a Pandas UDF.
- A managed Delta Lake table is created to store the binary image data along with labels.

This allows future use in ML pipelines or analytics workflows with full versioning and schema enforcement.

---

## ▶️ Running the Project

### Step 1: Set Up Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 2: Install Dependencies

```bash
pip install pyspark delta-spark numpy pillow requests
```

---

### Step 3: Run the Pipeline

Use the following command to ensure Delta dependencies are passed correctly:

```bash
PYSPARK_SUBMIT_ARGS="--packages io.delta:delta-core_2.12:2.4.0" python3 main.py
```

This ensures the Delta Lake package is available at runtime.

---

## 📤 Output

After successful execution:

- PNG images will be saved under `flat_files/mnist_png/`
- A managed Delta Lake table named `mnist_images_delta` will be created.
- You’ll see output showing the table schema like:

```
+-------------+-----------+
| col_name    | data_type |
+-------------+-----------+
| image_binary| binary    |
| label       | string    |
+-------------+-----------+
```

---

## 📈 Next Steps

✅ Convert all 70,000 MNIST images instead of just a sample  
🖥️ Visualize some of the generated PNG images using Matplotlib or PIL  
☁️ Upload the Delta table to cloud storage (e.g., AWS S3, Google Cloud Storage)  
🐳 Package the entire workflow into a Docker container  
💻 Turn it into a CLI tool (`mnist-to-delta`)  

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project, feel free to open an issue or submit a pull request.

---

## 📬 Contact

For questions or collaboration opportunities, reach out:

- LinkedIn: [Dheeraj Joshi](https://www.linkedin.com/in/dheeraj-joshi-311704203)
- Email: [dlovej009@gmail.com]

---

## 🚀 Acknowledgments

- MNIST Dataset: Yann LeCun et al.  
- Delta Lake: [delta.io](https://delta.io)  
- Spark Community: [spark.apache.org](https://spark.apache.org)

---
