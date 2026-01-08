import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit

# ==============================
# DATASET PATHS (MATCH YOUR DATA FOLDER)
# ==============================
DATASETS = {
    "brain_tumor": "data/brain_tumor/img1.png",
    "nist": "data/nist/img1.png",
    "sar_earthdata": "data/sar_earthdata/img1.png",
    "sar_iceye": "data/sar_iceye/img1.png",
    "ssdd_ship": "data/ssdd_ship/img1.png",
}

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================
# IMAGE PREPROCESSING
# ==============================
def preprocess_image(path, rgb=False):
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(f"[ERROR] Image not found at: {path}")

    if not rgb:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.resize(img, (2, 2))
    img = img / 255.0
    return img

# ==============================
# QRAM ENCODING
# ==============================
def qram_encode(image, dataset_name):
    pixels = image.flatten()
    qc = QuantumCircuit(3)

    for idx, value in enumerate(pixels):
        binary = format(idx, "02b")

        if binary[0] == "1":
            qc.x(0)
        if binary[1] == "1":
            qc.x(1)

        qc.ry(2 * np.arcsin(value), 2)

        if binary[0] == "1":
            qc.x(0)
        if binary[1] == "1":
            qc.x(1)

    qc.draw("mpl")
    plt.savefig(f"{OUTPUT_DIR}/qram_{dataset_name}.png")
    plt.close()

# ==============================
# MCQI ENCODING
# ==============================
def mcqi_encode(image, dataset_name):
    r, g, b = image[0, 0]

    qc = QuantumCircuit(3)
    qc.ry(2 * np.arcsin(r), 0)
    qc.ry(2 * np.arcsin(g), 1)
    qc.ry(2 * np.arcsin(b), 2)

    qc.draw("mpl")
    plt.savefig(f"{OUTPUT_DIR}/mcqi_{dataset_name}.png")
    plt.close()

# ==============================
# AMPLITUDE ENCODING
# ==============================
def amplitude_encode(image, dataset_name):
    vec = image.flatten()
    vec = vec / np.linalg.norm(vec)

    qc = QuantumCircuit(2)
    qc.initialize(vec, [0, 1])

    qc.draw("mpl")
    plt.savefig(f"{OUTPUT_DIR}/amplitude_{dataset_name}.png")
    plt.close()

# ==============================
# MAIN PIPELINE (DATASET LOOP)
# ==============================
for dataset, img_path in DATASETS.items():
    print(f"Processing {dataset}")

    gray_img = preprocess_image(img_path)
    rgb_img = preprocess_image(img_path, rgb=True)

    qram_encode(gray_img, dataset)
    mcqi_encode(rgb_img, dataset)
    amplitude_encode(gray_img, dataset)

print("✅ QRAM, MCQI, and Amplitude Encoding completed for all datasets.")
