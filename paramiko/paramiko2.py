import paramiko
import time
from pprint import pprint

iosxe_ao = {
    'hostname' : 'sandbox-iosxe-latest-1.cisco.com',
    'port' : '22',
    'username' : 'developer',
    'password' : 'C1sco12345',
    'look_for_keys' : False, 
    'allow_agent' : False
}
commands = ['show ip interface brief \n','show version \n']
max_buffer = 65535



def get_connection():
    ssh  = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(**iosxe_ao)
    return ssh

def show_command(ssh,cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)   
    return stdout.readlines()

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)

if __name__ == '__main__':
    ssh=get_connection()
    new_ssh=ssh.invoke_shell()
    output = clear_buffer(new_ssh)
    time.sleep(2)
    new_ssh.send("terminal length 0\n")
    output = clear_buffer(new_ssh)

    for command in commands:
        new_ssh.send(command)
        time.sleep(2)
        output = new_ssh.recv(max_buffer)
        print(' '.join(map(str, output)))
    new_ssh.close()
