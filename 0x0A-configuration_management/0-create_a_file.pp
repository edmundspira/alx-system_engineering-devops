# this Puppet manifest creates a new file in the /tmp directory.
$file_var = '/tmp/school'

file { $file_var:
    ensure  => file,
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
