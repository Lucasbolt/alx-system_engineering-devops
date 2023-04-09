#!/usr/bin/env bash
# resolves hostname and subdomains ip address.
# usage: 0-world_wide_web hostname [subdomain]

domain_lk () {
	line=$(dig +short $2.$1 | awk '{print $1}')
	echo "The subdomain $2 is a A record and points to $line"
}
if [ $# -ge 1 ]
then
	if [ ! -z $2 ]
	then
		domain_lk "$1" "$2"
	else
		domain_lk "$1" "www"
		domain_lk "$1" "lb-01"
		domain_lk "$1" "web-01"
		domain_lk "$1" "web-02"
	fi
fi
