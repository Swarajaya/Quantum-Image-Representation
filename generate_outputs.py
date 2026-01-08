import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# Quantum-inspired model functions
# ===============================

def frqi(img):
    # Phase-inspired transformation
    return np.sqrt(img)

def neqr(img):
    # Discrete intensity encoding
    return np.round(img * 15) / 15

def qram(img):
    # Lookup-based (lossless)
    return img.copy()

def mcqi(img):
    # Multi-channel inspired mapping
    return np.power(img, 1.2)

def amplitude(img):
    # Amplitude normalization
    norm = np.linalg.norm(img)
    return img if norm == 0 else img / norm


# ===============================
# Quantum geometric transformation
# ===============================

def quantum_geometric_transform(image, transform="rotate"):
    """
    Simulated quantum geometric transformation
    Rotation corresponds to SWAP operations on position qubits
    """
    if transform == "rotate":
        return np.rot90(image)      # 90° rotation
    elif transform == "flip":
        return np.fliplr(image)     # horizontal flip
    return image


MODELS = {
    "frqi": frqi,
    "neqr": neqr,
    "qram": qram,
    "mcqi": mcqi,
    "amplitude": amplitude
}

DATASETS = ["brain_tumor", "mnist", "sar", "ssdd"]

# ===============================
# Main generation loop
# ===============================

for dataset in DATASETS:
    print(f"\n🔹 Processing dataset: {dataset}")

    img_path = f"data/{dataset}.png"
    save_dir = f"outputs/{dataset}"
    os.makedirs(save_dir, exist_ok=True)

    # Load image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"❌ Image not found: {img_path}")

    # Resize + normalize
    img = cv2.resize(img, (64, 64))
    img = img / 255.0

    # Save original
    plt.imsave(f"{save_dir}/original.png", img, cmap="gray")

    # Apply each model
    for model_name, model_func in MODELS.items():
        output = model_func(img)

        # Save model output
        plt.imsave(f"{save_dir}/{model_name}.png", output, cmap="gray")

        # Apply geometric transformation (rotation)
        rotated = quantum_geometric_transform(output, "rotate")
        plt.imsave(
            f"{save_dir}/{model_name}_rotated.png",
            rotated,
            cmap="gray"
        )

    print(f"✅ Outputs saved in: {save_dir}")

print("\n🎉 ALL DATASET OUTPUTS GENERATED SUCCESSFULLY")
