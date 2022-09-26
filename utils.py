import pandas as pd
import altair as alt

def plustwo(df, y_column, color_column):
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')

    return alt.Chart(df).mark_line().encode(
        x='Year',
        y=y_column,
        color=color_column
    )
