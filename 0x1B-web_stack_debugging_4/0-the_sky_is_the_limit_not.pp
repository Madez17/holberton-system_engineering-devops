# Script replace limit to execute file
exec { 'replace_unlimit':
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
  path    => ['usr/bin', 'usr/sbin', '/bin'],
}
exec { 'restart-nginx':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
