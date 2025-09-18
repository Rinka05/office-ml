import requests

from requests.exceptions import RequestException , Timeout
# response = requests.get("https://httpbin.org/get")
# data = response.json()
# print(data)
# if response.status_code == 200:
#     print("request successful")
# else :
#     print("request failed")


# print(f"url : {data["url"]}")
# # print(f"method: {data["method"]}") //not an entity in json object

params = {
    "key1":"value1",
    "key2":"value2"
}

# responsep = requests.get("https://httpbin.org/get", params = "key1")
# print(f"url :{responsep.url}")

# responsep1 = requests.get("https://httpbin.org/get?key1", params = "key1")
# print(f"{responsep1.url}")

post1 = {
    "title":"my first post",
    "content":"mai pagal hu "
}

# response = requests.post("https://httpbin.org/post", json = post1)

# print(f"{response.status_code}")

# if response.status_code ==200:
#     created_post = response.json()
#     print(f"{created_post["json"]["title"]}")
#     print(f"{created_post["json"]["content"]}")

form_data ={
    "username":"alince",
    "password":"secret123"
}

# response = requests.post("https://httpbin.org/post", data = form_data)
# print(f"{response.status_code}")
# data = response.json()
# print(data["form"])

# headers = {
#     "user-agent":"myscript/1.0",
#     "x-custom-header":"custom/value"
# }
# response = requests.get("https://httpbin.org/get", headers=headers)

# try:
#     response = requests.get("https://httpbin.org/delay/1" , timeout = 3)
#     print("request completed within timout")
# except requests.exceptions.Timeout:
#     print("request time out")


# response1 = requests.get("https://httpbin.org/get")

# response2 = requests.get("https://httpbin.org/user-agent")
# print(f"{response2.status_code}")


# session = requests.Session()
# session.headers.update({"user-agent":"myapp/2.0"})

# response1 = session.get("https://httpbin.org/get")
# print(response1)
# response2 = session.get("https://httpbin.org/cookies/set/sessionid/12345")

# cookie_response = session.get("https://httpbin.org/cookies")
# print("cookies", cookie_response.json()["cookies"])

# response = requests.get("https://httpbin.org/get")

# print(f"{response.status_code}")
# print(f"{response.reason}")
# print(f"{response.headers["Content-Type"]}")
# print(f"{response.encoding}")

# print(f"url:{response.json()['url']}")
# # print(f"url:{response.json()['method']}")  //not a key to be accesed
# print(f"url:{response.elapsed}")


def fetch_data_with_error_handling():
    try:
        response = requests.get("https//httpbin.org/status/404", timout = 5)
        response.raise_for_status()
        # return response.json()
        print({response.json()})
    except Timeout:
        print("not able to resolve timout")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"http error :{e}")
        return None
    except RequestException as e:
        print(f"an error occured :{e}")
        return None