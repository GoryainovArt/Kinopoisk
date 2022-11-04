#8
import csv
import requests
import json
import os

file_path = "C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/all_data.csv"
token = "8975e57c24e1997e0d80dd473fb7dedf"
token_1 = "8975e57c24e1997e0d80dd473fb7dedf" 
token_2 = "b7f79199ab9ef13dd6ea387eb2ec9414" 
token_3 = "c82fcfa00f0612adcb880c03b3959bcf" 
token_4 = "29208b3099526728f9459aa479cd4fde" 
token_5 = "4f793d8dab05f72b294bdf67d860ee5d" 
token_6 = "23c88b417ed5ffb1adee8622ad017c36" 
token_7 = "4f1996ac3b31614d0ae5bd5d5e14b4f9" 
token_8 = "700a38932b5345b6fbd23a82c73f7107" 

token_list = [token_1, token_2, token_3]

k = int(input())  # k для 10*k + j
if k == 0:
    with open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/all_data.csv", "w", encoding="utf-8",newline='') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(("KP_id", "title", "title_alternative", "year", "poster", "trailer", "age", "actors","countries", "genres", "directors", "rating_kinopoisk", "kinopoisk_votes", "description"))
with open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/all_data.csv", "a", encoding="utf-8",newline='') as file, open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/one_day_limit.csv", "w",encoding="utf-8", newline='') as buff_file:
    a_pen = csv.writer(file)
    buf_wr = csv.writer(buff_file)
    for z in range(2):
        for j in range(1,11):
            page = (k+z) * 10 + j
            url = f"https://api.kinopoisk.cloud/movies/all/page/{page}/token/{token_list[z]}"
            response = requests.get(url)
            data = response.json()["movies"]
            print(page)
            print(data) 
            print("------------------------------")
            for i in data:
                print(i)
                if i["genres"] == None:
                    continue
                else:
                    if ("Концерт" in i["genres"]) or ("Музыка" in i["genres"]) or ("Документальный" in i["genres"]) or ("для взрослых" in i["genres"]) or ("Короткометражка" in i["genres"]) or (i['type'] != "movie"):
                        continue
                    else:
                        # Проверка и удаление табулятора
                        if i["title_alternative"] != None:
                            if "#" in i["title_alternative"]:
                                i["title_alternative"] = i["title_alternative"].replace("&#039;", "'", i["title_alternative"].count("&#039;"))
                        a_pen.writerow((i["id_kinopoisk"],i["title"],i["title_alternative"],i["year"],i["poster"],i["trailer"],i["age"],i["actors"],i["countries"],i["genres"],i["directors"],i["rating_kinopoisk"],i["kinopoisk_votes"],i["description"]))
                        buf_wr.writerow((i["id_kinopoisk"], i["title"], i["title_alternative"], i["year"], i["poster"],i["trailer"], i["age"], i["actors"], i["countries"], i["genres"], i["directors"], i["rating_kinopoisk"], i["kinopoisk_votes"], i["description"]))

