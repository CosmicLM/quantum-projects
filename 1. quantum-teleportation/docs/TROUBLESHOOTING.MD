
The Circuit build runs into an error with the if_test, stating InstuctionSet object does not have this attribute.

Traceback (most recent call last):
  File "/home/manjaro/Projects/Qiskit/main.py", line 10, in <module>
    circuit = run_teleportation()
  File "/home/manjaro/Projects/Qiskit/teleportation.py", line 36, in run_teleportation
    qc.x(2).if_test(qc.clbits[1], 1)
    ^^^^^^^^^^^^^^^
AttributeError: 'InstructionSet' object has no attribute 'if_test'

[2025-12-16, 15:54] - Upon recent findings, I conclude that the system may not be detecting objects from qiskit, rather it looks from the builtIn functions, as mentioned in the https://docs.python.org/3/library/functions.html#object


the error is that Qiskit actually has updated its commands and attribute, so the syntax was wrong. the actual method of using if_test is the following:

with qc.if_test((qc.clbits[1], 1)):
        qc.x(2)