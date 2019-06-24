import requests, json, re
import gzip, shutil, os
import pandas as pd
import io, sys
#from colored import fore, back, style

def do_file (dir_name):
	if os.path.exists(dir_name):
		shutil.rmtree(dir_name)
	os.mkdir(dir_name)

def download(fid):

	data_endpt = "https://api.gdc.cancer.gov/data/{}".format(fid)
	response = requests.get(data_endpt, headers = {"Content-Type": "application/json"})
	response_head_cd = response.headers["Content-Disposition"]
	file_name = re.findall("filename=(.+)", response_head_cd)[0]
	with open(file_name, "wb") as output_file:
    		output_file.write(response.content)
	fext = os.path.splitext(file_name)[1]
	print(file_name)
	if fext == ".gz":
		cmd = "gunzip " + file_name
		os.system(cmd)

	return(file_name)

dirname = sys.argv[1]

db = pd.read_csv("../Database/" + dirname + "-mirna.tsv", sep='\t')
db = db[db.mirna_count != 0]

do_file(dirname)
os.chdir('../Database/' + dirname)

do_file('RNAseq')

do_file('miRNA')

#print(fore.LIGHT_BLUE + style.BOLD + "Downloading RNAseq data..." + style.RESET)
print("Downloading RNAseq data...")
os.chdir("RNAseq")

with open("index.txt", mode='w+') as rna_file: 
	for i,row in db.iterrows():		
		print(i)
		file_name = download(row['rnaseq_fid'])
		case_ID = row["case"]
		rna_file.write(case_ID + "\t" + file_name + '\n')
os.chdir("..")

#print(fore.LIGHT_BLUE + style.BOLD + "Downloading miRNA data..." + style.RESET)
print("Downloading miRNA data...")
os.chdir("miRNA")

with open("index.txt", mode='w+') as mirna_file:
	for i,row in db.iterrows():
		print(i)
		file_name = download(row['mirna_fid'])
		case_ID = row["case"]
		mirna_file.write(case_ID + "\t" + file_name + '\n')
os.chdir("..")