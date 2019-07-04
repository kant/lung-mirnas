# lung-mirnas
Proyecto para procesar RNAseq y miRNAs para cáncer de pulmón.

## Contenido de Carpetas

- **Database (4 files)**    
   Esta carpeta es **fija** y contine los archivos originales (manifest) de los diferentes tipos de tejido de cancer de pulmón (NAD.txt, TAD.txt, NSC.txt, TSC,txt).

- **Data (2 directories)**  
   Carpeta **generada**. Contiene 2 directorios: "Adeno" & "Squamous", que contienen toda la informacion porducida de estos dos tipos grupos de tejido. 
     
   Hay 4 directorios (NAD,TAD,NSC & TSC); cada uno contiene un archivo de cuentas de RNASeq y otro de miRNASeq.
   
- **Graphs (2 files)**  
   Carpeta **generada** con 2 archivos ".png".
   - no_mirnas_ALL.png: Gráfica de cantidad de miRNAs por RNA de los 4 tipos de tejido.
   - no_files.png: Gráfica de cantidad de archivos descargados de RNASeq y de miRNASeq de los 4 tipos de tejido.

- **json (2 files)**  
   Carpeta **fija** con 2 scripts.
   - qbyfileid.json: Script para hacer el query a "The Cancer Genome Atlas" (TCGA) y obtener los CaseID a partir de los archivos manifest.
   - qbyMIRNA.json: Script que ayudara a obtener los nombres de los archivos a descargar a partir de CaseID.
   
- **pipeline (1 file)**  
   - biomart-20181212.txt: Archivo con la anotación de todos los genes de *Homo sapiens*, a partir de donde se mapearan los genes  obtenidos de los archivos de RNASeq. 

- **py (6 files)**  
   Carpeta **fija** con 6 scripts.
   - Util.py: Libreria creada para la descarga de información.
   - casemirna.py: Script para obtener rnaseq_fid, cantidad de mirnas, mirna_fname y el mirna_fid a partir de los CaseID
   - downdata.py: Script para bajar archivos de cuentas de RNASeq y de miRNASeq y dentro de crapetas, ademas crear un archivo llamado "index.txt" con un listado de tosos los archivos descargados.   
   - file_number.txt: Script para saber el numero de archivos de raw counts se tienen tanto de RNASeq como de miRNASeq y hacer graficas  
   - getcases.py: Script para obtener los caseID a partir de archivos manifest
   - getmirnasCounts.py: Script para graficar el numero de miRNAs de NAD,TAD,NSC y de TSC
  
- **R (4 files)**  
   Carpeta **fija** con 4 scripts.
   - 01-Rectify_rnaSeq.R: Script para procesar la información.
   - 02-PRE-QC.R: Script que hace un pre-control de calidad a los datos y genera plots.
   - 03-NORM.R: Script para realizar la normalizacion de la información.
   - 04-POST-QC.R: Script que hace un post-control de calidad a los datos.

   

# Instrucciones para procesar los datos

## Prerrequistos
 - Python (3.7.3)
 - librerias python (matplotlib.pyplot, numpy, glob, pandas, json, requests, re, gzip, shutil)
 - R (3.6.0)
 - librerias R (BiocParallel, parallel, NOISeq, EDASeq)

## Descarga de los datos (python)
   1. `bash sh/downdata.sh` [Descarga de datos de RNASeq y miRNASeq; Gráfica de miRNAs y de Archivos]

## Control de calidad y normalizacion (R)
   1. `Rscript --vanilla R/01-Rectify_rnaSeq.R Adeno` [Preprocesamiento de archivos]
   2. `Rscript --vanilla R/02-PRE-QC.R Adeno` [Control de calidad, graficas de los datos obtenidos]
   3. `Rscript --vanilla R/03-NORM.R Adeno` [Normalización]


 
 

