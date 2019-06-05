import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='Filename to be parsed')
args = parser.parse_args()
filename = args.file

df = pd.read_csv(filename, header=None, names=['raw'], sep='xyz123', encoding='latin-1')
df.shape

df.iloc[0].raw

positions = [
    ('tipo_registro', 1, 1),
    ('indicador_full_diario', 2, 1),
    ('tipo_atualizacao', 3, 1),
    ('cnpj', 4, 14),
    ('matriz_filial', 18, 1),
    ('razao_social', 19, 150),
    ('nome_fantasia', 169, 55),
    ('situacao_cadastral', 224, 2),
    ('dt_situacao_cadastral', 226, 8),
    ('motivo_situacao_cadastral', 234, 2),
    ('nm_cidade_exterior', 236, 55),
    ('cod_pais', 291, 3),
    ('nm_pais', 294, 70),
    ('cod_natureza_juridica', 364, 4),
    ('dt_inicio_atividade', 368, 8),
    ('cnae_fiscal', 376, 7),
    ('tipo_logradouro', 383, 20),
    ('logradouro', 403, 60),
    ('numero', 463, 6),
    ('complemento', 469, 156),
    ('bairro', 625, 50),
    ('cep', 675, 8),
    ('uf', 683, 2),
    ('cod_municipio', 685, 4),
    ('municipio', 689, 50),
    ('telefone_1', 739, 12),
    ('telefone_2', 751, 12),
    ('fax', 763, 12),
    ('email', 775, 115),
    ('quali_responsavel', 890, 2),
    ('capital_social', 892, 14),
    ('porte_empresa', 906, 2),
    ('opcao_simples', 908, 1),
    ('dt_opcao_simples', 909, 8),
    ('dt_exclusao_simples', 917, 8),
    ('opcao_mei', 925, 1),
    ('situacao_especial', 926, 23),
    ('dt_situacao_especial', 949, 8)
]

for p in positions:
    col_name = p[0]
    start = p[1] - 1
    end = start + p[2]
    df[col_name] = df.raw.str[start:end].str.strip()  # strip to trim whitespace

df.drop(columns='raw', inplace=True)

df.to_csv('parsed.csv', index=False)
