#!/bin/sh
exec /usr/bin/rspamc -h localhost:11334 -P q1 learn_spam
