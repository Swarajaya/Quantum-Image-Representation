import matplotlib.pyplot as plt
import numpy as np

# Models
models = [
    "FRQI",
    "NEQR",
    "QRAM",
    "MCQI",
    "Amplitude"
]

# Gate counts (use realistic + your evaluated values)
gates = [
    16384,   # FRQI (very high)
    32768,   # NEQR (very very high)
    12,      # QRAM
    3,       # MCQI
    1        # Amplitude
]

# Colors based on complexity
colors = [
    "red",     # FRQI
    "red",     # NEQR
    "orange",  # QRAM
    "green",   # MCQI
    "green"    # Amplitude
]

plt.figure(figsize=(10, 6))

bars = plt.bar(models, gates, color=colors)

# Log scale like research papers
plt.yscale("log")

plt.xlabel("Quantum Image Representation Models")
plt.ylabel("Gate Complexity (log scale)")
plt.title("Comparison of Quantum Image Representations based on Gate Complexity")

# Annotate values
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height)}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()

# Save for paper & WhatsApp sharing
plt.savefig("results/quantum_model_gate_comparison.png", dpi=300)
plt.show()
