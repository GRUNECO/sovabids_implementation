import os # For path manipulation
#import shutil # File manipulation
from sovabids.rules import apply_rules # Apply rules for conversion
from sovabids.convert import convert_them # Do the conversion
#from sovabids.datasets import lemon_prepare # Download the dataset
from sovabids.settings import REPO_PATH

current = os.getcwd()
sourcePath= os.path.join(current,'database')
bidsPath = os.path.join(current,'database_bids')
os.makedirs(bidsPath,exist_ok=True)
rulePath= os.path.join(current,'reglasBiomarcadores.yml')

source_path = os.path.abspath(sourcePath) # For the input data we will convert
bids_path= os.path.abspath(bidsPath) # The output directory that will have the converted data
rules_path = os.path.abspath(rulePath) # The rules file that setups the rule for conversion
mapping_path = os.path.abspath(os.path.join(bids_path,'code','sovabids','mappings.yml')) # The mapping file that will hold the results of applying the rules to each file


print('source_path:',source_path.replace(REPO_PATH,''))
print('bids_path:', bids_path.replace(REPO_PATH,''))
print('rules_path:',rules_path.replace(REPO_PATH,''))
print('mapping_path:',mapping_path.replace(REPO_PATH,''))

with open(rules_path,encoding="utf-8") as f:
    rules = f.read()
    print(rules)

apply_rules(source_path,bids_path,rules_path,mapping_path)
convert_them(mapping_path)
