from qiskit import QuantumCircuit
from qiskit_aer import aer_simulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


circuit = QuantumCircuit(5,2)

circuit.h()
