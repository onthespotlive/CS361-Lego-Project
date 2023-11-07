import curses
import random
import time

def print_large_text(stdscr):
    stdscr.clear()
    large_text = [
        r"$$\                                                 $$$$$$\  $$\      $$\ ",
        r"$$ |                                               $$  __$$\ $$ | $\  $$ |",
        r"$$ |      $$$$$$\   $$$$$$\   $$$$$$\              $$ /  \__|$$ |$$$\ $$ |",
        r"$$ |     $$  __$$\ $$  __$$\ $$  __$$\             \$$$$$$\  $$ $$ $$\$$ |",
        r"$$ |     $$$$$$$$ |$$ /  $$ |$$ /  $$ |             \____$$\ $$$$  _$$$$ |",
        r"$$ |     $$   ____|$$ |  $$ |$$ |  $$ |            $$\   $$ |$$$  / \$$$ |",
        r"$$$$$$$$\\$$$$$$$\ \$$$$$$$ |\$$$$$$  |            \$$$$$$  |$$  /   \$$ |",
        r"\________|\_______| \____$$ | \______/              \______/ \__/     \__|",
        r"                   $$\   $$ |                                             ",
        r"                   \$$$$$$  |                                             ",
        r"                    \______/                                              "
    ]

    for i, line in enumerate(large_text):
        stdscr.addstr(i, 0, line)

    stdscr.refresh()
    ##time.sleep(1)

def search_set(stdscr):
    print_large_text(stdscr)
    stdscr.addstr(13, 0, "Enter your search request: ")
    stdscr.refresh()
    curses.echo()
    request = stdscr.getstr(14, 0).decode()
    curses.noecho()
    stdscr.addstr(15, 0, f"Searching for set with request: {request}")
    stdscr.refresh()
    stdscr.getch()

def random_set(stdscr):
    print_large_text(stdscr)
    stdscr.addstr(13, 0, "Random set placeholder*")
    stdscr.refresh()
    stdscr.getch()

def explore_lego_starwars(stdscr):
    while True:
        print_large_text(stdscr)
        stdscr.addstr(13, 0, "Explore Lego Starwars:")
        stdscr.addstr(14, 0, "1. Option 1")
        stdscr.addstr(15, 0, "2. Option 2")
        stdscr.addstr(16, 0, "3. Option 3")
        stdscr.addstr(17, 0, "4. Go back")

        choice = stdscr.getch()

        if choice == ord('1'):
            stdscr.addstr(17, 0, "Option 1 selected. Confirm? (y/n)")
            stdscr.refresh()
            confirm = stdscr.getch()
            if confirm == ord('y'):
                stdscr.addstr(18, 0, "Option 1 confirmed")
                stdscr.refresh()
                stdscr.getch()
            else:
                stdscr.addstr(18, 0, "Option 1 not confirmed")
                stdscr.refresh()
                stdscr.getch()
        elif choice == ord('2'):
            stdscr.addstr(17, 0, "Option 2 selected. Confirm? (y/n)")
            stdscr.refresh()
            confirm = stdscr.getch()
            if confirm == ord('y'):
                stdscr.addstr(18, 0, "Option 2 confirmed")
                stdscr.refresh()
                stdscr.getch()
            else:
                stdscr.addstr(18, 0, "Option 2 not confirmed")
                stdscr.refresh()
                stdscr.getch()
        elif choice == ord('3'):
            stdscr.addstr(17, 0, "Option 3 selected. Confirm? (y/n)")
            stdscr.refresh()
            confirm = stdscr.getch()
            if confirm == ord('y'):
                stdscr.addstr(18, 0, "Option 3 confirmed")
                stdscr.refresh()
                stdscr.getch()
            else:
                stdscr.addstr(18, 0, "Option 3 not confirmed")
                stdscr.refresh()
                stdscr.getch()
        elif choice == ord('4'):
            break

def main_menu(stdscr):
    while True:
        ##stdscr.clear()
        print_large_text(stdscr)
        stdscr.addstr(13, 0, "Main Menu:")
        stdscr.addstr(14, 0, "1. Search Set")
        stdscr.addstr(15, 0, "2. Random Set")
        stdscr.addstr(16, 0, "3. Explore Lego Starwars")
        stdscr.addstr(17, 0, "4. Exit")

        choice = stdscr.getch()

        if choice == ord('1'):
            search_set(stdscr)
        elif choice == ord('2'):
            random_set(stdscr)
        elif choice == ord('3'):
            explore_lego_starwars(stdscr)
        elif choice == ord('4'):
            break

if __name__ == "__main__":
    curses.wrapper(print_large_text)
    curses.wrapper(main_menu)
