x = int(input("請輸入他跑了幾分幾秒(分鐘): "))
y = int(input("請輸入他跑了幾分幾秒(秒數): "))
z = int(input("請輸入他跑了幾公里: "))

time = x * 60 + y
speed_km_per_second = float(z) / time
speed_mile_per_second = speed_km_per_second / 1.6
speed_mile_per_hour = speed_mile_per_second * 3600

print("Speed = %.1f Miles/hour" % speed_mile_per_hour)