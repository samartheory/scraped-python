from bs4 import BeautifulSoup
import requests #we use another library "requests" which helps us getting html of websites
minemp = int(input('Set minimum employees'))
fullHTML = requests.get('https://angel.co/jobs').text
soup = BeautifulSoup(fullHTML,'lxml')
blocks = soup.find_all('div',class_='styles_component__15ev_ !border-landing-gray')

'''in the loop below we have made a function which prints the information of company
only if the employee no. is > minemp
'''
for idx,block in enumerate(blocks):
    emp = block.find('span',class_='__halo_fontSizeMap_size--2xs __halo_lineHeight_comfortable __halo_fontWeight_medium __halo_color_slate--500 styles_uppercase__382zl').text
    emptemp=(emp.split("-",1))
    if len(emptemp)>1:
        empno = int(emptemp[0])
    else:
        empno = int(emptemp[0].split("+",1)[0])

    if empno>minemp :
        halo = block.find('div',class_='styles_component__1WTsC styles_flexColumn__1dh8k __halo_padding_left_2').h4.text
        loca=block.find('span',class_='__halo_fontSizeMap_size--sm __halo_color_slate--900').text.split("•",1)[0]
        with open('texts/data.txt','a') as s: #this part appends the already existing file if the files dosent exist then it makes a new one
            s.write(f'{halo} based in {loca} with {emp} \n')
           # s.write('\n')