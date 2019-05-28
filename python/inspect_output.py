import yaml
import matplotlib.pyplot as plt


with open("test_output10.yml") as stream:
        data = yaml.safe_load(stream)

print(data)

pitch = data.get("pitch")
pitchConfidence = data.get("pitch_confidence")

print(pitch)
print(pitchConfidence)

plt.plot(pitch)
plt.show()

plt.plot(pitchConfidence)
plt.show()
