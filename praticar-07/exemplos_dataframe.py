import pandas as pd

dados = {
    'nome': ['Alice','Bruno','Carlos'],
    'idade': [25,35,22],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Vitória']
}

df = pd.DataFrame(dados)
print(df)