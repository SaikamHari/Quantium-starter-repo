import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("data/processed_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Create app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    
    html.H1("Pink Morsel Sales Dashboard", 
            style={"textAlign": "center", "color": "#2c3e50"}),

    html.Div([
        html.Label("Select Region:", style={"fontSize": "18px"}),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True
        )
    ], style={"textAlign": "center", "marginBottom": "20px"}),

    dcc.Graph(id="sales-chart")

], style={
    "backgroundColor": "#f4f6f7",
    "padding": "20px"
})

# Callback
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Sales Over Time",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white"
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)