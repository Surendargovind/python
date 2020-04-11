import requests
from bs4 import BeautifulSoup

def check(prompt):
    while True:
        value = input(prompt).upper()
        if value == "YES" or value == "NO":
            break
        else:
            print("Please enter either YES or NO")
            continue
    return value

def ag(prompt):
    while True:
        val=int(input(prompt))
        if val in range(1, 100):
            break
        else:
            print("Enter valid age")
            continue
    return val

def gd(prompt):
    while True:
        r= input(prompt).upper()
        if r == "M" or r == "F":
            break
        else:
            print("Please enter Gender as M or F")
            continue
    return r
age = ag("\nEnter your age :")
gen=gd("\nEnter your gender M/F : ")
print("\nPlease enter Yes or No for the following questions".upper())
print("""\nNormal body temperature :96 to 98.6 F,
body Temperature for fever : 98.6 to 102 F,
High Fever : greater than 102 F""")
temp=check("\nYour body temperature is > 98.6 F :")
sor = check("\nSore throat ???? :")
smel = check("\nLoss sense of smell ??? :")
coug = check("\nSevere Cought ??? :")
breat = check("\n Difficulty in Breathing ??? :")

print("\n----------RESULT-------------")

if age >= 50:
    print("\npeople greater than 50 age are at highest risk from COVID-19.So please stay safe".upper())
elif temp=="YES" and sor=="YES" and smel=="YES"and coug=="YES" and breat=="YES":
    print("\nYOURE INFECTED BY COVID-19 VIRUS.PLEASE VISIT NEARBY HOSPITAL".upper())
elif sor=="YES" or smel=="YES" or coug=="YES" or breat=="YES" or temp=="YES":
    print("\nYou have covid-19 virus symptoms.Please stay isolated".upper())
else:
    print("\nYou're Normal".upper())

print("\n----------ALERT-------------")

print("""\n\nSTAY HOME.SAVE LIVES ,
\nHelp stop coronavirus,
\nSTAYhome,
\nKEEPa safe distance,
\nWASHhands often,
\nCOVERyour cough,
\nSICK?Call the helpline""")
print("\nCoronovirus status in usa".upper())
response=requests.get("https://www.worldometers.info/coronavirus/country/us/")
soup=BeautifulSoup(response.content,"html.parser")
data=soup.find("tr",attrs={"class":"total_row"})
result=data.text
lst=list(result.split())
print("\nTotal Number of Coronavirus Cases in United states :" +lst[1])
print("\nTotal Number of New cases  :" +lst[2])
print("\nTotal Number of Deaths in United states  :" +lst[3])
print("\nTotal Number of New Dealth  :" +lst[4])
print("\nTotal Number of Active cases  :" +lst[5])
print("\nTotal Number of cases as per in 1 Million population  :" +lst[6])
print("\nTotal Number of Death as per in 1 Million population  :" +lst[7])
print("\nNumber of person tested in United states :" +lst[8])
print("\nNumber of test  as per in 1 Million population  :" +lst[9])
