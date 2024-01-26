# issue is fundamentally an nginx ulimit problem
exec { 'nginx-limit-fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# restart the service entirely while
# ensuring the above patch is applied
exec { 'nginx-limit-fix':
  command => 'nginx restart',
  path    => '/etc/init.d/',
  require => Exec['fix-for-nginx'],
}
