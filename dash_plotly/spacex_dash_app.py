# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
launch_sites = spacex_df['Launch Site'].unique()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),

                                dcc.Dropdown(id='site-dropdown',
                                             options=[
                                                 {'label': 'All Sites',
                                                     'value': 'ALL'},
                                                 {'label': launch_sites[0],
                                                     'value': launch_sites[0]},
                                                 {'label': launch_sites[1],
                                                     'value': launch_sites[1]},
                                                 {'label': launch_sites[2],
                                                     'value': launch_sites[2]},
                                                 {'label': launch_sites[3],
                                                     'value': launch_sites[3]},
                                             ],
                                             value='ALL',
                                             placeholder="Select a Launch Site here",
                                             style={'width': '80%', 'padding': '3px', 'text-align-last': 'center',
                                                    'font-size': '20px'},
                                             searchable=True
                                             ),

                                html.Br(),

                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),

                                dcc.RangeSlider(id='payload-slider',
                                                min=0,
                                                max=10000,
                                                step=1000,
                                                marks={0: '0 kg',
                                                       1000: '1000 kg',
                                                       2000: '2000 kg',
                                                       3000: '3000 kg',
                                                       4000: '4000 kg',
                                                       5000: '5000 kg',
                                                       6000: '6000 kg',
                                                       7000: '7000 kg',
                                                       8000: '8000 kg',
                                                       9000: '9000 kg',
                                                       10000: '10000 kg'},
                                                value=[min_payload, max_payload]),

                                html.Div(
                                    dcc.Graph(id='success-payload-scatter-chart')),
                                ])


@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    print(entered_site)
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, names='Launch Site', values='class',
                     title='Total Success Launches By site')
        return fig
    else:
        filtered_df = spacex_df.loc[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df, names='class',
                     title='Total Success Launches for site ' + entered_site)
        return fig


@app.callback(
    Output(component_id='success-payload-scatter-chart',
           component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(entered_site, payload_slider):
    low, high = payload_slider
    title_prefix = "Correlation between Payload mass and Success for "
    if entered_site == 'ALL':
        df = spacex_df
        mask = (df['Payload Mass (kg)'] > low) & (
            df['Payload Mass (kg)'] < high)
        fig = px.scatter(
            df[mask], x="Payload Mass (kg)", y="class",
            color="Booster Version",
            size='Payload Mass (kg)',
            title=title_prefix + "all sites",
            hover_data=['Payload Mass (kg)'])
    else:
        df = spacex_df.loc[spacex_df['Launch Site'] == entered_site]
        mask = (df['Payload Mass (kg)'] > low) & (
            df['Payload Mass (kg)'] < high)
        fig = px.scatter(
            df[mask], x="Payload Mass (kg)", y="class",
            color="Booster Version",
            size='Payload Mass (kg)',
            title=title_prefix + entered_site,
            hover_data=['Payload Mass (kg)'])
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server()
