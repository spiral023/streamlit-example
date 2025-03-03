"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

import streamlit as st
import altair as alt
import pandas as pd
import math
from collections import namedtuple

def generate_spiral_points(total_points, num_turns):
    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    return data

def main():
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    data = generate_spiral_points(total_points, num_turns)

    df = pd.DataFrame(data)
    chart = alt.Chart(df, height=500, width=500).mark_circle(color='#FF0000', opacity=0.5).encode(x='x:Q', y='y:Q')

    st.altair_chart(chart)

if __name__ == "__main__":
    main()

    data = generate_spiral_points(total_points, num_turns)

    df = pd.DataFrame(data)
    chart = alt.Chart(df, height=500, width=500).mark_circle(color='#0068c9', opacity=0.5).encode(x='x:Q', y='y:Q')

    st.altair_chart(chart)

if __name__ == "__main__":
    main()
