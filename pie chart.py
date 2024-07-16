import plotly.express as px

lables=["category A","category B","category C","category D"]

values=[15,40,60,45]

fig=px.pie(names=lables,values=values,title='my Pie chart')

fig.show()
