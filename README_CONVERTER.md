# Conversor de PDF para Texto - CardioIA

Esta aplicação converte automaticamente todos os arquivos PDF na pasta `docs/` para formato de texto (.txt) e os organiza na pasta `docs/.txt/`.

## Pré-requisitos

1. Python 3.7 ou superior
2. Instalar as dependências:

```bash
pip install -r requirements.txt
```

## Como usar

### Método 1: Execução simples
```bash
python run_converter.py
```

### Método 2: Execução completa
```bash
python pdf_converter.py
```

## Estrutura de arquivos

```
CardioIA.Batimentosdedados/
├── docs/
│   ├── *.pdf                    # Arquivos PDF originais
│   └── .txt/                    # Arquivos .txt convertidos (pasta existente)
├── pdf_converter.py             # Aplicação principal
├── run_converter.py             # Script de execução simples
├── requirements.txt             # Dependências
└── README_CONVERTER.md          # Este arquivo
```

## Funcionalidades

- **Conversão automática**: Encontra e converte todos os PDFs na pasta docs/
- **Múltiplos métodos**: Usa pdfplumber como método principal e PyPDF2 como fallback
- **Organização automática**: Cria a pasta .txt/ automaticamente
- **Logs detalhados**: Mostra progresso e estatísticas da conversão
- **Tratamento de erros**: Continua a conversão mesmo se alguns arquivos falharem

## Arquivos atuais para conversão

- `1_diretriz_prevencao_cardiovascular_sbc_2013.pdf`
- `2_artigo_insuficiencia_cardiaca_scielo.pdf`  
- `3_relatorio_estatistica_cardiovascular_brasil_intro.pdf`

## Solução de problemas

### Erro de dependências
```bash
pip install --upgrade PyPDF2 pdfplumber
```

### Erro de permissões
```bash
chmod +x run_converter.py
chmod +x pdf_converter.py
```

### PDFs não encontrados
Verifique se os arquivos PDF estão na pasta `docs/` do projeto.

## Saída esperada

Após a conversão, você terá:
- `docs/.txt/1_diretriz_prevencao_cardiovascular_sbc_2013.txt`
- `docs/.txt/2_artigo_insuficiencia_cardiaca_scielo.txt`
- `docs/.txt/3_relatorio_estatistica_cardiovascular_brasil_intro.txt`

