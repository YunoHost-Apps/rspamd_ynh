# /etc/rspamd/local.d/options.inc
# With redis configured, the longest chain of symbol timeouts is 9s. The stock
# task_timeout of 8s cuts it off and rspamd scores the mail on partial results
task_timeout = 10s;
