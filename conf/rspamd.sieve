require ["fileinto"];

##
## Global spam filter
## Automatically moves spam to Junk folder
##

# Check for Rspamd spam header
if header :is "X-Spam" "Yes" {
    # Create Junk folder if it doesn't exist and file message there
    fileinto :create "Junk";
}
