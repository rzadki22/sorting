import json
import plotly.graph_objects as go

from research import ORDERED, REVERSED, RANDOM

def show_algorithm_complexities(filename):
    with open(filename) as f:
        result = json.load(f)

    domain = list(result[ORDERED].keys())

    figure = go.Figure()
    figure.add_trace(go.Scatter(x=domain, y=list(result[ORDERED].values()), mode="lines+markers", name=ORDERED))
    figure.add_trace(go.Scatter(x=domain, y=list(result[REVERSED].values()), mode="lines+markers", name=REVERSED))
    figure.add_trace(go.Scatter(x=domain, y=list(result[RANDOM].values()), mode="lines+markers", name=RANDOM))

    figure.show()


if __name__ == "__main__":

    filename = "BubbleSort_300.json"
    show_algorithm_complexities(filename)
    filename = "BubbleSortNaive_300.json"
    show_algorithm_complexities(filename)
    filename = "InsertSort_300.json"
    show_algorithm_complexities(filename)