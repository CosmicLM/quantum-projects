from quantum_teleportation import experimenta
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from phase_analyzer import experimentb


print('Bulidng Circuit..')
qc_a = experimenta()
qc_b = experimentb()

print("Drawing Circuit..")
qc_a.draw('mpl', filename='teleportation_circuit.png')
qc_b.draw('mpl', filename='phase_circuit.png')
plt.show()


#Execute as a batch
print("Simulating Teste Suite...")
simulator = AerSimulator()
job = simulator.run([qc_a, qc_b], shots=2048)
result = job.result()

#Extract Individual Counts
counts_a = result.get_counts(0)
counts_b = result.get_counts(1)


#show results
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
plot_histogram(counts_a, ax=ax[0], title="Experiment A: Bit-Flip Verification")
plot_histogram(counts_b, ax=ax[1], title="Experiment B: Phase-Flip Verification")
plt.show()

