import matplotlib.pyplot as plt

if __name__ == '__main__':
    perses_x = [0, 31, 32, 49, 50, 81]
    perses_y = [71, 71, 69, 69, 62, 62]

    ssreducer_x = [0, 6, 7, 15, 16, 18, 19, 26]
    ssreducer_y = [71, 71, 57, 57, 54, 54, 37, 37]

    plt.figure(figsize=(8, 5))

    plt.plot(perses_x, perses_y, marker='o', linestyle='-', linewidth=2, label='Perses')
    plt.plot(ssreducer_x, ssreducer_y, marker='s', linestyle='-', linewidth=2, label='DRReducer')

    plt.xlabel('Predict times')
    plt.ylabel('Remain tokens')

    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig("example.pdf")
    plt.show()
