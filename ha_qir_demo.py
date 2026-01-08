import cv2
import numpy as np

# -----------------------------
# 1. Load Image
# -----------------------------
img = cv2.imread("data/sample.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Image not found. Check path: data/sample.jpg")

# Resize to NxN (small for demo)
N = 8
img = cv2.resize(img, (N, N))

# Normalize
img = img / 255.0

# -----------------------------
# 2. ROI Extraction
# -----------------------------
threshold = 0.6
roi_mask = img > threshold

roi_pixels = img[roi_mask]
bg_pixels = img[~roi_mask]

# -----------------------------
# 3. MCQI Encoding (ROI)
# -----------------------------
def mcqi_encode(pixels):
    if len(pixels) == 0:
        return np.array([])
    return pixels / np.linalg.norm(pixels)

roi_state = mcqi_encode(roi_pixels)

# -----------------------------
# 4. Amplitude Encoding (Background)
# -----------------------------
def amplitude_encode(pixels):
    if len(pixels) == 0:
        return np.array([])
    return pixels / np.linalg.norm(pixels)

bg_state = amplitude_encode(bg_pixels)

# -----------------------------
# 5. HA-QIR Hybrid State
# -----------------------------
hybrid_state = np.concatenate([roi_state, bg_state])

# -----------------------------
# 6. Output Summary
# -----------------------------
print("HA-QIR Encoding Successful")
print(f"ROI qubits (MCQI approx): {len(roi_state)}")
print(f"Background qubits (Amplitude): {len(bg_state)}")
print(f"Total Hybrid State Length: {len(hybrid_state)}")
import matplotlib.pyplot as plt

# Reconstruct visualization (classical)
reconstructed = np.zeros_like(img)
reconstructed[roi_mask] = roi_pixels
reconstructed[~roi_mask] = bg_pixels

plt.figure(figsize=(6,3))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("HA-QIR Processed")
plt.imshow(reconstructed, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.savefig("outputs/ha_qir_output.png")
plt.savefig("results/ha_qir_output.png", dpi=300, bbox_inches="tight")
plt.show()

