import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
from read_shloka import create_list, get_shloka_number
from vaakya_sandhi import *


app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
server=app.server

def app_design():

    heading1 = dcc.Markdown('# **श्रीमद्भगवद्गीता विन्यास**')
    heading2 = dcc.Markdown('## **पदाभिज्ञानम्**')
    heading3 = dcc.Markdown('### **श्लोकः**')
    heading4 = dcc.Markdown('### **पुना रचितः श्लोकः**')
    heading5 = dcc.Markdown('### **प्रक्रिया-सार**')

    shloka = html.H5(id='shloka')
    para1 = html.P('उपरिदत्ते श्लोके प्रयुक्तां पदां लिखतु', id='instructions')
    nivista = dbc.Input(id='input', type='text')
    previous_shloka = dbc.Button('सूत्राणि पश्यतु', id='Show', n_clicks=0, block=True, color='secondary')
    next_shloka = dbc.Button('अग्रिमः श्लोकः', id='Next', n_clicks=0, block=True, color='primary')

    instructions = '**अधोदत्ते श्लोके प्रयुक्ताः पदाः लिखतु।** \n - द्वाभ्यां पदाभ्यां मध्ये अवसानं (space) स्यात्। \n - वाक्यान्तं निर्दिष्टुम् दण्डं (। उत् ॥) प्रयुक्तव्यम्। \n - वसर्गान्ताः शब्दाः सकारानता एव स्युः।'

    constructed_shloka = html.H5(id='constructed_shloka')
    table = html.Div(id='table')


    layout = html.Div([

        dbc.Row(heading1,justify='center'),

        dbc.Row(heading2,justify='center'),

        dbc.Alert(dcc.Markdown(instructions)),

        dbc.Row(heading3,justify='center'),

        dbc.Row(shloka,justify='center'),
        
        para1,
        nivista,

        dbc.Row([
            dbc.Col(previous_shloka),
            dbc.Col(next_shloka)
        ]),

        html.Hr(),

        dbc.Row(heading4,justify='center'),

        dbc.Row(constructed_shloka,justify='center'),

        html.Hr(),

        dbc.Row(heading5,justify='center'),

        dbc.Row(table,justify='center'),

    ])

    return layout

@app.callback(
    [dash.dependencies.Output('shloka', 'children'),
    dash.dependencies.Output('table', 'children'),
    dash.dependencies.Output('constructed_shloka', 'children')],
    [dash.dependencies.Input('Next', 'n_clicks'),
    dash.dependencies.Input('Show', 'n_clicks'),
    dash.dependencies.State('input', 'value'),]
)
def update_app(clicks1, clicks2, input):

    ctx = dash.callback_context

    shloka_list = create_list()

    try:
        df = pd.read_csv('pada.csv')
        ll = list(df['पदाः'])
        ii = len(df)

    except:
        df = pd.DataFrame(columns=['क्रमाङ्क', 'पदाः'])
        ii = 0

    if clicks1 == 0 and clicks2 == 0:
        sh = shloka_list[ii]
        aa = '-'
        bb = '-'

    else:

        click_button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if click_button_id == 'Next':

            row = {'क्रमाङ्क': ii + 1, 'पदाः': input.split(' ')}
            df = df.append(row, ignore_index=True)
            df.to_csv('pada.csv', index=False)
            
            sh = shloka_list[ii+1]
            aa = '-'
            bb = '-'

        if click_button_id == 'Show':

            mm = input.split(' ')

            sh = shloka_list[ii]
            aa = ', '.join(mm)

            qq = vaakya_sandhi(0, mm)

            aa = dbc.Table.from_dataframe(qq[2])

            bb = [get_shabda(qq[0]), html.Br(), get_shabda(qq[1])]

            # print(aa, flush=True)

    r = sh.split('\n')

    if r[-1] == '':
        del r[-1]
    
    if len(r) == 2:
        r.insert(1, html.Br())
    elif len(r) == 4:
        r.insert(1, html.Br())
        r.insert(3, html.Br())
        r.insert(5, html.Br())

    # print(r, flush=True)

    return [r, aa, bb]

app.layout = app_design()
app.run_server(debug=True)