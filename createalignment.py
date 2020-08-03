import dash
import dash_html_components as html
import dash_bio as dashbio
import six.moves.urllib.request as urlreq
from six import PY3

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
data = urlreq.urlopen(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/' +
    'alignment_viewer_p53.fasta'
).read()
if PY3:
    data = data.decode('utf-8')

class CreateAlignment:
    def __init__(self, server, url):
        app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server, url_base_pathname=url)
        app.layout = html.Div([
            dashbio.AlignmentChart(
                id='my-alignment-viewer',
                data=data
            ),
            html.Div(id='alignment-viewer-output')
        ])


