# PPExec: Kill a process named Killmenow.
exec {'killmenow':
    path    => ['/usr/bin/', '/bin/'],
    command => 'pkill -15 killmenow'
}
