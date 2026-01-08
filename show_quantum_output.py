import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Paths (SAFE FOR WINDOWS)
# -----------------------------
IMAGE_PATH = os.path.join("data", "brain_tumor.jpg")
OUTPUT_DIR = "outputs"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "brain_tumor_quantum_output.png")

# -----------------------------
# Check image exists
# -----------------------------
if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"❌ Image not found at: {IMAGE_PATH}")

# -----------------------------
# Load image
# -----------------------------
img = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("❌ Image loaded as None. File may be corrupted.")

# -----------------------------
# Resize + normalize
# -----------------------------
img = cv2.resize(img, (128, 128))
norm_img = img / 255.0

# -----------------------------
# Simulated quantum processing
# (phase-style transformation)
# -----------------------------
quantum_processed = np.sin(norm_img * np.pi)

# -----------------------------
# Save output
# -----------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
plt.imsave(OUTPUT_PATH, quantum_processed, cmap="gray")

# -----------------------------
# Display results
# -----------------------------
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Quantum Processed Image")
plt.imshow(quantum_processed, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()

print(f"✅ Output saved at: {OUTPUT_PATH}")
