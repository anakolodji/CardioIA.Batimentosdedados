# CardioIA.Batimentosdedados

# CardioIA: Base de Dados para Simulação de Ecossistema de Cardiologia Inteligente

Este repositório organiza uma coleção de dados públicos e multimodais para alimentar os futuros módulos de inteligência artificial do projeto CardioIA. O objetivo é construir uma base de dados sólida e clinicamente relevante que simule um ecossistema de cardiologia, abrangendo as três modalidades de informação mais críticas para a análise clínica: dados numéricos de pacientes, conhecimento textual médico e evidências visuais de exames.

A curadoria foi dividida em três categorias principais, cada uma contida em sua respectiva subpasta e acessível através de links públicos.

# Descrição das Categorias de Dados

## Parte 1: Dados Numéricos de Pacientes Cardíacos
Esta seção contém arquivos de dados estruturados com variáveis de pacientes, essenciais para treinar modelos de predição de risco, estratificação de pacientes e análise de tendências epidemiológicas.

Objetivo: Reunir conjuntos de dados públicos contendo variáveis clínicas e comportamentais como idade, sexo, pressão arterial, colesterol, glicose, fatores de estilo de vida (tabagismo, álcool, atividade física) e desfechos clínicos.

Conteúdo:

### 1_cardiovascular_disease_kaggle.csv 
Descrição: Um conjunto de dados em larga escala com 70.000 registros de pacientes e 11 características, ideal para predição de risco geral. Ele categoriza de forma única as características como Objetivas, de Exame e Subjetivas, fornecendo uma estrutura clara para análise.   

Variáveis Notáveis: Idade (em dias), altura, peso, gênero (codificado como 1: mulheres, 2: homens), pressão arterial sistólica/diastólica (ap_hi, ap_lo), colesterol e glicose (categóricos: 1-normal, 2-acima do normal, 3-muito acima do normal) e fatores de estilo de vida chave (smoke, alco, active).   

Relevância Clínica: Seu grande volume e a inclusão de fatores comportamentais o tornam inestimável para treinar modelos de base robustos que podem identificar a importância relativa dos marcadores de estilo de vida versus os clínicos.


### 2_heart_disease_uci_consolidado.csv
Descrição: Um conjunto de dados clássico e amplamente citado, originário de quatro bancos de dados (Cleveland, Hungria, Suíça e Long Beach V.A.) de 1988. Ele se concentra em um conjunto mais granular de 14 atributos clínicos.

Variáveis Notáveis: Idade (em anos), sexo (1: masculino, 0: feminino), tipo de dor no peito (cp), pressão arterial em repouso (trestbps), colesterol sérico (chol), glicemia de jejum (fbs), resultados do ECG em repouso (restecg), frequência cardíaca máxima (thalach) e depressão do segmento ST (oldpeak).

Relevância Clínica: Este conjunto de dados é a referência para tarefas de predição clínica. Suas características estão diretamente ligadas a procedimentos diagnósticos (por exemplo, testes de esforço, leituras de ECG), tornando-o perfeito para construir modelos que imitam os caminhos de tomada de decisão clínica.

### 3_framingham_heart_study_kaggle.csv
Esses conjuntos de dados acompanham os pacientes ao longo do tempo, permitindo a modelagem da progressão da doença e do risco a longo prazo — uma capacidade muito mais avançada.

Descrição: Uma pedra angular da epidemiologia cardiovascular, este conjunto de dados inclui mais de 4.200 registros com o objetivo específico de prever o risco de doença cardíaca coronária (DCC) em 10 anos.

Variáveis Notáveis: Inclui fatores de risco padrão, além de variáveis como nível de escolaridade (education), cigarros por dia (cigsPerDay) e uso de medicação (BPMeds).

Relevância Clínica: Este é o padrão-ouro para a modelagem de risco a longo prazo. Qualquer módulo de estratificação de risco dentro do CardioIA deve ser comparado com modelos treinados com esses dados. Ele permite passar da pergunta "Este paciente tem doença cardíaca?" para "Qual é o risco deste paciente de desenvolver doença cardíaca na próxima década?".

Fontes Principais: Kaggle , UCI Machine Learning Repository.

## Parte 2: Textos sobre Saúde Cardiovascular
Esta seção reúne uma coleção de arquivos de texto (.txt) para treinar os módulos de Processamento de Linguagem Natural (PLN) do CardioIA, permitindo que o sistema compreenda o contexto clínico, as diretrizes e a narrativa do paciente.

