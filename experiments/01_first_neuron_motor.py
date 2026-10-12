"""
Experiment 01: The First Neuron — Controlling a Robot's Motor
-------------------------------------------------------------
Domain: Deep Learning + Robotics (Embodied Intelligence)
Objective: Teach a single artificial neuron how to brake a robot 
           based on distance from an obstacle, without hardcoding rules.
"""

# 1. The Physical Data (What the robot observes)
# Distance from wall (meters) -> Required Brake Force (0.0 = no brake, 1.0 = full brake)
sensor_distances = [0.2, 0.5, 0.8, 1.2, 1.8]   # Closer to wall -> needs more brake
true_brake_force = [0.9, 0.75, 0.5, 0.25, 0.0]  # The real-world physical target

# 2. The Artificial Neuron (The Brain's single knob)
# Formula: predicted_brake = weight * distance + bias
weight = 0.0   # Initial guess (completely clueless)
bias = 0.5     # Initial baseline
learning_rate = 0.1

print("=" * 60)
print("🤖 ROBOT NEURON: LEARNING HOW TO BRAKE FROM SCRATCH")
print("=" * 60)

# 3. The Learning Loop (Training over 25 steps / epochs)
for epoch in range(1, 26):
    total_error = 0.0
    weight_gradient = 0.0
    bias_gradient = 0.0
    
    # Test our neuron against all sensor readings
    for dist, target in zip(sensor_distances, true_brake_force):
        # A. FORWARD PASS: The neuron makes a guess
        guess = (weight * dist) + bias
        
        # B. CALCULATE ERROR: How far off was the guess?
        error = guess - target
        total_error += error ** 2
        
        # C. GRADIENT: Which direction should we nudge the knob?
        weight_gradient += 2 * error * dist
        bias_gradient += 2 * error
    
    # D. BACKPROPAGATION / UPDATE: Nudge the knobs in the opposite direction of error
    weight -= learning_rate * (weight_gradient / len(sensor_distances))
    bias -= learning_rate * (bias_gradient / len(sensor_distances))
    
    # Print progress every 5 steps
    if epoch % 5 == 0 or epoch == 1:
        print(f"Step {epoch:02d} | Error: {total_error:.4f} | Weight: {weight:.2f} | Bias: {bias:.2f}")

print("=" * 60)
print("✅ TRAINING COMPLETE! Let's test our trained robot neuron:")
print("=" * 60)

test_distances = [0.3, 1.0, 1.5]
for test_dist in test_distances:
    predicted_brake = max(0.0, min(1.0, (weight * test_dist) + bias))
    print(f"Obstacle at {test_dist}m  -->  Brake Command: {predicted_brake * 100:.1f}% power")
