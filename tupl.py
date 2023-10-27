countries = ("russia", "usa", "canada", "mexico", "brazil", "argentina",
             "chile")
temp = list(countries)
temp = list(countries) + ["india"]
temp.append("India")
temp.pop(0)
print(temp)
countries = tuple(temp)
print(countries)
