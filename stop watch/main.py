import time
print("Press enter to start...")
print("Press ctrl+c to cancel...")

# Infinite loop for the stopwatch

while True:
    try:
        input()
        start_time = time.time()
        print("Stopwatch started ...!")
    except:
        print("Stopwatch stopped ...!")
        end_time = time.time()
        print("Total time: ", round(end_time - start_time, 2), " seconds")
        break
    