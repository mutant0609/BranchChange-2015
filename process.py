#!/usr/bin/env python3
#import numpy as np
import csv
import re
import sys
import os

workpath=os.path.dirname(os.path.abspath(__file__))

from sys import argv
mainlist=[]
checklist=[]
branchlist=[]
cutoff=[]
def form_cutoff():
	for row in branchlist:
		cutoff.append([row,0])
# if eligible but cpi<9 then changes are being made un current strengtg.. no such change in cpi>9 case
def is_eligible(arg1,arg2,arg3):
	if(arg1 in branchlist): #arg1=name of branch B to which change is sought
		index=branchlist.index(arg1)
		line=mainlist[index]


		check_cutoff=cutoff[index]
		if((round(1.1*float(line[1]),0)-float(line[2])>0 or float(arg2)==float(check_cutoff[1])) and float(arg2)>=9.00): # arg2 is cpi of candidate
			line2=mainlist[branchlist.index(arg3)]
			line2[2]=str(float(line2[2])-1)
			mainlist[branchlist.index(arg3)]=line2

			line[2]=str(float(line[2])+1)
			mainlist[branchlist.index(arg1)]=line
			if round(1.1*float(line[1]),0)-float(line[2])==0:

				add_new=cutoff[index]
				add_new[1]=arg2
				cutoff[index]=add_new
			return True
		else:	# Take care to round off values being compared in if conditions in final work

			line2=mainlist[branchlist.index(arg3)] # arg3 is current branch
			if (round(0.75*float(line2[1]),0)<=float(line2[2])-1 and (round(1.1*float(line[1]),0)-float(line[2])>0 or float(arg2)==float(check_cutoff[1])) and isfair(cpi=float(arg2),branchB=arg1)):

				line2[2]=str(float(line2[2])-1)
				mainlist[branchlist.index(arg3)]=line2

				line[2]=str(float(line[2])+1)
				mainlist[branchlist.index(arg1)]=line
				if round(1.1*float(line[1]),0)-float(line[2])==0:
					add_new=cutoff[index]
					add_new[1]=arg2
					cutoff[index]=add_new

				return True
			if(round(0.75*float(line2[1]),0)>=float(line2[2])-1):

				add_to_fairness_check(cpi=float(arg2),branchB=arg1)	#should add cpi, i.e. arg2 of candidate to a list under branch B, i.e. arg1
				return False

			else:
				return False
def tosort(row):
	word=row[0]

	lastletter=float(word[-1:])
	return (lastletter,row[1])

def add_to_fairness_check(cpi,branchB):
	index=branchlist.index(branchB)
	line4=checklist[index]
	if float(cpi)>float(line4[1]):

		line4[1]=str(cpi)
		checklist[index]=line4

def isfair(cpi,branchB):
	index=branchlist.index(branchB)
	line3=checklist[index]	#checklist to maintain the fairness list.. i.e. highest cpi denied branch change due to rule ii
							#order same as mainlist
	if cpi<float(line3[1]):	#should be <= for fairness?

		return False
	else:

		return True

def form_checklist():

	for row in branchlist:
		checklist.append([row,0])# initially nobody is denied branch change
def form_branchlist():	#should be done before any changes to mainlist capacities
	#branchlist=[]
	for row in mainlist:
		branchlist.append(row[0])


#if(False):
    #print("You must provide exactly one command-line argument the input csv file!!!")
