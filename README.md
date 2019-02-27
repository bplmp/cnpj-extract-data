# Extract CNPJ data

A simple script to extract CNPJ data based on a column value. The unzipped CNPJ data for all Brazil is about 90 GB. This script unzipped and then extracted all lines with a specific CNAE code in about 45 min.

## Requirements

- `sudo apt-get install p7zip-full` for extracting data zip file.
- `sudo apt-get install parallel` for parallel processing, since the file is so large.

Need to use 7zip because file seems to be corrupted.

## Usage

1. Download zip file with data from [here](http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj).
2. Alter `regexp.txt` for the pattern you are looking for. In the example, I'm looking for `8112500`, which is the [CNAE code](https://cnae.ibge.gov.br/?view=subclasse&tipo=cnae&versao=10&subclasse=8112500&chave=condom%C3%ADnio) for condominiums. Note that the data is position delimited, so you might have to change the position in the regexp. Take a look at the [data layout file here](https://fazendagovbr.sharepoint.com/sites/MFDATA/RFB/LAYOUT_DADOS_ABERTOS_CNPJ.pdf).
3. Allow script to execute with `sudo chmod +x extract-data.sh`.
4. Run with `./extract-data.sh`.
