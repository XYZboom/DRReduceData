import matplotlib.pyplot as plt
from adjustText import adjust_text

if __name__ == '__main__':
    perses_x = [0, 31, 32, 49, 50, 81]
    perses_y = [71, 71, 69, 69, 62, 62]

    ssreducer_x = [0, 6, 7, 15, 16, 18, 19, 26]
    ssreducer_y = [71, 71, 57, 57, 54, 54, 37, 37]

    plt.figure(figsize=(10, 6))  # 略微加宽，给标签更多横向空间

    line1, = plt.plot(perses_x, perses_y, marker='o', linestyle='-', linewidth=2, label='WDD')
    line2, = plt.plot(ssreducer_x, ssreducer_y, marker='s', linestyle='-', linewidth=2, label='DRReducer')

    # 收集所有文本对象，初始位置放在点上方
    texts = []
    offset = 1.5
    used_dot = set()
    for x, y in zip(perses_x, perses_y):
        if (x, y) in used_dot:
            continue
        used_dot.add((x, y))
        texts.append(plt.text(x, y + offset, f'({x}, {y})',
                              ha='center', va='bottom', fontsize=14))
    for x, y in zip(ssreducer_x, ssreducer_y):
        if (x, y) in used_dot:
            continue
        used_dot.add((x, y))
        texts.append(plt.text(x, y + offset, f'({x}, {y})',
                              ha='center', va='bottom', fontsize=14))

    # 自动调整标签位置，避免相互重叠以及与线条/点的碰撞
    adjust_text(texts,
                expand=(0.8, 1.2),  # 让标签稍微分散一些
                force_text=(0.2, 0.5),  # 文本间排斥力
                )

    plt.xlabel('Number of Query Invocations', fontsize=20)
    plt.ylabel('Reduced Size (tokens)', fontsize=20)

    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.legend(title='(X, Y) = (Number of Query Invocations, Reduced Size)',
               title_fontsize=13, fontsize=12)

    plt.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig("example.pdf")
    plt.show()
