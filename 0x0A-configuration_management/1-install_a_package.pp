#!/usr/bin/pup
# Ensure python3-pip is intialzied
package { 'python3-pip' :
  ensure => installed,
}
package {'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip',
  require => package['python3-pip'],
}
package {'Werkzeug':
  ensure   => '2.0.1',
  provider => 'pip',
  require => package['python3-pip'],
}
