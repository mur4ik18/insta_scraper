import requests
import json
url = input('Введите ссылку на профиль: ')
import os
class Instagram:
    
    def __init__(self, headers=None, proxy=None, cookies=None):
        # header init
        self.__headers  = headers
        # proxy init
        self.__proxy    = proxy
        # cookies init
        self.__cookies  = cookies

    def get_user_info(self,url):
        
        info_user       = requests.get(url, headers=self.__headers, 
                          proxies=self.__proxy, params={"__a":1})
        f = open('text.txt','w+')
        f.write(info_user.text)
        f.close()
         
        # get JSON
        json_info = info_user.text
        print(json_info)
        # json => dict
        return json.loads(json_info)
    def get_name(self, user_info):
        return user_info["graphql"]["user"]['full_name']
    def get_count_subscribers(self, user_info):
        return user_info["graphql"]["user"]["edge_followed_by"]["count"]

    def get_posts_count(self, user_info):
        likes           = 0
        comments        = 0
        count_of_posts  = user_info["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]
        posts = len(user_info["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"])
        for i in user_info["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
            comments    +=i["node"]["edge_media_to_comment"]["count"]
            likes       +=i["node"]["edge_liked_by"]["count"]

        return count_of_posts,comments,likes,posts

headers = {
 "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
 "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
}

m = Instagram(headers=headers)
t = m.get_user_info(url)
l = m.get_posts_count(t)

os.system('cls')

print("\033[1;32;40m Имя пользователя    | "+ f"\033[1;31;40m {m.get_name(t)}")
print("\033[1;32;40m Кол-во подписчиков  | "+ f"\033[1;31;40m {m.get_count_subscribers(t)}")
print("\033[1;32;40m Кол-во постов       | "+ f"\033[1;31;40m {l[0]}")
print("\033[1;32;40m -----------------------------------------------")
print("\033[1;32;40m Последних постов    | "+ f"\033[1;31;40m {l[3]}")
print("\033[1;32;40m Кол-во комментариев | "+ f"\033[1;31;40m {l[1]}")
print("\033[1;32;40m Кол-во лайков       | "+ f"\033[1;31;40m {l[2]}")
print("\033[1;32;40m Сред. кол-во лайков | "+ f"\033[1;31;40m {l[2]/l[3]}")
print("\033[1;32;40m Сред. кол-во комм.  | "+ f"\033[1;31;40m {l[1]/l[3]}")