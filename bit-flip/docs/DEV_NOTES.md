# 🛠️ Developer Notes & Architectural Log

This document records the technical reasoning, architectural decisions, and key learnings discovered during the development of Bit-Flip.

---

## 📅 Log Entries

### [Date: 2025-12-30] [My understanding of the Project
**Context:**
At first, I thought that the project was simply to measure the qubits the way I measured static or coherence, however i then found out that it is much more complex.

**Decision/Discovery:**
I then found out about what Ancillas were. They are 'disposable' bits, we use these to indirectly measure the Qubits that are in superposition. Without them, we would not be able to get an accurate reading, and we would then force the Qubits that are in superposition to choose a state. because of this, we 'kill' the probability aspect of the quantum computer, and turn it into a coin flip. Measurment kills results.

$$|\psi\rangle = \alpha|00\rangle + \beta|11\rangle$$

If we measured these directly, we'd just get $00$ or $11$ and lose the $\alpha$ and $\beta$ coefficients. We want to check if they are "the same" (parity = 0) or "different" (parity = 1) without collapsing the state.

**Reasoning:**
* **Constraint:** the Limitation was how exactly was it possible to measure these bits with them 'dying out'? and lastly, how do we know if the ancillas are actually correct, given the fact that the ancillas themselves are noisy, how can we trust these results?

* **Requirement:** I then discovered the recovery, the Lookup table is a set of conditions that we may place, in order to correct these data qubits, ensuring fault tolerance and data coherence, even if the ancillas fail.

For the 3-qubit code, we have two ancillas:Ancilla 1 ($S_1$): Checks the parity of Data Qubit 0 and Data Qubit 1.Ancilla 2 ($S_2$): Checks the parity of Data Qubit 1 and Data Qubit 2.A result of 0 means they match (good), and 1 means they are different (flag!).

* **Outcome:** so, in summary, there are 3 qubits, and 2 ancilla qubits in our circuit. the main purpose is to measure the fault tolerance, the error instead of the data itself, to see if our quantum computer is reliable. we do this by encoding two qubits, and wiring one qubit to be a fault (applying an X gate, for exmaple). we then use the ancillas to measure the parity, or relation, of these qubits, and then with a conditional logic, we formulate a lookup table to correct all information from the data qubits. by doing so, we measure the fault tolerance of the ancillas, and the probability of them being wrong. 

---

### [Date: YYYY-MM-DD] [Short Title of Decision/Discovery]
**Context:**
[Briefly describe the problem, situation, or initial understanding before the change.]

**Decision/Discovery:**
[What action did you take?]

**Reasoning:**
* **Constraint:** [...]
* **Requirement:** [...]
* **Outcome:** [...]

---

## 🔮 Future Optimizations
* **[Category]:** [Idea for future improvement]
* **[Category]:** [Idea for future improvement]