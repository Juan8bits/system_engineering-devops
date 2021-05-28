# Restart NGINX according to requests input
exec { 'sed -i s/15/5000/g /etc/default/nginx':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
}

exec { 'sudo service nginx restart':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
}
