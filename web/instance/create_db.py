# create_db.py

import os, sys
sys.path.append(os.getcwd())
from project.app import db

if __name__=='__main__':
	db.create_all()
