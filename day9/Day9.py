# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Korea": ["Seoul", "Busan", "Dajeon"],
# }
# 
# print(travel_log["Korea"][1])
# 
# nested_list = ["A", "B", ["C", "D"]]
# 
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Korea": {
        "cities_visited": ["Seoul", "Busan", "Dajeon"],
        "total_visits": 5,
    }
}

print(travel_log["Korea"]["cities_visited"][1])
