from datetime import datetime
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")

### Configuration PROCON CNRF

## GCP pointing ------------

# GCP project name
project = 'dev-data'

# GCP bucket name
bucket_name = 'bvs-bigdata-datalake-stage-external-cadastral-rf-dev'

# Blob path
blob_path1 = 'datalake/stage/external/cadastral/rf/data/procon_cnrf/partitions/monthly/' + str(year) + '/' + str(month) + '/'
blob_path2 = 'datalake/stage/external/cadastral/rf/data/procon_cnrf_log/partitions/monthly/' + str(year) + '/' + str(month) + '/'



## File Names ------------

# file name to save logging information
log_filename = "procon_cnrf.log"

# File name to save the downloaded data
zip_filename = "data.zip"

# File name to save data in GCP
filename = "procon_cnrf.csv"



## Scrap definitions ------------

# Download URL 
url = 'http://dados.mj.gov.br/dataset/8ff7032a-d6db-452b-89f1-d860eb6965ff/resource/c2cce323-24c2-4430-8918-e24b2966213c/download/crf2019-dados-abertos.zip'

# Headers necessarry to request the data
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'} 

# Boolean for request certification on data request
certif = False