t = eval(input("temperature = "))
aqi = eval(input("AQI = "))
if t > 37 or aqi > 150:
    print("避免外出")
else:
    print("可依需要待在戶外")