def main():

	with open(os.path.join(workpath,'./../media/documents/input_programmes.csv'), 'r') as capacities:
		for line in csv.reader(capacities):
			entry=line[1]
			if re.search(r"[0-9].*",entry):
				mainlist.append(line)
	a=0
	data = []
	capacities1=[]
	output=[]
	ineligiblemat=[]
	#script,filename = argv
	with open(os.path.join(workpath,'./../media/documents/input_options.csv'), 'r') as csvfilename:
		with open(os.path.join(workpath,'cpi_sorted.csv'), 'w') as cpi_sorted:
			writer = csv.writer(cpi_sorted)
			for row in csv.reader(csvfilename):
				new=[]
				entry = row[0]
				if re.search(r"[0-9].*",entry):
					for word in row:
						if len(word) !=0:
							new.append(word)
					data.append(new)
			writer.writerows(sorted(data, key=lambda row: float(row[3]), reverse=True))
	with open(os.path.join(workpath,'./../media/documents/input_programmes.csv'), 'r') as csvfilename:
		for row in csv.reader(csvfilename):
			capacities1.append(row)
	eligiblemat=sorted(data, key=lambda row: float(row[3]), reverse=True)
	header=['RollNumber', ' Name', ' Current Branch', 'Destination Branch'];
	j=0
	while j<len(eligiblemat):

		row=eligiblemat[j]
		if((row[4]=='GE' or row[4]=='OBC') and float(row[3])<8.00):

			ineligible=eligiblemat[j]
			ineligiblemat.append([ineligible[0],ineligible[1],ineligible[2],'Ineligible'])
			del eligiblemat[j]
			j=j-1
		elif((row[4]=='GE' or row[4]=='OBC')):
			j=j+1
			continue
		else:

			if (float(row[3])<7.00):

				ineligible=eligiblemat[j]
				ineligiblemat.append([ineligible[0],ineligible[1],ineligible[2],'Ineligible'])
				del eligiblemat[j]
				j=j-1
		j=j+1

	with open(os.path.join(workpath,'eligible.csv'), 'w') as eligible:
		writer=csv.writer(eligible)
		writer.writerows(eligiblemat)
	toprocess=eligiblemat

	prev=[]
	final=[]
	temp=[]

	prev_unhappy=[]
	unhappy=[]

	form_branchlist()
	form_checklist()
	form_cutoff()
	i=0
	while True:

		prev=temp

		prev_unhappy=unhappy
		temp=[]
		unhappy=[]

		i=0
		while i<len(toprocess):

			words=toprocess[i]
			j=5

			while j<len(words) :

				if ([words[0],words[1],words[2],words[j]] in prev):
					temp.append([words[0],words[1],words[2],words[j]])

					break
				if(is_eligible(arg1=words[j],arg2=words[3],arg3=words[2])):#to write suitable functions


					if j==5:

						final.append([words[0],words[1],words[2],words[j]])

						del toprocess[i]

						i=i-1
						break
					else:

						temp.append([words[0],words[1],words[2],words[j]])
						break
				j=j+1;
				if(j==len(words)):

					unhappy.append([words[0],words[1],words[2],'Branch Unchanged'])

			i=i+1
		if (0==len(toprocess)) or (temp==prev and prev_unhappy==unhappy):

			break

	if len(toprocess)==0:
		with open(os.path.join(workpath,'./../media/documents/allotment.csv'), 'w') as finalcsv:
			writer=csv.writer(finalcsv)
			final.insert(0,header)
			writer.writerows(final)
			writer.writerows(unhappy)
			writer.writerows(ineligiblemat)

	elif temp==prev:
		with open(os.path.join(workpath,'./../media/documents/allotment.csv'), 'w') as finalcsv:
			writer=csv.writer(finalcsv)

			final.insert(0,header)
			writer.writerows(final)
			writer.writerows(temp)
			writer.writerows(unhappy)
			writer.writerows(ineligiblemat)
	with open(os.path.join(workpath,'./../media/documents/output_stats.csv'),'w') as finconfig:
		writer=csv.writer(finconfig)
		writer.writerows(mainlist)
		writer.writerows(checklist)
		writer.writerows(cutoff)
	total=[]
	''''''
	with open(os.path.join(workpath,'./../media/documents/allotment.csv'), 'r') as fin:
		for row in csv.reader(fin):
			total.append(row)

	with open(os.path.join(workpath,'./../media/documents/allotment.csv'),'w') as tocheck:
		writer=csv.writer(tocheck)
		total.remove(header)
		total=sorted(total, key=tosort)
		total.insert(0,header)
		writer.writerows(total)

