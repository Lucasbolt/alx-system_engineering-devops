# Allow the user holberton to login and open files without error

# Increases hard file limit for user
exec {'increase hard file limit for holberton user.'
  command => 'sed -i "/holberton hard/s/5/65536/" /etc/security/limits.conf',
  path => '/usr/local/bin:/bin/'
}

#Increases soft file limit for user.
exec {'increase soft file limit for holberton user.'
  command => 'sed -i "/holberton soft/s/4/65536/" /etc/security/limits.conf',
  path => '/usr/local/bin/:/bin/'
}
