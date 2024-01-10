import requests as rqs


# GET
# res_1 = rqs.get("https://httpbin.org/get")
# print(res_1.status_code)
# res_1_json = res_1.json()
# print(res_1_json)
# del res_1_json["args"]
# print(res_1_json)


# params = {"name": "Lex", "age": 1000}
# res_2 = rqs.get("https://httpbin.org/get", params=params)
# print(res_2.status_code)
# res_2_json = res_2.json()
# print(res_2_json)

print(
    "--------------------------------------------------------------------------------------------------------------------"
)

# POST
# payload = {"name": "Lex", "age": 1000}
# res_3 = rqs.post("https://httpbin.org/post", data=payload)
# print(res_3.status_code)
# res_3_json = res_3.json()
# print(res_3_json)

print(
    "--------------------------------------------------------------------------------------------------------------------"
)

# Handle
# res_4 = rqs.get("https://httpbin.org/status/404")
# print(res_4.status_code)
# print(res_4.headers)

# if res_4.status_code == rqs.codes.not_found:
#     print("Not Found")
# else:
#     print(res_4.status_code)

# Change User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
    "Accept": "image/svg+xml",
}

# res_5 = rqs.get("https://httpbin.org/user-agent", headers=headers)
# print(res_5.status_code)
# print(res_5.headers)
# print(res_5.text)

print(
    "--------------------------------------------------------------------------------------------------------------------"
)

# Download Image
# res_6 = rqs.get("https://httpbin.org/image", headers=headers)

# with open("sorted/requests/image_test.svg", "wb") as f:
#     f.write(res_6.content)

print(
    "--------------------------------------------------------------------------------------------------------------------"
)

# Timeout
# for i in [1, 2, 3]:
#     try:
#         res_7 = rqs.get("https://httpbin.org/delay/2", timeout=3)
#     except:
#         print(i)
#         continue

#     res_7_json = res_7.json()
#     del res_7_json["args"]
#     print(res_7_json)

print(
    "--------------------------------------------------------------------------------------------------------------------"
)

# Proxy Server

proxies = {"http": "46.4.96.137:80"}
res_8 = rqs.get("https://httpbin.org/get", proxies=proxies)
print(res_8.text)
# res_8_json = res_8.json()
# print(res_8_json)