Objetivo: Construir um corpus diversificado com textos normativos, científicos e narrativos sobre doenças cardíacas, tratamentos e saúde pública.

Conteúdo:

### 1_diretriz_prevencao_cardiovascular_sbc_2013.txt
Texto da "I Diretriz Brasileira de Prevenção Cardiovascular" da Sociedade Brasileira de Cardiologia, representando o padrão-ouro da prática clínica no Brasil.

Relevância Clínica: Este texto é o código-fonte para sistemas especialistas baseados em regras. Ele contém lógica explícita do tipo "se-então" (por exemplo, "Se o paciente tem X, recomenda-se Y com evidência de Classe I"). Isso pode ser usado para validação de modelos e para a construção de módulos de IA explicável.

### 2_artigo_insuficiencia_cardiaca_scielo.txt
Artigo científico da base SciELO sobre fisiopatologia e tratamento da insuficiência cardíaca, rico em terminologia clínica.

Relevância Clínica: Estes textos são cruciais para treinar modelos de Reconhecimento de Entidades Nomeadas (NER) para identificar conceitos clínicos chave: doenças, sintomas, medicamentos, dosagens e desfechos.

### 3_relatorio_estatistica_cardiovascular_brasil_intro.txt
Texto introdutório da publicação "Estatística Cardiovascular – Brasil", fornecendo o contexto epidemiológico nacional.

Relevância Clínica: Este corpus fornece o contexto epidemiológico. Modelos treinados com esses dados podem compreender tendências em nível populacional, o que é vital para módulos focados em saúde pública dentro do CardioIA.

### Textos Narrativos e Históricos - Projeto Gutenberg 
4_gutenberg_cases_organic_diseases_heart.txt: Texto médico histórico do Projeto Gutenberg, descrevendo sintomas cardíacos em linguagem arcaica, útil para treinar modelos robustos à variedade linguística dos pacientes.

5_gutenberg_disturbances_of_the_heart.txt: Discute arritmia e fibrilação em termos médicos do início do século XX.

6_gutenberg_arteriosclerosis_hypertension.txt: Fornece contexto histórico sobre a compreensão da hipertensão e da angina.

Fontes Principais: Sociedade Brasileira de Cardiologia (SBC) , SciELO , Biblioteca Virtual em Saúde (BVS) , Projeto Gutenberg.

Relevância Clínica: Estes textos são essenciais para construir modelos de PLN robustos que possam compreender os desfechos e as descrições relatados pelos pacientes. Um paciente não dirá "Estou experimentando dispneia paroxística noturna", mas pode dizer "Acordo ofegante". Esses textos ajudam a preencher essa lacuna linguística.

## Parte 3: Imagens Médicas de Eletrocardiogramas (ECG)
Esta seção foca em imagens de ECG, uma modalidade de exame fundamental, de baixo custo e rica em informações para o diagnóstico cardiológico.

Objetivo: Reunir imagens de ECG (.jpg ou .png) que representem diversas condições cardíacas, servindo como base para o desenvolvimento dos módulos de visão computacional do CardioIA.

Conteúdo:

links_ecg_datasets.txt: Um arquivo de texto contendo link para as pastas dos principais conjuntos de dados públicos de imagens de ECG. Esses repositórios contêm milhares de imagens categorizadas, incluindo:

ECG Images Dataset of Cardiac Patients (Kaggle): Imagens classificadas como Infarto do Miocárdio, Batimento Cardíaco Anormal, Histórico de Infarto e Normal.

Fontes Principais: Kaggle.

OB> Em minha pesquisa encontrei também um conjunto de dados único que inclui não apenas as imagens de ECG plotadas, mas também os dados brutos do sinal e fotos dos ECGs capturados usando vários métodos do mundo real (por exemplo, câmera de celular), simulando a prática clínica, que podem ser  de grade relevância ao uso prátco da app, e podem ser adicionados quando necessário.

# Acesso ao Conjunto Completo de Dados
Os arquivos de dados preparados e organizados para este projeto estão disponíveis para download através dos seguintes links públicos do Google Drive:

Link para Dados Numéricos: `https://drive.google.com/drive/folders/1U3HpAUx64SHBys3dACNnIAp2ll-2VEJs?usp=drive_link`

Link para Dados Textuais: `https://drive.google.com/drive/folders/1cSdpPSWXBGtvLjdPmsR83QNLCTNX47X-?usp=drive_link`

Link para Imagens de ECG: `https://drive.google.com/drive/folders/1tmdrS3BdXi10zUFHADl3NoW_LBNG4Kox?usp=drive_link`
 
Qualquer dúvida entre em contato!