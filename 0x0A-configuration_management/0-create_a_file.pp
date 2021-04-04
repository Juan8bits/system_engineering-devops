# PPFile-> Create a file in /tmp in which:
#   File path is "/tmp/holberton".
#   File permission is "0744".
#   File owner is "www-data".
#   File group is "www-data".
#   File contains "I love Puppet".
file {'holberton':
    ensure  => 'present',
    path    => '/tmp/holberton',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
