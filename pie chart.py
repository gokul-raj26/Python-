import plotly.express as px

lables=["Shirts","T-Shirts","Trousers","Shorts"]

values=[15,40,60,45]

fig=px.pie(names=lables,values=values,title='MY PIE CHART')

fig.show()



