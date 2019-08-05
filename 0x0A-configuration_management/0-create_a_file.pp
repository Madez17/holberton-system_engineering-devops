#!/usr/bin/env bash
# Create a file holberton in the tmp
file { '/tmp/holberton':
path    => '/tmp/holberton',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet'
}
