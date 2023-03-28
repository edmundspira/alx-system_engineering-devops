# this Puppet manifest installs `flask` from `pip3`

exec { 'update-apt':
    command     => '/usr/bin/apt-get update',
    refreshonly => true,
}

package { 'python3-pip':
    ensure  => installed,
    require => Exec['update-apt'],
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3-pip'],
}
