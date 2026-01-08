from qiskit import QuantumCircuit
import numpy as np
import matplotlib.pyplot as plt

# 2x2 image pixel values
pixels = [0.2, 0.5, 0.7, 0.9]

# 2 address qubits + 1 data qubit
qc = QuantumCircuit(3)

for i, value in enumerate(pixels):
    binary = format(i, '02b')

    # Set address qubits
    if binary[0] == '1':
        qc.x(0)
    if binary[1] == '1':
        qc.x(1)

    # Encode pixel value in data qubit
    qc.ry(2 * np.arcsin(value), 2)

    # Reset address qubits
    if binary[0] == '1':
        qc.x(0)
    if binary[1] == '1':
        qc.x(1)

# Draw, save, and show circuit
qc.draw(output='mpl')
plt.savefig("qram_circuit.png")
plt.show()
