from qiskit import QuantumCircuit

#In this project, we will define a quantum circuit, prepare a message to be sent via Quantum Teleportation,
# which uses 3 Qubits to send on message (qubit 1) to the destination (qubit 3) via qubit 2.

#This defines the quantum circuit state, of the Quantum Computing, in other words, the wires and qubits.
qc = QuantumCircuit(3, 3)

def experimenta():
#Part 1 - Prepare the message to be sent, we will start with a X gate on Qubit 0, to flip the Qubit into a 1 state, 
#before starting the entanglement process.
    qc.x(0)

#Part 2, Hadarmards Gate on Qubit 1 allowing the Qubit to enter a process of entanglement,
#which means a probability of 50% of being 1 and a 0. This is where we call the superposition of the qubitm functioning as a 0 and 1 at the same time.
    qc.h(1)

#We will now entangle Qubit 1 with Qubit 2, by applying  CNOT Gate 
#The connection happens through qubit 0 entangling with the other 1 and 2 qubits. 
# by doing so, we are essentialyl spreading the message equally accross our connections.

    qc.cx(1, 2)

    qc.barrier() #visual separator

#Part 3 concludes the half of our circuit. Qubit 0, now distroys its quantum state, collapsing the connection. By doing so, Qubit 0 then turns into their end state
#This allows Qubit 2 to fully reconstruct its state perfectly, according to Qubit 0, to get the information necessary.
#this is called a "Bell Basis Measurement" 
    qc.cx(0,1)
    qc.h(0)
    qc.measure([0,1], [0,1])
#series of if statements, this step is crucial to copy the state that Qubit 0 had into Qubit 2,
#This process is called correction phase.



#if the second bit from qubit 1 is 1, apply X to qubit 2
    with qc.if_test((qc.clbits[1], 1)):
        qc.x(2)

#If the first bit from qubit 0 is 1, apply Z to qubit 2
    with qc.if_test((qc.clbits[0], 1)):
        qc.z(2)

#as of now, Qubit 2 should match the original Qubit 0 in code, so we now use a verifcation method, measuring both qubits.

    qc.barrier() #visual separator

    qc.measure(2, 2)

    return qc

