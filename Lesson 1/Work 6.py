start_running = 4
end_running = 10
day = 1
while start_running < end_running:
    start_running += start_running * 0.1
    day += 1
    print(f"день: {day}")
    print(f"км = {start_running:.2f}")