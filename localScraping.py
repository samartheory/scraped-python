# This is the basic code for using the beautiful soup lib. 
from bs4 import BeautifulSoup

with open('kane.html','r') as loc: #“With” command in python code not in lib. It helps in dealing with files
   content = loc.read()             #loc is the name for the file 'r' specifies the read operation

#lxml is another package we installed 
soup=BeautifulSoup(content,'lxml')
#print(soup.prettify())


spec=soup.find('a')#find func helps us to find the 
#print(spec)        #instances of a tag we can replace the tagname to our liking
                   #if we want to print all the instances of a tag we can use "find_all()"

with open('jimshaped.html','r') as loc2:#we open another file using the same fucntion
   content2 = loc2.read()

jim=BeautifulSoup(content2,'lxml')
mainBo=jim.find_all('div',class_='card-body') #we can target the specified class of a tag using this syntax

for courses in mainBo:   #we run a loop to cycle through all the divs with class cadr-body which we specified above
   coursename=courses.h5.text  #this way we can select any tag inside a tag **.text can select only the text part
   courseprice=courses.a.text.split()[-1] #we splt the string and select the last element 
   print(f"Get {coursename} for {courseprice}") #we print them using dynamic string
