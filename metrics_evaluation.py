import time
import cv2
import numpy as np
from qiskit import QuantumCircuit

# ==========================
# DATASET PATHS
# ==========================
DATASETS = {
    "brain_tumor": "data/brain_tumor/img1.png",
    "nist": "data/nist/img1.png",
    "sar_earthdata": "data/sar_earthdata/img1.png",
    "sar_iceye": "data/sar_iceye/img1.png",
    "ssdd_ship": "data/ssdd_ship/img1.png",
}

# ==========================
# IMAGE PREPROCESSING
# ==========================
def preprocess_image(path, rgb=False):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {path}")

    if not rgb:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.resize(img, (2, 2))
    img = img / 255.0
    return img

# ==========================
# QRAM CIRCUIT
# ==========================
def build_qram(image):
    pixels = image.flatten()
    qc = QuantumCircuit(3)

    for i, v in enumerate(pixels):
        b = format(i, "02b")
        if b[0] == "1": qc.x(0)
        if b[1] == "1": qc.x(1)
        qc.ry(2 * np.arcsin(v), 2)
        if b[0] == "1": qc.x(0)
        if b[1] == "1": qc.x(1)

    return qc

# ==========================
# MCQI CIRCUIT
# ==========================
def build_mcqi(image):
    r, g, b = image[0, 0]
    qc = QuantumCircuit(3)
    qc.ry(2 * np.arcsin(r), 0)
    qc.ry(2 * np.arcsin(g), 1)
    qc.ry(2 * np.arcsin(b), 2)
    return qc

# ==========================
# AMPLITUDE ENCODING CIRCUIT
# ==========================
def build_amplitude(image):
    vec = image.flatten()
    vec = vec / np.linalg.norm(vec)
    qc = QuantumCircuit(2)
    qc.initialize(vec, [0, 1])
    return qc

# ==========================
# METRICS EVALUATION
# ==========================
print("\nMETRICS EVALUATION (2x2 Image)\n")

for name, path in DATASETS.items():
    gray = preprocess_image(path)
    rgb = preprocess_image(path, rgb=True)

    # ---- QRAM ----
    start = time.time()
    qram_circuit = build_qram(gray)
    qram_time = time.time() - start

    # ---- MCQI ----
    start = time.time()
    mcqi_circuit = build_mcqi(rgb)
    mcqi_time = time.time() - start

    # ---- Amplitude ----
    start = time.time()
    amp_circuit = build_amplitude(gray)
    amp_time = time.time() - start

    print(f"Dataset: {name}")
    print(" QRAM      | Qubits:", qram_circuit.num_qubits,
          "| Gates:", qram_circuit.size(),
          "| Depth:", qram_circuit.depth(),
          "| Time:", round(qram_time, 6), "s")

    print(" MCQI      | Qubits:", mcqi_circuit.num_qubits,
          "| Gates:", mcqi_circuit.size(),
          "| Depth:", mcqi_circuit.depth(),
          "| Time:", round(mcqi_time, 6), "s")

    print(" Amplitude | Qubits:", amp_circuit.num_qubits,
          "| Gates:", amp_circuit.size(),
          "| Depth:", amp_circuit.depth(),
          "| Time:", round(amp_time, 6), "s")
    print("-" * 60)

print("Metrics evaluation completed.")
