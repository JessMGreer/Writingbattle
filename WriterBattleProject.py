import random
import time
import sys
import curses


writing_prompts = ['Writing prompt 1',
    'Writing prompt 2',
    'Writing prompt 3'
    ]


print("Welcome to the Battle of the Writers!\nYou each have 60 seconds to write your next bestselling novel\nEach player will have 10 seconds to read the writing prompt and prepare to write. Once you see 'Begin', you start. \n Good luck, and may the odds be ever in your favor")
print("That's actually a tad bit ominous given the context of the quote\nDon't worry, nothing bad will happen to the person who doesn't win")
print("Except the dishonor it will bring onto you, your family, and your cow")
print("Before we begin, let's introduce ourselves to the arena\nahem, I mean the audience\n")

#Enter writer 1's name: 
writer_one = str(input("Writer 1, please step forward and introduce yourself. What is your name? "))
#greet writer #1
print("Hello, " + str(writer_one))
#enter writer 2's name: 
writer_two = str(input("Writer 2, please step forward and introduce yourself. What is your name? "))

#greet writer #2
print("Hello, " + str(writer_two))

#print out a random prompt
Rand_wp = random.choice(writing_prompts)


def main(stdscr):
    curses.noecho()
    stdscr.nodelay(True)

    start_time = time.time()
    input_string = ""
    input_string2 = ""

    #writer one turn!
    stdscr.addstr(f"Hello, {writer_one}\n")
    stdscr.addstr("\n")
    stdscr.addstr(Rand_wp + "\n")
    stdscr.addstr("\n")
    stdscr.addstr("\nYou have 60 seconds. begin!")
    stdscr.addstr("\n")
    while True:
        if time.time() - start_time > 60:
            break
        c=stdscr.getch()
        if c == -1: #no input
            time.sleep(.01)
        else:
            if c==10: #enter key
                break
            elif c == 263 or c ==127: #back/del key
                input_string = input_string[:-1]
                stdscr.addch(8) #backspace
                stdscr.addch(' ')
                stdscr.addch(8)
            else:
                input_string += chr(c)
                stdscr.addch(c)
    stdscr.addstr("\ntime is up!")
    stdscr.addstr('\nThis is the text you submitted: \n' + input_string)
    stdscr.refresh()
    time.sleep(10)

    ###writer two's turn! 

    stdscr.addstr(f"Hello, {writer_two}\n")
    stdscr.addstr("\n")
    stdscr.addstr(Rand_wp + "\n")
    stdscr.addstr("\nYou have 60 seconds. begin!\n")
    stdscr.addstr("\n")
    while True:
        if time.time() - start_time > 60:
            break
            c = stdscr.getch() #getch() allows the user to put in their input on the screen. The computer reads each character. 
            if c == -1: #no input
                time.sleep(.01)
            else:
                if c==10: #enter key
                    break
                elif c == 263 or c ==127: #back/del key
                    input_string2 = input_string2[:-1]
                    stdscr.addch(8) #backspace
                    stdscr.addch(' ')
                    stdscr.addch(8)
                else:
                    input_string2 += chr(c)
                    stdscr.addch(c)

    stdscr.addstr("\ntime is up!")
    stdscr.addstr('\nThis is the text you submitted: \n' + input_string2)
    stdscr.refresh()
    time.sleep(10)


if __name__ == "__main__":
    curses.wrapper(main)


#computer must decide winner 

#Creativity: 8
#Grammar: 2
#used prompt: 8
#two extra points cause you tried your best: 2

