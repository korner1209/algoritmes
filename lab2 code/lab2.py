import matplotlib.pyplot as plt

filename = 'DS2.txt'

x_coords = []
y_coords = []

with open(filename, 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        x_coords.append(x)
        y_coords.append(y)

plt.figure(figsize=(960/100, 540/100), dpi=100)

plt.scatter(x_coords, y_coords, c='black', marker='.')

plt.xlabel('X координата')
plt.ylabel('Y координата')

output_filename = 'result.png'
plt.savefig(output_filename, format='png')

plt.show()
