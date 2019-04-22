from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render_to_response
from django.template import RequestContext
# from .sum import *
# from .deduplicate import *
# Create your views here.

# def rome(request):
# 	return HttpResponse('<h1> it is displaying </h1>')








import sys
from django.http import HttpResponse

def print_http_response(f):
    """ Wraps a python function that prints to the console, and
    returns those results as a HttpResponse (HTML)"""

    class WritableObject:
        def __init__(self):
            self.content = []
        def write(self, string):
            self.content.append(string)

    def new_f(*args, **kwargs):
        printed = WritableObject()
        sys.stdout = printed
        f(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return HttpResponse(['<BR>' if c == '\n' else c for c in printed.content ])
    return new_f



# @print_http_response
def rome(request):
   # print ("some output here")
   # return HttpResponse('<h1> it is displaying </h1>')
   # return render(request,'homepage.html')



   import pandas as pd
   import numpy as np
   normal = pd.read_csv('home/normal.csv')
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
   printable = final.to_dict(orient='records')
   # printable = printable.objects.all()
   # printable = final.values.tolist()
	# print(printable)
		# return {
	 #        "printable": printable
	 #    }
   return render_to_response('homepage.html', {'results': printable,'dup': len(printable),'original':len(normal)}, RequestContext(request)) 
