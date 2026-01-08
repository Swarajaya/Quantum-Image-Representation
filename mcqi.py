from qiskit import QuantumCircuit
import numpy as np
import matplotlib.pyplot as plt

# One RGB pixel values
R, G, B = 0.6, 0.3, 0.8

# 3 qubits for R, G, B channels
qc = QuantumCircuit(3)

# Encode RGB channels using rotations
qc.ry(2 * np.arcsin(R), 0)  # Red
qc.ry(2 * np.arcsin(G), 1)  # Green
qc.ry(2 * np.arcsin(B), 2)  # Blue

# Draw, save, and show circuit
qc.draw(output='mpl')
plt.savefig("mcqi_circuit.png")
plt.show()
