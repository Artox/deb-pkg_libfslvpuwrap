#
# Regular cron jobs for the libfslvpuwrap package
#
0 4	* * *	root	[ -x /usr/bin/libfslvpuwrap_maintenance ] && /usr/bin/libfslvpuwrap_maintenance
