# Puppet manifest to install nginx on a new Ubuntu server and add the custom header
#+ `X-Served-By` with value of hostname to the response header.

exec { 'update-package-index':
    command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure  => installed,
    require => Exec['update-package-index'],
}

service { 'nginx':
    ensure    => 'running',
    enable    => true,
    hasstatus => true,
    restart   => '/usr/sbin/service nginx reload',
}

file { '/etc/nginx/conf.d/custom_headers.conf':
    ensure  => 'present',
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => "add_header X-Served-By \"${::hostname}\";",
    require => Package['nginx'],
    notify  => Service['nginx'],
}
