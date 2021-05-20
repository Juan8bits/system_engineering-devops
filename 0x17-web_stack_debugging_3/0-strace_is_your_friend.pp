# Fix  error 500 internal server
exec { 'FixApache':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => shell,
}
