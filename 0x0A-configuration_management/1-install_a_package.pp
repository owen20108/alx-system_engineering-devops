# site.pp or your_module_name/manifests/init.pp

class your_module_name {
  package { 'python3-pip':
    ensure => installed,
  }

  package { 'Flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3-pip'],
  }
}

