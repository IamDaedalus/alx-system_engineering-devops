# this pp file executes a command
exec { 'kill process':
  command => ['/usr/bin/pkill', '-f killmenow']
}
