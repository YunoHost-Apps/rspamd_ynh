#!/bin/sh
set -eu

RSPAMC="/usr/bin/rspamc -h localhost:11334 -P q1"

if [ -n "${1:-}" ]; then
  exec $RSPAMC -d "$1" learn_spam
else
  exec $RSPAMC learn_spam
fi
