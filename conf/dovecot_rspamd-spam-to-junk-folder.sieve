require ["fileinto"];

##
## Global spam filter
## Automatically moves spam to Junk folder
##

# Check for Rspamd spam header
# NOTE: that header when receive by Rspamd is deleted prior to be analized
# so when testing with `swaks --to admin@domain.tld --header-X-Spam "yes" --from evil@example.com --server 127.0.0.1`
# Rspamd will firstly remove that header, analyze the email, set or not X-Spam "yes"
# if you wand to avoid that, add remove_upstream_spam_flag = false;
# in the milter_headers section of /etc/rspamd/modules.d/milter_headers.conf
if header :contains "X-Spam" "Yes" {
    fileinto "Junk";
}
