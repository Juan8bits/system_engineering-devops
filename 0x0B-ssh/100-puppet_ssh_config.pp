# PPFile that config ssh_config file.
file_line{ 'Turn off passwd auth':
    path  => '/etc/ssh/ssh_config',
    line  => 'PasswordAuthentication yes',
    match => '^PasswordAutentication*$',
}
file_line{ 'Declare identity file':
    path  => '/etc/ssh/ssh_config',
    line  => 'IdentityFile ~/.ssh/holberton',
    match => '^IdentityFile*$',
}
