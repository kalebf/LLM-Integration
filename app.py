from dash import Dash, dcc, html, Input, Output, State
from llm_agent import generate_sql
from query_runner import run_query
from visualizer import visualize_dataframe




app = Dash(__name__)

