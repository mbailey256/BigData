import os
import sys
#import pandas as pd

for f in os.listdir("./data"):
	os.system(" cd tmp; unzip ../data/%s" % f)
	csv_file = f.replace(".zip", ".csv")
#	data = pd.read_csv("tmp/%s" % csv_file)
#	import pdb; pdb.set_trace()	
