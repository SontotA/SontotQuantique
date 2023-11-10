import numpy as np
from qiskit import *
from qiskit import Aer
from qiskit.visualization import plot_histogram, plot_state_city

c = QuantumCircuit(3)

#on créer les circuits

c.h(0)
c.cx(0,1)
c.h(2)
c.cx(2,1)
c.x(2)
c.cx(2,0)
c.x(2)
c.barrier()
c.swap(0,1)
c.x(0)
c.x(1)
c.cx(2,1)
c.x(2)
c.cx(2,0)
c.x(2)

print(c.draw())

# on mesure le deuxieme circuits

c2 = QuantumCircuit(3)
c2.measure_all()


be = BasicAer.get_backend('qasm_simulator') 
c = c.compose(c2)
result = be.run(transpile(c, be), shots=1000).result()
counts  = result.get_counts(c)
print(counts)
plot_histogram(counts,filename="output.png")
