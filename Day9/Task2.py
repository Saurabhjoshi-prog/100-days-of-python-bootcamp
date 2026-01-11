travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
print(travel_log["France"][1])
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
#Nesting a Dictionary inside a Dictionary
happy_list={"a":{1:"a",2:"b"},"b":{1:"a",2:"b"}}
#Figure out how to print out "Stuttgart" from the following list:
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log["Germany"]["cities_visited"][2])