# Managed by the YunoHost rspamd app: changes to this file are overwritten on upgrade.
# Delete the first line to keep your own version, the app then leaves this file alone.
#
# Senders for which rspamd skips greylisting.
#
# rspamd matches these entries against the reverse DNS name of the connecting
# server and its registered domain, NOT against the sender address. So an entry
# must be the domain the provider's outgoing mail servers are named after.
#
# The big mailbox providers deliver from large server pools and often retry a
# temporarily rejected mail from a different network, so greylisting delays
# their mail by hours or lets it bounce.

# Microsoft: Outlook.com, Hotmail, Microsoft 365 (*.outbound.protection.outlook.com)
outlook.com
# Google: Gmail, Google Workspace (mail-*.google.com, *.1e100.net)
google.com
1e100.net
# Yahoo and AOL (*.mail.yahoo.com)
yahoo.com
# Apple iCloud (*.me.com, *.eps.apple.com)
me.com
apple.com
