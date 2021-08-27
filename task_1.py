from  bs4 import BeautifulSoup
import requests
import json
def task1():
    url="https://www.imdb.com/india/top-rated-indian-movies/"
    page=requests.get(url)
    # print(page)
    soup=BeautifulSoup(page.text,"html.parser")
    # html ka code(soup ,me)
    # list1=[]
    main=soup.find("div",class_="lister")
    main1=main.find("tbody",class_="lister-list")
    trs=main1.find_all("tr")
    list1=[]
    a=1
    for i in trs:
        position=i.find('style',Class_="position:relative")
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        name=movie_name
        release_year=i.find("td",class_="titleColumn").span.get_text()[1:5]
        year=int(release_year)#             with open("movies_dec.json","w")as f:
    #                 json.dump(movies_dec,f,indent=5)
    #
        mov=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_rate=float(mov)
        y=i.find("td",class_="posterColumn").a["href"]
        link="https://www.imdb.com"+y
        url=link
        k={"position":a,"movie_name":name,"year":year,"IMDb_Rating":movie_rate,"url":url}
        list1.append(k)
        a+=1
    with open("file.json","w") as open_file:
        json.dump(list1,open_file,indent=4)
    return list1
(task1())














