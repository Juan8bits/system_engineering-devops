# PPFile that config ssh_config file.
file_line{ 'Turn off passwd auth':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no',
    match  => '(PasswordAuthentication.no)\n',
}

file_line{ 'Declare identity file':
    ensure => 'present'
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/holberton',
    match  => '(IdentityFile.+)\n',
}
