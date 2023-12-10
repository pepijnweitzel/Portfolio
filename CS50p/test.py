import math
probs = [0.1234535, 0.234621534, 0.87461532, 0.7853254, 0.13354367, 0.5462345214, 0.2345645731, 0.43252614531, 0.32463457154]

probability = 1

for prob in probs:
    probability *= prob

print(f"math: {math.prod(probs)}")
print(f"prob: {probability}")
