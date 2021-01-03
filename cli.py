from termcolor import colored, cprint


def main():
    print('ちんぽにゃ--------------STDOUT^---------------')
    return 'RETURN'

def color():
    cprint('STDOUT', 'green')
    text = colored('RETURN', 'red')
    return text
