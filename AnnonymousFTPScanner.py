import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', '')
        print('\n [+] ' + str(hostname) + ' FTP Anonymous Login Succeeded.')
        ftp.quit()
        return True
    except Exception as e:
        print('\n [-] ' + str(hostname) + ' FTP Anonymous Login Fails. Error: ' + str(e))
        return False

if __name__ == '__main__':
    anonLogin('xx.xx.xx.xx')
