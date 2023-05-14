include stdlib

file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => file('/var/www/html/wp-settings.php'), # Content of the file
}

file_line { 'change_line_in_apple':
  path    => '/var/www/html/wp-settings.php',
  line    => 'require_once( ABSPATH . WPINC . '/class-wp-locale.php' );',
  match   => 'require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );',
}
