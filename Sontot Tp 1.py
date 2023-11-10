import numpy as np
from qiskit import *
from qiskit import Aer
from qiskit.visualization import plot_histogram, plot_state_city

c = QuantumCircuit(3)

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

c2 = QuantumCircuit(3)
c2.measure_all()

# be = Aer.get_backend('statevector_simulator')
# job = be.run(c)
# result = job.result()
# outputState = result.get_statevector(c,decimals = 3)
# print(outputState)
# plot_state_city(outputState, filename="state_city_plot.png")

be = BasicAer.get_backend('qasm_simulator') # the device to run on
c = c.compose(c2)
result = be.run(transpile(c, be), shots=1000).result()
counts  = result.get_counts(c)
print(counts)
plot_histogram(counts,filename="output.png")
