
''' This script is specially design for cisco router and switches. This
is going to be use to ssh into cisco devices.  This script is base on Pexpect
and to be able to use it, you would need a good knowledge of pexpect.

PEXPECT LICENSE

    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt

    Copyright (c) 2014, Noah Spurrier <noah@noah.org>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
    
My info:
Written by David Gomez
Questions: davidgomez.255@gmail.com
'''
import sys
import pexpect

#This function is to ssh to the device
def cjump(usr, pwd, enpwd, ip):
    child = pexpect.spawn(
        'ssh -o StrictHostKeyChecking=no -l ' + usr + " " + ip)
    index = child.expect(
        ['[Pp]assword:', pexpect.EOF, pexpect.TIMEOUT, 'refused'])
    if index == 0:
        child.sendline(pwd)
        #The child expect will return integer number of the match
        #'~>' Linux prompt, '>' device prompt, '#', enable prompt
        index = child.expect(['~>', '>', 'assword:', '#', pexpect.EOF, pexpect.TIMEOUT])
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
#this funtion will put the device in enable mode
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
#This function will return a hostname name
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
#This function will disable the more page when getting loging outputs
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
#this will return the device running config
def runconfig(child, hostname):
    host = hostname
    child.sendline('term len 0')
    child.expect(host + '#')
    child.sendline('show run')
    child.expect(host + '#')
    run = child.before.split('\n')
    return run
#this will close the ssh sesssion 
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








