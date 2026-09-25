require ["vnd.dovecot.pipe", "copy", "imapsieve", "environment", "variables"];

if environment :matches "imap.mailbox" "*" {
  set "mailbox" "${1}";
}

if string :is "${mailbox}" [ "Trash", "Junk" ] {
  stop;
}

if environment :matches "imap.user" "*" {
  set "username" "${1}";
}

# username is passed and only used if per_user setting is set to true
pipe :copy "rspamd-learn-ham.sh" [ "${username}" ];
