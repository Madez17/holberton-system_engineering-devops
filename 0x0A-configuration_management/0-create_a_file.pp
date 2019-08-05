#!/usr/bin/env bash
#Create a file holberton in the temp
file { '/tmp/holberton':
ensure => file,
mode => '0744',
owner => 'www-data',
group => 'www-data',
content => 'I love Puppet'
}
