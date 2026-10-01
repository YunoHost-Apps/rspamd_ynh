require ["vnd.dovecot.debug", "vnd.dovecot.pipe", "copy", "imapsieve", "environment", "variables"];
debug_log "IMAPSieve learn spam triggered";

if environment :matches "imap.user" "*" {
  set "username" "${1}";
}

# username is passed and only used if per_user setting is set to true
pipe :copy "rspamd-learn-spam.sh" [ "${username}" ];
