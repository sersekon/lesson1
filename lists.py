#numbers = [3, 5, 7, 9, 10.5]
#print(numbers)
#numbers.append("Python")
#len(numbers)
#print(numbers)
#print(numbers[0])
#print(numbers[4])
#print(numbers[1:3])
#del numbers[5]
#print(numbers)

weather = {"city": "Москва", "temperature": "20"}
print(weather["city"])
weather["temperature"]= int(weather["temperature"])- 5
print(weather)

print(weather.get("country", "Россия"))
weather.get("country")
weather["date"] = "27.05.2019"
print(weather)
