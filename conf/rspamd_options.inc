# /etc/rspamd/local.d/options.inc
# Use the local unbound instead of /etc/resolv.conf (dnsmasq and its public upstreams)
dns {
  nameserver = ["127.0.0.1:5353"];
}
