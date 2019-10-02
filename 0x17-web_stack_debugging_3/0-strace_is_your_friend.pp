# Script replace a line with puppet
file_line { 'replace_line':
  ensure => present,
  path   => '/var/www/html/wp-settings.php',
  line   => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match  => '^*class-wp-locale.phpp*',
}
