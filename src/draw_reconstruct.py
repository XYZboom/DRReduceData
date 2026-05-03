import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure


def draw(df: pd.DataFrame, probs=None, vert=True, vert_stats=False):
    if probs is None:
        probs = ['w', 'w/o']
    np.random.seed(0)
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    df.columns = ['_'.join(col).strip() for col in df.columns.values]
    stats = [
        ('P', 'Query Times'),
        ('T', 'Time'),
        ('R', 'Remain Tokens'),
        # ('S', 'Speed(token/s)')
    ]  # predict times, times, remain tokens, speed
    stat_label_map = {
        'T': 'Seconds'
    }
    col_str = '{p}_{stat}'
    _figs = dict()
    for stat_i, (stat, stat_label) in enumerate(stats):
        cols = []
        for prob in probs:
            col_name = col_str.format(p=prob, stat=stat)
            col = list(filter(lambda v: not np.isnan(v), df[col_name].values))
            cols.append(col)
        _fig, ax = plt.subplots(figsize=(4, 4), constrained_layout=True)
        ax.boxplot(
            cols,
            widths=0.5,
            tick_labels=[_l for _l in probs],
            flierprops=dict(marker='None'),
            vert=vert,
        )
        if not vert:
            ax.set_ylabel('Reconstruct Dependencies')
            x_label = stat_label_map.get(stat)
            if x_label is not None:
                ax.set_xlabel(x_label)
        for i, (col, color) in enumerate(zip(cols, colors)):
            scale = 0.06 if vert else 0.08
            x = np.random.normal(i + 1, scale, size=len(col))  # 抖动
            if vert:
                ax.scatter(x, col, alpha=0.7, s=30, color=color, edgecolors='white', linewidth=0.5)
            else:
                ax.scatter(col, x, alpha=0.7, s=30, color=color, edgecolors='white', linewidth=0.5)
        ax.set_title(stat_label)
        _figs[stat] = _fig
    return _figs


if __name__ == '__main__':
    df = pd.read_excel(
        "reconstruct.xlsx",
        header=[0, 1],
        engine='openpyxl',
        engine_kwargs=dict(data_only=True)
    )
    # fig = draw(df)
    # fig.savefig('reconstruct.pdf')

    df2 = pd.read_excel(
        "reconstruct.xlsx",
        header=[0, 1],
        skiprows=[15, 19, ],
        # nrows=18,
        engine='openpyxl',
        engine_kwargs=dict(data_only=True)
    )
    plt.rcParams['font.size'] = 16
    figs = draw(df2, vert=False)
    for name in figs:
        fig: Figure = figs[name]
        fig.show()
        fig.savefig(f'{name}.pdf', dpi=300)
