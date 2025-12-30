from qiskit import QuantumCircuit
#In experiment B, the Qubits will be analyzed for relative phase
#rather than bits. This is crucial to actually examine if the computer is actually
#Sending over the bit as a teleporter, or as a relay.





#Part 1, Setup - Unlike Experiment A, there will be no X gate. this is because
#we will be measuring exactly "as is" when it comes to q0 function and message.
def experimentb():
    
    circuit = QuantumCircuit(3, 3)
    
    #Applying Hadamard Gate on 0, and 1 
    circuit.h([0,1])
    
    #by applying a CNOT gate on q1 and q2, we provide a link
    # between q1 and q2 causing the latter to be part of the superposition with q1.
    
    circuit.cx(1,2)
    
    #q0 links with the rest of the Qubits, with a CNOT q0 to q1. 
    #by doing so, all qubits are united together in entanglement.
    circuit.cx(0,1)
    
    #applying Hadamard gate to q0 translates the "phase" to location
    circuit.h(0)
    
    #circuit bell measurement is applied to q0, causing is to end the superposition
    #this happens due to wavefunction collapse, as teleportation is a destructive transfer of
    #via q1, to q2, ultimately "teleporting" itself to q2. 
    circuit.measure([0,1], [0,1])

    with circuit.if_test((circuit.clbits[1], 1)):
        circuit.x(2)

#If the first bit from qubit 0 is 1, apply Z to qubit 2
    with circuit.if_test((circuit.clbits[0], 1)):
        circuit.z(2)
    
    circuit.h(2)
    
    circuit.measure(2, 2)

    return circuit




