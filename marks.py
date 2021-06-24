import plotly.graph_objects as go
import pandas as pd
import csv
df=pd.read_csv("data.csv")
studentdf=df.loc[df["student_id"]=="TRL_xsl"]
d=studentdf.groupby("level")["attempt"].mean()
print(d)
figure=go.Figure(go.Bar(
    x=d,
    y=["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation="h"
))
figure.show()

