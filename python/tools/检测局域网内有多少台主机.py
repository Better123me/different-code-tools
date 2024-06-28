import platform
import subprocess


ip = '10.196.143.87'

def ping_func(ip):
    if (platform.system() == 'Windows') :
        ping = subprocess.Popen(
            'ping -n 1 {}'.format(ip), 
            shell=False, 
            close_fds=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
            )
    else:
        ping = subprocess.Popen(
            'ping -c 1 {}'.format(ip), 
            shell=False, 
            close_fds=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
            )
    try:
        out, err = ping.communicate(timeout=8)
        if 'ttl' in out.decode('GBK').lower():
            print("ip {} is alive".format(ip))
        print(out.decode('GBK').lower())
    except:
        print(out)
    ping.kill()
    
ping_func(ip)
