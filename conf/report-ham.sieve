require ["vnd.dovecot.pipe", "copy", "imapsieve", "environment", "variables"];

if environment :matches "imap.mailbox" "*" {
  set "mailbox" "${1}";
}

if string :is "${mailbox}" [ "Trash", "Junk", "Spam" ] {
  stop;
}

if environment :matches "imap.user" "*" {
  set "username" "${1}";
}

# username is passed but currently not used by the shell script
pipe :copy "rspamd-learn-ham.sh" [ "${username}" ];
