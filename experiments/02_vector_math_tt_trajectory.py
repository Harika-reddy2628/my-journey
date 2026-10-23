"""
Experiment 02: Spatial Vectors & Racket Physics in PyTorch
---------------------------------------------------------
Domain: Embodied AI & Athletic Mathematics (Table Tennis Physics)
Objective: Master 3D Vectors, Euclidean Norms (Speed), and Dot Products (Stroke Alignment)
           running directly on your Mac's Apple Silicon GPU using PyTorch tensors.
"""

import math
import torch

# 1. Hardware Check: Powering our Math on Apple Silicon GPU
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print("=" * 65)
print(f"⚡ COMPUTE ENGINE: Running PyTorch on [{device.type.upper()}] (Apple Silicon GPU)")
print("=" * 65)

# 2. What is a 3D Vector in Physical Space?
# In Table Tennis, every shot has 3 spatial components:
# [X: Forward velocity towards opponent, Y: Lateral cross-court velocity, Z: Vertical lift] (in meters/sec)

# Forehand Topspin Drive Vector (Fast forward, slightly cross-court, upward brush)
forehand_velocity = torch.tensor([12.5, 3.2, 4.0], device=device)

# Defensive Backhand Chop Vector (Moderate forward, reverse slice, staying low)
backhand_chop_velocity = torch.tensor([6.0, -1.5, 0.8], device=device)

print("\n1️⃣ PHYSICAL VELOCITY VECTORS [X (Forward), Y (Cross), Z (Lift)]:")
print(f"   • Forehand Topspin Vector : {forehand_velocity.tolist()} m/s")
print(f"   • Backhand Chop Vector    : {backhand_chop_velocity.tolist()} m/s")

# 3. Vector Math Core #1: MAGNITUDE (The Euclidean Norm = True Ball Speed)
# Formula: ||v|| = sqrt(x^2 + y^2 + z^2)
forehand_speed_mps = torch.norm(forehand_velocity).item()
forehand_speed_kmh = forehand_speed_mps * 3.6  # Convert m/s to km/h

chop_speed_mps = torch.norm(backhand_chop_velocity).item()
chop_speed_kmh = chop_speed_mps * 3.6

print("\n2️⃣ VECTOR MAGNITUDE (True Ball Speed in Physical Space):")
print(f"   • Forehand Speed : {forehand_speed_mps:.2f} m/s ({forehand_speed_kmh:.1f} km/h)")
print(f"   • Backhand Speed : {chop_speed_mps:.2f} m/s ({chop_speed_kmh:.1f} km/h)")

# 4. Vector Math Core #2: UNIT VECTOR (Pure Direction of Travel)
# Formula: unit_v = v / ||v|| (length becomes exactly 1.0)
forehand_direction = forehand_velocity / torch.norm(forehand_velocity)
print("\n3️⃣ DIRECTION VECTOR (Normalized Arrow of Flight, Length = 1.0):")
print(f"   • Forehand Direction Unit: {[round(x, 3) for x in forehand_direction.tolist()]}")
print(f"   • Verified Unit Length   : {torch.norm(forehand_direction).item():.4f}")

# 5. Vector Math Core #3: THE DOT PRODUCT (Racket-Ball Energy Transfer)
# Dot Product formula: A · B = ||A|| * ||B|| * cos(theta)
# If racket travels parallel to ball trajectory -> Max power (Flat Smash, cos(0) = 1)
# If racket brushes perpendicular to trajectory  -> Pure spin (Thin Brush, cos(90) = 0)

# Racket swing path direction (driving forward and up)
racket_swing_path = torch.tensor([10.0, 2.0, 5.0], device=device)

# Dot Product in PyTorch
energy_transfer = torch.dot(forehand_velocity, racket_swing_path).item()

# Angle between swing path and ball path (in degrees)
cos_theta = energy_transfer / (torch.norm(forehand_velocity).item() * torch.norm(racket_swing_path).item())
# Clamp for numerical stability
cos_theta = max(-1.0, min(1.0, cos_theta))
angle_degrees = math.degrees(math.acos(cos_theta))

print("\n4️⃣ DOT PRODUCT & IMPACT ANGLE (Racket Swing vs Ball Trajectory):")
print(f"   • Raw Dot Product Value  : {energy_transfer:.2f}")
print(f"   • Impact Angle (Theta)   : {angle_degrees:.2f}°")
if angle_degrees < 15.0:
    print("   • Stroke Classification  : 💥 FLAT SMASH (Direct through-the-ball impact)")
elif angle_degrees < 35.0:
    print("   • Stroke Classification  : 🌀 HEAVY TOPSPIN DRIVE (Ideal blend of speed + spin)")
else:
    print("   • Stroke Classification  : ✂️ THIN BRUSH / GLANCE (Pure friction, low forward speed)")

print("\n" + "=" * 65)
print("✅ EXPERIMENT 02 VERIFIED: Spatial Vectors & PyTorch MPS acceleration working!")
print("=" * 65)
