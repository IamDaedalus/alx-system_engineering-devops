# this pp file installs a package
package { 'flask':
 ensure   => installed,
 provider => 'pip3'
}
