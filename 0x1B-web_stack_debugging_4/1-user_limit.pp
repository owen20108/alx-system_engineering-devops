# 1-user_limit.pp: change the OS configuration to login with the holberton user;
# and open a file without any error message.
exec { 'correct-hard':
  command  => 'sudo sed -i \'s/nofile 5/nofile 30000/\' /etc/security/limits.conf',
  provider => shell,
}
