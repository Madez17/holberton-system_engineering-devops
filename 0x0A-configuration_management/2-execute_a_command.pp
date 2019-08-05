#!/usr/bin/env bash
# create a manifest that kills a process named killmenow
exec { 'kill_process_file':
command => 'pkill killmenow',
path    => '/usr/bin:/usr/sbin:/bin'
}
