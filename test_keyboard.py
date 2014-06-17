import curses
import sys
import os

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    # fix stdout ( @see http://stackoverflow.com/questions/3657103/python-print-not-functioning-correctly-after-using-curses )
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
			if c == curses.KEY_UP: 
				print "UUUUUP"
				stdscr.addstr("Up")
			elif c == curses.KEY_DOWN: 
				stdscr.addstr("Down")
			elif c == curses.KEY_LEFT:
				stdscr.addstr("Left")
			elif c == curses.KEY_RIGHT:
				stdscr.addstr("Right")			
			
			stdscr.refresh()
			# return cursor to start position
			# stdscr.move(0, 0)

curses.wrapper(main)
