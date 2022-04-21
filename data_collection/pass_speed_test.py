from pynput import keyboard                 # pip install pynput
from threading import Thread
from pynput.keyboard import Key, Listener
import csv
import time

passcode = ".tie5Roanl"
passcode_list = ['.', 't', 'i', 'e', '5', 'shift_r', 'R', 'o', 'a', 'n', 'l']
keys_being_pressed = []
char_index = 0
previous_end_press_time = -1
row_to_write = [". hold time", ". to t time", "t hold time", "t to i time", "i hold time", 
    "i to e time", "e hold time", "e to 5 time", "5 hold time", "5 to Lshift time", "Lshift hold time", 
    "Lshift to r time", "r hold time", "r to o time", "o hold time", "o to a time", "a hold time", 
    "a to n time", "n hold time", "n to l time", "l hold time"]
run_continue_flag = True

def on_key_release(key):
    try:
        if(key.name == "enter"):
            pass
        else:
            raise
    except:
        global run_continue_flag
        try:
            update_key_timings()
            if(char_index == len(passcode_list)):
                run_continue_flag = False
        except:
            run_continue_flag = False
            

def on_key_press(key):
    if(check_char_with_passcode(key)):
        global char_index
        global previous_end_press_time
        char_index += 1
        keys_being_pressed.append({"key": key, "start_time": time.time()})
        if(previous_end_press_time > 0):
            key_time_between = keys_being_pressed[0]["start_time"] - previous_end_press_time
            row_to_write.append("{:.4f}".format(key_time_between))
            previous_end_press_time = -1
    else:
        run_continue_flag = False

def check_char_with_passcode(key):
    try:
        return (key.char == passcode_list[char_index])
    except:
        try:
            return (key.name == passcode_list[char_index])
        except:
            return False

def update_key_timings():
    key_release_time = time.time()
    key_released = keys_being_pressed.pop(0)
    key_hold_time = key_release_time - key_released["start_time"]
    row_to_write.append("{:.4f}".format(key_hold_time))
    if(len(keys_being_pressed) > 0):
        key_time_between = keys_being_pressed[0]["start_time"] - key_release_time
        row_to_write.append("{:.4f}".format(key_time_between))
    else:
        global previous_end_press_time
        previous_end_press_time = key_release_time

if __name__ == "__main__":
    rounds = int(input("Please enter the amount of times you want to enter the password\n"))
    print("Successful password entries will be marked with a ✅ and added to the CSV file, ❌ will not\n\nType: " + passcode)

    csvfile = open('output.csv', 'w', newline='')
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(row_to_write)

    for round in range(rounds):
        if(round % 10 == 0 and round != 0):
            round_percentage = (round / rounds) * 100
            round_percentage_string = "{:.1f}".format(round_percentage)
            print(f"{round_percentage_string}% complete")
        success_flag = False
        while(not success_flag):  
            row_to_write = []
            keys_being_pressed = []
            char_index = 0
            previous_end_press_time = -1
            run_continue_flag = True
        
            with Listener(on_press = on_key_press, on_release = on_key_release) as listener:
                def stop_run():
                    
                    while(run_continue_flag):
                        pass
                    listener.stop()

                Thread(target=stop_run).start()
                listener.join()

                if(char_index == len(passcode_list)):
                    print("✅")
                    csv_writer.writerow(row_to_write)
                    success_flag = True
                else:
                    print("❌")
                    round -= 1