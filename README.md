# Extract CNPJ data

A simple script to extract [public CNPJ (Brazilian business tax)](http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj) data based on a column value.

The unzipped CNPJ data for all Brazil is about 90 GB. This script unzipped and then extracted all lines with a specific CNAE code in about 45 min on my laptop.

## Requirements

- [GNU Parallel](https://www.gnu.org/software/parallel/) for parallel processing, since the file is so large.
- [7zip](https://www.7-zip.org/) (recommended) for extracting data zip file. I had to use 7zip because file seemed to be corrupted.

### Installation

#### GNU Parallel

- Ubuntu: `sudo apt-get install parallel`
- Mac: `brew install parallel`.

#### 7zip

- Ubuntu: `sudo apt-get install p7zip-full`
- Mac: `brew install p7zip`

## Usage

1. Download zip file with CNPJ data from [here](http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj). Attention: the file is large and their server is usually slow. I recommend dowloading with [lftp](https://en.wikipedia.org/wiki/Lftp) or [wget](https://en.wikipedia.org/wiki/Wget).
2. Extract the zip file. I had to use 7zip to do that, by running `7z x DOWNLOADED_ZIP_FILE.zip`, because the file seemed to be corrupted and 7zip was the only utility that managed to extract it properly.
3. Alter `regexp.txt` for the pattern you are looking for. In the example, I'm looking for `8112500`, which is the [CNAE code](https://cnae.ibge.gov.br/?view=subclasse&tipo=cnae&versao=10&subclasse=8112500&chave=condom%C3%ADnio) for condominiums, and starts at position 376 (375 in the regex because it is zero-indexed). Note that the data is position delimited, so you will have to change the position in the regexp if you're filtering for a different column. Take a look at the [data layout file here](https://fazendagovbr.sharepoint.com/sites/MFDATA/RFB/LAYOUT_DADOS_ABERTOS_CNPJ.pdf).
4. Allow script to execute with `sudo chmod +x extract-data.sh`.
5. Run with `./extract-data.sh EXTRACTED_ZIP_FILENAME`.
