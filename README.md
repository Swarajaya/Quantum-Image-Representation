 Quantum Image Representation: A Comparative Study with Hybrid Adaptive Encoding (HA-QIR)

This repository contains the complete implementation and experimental setup for the research project **"Quantum Image Representation: A Comparative Study with Hybrid Adaptive Encoding (HA-QIR)"**.

The work presents a comparative evaluation of multiple quantum image representation techniques and proposes a novel hybrid framework designed for efficient and scalable quantum image encoding under NISQ-era constraints.

---

## 📌 Project Overview

Quantum image representation plays a crucial role in quantum image processing, enabling classical images to be encoded into quantum states for further quantum operations. Existing methods often suffer from high qubit requirements, increased circuit depth, or loss of image fidelity.

This project:
- Implements and compares classical quantum image representation techniques.
- Introduces **HA-QIR**, a Hybrid Adaptive Quantum Image Representation framework.
- Evaluates performance using real-world datasets under identical experimental conditions.

---

## 🧠 Implemented Quantum Image Representation Techniques

The following quantum image representation models are implemented and evaluated:

- **FRQI (Flexible Representation of Quantum Images)**
- **NEQR (Novel Enhanced Quantum Representation)**
- **MCQI (Multi-Channel Quantum Image Representation)**
- **QRAM-based Encoding**
- **Amplitude Encoding**
- **Proposed HA-QIR (Hybrid Adaptive Quantum Image Representation)**

---

## 🧩 Proposed Method: HA-QIR

HA-QIR is a hybrid encoding framework that:
- Separates images into **Region of Interest (ROI)** and background.
- Applies **MCQI encoding** to ROI for high-fidelity representation.
- Uses **amplitude encoding** for background regions to reduce qubit and circuit overhead.
- Combines both representations using adaptive weighted superposition.

This approach achieves an improved trade-off between accuracy, scalability, and quantum resource utilization.

---

## 📊 Datasets Used

Only datasets actually used in this project are included:

- **MNIST** – handwritten digit images
- **Brain Tumor MRI Dataset**
- **SAR Earth Data**
- **SAR Iceye Dataset**
- **SAR Ship Detection Dataset (SSDD)**

All datasets were used strictly for **representation and simulation purposes**, not for classical learning or classification.

---

## 🧪 Experimental Setup

- Programming Language: **Python**
- Quantum Framework: **Qiskit**
- Image Processing: **NumPy, OpenCV, Matplotlib**
- Execution Environment: **Quantum simulators (NISQ-compatible)**
- Image Preprocessing:
  - Grayscale conversion
  - Fixed \(N \times N\) resizing
  - Pixel normalization

All methods were evaluated under identical conditions to ensure fair comparison.

---

## 📈 Evaluation Metrics

- Qubit count
- Quantum circuit depth
- Encoding fidelity
- Scalability
- Resource efficiency

---

## 📁 Repository Structure

├── data/ # Datasets used in the study
├── outputs/ # Generated quantum states and visualizations
├── src/ # Source code for all encoding techniques
│ ├── frqi.py
│ ├── neqr.py
│ ├── mcqi.py
│ ├── amplitude.py
│ ├── haqir.py
├── results/ # Experimental results and analysis
├── requirements.txt # Required Python dependencies
└── README.md

yaml
Copy code

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/USERNAME/quantum-image-representation-haqir.git
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run desired encoding script from src/.

📜 License
This project is intended for academic and research purposes.

