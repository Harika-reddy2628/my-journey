---
name: quantum-bloch-visualizer
description: >-
  Visual and geometric quantum computing fundamentals via the 3D Bloch sphere,
  Quirk interactive browser simulator, and IBM Quantum Composer. Demystifies qubits,
  superposition, and entanglement through spatial rotations without dry blackboard math.
---

# Visual Quantum Computing: The Bloch Sphere & Interactive Circuits

This skill teaches quantum computing purely through **spatial geometry and interactive simulation**.

## 1. The Core Geometric Truth: The Bloch Sphere
* A classical bit is a switch: either `0` or `1`.
* A **qubit** is a vector pointing to any location on the surface of a **3D unit sphere (The Bloch Sphere)**:
  * North Pole: $|0\rangle$ (100% chance of measuring 0)
  * South Pole: $|1\rangle$ (100% chance of measuring 1)
  * Equator: Perfect 50/50 **Superposition**!

## 2. Quantum Gates are Ball Rotations
* **$X$-Gate (Bit Flip):** Rotates the vector $180^\circ$ around the X-axis (North Pole flips to South Pole).
* **$Z$-Gate (Phase Flip):** Rotates the vector $180^\circ$ around the Z-axis (changes relative phase).
* **$H$ (Hadamard Gate):** Rotates from North Pole ($|0\rangle$) to the Equator ($|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$). That is how you create an unhackable, true quantum random coin-flip!

## 3. Interactive Web Tooling (Zero Installation)
1. **Quirk Simulator:** Open [algassert.com/quirk](https://algassert.com/quirk) in your browser. Drag an $H$ gate onto wire 0. Watch the amplitude and chance display pulse at 50%.
2. **IBM Quantum Composer:** Open [quantum.ibm.com/composer](https://quantum.ibm.com/composer). Assemble visual circuits and run them on real superconducting quantum hardware in New York!

## 4. 10-Line Qiskit Quantum Coin Flip
```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)
qc.h(0)         # Rotate qubit to the equator (Superposition)
qc.measure(0, 0) # Measure state: collapses to 0 or 1 with 50% probability

sim = AerSimulator()
result = sim.run(qc, shots=1000).result().get_counts()
print("Quantum Measurement Counts:", result) # e.g. {'0': 508, '1': 492}
```
