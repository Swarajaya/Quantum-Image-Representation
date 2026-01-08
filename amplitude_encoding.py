from qiskit import QuantumCircuit
import numpy as np
import matplotlib.pyplot as plt

# 2x2 image flattened
image = np.array([0.2, 0.5, 0.7, 0.9])

# Normalize the vector
state = image / np.linalg.norm(image)

# 2 qubits required for 4 amplitudes
qc = QuantumCircuit(2)

# Initialize amplitudes
qc.initialize(state, [0, 1])

# Draw, save, and show circuit
qc.draw(output='mpl')
plt.savefig("amplitude_circuit.png")
plt.show()
