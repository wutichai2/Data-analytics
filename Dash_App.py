import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('test datavis'),
    dcc.Graph(id='test',
              figure={
                  'data' : [
                      {'x' :[1,2,3,4,5], 'y':[5,6,7,8,9,1], 'type':'line','name':'wut'},
                      {'x' :[1,2,3,4,5], 'y':[8,3,6,1,2,5], 'type':'bar','name':'cars'}
                  ],
                  'layout': {
                      'title':'Basic Dash Example'
                  }
              })
        ])

if __name__ == '__main__':
    app.run_server(debug=True)