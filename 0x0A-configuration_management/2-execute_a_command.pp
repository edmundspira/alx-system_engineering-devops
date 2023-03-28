# manifest that kills a process `killmenow` using pkill

package { 'procps':
    ensure => 'installed',
}

exec { 'kill-process':
    command => '/usr/bin/pkill -f killmenow',
    onlyif  => '/usr/bin/pgrep -f killmenow',
    require => Package['procps'],
}
