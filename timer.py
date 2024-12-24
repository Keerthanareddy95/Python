import time

def countdown_timer(seconds):
    #countdown_timer takes input in seconds
    while seconds > 0:
        mins, secs = divmod(seconds,60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's Up!")

if __name__ == "__main__":
    countdown_time = int(input("Enter the time in seconds : "))
    countdown_timer(countdown_time)