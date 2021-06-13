# Documentação | bot-procon Cadastro Ancional de Reclamações Fundamentadas

<br/>

## 1. Introdução

O bot procon foi desenvolvido para coletar dados disponíveis de Reclamações Fundamentadas - realizado no âmbito do PROCON: https://dados.gov.br/dataset/cadastro-nacional-de-reclamacoes-fundamentadas-procons-sindec1

Os dados são fornecidos através de um único endereço:

* URL: http://dados.mj.gov.br/dataset/8ff7032a-d6db-452b-89f1-d860eb6965ff/resource/c2cce323-24c2-4430-8918-e24b2966213c/download/crf2019-dados-abertos.zip

O endereço retorna os dados em arquivo compactado (zip), contendo um arquivo csv. O csv é extraído e armazenado na stage área.

OBS: A cada ano existirá um novo link para download das informações. A string deste novo endereço não pode ser inferida a partir do exemplo dos anos anteriores. Portano, o novo endereço deverá ser coletado e alterado no arquivo de confirguração do robo (variável: url)

<br/>

## 2. Resultado do bot (Outputs)

O bot irá gerar dois arquivos no final da execução.

* _procon_cnrf.csv: contém os dados das reclamações fundamentadas no PROCON em relação ao ano em específico.

```
-Formatação:
    Delimitação: ";"
    codificação: "uft-8"

-Campos:
	DataArquivamento
    DataAbertura
    CodigoRegiao
    Regiao
    UF
    strRazaoSocial
    strNomeFantasia
    Tipo
    NumeroCNPJ
    RadicalCNPJ
    RazaoSocialRFB
    NomeFantasiaRFB
    CNAEPrincipal
    DescCNAEPrincipal
    Atendida
    CodigoAssunto
    DescricaoAssunto
    CodigoProblema
    DescricaoProblema
    SexoConsumidor
    FaixaEtariaConsumidor
    CEPConsumidor
```

* _procon_cnrf.log: contém informações de log e tempo de execução do bot.
Obs.: Os arquivos contém uma "string" padrão no nome, com data e hora de execução.

```log
2021-06-04 14:50:34,631 - INFO - Conectado com sucesso no Bucket: bvs-bigdata-datalake-stage-external-cadastral-rf-dev
2021-06-04 14:50:35,713 - INFO - Download finalizado. URL: http://dados.mj.gov.br/dataset/8ff7032a-d6db-452b-89f1-d860eb6965ff/resource/c2cce323-24c2-4430-8918-e24b2966213c/download/crf2019-dados-abertos.zip: 
2021-06-04 14:50:37,784 - INFO - Arquivo salvo no BUCKET: <Bucket: bvs-bigdata-datalake-stage-external-cadastral-rf-dev> e BLOB: <Blob: bvs-bigdata-datalake-stage-external-cadastral-rf-dev, datalake/stage/external/cadastral/rf/data/PROCON/partitions/monthly/2021/06/20210604_145032_procon.csv, 1622818237718450>
2021-06-04 14:50:37,784 - INFO - Aplicação finalizada. Tempo de execução: 5.322484493255615s
```

<br/>

## 3. Funcionalidades

* O bot acessa a URL fornecida para baixaro arquivo compactado (zip) contendo o arquivo csv de dados.
* Valida a conexão com o bucket e projeto no GCP, em seguida cria o blob para o a sequência do trabalho.
* Realiza a descompactação do arquivo zip.
* Aciona a função de upload para o GCP, que subir os dados em um arquivo CSV.
* Armazena o log de processamento/execução do bot, no mesmo bucket e blob do arquivo CSV

<br/>

## 4. Conteúdo

O bot é composto por quatro arquivos:

* bot_procon.py: programação python para download e upload de dados.
* gcp_connect.py: programação python para fornecer conexão com o GCP.
* bot_config.py: programação python para fornecer os parametros e as configurações do bot.
    * GCP project, Bucket and Blob;
    * Nome dos arquivos;
    * Parametros de requisição.
* Dockerfile: script Docker para construir o container da aplicação.