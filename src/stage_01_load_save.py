import argparse
import pandas as pd
from utils.all_utils import read_yaml,create_directory
import os

def get_data(config_path):
    config=read_yaml(config_path)
    remote_data_path =config["data_source"]
    df=pd.read_csv(remote_data_path,sep=";")
    artifects_dir=config['artifacts']['artifacts_dir']
    raw_local_dir=config['artifacts']['raw_local_dir']
    raw_local_file=config['artifacts']['raw_local_file']


    raw_local_dir_path=os.path.join(artifects_dir,raw_local_dir)
    raw_local_file_path=os.path.join(raw_local_dir_path,raw_local_file)
    create_directory(dirs=[raw_local_dir_path])
    print(raw_local_file_path)
    df.to_csv(raw_local_file_path,sep=",",index=False)
    

'''
def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)
        print(f"directory is created at {dir_path}")

'''
if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    parsed_args=args.parse_args()
    get_data(config_path=parsed_args.config)


