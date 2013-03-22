import os
import signal
from time import sleep

def parse_time(time):
    ''' takes a string and returns a [h,m,s] list '''
    print time
    remaining = time
    if 'h' in time:
        h = time.split('h')[0]
        remaining = ''.join(time.split('h')[1:])
    else: h = 0
    print remaining 
    if 'm' in remaining:
        m = remaining.split('m')[0] 
        remaining = ''.join(time.split('m')[1:])
    else: m = 0
    s = remaining if remaining else 0
    return [int(h), int(m), int(s)]

def display_time_tuple(tup):
    return ' '.join( map( lambda t: str(t[0]) + t[1],
                          zip(tup, ('h', 'm', 's'))) )

def decr_time(time):
    #TODO make this better
    if time[2] > 0:
        time[2] -= 1
    elif time[2] == 0 and time[1] > 0:
        time[1] -= 1
        time[2] = 59
    elif time[1] == 0 and time[0] > 0:
        time[0] -= 1
        time[1] = 59
    else:
        time = [0,0,0]
    return time

def timer(time, func=None):
    ''' takes a time list and an action for when time runs out '''

    os.system('cls' if os.name=='nt' else 'clear')
    print display_time_tuple(time)
    if time == [0,0,0]:
        print "done"
        if func: func()
    else:
        sleep(1)
        timer(decr_time(time),func)

def signal_handler(signal, frame):
    sys.exit('timer interrupted')

if __name__ == '__main__':
    import sys
    signal.signal(signal.SIGINT, signal_handler)
    timer(parse_time(sys.argv[1]))
