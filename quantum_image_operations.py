from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
import os

# ---------- Quantum Image Operations ----------

def quantum_horizontal_flip(qc, position_qubits):
    """
    Horizontal flip by reversing x-coordinate qubits
    """
    for q in position_qubits:
        qc.x(q)
    return qc


def quantum_vertical_flip(qc, position_qubits):
    """
    Vertical flip using X gates on position qubits
    """
    qc.barrier()
    for q in reversed(position_qubits):
        qc.x(q)
    return qc


def quantum_reflection(qc, q1, q2):
    """
    Basic geometric reflection using SWAP
    """
    qc.barrier()
    qc.swap(q1, q2)
    return qc


def quantum_image_filter(qc, target_qubit):
    """
    Simple quantum filtering using interference
    """
    qc.barrier()
    qc.h(target_qubit)
    qc.z(target_qubit)
    qc.h(target_qubit)
    return qc


# ---------- Example Usage ----------

def apply_operations():
    os.makedirs("results", exist_ok=True)

    # Example circuit (simulate encoded image)
    qc = QuantumCircuit(3)
    qc.h([0, 1, 2])  # assume encoded image

    # Position qubits (example)
    position_qubits = [0, 1]

    # Apply operations
    quantum_horizontal_flip(qc, position_qubits)
    quantum_vertical_flip(qc, position_qubits)
    quantum_reflection(qc, 0, 1)
    quantum_image_filter(qc, 2)

    # Save circuit
    circuit_drawer(
        qc,
        output="mpl",
        filename="results/quantum_image_operations.png"
    )

    print("Quantum image operations applied and saved.")


if __name__ == "__main__":
    apply_operations()
