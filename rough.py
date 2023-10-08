import urllib.request
from bs4 import BeautifulSoup
import requests
import difflib
import re
kk='Giordano_Bruno'
q12='https://en.wikipedia.org/wiki/'+kk
link = requests.get(q12).text
final=[]
soup=BeautifulSoup(link,'lxml')
body=soup.find('body')
print()
first_div=body.find('div',id='content',class_='mw-body',role='main')
first_h1=first_div.find('h1',id='firstHeading',class_='firstHeading').text
print()
bod = soup.find('div',class_='mw-parser-output')


parent_ul=bod.find('div',id='toc',class_='toc',role='navigation')
ul=parent_ul.find('ul')
li=ul.find_all('li')

all_headings=len(parent_ul.find_next_siblings(re.compile('^h[1-99]')))
# print(all_headings)

# To find only direct children___not childrens of children
mains=len(ul.find_all('li',recursive=False))
# print(mains)


ab = []
for x in ul.find_all('li',recursive=False):
    hh=x.find_all('li')
    ab.append(len(hh))

# print(ab)
ddd=ab.index(0)
# print(ddd)
final.append(first_h1)
final.append("\n")
# print(first_h1)
hh = bod
kk = hh.find()
mainps=kk.find_next_sibling('h2').find_previous_siblings('p')
for dd in range(len(mainps)-1,-1,-1):
    final.append(mainps[dd].text)
    final.append("\n")
    # print(mainps[dd].text)

h2=bod.find()

kkk=ddd


# def h2p(p):
#
#     p=p.find_next_sibling()
#
#     if p.name=='h3' :
#
#         if p.name=='h3'and p.find_next_sibling().name=='h2':
#             print(p.text)
#
#             exit()
#         elif p.name == 'h3':
#
#             print(p.text)
#
#             return h2p(p)
#     if p.name=='blockquote' :
#
#         if p.name=='blockquote'and p.find_next_sibling().name=='h2':
#             print(p.text)
#
#             exit()
#         elif p.name == 'blockquote':
#
#             print(p.text)
#
#             return h2p(p)
#
#     if p.name=='p':
#         if p.name=='p'and p.find_next_sibling().name=='h2':
#             print(p.text)
#
#             exit()
#
#
#
#         elif p.name=='p':
#             print(p.text)
#
#             return h2p(p)
#
#     if p.name!='p' and p.name!='h3':
#
#         return h2p(p)
#     elif p.name != 'p' and p.name != 'h3' and p.find_next_sibling().name=='h2':
#         exit()

def h2p(p):

    p=p.find_next_sibling()
    try:

        if p.name=='h3' :

            if p.name=='h3'and p.find_next_sibling().name=='h2':
                final.append(p.text)
                final.append('\n')
                # print(p.text)

                return

            elif p.name == 'h3':
                final.append(p.text)
                final.append('\n')

                # print(p.text)

                return h2p(p)

        if p.name=='blockquote' :

            if p.name=='blockquote'and p.find_next_sibling().name=='h2':
                final.append(p.text)
                final.append("\n")
                # print(p.text)

                return
            elif p.name == 'blockquote':
                final.append(p.text)
                final.append("\n")

                # print(p.text)

                return h2p(p)



        if p.name=='p':
            if p.name=='p'and p.find_next_sibling().name=='h2':
                final.append(p.text)
                final.append("\n")
                # print(p.text)

                return




            elif p.name=='p':
                final.append(p.text)
                final.append("\n")
                # print(p.text)

                return h2p(p)



        if p.name!='p' and p.name!='h3':

            return h2p(p)
        elif p.name != 'p' and p.name != 'h3' and p.find_next_sibling().name=='h2':
            return
    except:
        pass









for headings in range(kkk):
    h2 = h2.find_next_sibling('h2')
    final.append(h2.text)
    final.append("\n")
    # print(h2.text)
    print()
    p = h2
    h2p(p)
afmain=h2

def jg(pp):

    pp=pp.find_next_sibling()
    try:

            if pp.name == 'ul':
                if pp.name == 'ul' and pp.find_next_sibling().name == 'h2':


                    lissss=pp.find_all('li')
                    # print(len(lissss))
                    for aa in lissss:
                        final.append(aa.text)
                        final.append("\n")
                        # print(aa.text)
                    return

                elif pp.name =="ul" and pp.find_next_sibling().name != 'h2':
                    lissss = pp.find_all('li')
                    # print(len(lissss))
                    for aa in lissss:
                        final.append(aa.text)
                        final.append("\n")
                        # print(aa.text)
                    return jg(pp)

            if pp.name == 'blockquote':

                if pp.name == 'blockquote' and pp.find_next_sibling().name == 'h2':
                    final.append(pp.text)
                    final.append("\n")
                    # print(pp.text)

                    return
                elif pp.name == 'blockquote':
                    final.append(pp.text)
                    final.append("\n")

                    # print(pp.text)

                    return jg(pp)

            if pp.name == 'p':
                if pp.name == 'p' and pp.find_next_sibling().name == 'h2':
                    final.append(pp.text)
                    final.append("\n")
                    # print(pp.text)

                    return

                elif pp.name == 'p':
                    final.append(pp.text)
                    final.append("\n")
                    # print(pp.text)

                    return h2p(pp)

            if pp.name == 'div' :

                if pp.name == 'div' and pp.find_next_sibling().name == 'h2':
                    lliss=pp.find_all('li')
                    # print(len(lliss))
                    for rr in lliss:
                        final.append(rr.text)
                        final.append("\n")
                        # print(rr.text)
                    return
                elif pp.name == 'div' and pp.find_next_sibling().name != 'h2':
                    lliss = pp.find_all('li')
                    # print(len(lliss))
                    for rr in lliss:
                        final.append(rr.text)
                        final.append("\n")
                        # print(rr.text)
                    return jg(pp)





            if pp.name != 'div' and p.name != 'ul':

                return jg(pp)
            # elif pp.name != 'div' and p.name != 'ul' and p.find_next_sibling().name == 'h2':
            #     return
    except:
        pass




for dfdf in range(len(ab)-kkk):
    afmain=afmain.find_next_sibling('h2')
    final.append(afmain.text)
    final.append("\n")
    # print(afmain.text)
    # print()
    pp=afmain
    jg(pp)



for fwfw in final:
    print(fwfw)


