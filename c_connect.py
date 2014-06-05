#!/user/bin/python
import sys
import pexpect

def cjump(usr, pwd, enpwd, ip):
    child = pexpect.spawn(
        'ssh -o StrictHostKeyChecking=no -l ' + usr + " " + ip)
    index = child.expect(
        ['[Pp]assword:', pexpect.EOF, pexpect.TIMEOUT, 'refused'])
    if index == 0:
        child.sendline(pwd)

        index = child.expect(
            ['~>', '>', 'assword:', '#', pexpect.EOF, pexpect.TIMEOUT])
        if index == 0:
            return 'Connection Closed'
        elif index == 1:
            return True, child
        elif index == 2:
            child.sendcontrol('c')
            return 'Please check your TACAS Username and Password'
        elif index == 3:
            return 'enable'
        elif index == 4:
            return 'Timeout'
        elif index == 5:
            return 'Timeout'
    elif index == 1:
        return 'Getting EOF Error'
    elif index == 2:
        return 'Timeout2'
    elif index == 3:
        return 'connection refused'
    else:
        return False
def enable(child, enpwd):

    child.sendline('enable')


    i = child.expect(
        ['[Pp]assword:', '>', '#', pexpect.EOF, pexpect.TIMEOUT])
    if i == 0:
        child.sendline(enpwd)

        i = child.expect(
            ['[Pp]assword:', '>', '#', pexpect.EOF, pexpect.TIMEOUT])
        if i == 0:
            return 'Please check enable Password'
        elif i == 1:
            return 'Please check enable Password'
        elif i == 2:
            return True
        elif i == 3:
            return 'Getting EOF Error'
        elif i == 4:
            return 'Timeout'
    elif i == 1:
        return False

    elif i == 2:
        return True
    elif i == 3:
        return 'Getting EOF Error'
    elif i == 4:
        return 'Timeout'

def hostname(child):
    child.sendline(' ')
    index = child.expect(['#', pexpect.EOF, pexpect.TIMEOUT])
    if index == 0:
        host = child.before
        host = host.rsplit()
        host = host[0]
        return host
    elif index == 1:
        return 'Getting EOF Error'
    elif index == 2:
        return 'Getting EOF Error'

def term(child,hostname):
    host = hostname
    child.sendline('terminal length 0')
    index = child.expect(
        [host + '#', pexpect.EOF, pexpect.TIMEOUT])
    if index == 0:
        return True
    elif index == 1:
        return 'Getting EOF Error'
    elif index == 2:
        return 'Getting EOF Error'

def runconfig(child, hostname):
    host = hostname
    child.sendline('term len 0')
    child.expect(host + '#')
    child.sendline('show run')
    child.expect(host + '#')
    run = child.before.split('\n')
    return run

def prompt(child, hostname):
    host = hostname
    index = child.expect(
        [host + '#', pexpect.EOF, pexpect.TIMEOUT])
    if index == 0:
        return True
    elif index == 1:
        return 'Getting EOF Error'
    elif index == 2:
      return 'Getting EOF Error'

def close(child):
    child.sendline('exit')
    i = child.expect([':~>', '>',pexpect.EOF, pexpect.TIMEOUT])
    if i == 0:
        return True
    if i == 1:
        return True
    elif i == 2:
        return 'Getting EOF Error'
    elif 1 == 2:
        return 'Timeout'
