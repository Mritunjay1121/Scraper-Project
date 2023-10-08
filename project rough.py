import urllib.request
from bs4 import BeautifulSoup
import requests
import difflib
import re

link=requests.get('https://en.wikipedia.org/wiki/Giordano_Bruno').text

soup=BeautifulSoup(link,'lxml')
body=soup.find('body')
print()
first_div=body.find('div',id='content',class_='mw-body',role='main')
first_h1=first_div.find('h1',id='firstHeading',class_='firstHeading').text
print()
bod = soup.find('div',class_='mw-parser-output')



#
# cc = bod.find('h3')
# def dfe(h2):
#
#     h2=h2.find_previous_sibling()
#     try:
#         if h2.name=='h2':
#             x=h2
#             print(x)
#             print()
#             return dfe(h2)
#     except:
#         if h2.name!='h2':
#             exit()
#
# #
#
#
#
#





parent_ul=bod.find('div',id='toc',class_='toc',role='navigation')
ul=parent_ul.find('ul')
li=ul.find_all('li')

all_headings=len(parent_ul.find_next_siblings(re.compile('^h[1-99]')))
print(all_headings)

# To find only direct children___not childrens of children
mains=len(ul.find_all('li',recursive=False))
print(mains)
c=0


# for aaa in range(mains):
# h3=parent_ul.find_next_sibling('h3')
# print(h3)
# print()
# dfeh(h3)

# dfe(h2)
    # if hh.name=='p':
    #     p

    # print(aaa)
# To find only direct children use "recursive=FALSE"
# lis=ul.find('li')
# print(len(lis))

# hh=lis.find_next_siblings('li')
# sub_headings=len(hh)+1
# kk=[]
# print("sub_headings",sub_headings)
# print("all_headings",all_headings)
# if lis.ul is None:
#     pass
# else:
#     kk.append(len(lis.ul.find_all('li')))
#
# for x in hh:
#     ab=x.ul
#     if x.ul is None:
#         kk.append(0)
#         # pass
#     else:
#         kk.append(len(ab.find_all('li')))
# print("list of no. of sub sub headings", kk)
#
# h2 = parent_ul.find_next_sibling('h2')
#
# span1=h2.find('span',class_='mw-headline')
# print(span1.text)
# h3_1=h2.find_next_siblings('h3',limit=kk[0])
#
#
#
# for aaa in h3_1:
#     span_h3 = aaa.find('span', class_='mw-headline')
#     print(span_h3.text)
# print()


# for x in kk[1:]:
#     h2=h2.find_next_sibling('h2')
#     span_h2_text=h2.find('span',class_='mw-headline')
#     print(span_h2_text.text)
#
#     h3=h2.find_next_siblings('h3',limit=x)
#
#     for ab in range(len(h3)):
#             aa=h3[ab]
#             try:
#                 ss=aa.find('span',class_='mw-headline')
#                 print(ss.text)
#             except:
#                 pass
    # dfeh(kyon)

    # print(kk)
    # print()





h2=bod.find('h2',recursive=False)
print(h2.text)
def dfeh(h3):

    h3=h3.find_next_sibling()
    try:
        if h3.name=='p':
            x=h3
            print(x)
            print()
            return dfeh(h3)
    except:
        if h3.name!='p' :

            exit()
for k in range(mains):

    def sff(h2):

        h2 = h2.find_next_sibling()
        # try:
        #     h3 = h2.find_next_sibling('h3')
        #     print(h3.text)
        #     dfeh(h3)
        # except:
        #     pass


        try:
            if h2.name == 'p':
                x = h2
                print(x)
                print()
                return sff(h2)
        except:
            if h2.name != 'p':
                exit()
    sff(h2)




