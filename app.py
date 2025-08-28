import pandas as pd
from utils import es_primo
def f(event, context):
    print("Hola desde lambda con Zappa")
    print(es_primo(5))
    return{}
    