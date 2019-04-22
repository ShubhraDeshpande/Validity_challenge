import pandas as pd
import numpy as np

def dup(file):
	normal = pd.read_csv(file)
	seen = set()
	unique_email_id =[]
	for i in range(len(normal)):
		if normal['email'][i] not in seen:
			unique_email_id.append(normal['id'][i])
			seen.add(normal['email'][i])
	u_email= pd.DataFrame()
	DG=normal.groupby(['email'])
	uni_email_pd = pd.concat([DG.get_group(item) for item, value in DG.groups.items() if len(value)==1])
	DG1 = uni_email_pd.groupby(['phone'])
	uni_phone_pd = pd.concat([DG1.get_group(item) for item, value in DG1.groups.items() if len(value)==1])
	DG2 = uni_phone_pd.groupby(['address1'])
	uni_add1_pd = pd.concat([DG2.get_group(item) for item, value in DG2.groups.items() if len(value)==1])
	final1 = uni_add1_pd
	final1["name"] = final1["first_name"].map(str) + final1["last_name"]
	DG3 = final1.groupby(['name'])
	final = pd.concat([DG3.get_group(item) for item, value in DG3.groups.items() if len(value)==1])
	experiment = uni_add1_pd
	experiment["name"] = experiment["last_name"].map(str) + experiment["first_name"]
	DG3 = experiment.groupby(['name'])
	final = pd.concat([DG3.get_group(item) for item, value in DG3.groups.items() if len(value)==1])
	final = final.drop(['id'], axis=1)
	final = final.reset_index()
	printable = final.values.tolist()
	# print(printable)
	return {
        "printable": printable
    }

printable = dup('home/normal.csv')
