import os
import cv2
import numpy as np
from math import pi
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import circuit_drawer

# ===============================
# CONFIG
# ===============================
DATASETS = {
    "brain_tumor": "data/brain_tumor/img1.png",
    "nist": "data/nist/img1.png",
    "sar_iceye": "data/sar_iceye/img1.png",
    "sar_earthdata": "data/sar_earthdata/img1.png",
    "ssdd_ship": "data/ssdd_ship/img1.png",
}

IMAGE_SIZE = 2  # 2x2 image (mandatory for quantum feasibility)

os.makedirs("outputs", exist_ok=True)

# ===============================
# IMAGE PREPROCESSING
# ===============================
def load_and_preprocess(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None

    img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
    img = img / 255.0  # normalize [0,1]
    return img

# ===============================
# FRQI IMPLEMENTATION
# ===============================
def frqi_circuit(image):
    n_pixels = IMAGE_SIZE * IMAGE_SIZE
    n_pos_qubits = int(np.log2(n_pixels))
    qc = QuantumCircuit(n_pos_qubits + 1)

    # Superposition of position qubits
    for i in range(n_pos_qubits):
        qc.h(i)

    pixel_values = image.flatten()

    for idx, intensity in enumerate(pixel_values):
        angle = intensity * pi
        bin_idx = format(idx, f'0{n_pos_qubits}b')

        for q, bit in enumerate(bin_idx):
            if bit == '0':
                qc.x(q)

        qc.mcry(angle, list(range(n_pos_qubits)), n_pos_qubits)

        for q, bit in enumerate(bin_idx):
            if bit == '0':
                qc.x(q)

    return qc

# ===============================
# NEQR (SIMPLIFIED VERSION)
# ===============================
def neqr_circuit(image):
    n_pixels = IMAGE_SIZE * IMAGE_SIZE
    n_pos_qubits = int(np.log2(n_pixels))
    n_intensity_qubits = 2  # simplified intensity bits

    qc = QuantumCircuit(n_pos_qubits + n_intensity_qubits)

    for i in range(n_pos_qubits):
        qc.h(i)

    pixel_values = (image.flatten() * 3).astype(int)

    for idx, val in enumerate(pixel_values):
        bin_idx = format(idx, f'0{n_pos_qubits}b')

        for q, bit in enumerate(bin_idx):
            if bit == '0':
                qc.x(q)

        for bit in range(n_intensity_qubits):
            if (val >> bit) & 1:
                qc.mcx(list(range(n_pos_qubits)), n_pos_qubits + bit)

        for q, bit in enumerate(bin_idx):
            if bit == '0':
                qc.x(q)

    return qc

# ===============================
# MAIN PIPELINE
# ===============================
simulator = AerSimulator()

with open("outputs/output.txt", "w") as f:
    for name, path in DATASETS.items():
        print(f"Processing dataset: {name}")

        img = load_and_preprocess(path)
        if img is None:
            print(f"Image not found for {name}")
            f.write(f"{name}: Image not found\n")
            continue

        # ---- FRQI ----
        frqi = frqi_circuit(img)
        frqi_result = simulator.run(frqi).result()

        circuit_drawer(
            frqi,
            output="mpl",
            filename=f"outputs/frqi_{name}.png"
        )

        # ---- NEQR ----
        neqr = neqr_circuit(img)
        neqr_result = simulator.run(neqr).result()

        circuit_drawer(
            neqr,
            output="mpl",
            filename=f"outputs/neqr_{name}.png"
        )

        f.write(f"{name}:\n")
        f.write(f"  FRQI depth: {frqi.depth()}\n")
        f.write(f"  FRQI qubits: {frqi.num_qubits}\n")
        f.write(f"  NEQR depth: {neqr.depth()}\n")
        f.write(f"  NEQR qubits: {neqr.num_qubits}\n\n")

print("All datasets processed successfully.")
