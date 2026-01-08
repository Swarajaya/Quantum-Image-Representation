import numpy as np
from qiskit import QuantumCircuit
from math import pi

def frqi_circuit(image):
    n = int(np.log2(image.size))  # number of position qubits
    qc = QuantumCircuit(n + 1)

    # Put position qubits into superposition
    for i in range(n):
        qc.h(i)

    # Encode pixel values using rotations
    flat_image = image.flatten()
    for idx, pixel in enumerate(flat_image):
        angle = pixel * pi
        qc.cry(2 * angle, idx % n, n)

    return qc
