P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100
CI = P * (pow((1 + R / 100), T)) - P

print("Simple Interest: ₹", SI)
print("Compound Interest: ₹", round(CI, 2))
