import os

hosts_filename = ''
if os.name == 'nt':
  hosts_filename = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
else:
  hosts_filename = '/etc/hosts'


def redirect():
  # Redirect prolifewhistleblower.com to 127.0.0.1
  try:
    with open(hosts_filename, 'a') as hosts:
      hosts.write('\n127.0.0.1 prolifewhistleblower.com\n')
  except IOError:
    print('Unable to append to {}'.format(hosts_filename))
    print('Please run again but with sudo, as Administrator, or a user with write access to the hosts file.')
    exit(1)


def end_redirect():
  # Remove the redirect from the hosts file
  try:
    with open(hosts_filename, 'r') as hosts:
      lines = hosts.readlines()
    with open(hosts_filename, 'w') as hosts:
      for line in lines:
        if not 'prolifewhistleblower.com' in line:
          hosts.write(line)
  except IOError:
    print('Unable to remove the redirect we added to {}'.format(hosts_filename))
    print('Please remove it yourself or run me with sudo, as Administrator, or a user with write access to the hosts file.')
    exit(1)
