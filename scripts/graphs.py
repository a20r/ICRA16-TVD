
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def plot_number_of_nodes():
    data = [["Portugal and Rocha", "A", 7],
            ["Portugal and Rocha", "B", 60],
            ["Portugal and Rocha", "C", 66],
            ["TVD", "A", 2],
            ["TVD", "B", 21],
            ["TVD", "C", 37]]
    data = pd.DataFrame(
        data, columns=["Algorithm", "Map", "Number of Nodes"])
    sns.set_context("poster", font_scale=3)
    ax = sns.barplot("Map", y="Number of Nodes", hue="Algorithm", data=data)
    lgd= ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
                   fancybox=True, shadow=True, ncol=5)
    plt.savefig("figs/number_of_nodes.pdf",
                bbox_extra_artists=(lgd,), bbox_inches="tight")
    # plt.show()


if __name__ == "__main__":
    plot_number_of_nodes()
