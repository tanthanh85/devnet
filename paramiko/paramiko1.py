import paramiko
import time

iosxe_ao = {
    'hostname' : 'sandbox-iosxe-latest-1.cisco.com',
    'port' : '22',
    'username' : 'developer',
    'password' : 'C1sco12345',
    'look_for_keys' : False, 
    'allow_agent' : False
}
command = 'show version \n'

ssh  = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(**iosxe_ao)

def show_command(ssh,cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)   
    return stdout.readlines()

if __name__ == '__main__':
    output = show_command(ssh,command)
    
    print(' '.join(map(str, output)))
    ssh.close()