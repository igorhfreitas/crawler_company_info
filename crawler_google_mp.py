import pandas as pd
from unidecode import unidecode
from bs4 import BeautifulSoup
import requests
import time

def get_google_KP_info(i):

    new_dataframe=pd.DataFrame()
    new_dict={}
    time.sleep(45)
    comp_url=i.replace(' ','+')
    response = requests.get('https://www.google.com/search?q='+comp_url,verify=False)
    html=response.text
    soup = BeautifulSoup(html, 'html.parser')
    new_dict['Entity Description']=i

    #teste=soup.find(class_='BNeawe s3v9rd AP7Wnd',recursive=True)
    #teste.get_text("|", strip=True)

    teste=soup.find_all(class_='BNeawe s3v9rd AP7Wnd',recursive=True)
    #teste=soup.find_all(class_='ifM90',recursive=True)
    #print(teste)

    linha=0
    for j in teste:
        print(j)
        txt_teste=j.get_text(strip=True)
        linha+=1
        chave=['sede:','fundador:','endereço:','endereco:','matriz:','pessoas-chave:','presidente:','diretores:','subsidiarias:']
        if any(x in unidecode(txt_teste.lower()) for x in chave):
            position=txt_teste.index(':')
            key=txt_teste[:position]
            value=txt_teste[position+1:]
            #if len(key)>20:
                #continue
            new_dict['Erro']=False
            new_dict[key]=value

        else:
            new_dict['Erro']=True

        #new_dict[key]=value

    #print(new_dict)
    new_dataframe=new_dataframe.append(new_dict,ignore_index=True,sort=True)
    return new_dataframe

def func_teste(x):
    lista=list(range(x))
    return pd.DataFrame(lista)
