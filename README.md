# ⚛️ Quantum Circuit Proofs & Experiments

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Qiskit](https://img.shields.io/badge/Qiskit-6929C4?style=for-the-badge&logo=ibm&logoColor=white)
![Status](https://img.shields.io/badge/Status-Verified-success?style=for-the-badge)

A collection of quantum algorithms designed, implemented, and verified using **Qiskit** and the **Aer Simulator**. This repository documents my work in validating fundamental quantum mechanics phenomena through code.

## 📂 Project 1: Quantum Teleportation & Phase Analysis

This module implements the quantum teleportation protocol to transfer a qubit's state to a remote target using entanglement (Bell States) and classical communication.

### 🔬 Key Concepts Implemented
* **Entanglement Creation:** Generating Bell pairs to link qubits $q_1$ and $q_2$.
* **Basis Change:** Applying Hadamard gates to translate phase information into measurable bit-flips.
* **Dynamic Circuits:** Using `if_test` to apply conditional logic based on mid-circuit measurements.
* **State Reconstruction:** verifying the state was successfully "teleported" to the destination qubit.

---

## 📊 Visual Verification

*(These results were generated directly from the execution of the circuit scripts)*

### 1. Circuit Architecture
The following diagram illustrates the gate logic used for the teleportation protocol, including the Bell measurement and conditional X/Z corrections.

![Circuit Diagram](./quantum-teleportation/results/teleportation_circuit.png)

### 2. Execution Results
Histogram analysis confirming the probability distribution of the measured states.

![Results Histogram](./quantum-teleportation/results/results.png)

---

## 🛠️ Usage

To replicate these experiments:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/CosmicLM/quantum-projects.git](https://github.com/CosmicLM/quantum-projects.git)
    cd quantum-projects
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the analysis**
    ```bash
    # Navigate to the study module
    cd teleportation_phase_study
    python main.py
    ```

## 🧩 Structure
* `quantum_teleportation.py`: Core logic for the teleportation protocol and qubit setup.
* `phase_analyzer.py`: Logic for analyzing phase relationships.
* `main.py`: Orchestrator script that compiles the circuits and runs the Aer simulator.

---

### 👤 Author
**Eduardo de Souza Lima**
* [GitHub Profile](https://github.com/CosmicLM)
* [LinkedIn](https://linkedin.com/in/edusouzalima)
