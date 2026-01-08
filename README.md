Quantum Image Representation – Comparative Study and Hybrid HA-QIR
📌 Project Overview

This project presents a comparative experimental study of quantum image representation techniques and proposes a novel Hybrid Adaptive Quantum Image Representation (HA-QIR) method. The study evaluates how different quantum encoding schemes represent classical images in quantum states under limited quantum resources.

The work focuses on resource efficiency, scalability, and information preservation, which are critical challenges in near-term quantum image processing.

🧠 Key Objectives

Implement and analyze major Quantum Image Representation (QIR) models

Compare models using quantum resource metrics

Perform basic quantum image operations

Propose a novel hybrid encoding strategy (HA-QIR) to balance fidelity and efficiency

🔬 Quantum Image Representation Models Implemented

The following models are implemented and evaluated:

FRQI (Flexible Representation of Quantum Images)

Encodes pixel intensity using rotation angles

Simple but probabilistic and less scalable

NEQR (Novel Enhanced Quantum Representation)

Encodes pixel values directly into basis states

Exact representation with higher qubit cost

MCQI (Multi-Channel Quantum Image Representation)

Supports RGB images

Efficient balance between fidelity and resources

QRAM-based Encoding

Uses quantum random access memory concepts

Enables fast pixel access

Amplitude Encoding

Extremely low qubit usage

Suffers from information loss and scalability issues

🚀 Proposed Novel Method: HA-QIR

Hybrid Adaptive Quantum Image Representation (HA-QIR) combines strengths of multiple encodings:

Region of Interest (ROI) → MCQI (high fidelity)

Background regions → Amplitude Encoding (low qubits)

Position information → QRAM-style indexing

This adaptive strategy:

Reduces qubit count

Lowers circuit depth

Preserves important image features

📊 Datasets Used

Representative samples from the following public benchmark datasets were used:

Brain Tumor MRI Dataset (medical imaging)

MNIST (handwritten digits)

SAR Earth Observation Dataset

ICEYE SAR Dataset

SSDD (SAR Ship Detection Dataset)

Note: Images were resized to small dimensions (e.g., 2×2, 4×4) to ensure quantum simulation feasibility.

🧪 Experimental Setup

Programming Language: Python

Quantum Framework: Qiskit

Execution: Classical quantum simulator

Preprocessing: Grayscale conversion, normalization, resizing

📈 Evaluation Metrics

Each model is evaluated using:

Qubit requirements

Encoding execution time

Gate count

Circuit depth

Scalability

Information loss

🧩 Quantum Image Operations Performed

After encoding, the following quantum image operations are demonstrated:

Quantum Geometric Transformations (rotation, coordinate mapping)

Quantum Image Flipping (horizontal and vertical)

Quantum Image Filtering (basic interference-based filtering)

📂 Project Structure (Suggested)
Quantum-Image-Representation/
│
├── data/                 # Sample images (datasets)
├── circuits/             # Quantum circuit implementations
├── models/               # FRQI, NEQR, MCQI, QRAM, Amplitude
├── ha_qir/               # Proposed HA-QIR implementation
├── results/              # Output images and plots
├── paper/                # Research paper (IEEE format)
└── README.md

📌 Key Contributions

Comprehensive comparison of five quantum image representation techniques

Experimental evaluation across multiple datasets

Proposal of a resource-aware hybrid encoding strategy

Demonstration of quantum image operations

Suitable for near-term (NISQ) quantum devices

🧪 Current Status

✅ Implementations completed

✅ Comparative analysis performed

✅ Novel technique proposed

✅ Research paper draft prepared

🔄 Extension possible to real quantum hardware

📄 Publication

This work is prepared as a research paper suitable for:

arXiv (free preprint)

IEEE / Springer / ACM conferences (subject to submission)

👤 Author

Swarajaya Singh Sawant
Department of Artificial Intelligence and Machine Learning
COER University
📧 Email: swarajayasawant19@gmail.com
Minor update to documentation


🏷️ Keywords


Quantum Image Processing, FRQI, NEQR, MCQI, QRAM, Amplitude Encoding, Hybrid Quantum Models, HA-QIR
