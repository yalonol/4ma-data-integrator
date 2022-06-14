import yaml
import json
import os
from dotenv import load_dotenv
from dataclasses import dataclass, field, InitVar
from com.fourm.common.vault_utils.vault import Vault

@dataclass
class Config:
    def __init__(self, config_path):
        with open(config_path, 'r') as main_file:  
            main_config = yaml.safe_load(main_file)
            self.PHASE_ID: int           = None
            self.WORK_UNIT_ID: int       = None

            self.LOG_FILE_BASE           = main_config["LOG_FILE_BASE"]
            self.FILE_ENCODING           = main_config["FILE_ENCODING"]
            self.LAST_MODIFIED_FORMAT    = main_config["LAST_MODIFIED_FORMAT"]
            self.DATE_TIME_FORMAT        = main_config["DATE_TIME_FORMAT"]
            self.VERSIONING_FORMAT       = main_config["VERSIONING_FORMAT"]
            self.CRS_TYPE                = main_config["CRS_TYPE"]
            self.VERBOSE                 = main_config["VERBOSE"]
            self.WARNINGS_ALERT          = main_config["WARNINGS_ALERT"]

            self.VAULT_TOKEN             = os.getenv('VAULT_TOKEN')
            self.VAULT_URL               = main_config["VAULT_URL"]
            self.SECRET_PATH             = main_config["SECRET_PATH"]
            
            vault                        = Vault(vault_url = self.VAULT_URL, secret_path = self.SECRET_PATH, token = self.VAULT_TOKEN)
            self.GOOGLE_CREDENTIALS:dict = vault.get_credentials()
            
        
