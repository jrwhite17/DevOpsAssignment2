#!/bin/bash
# Pass the following information to the routine to generate the certificate:
#
# $1 = Country Name (2 letter code) [GB]:.
# $2 = State or Province Name (full name) [Berkshire]:.
# $3 = Locality Name (eg, city) [Newbury]:.
# $4 = Organization Name (eg, company) [My Company Ltd]:.
# $5 = Organizational Unit Name (eg, section) []:.
# $6 = Common Name (eg, your name or your server's hostname) []:.
# $7 = IP address
# $8 = Email Address []:.

umask 77 ; echo "$1
$2
$3
$4
$5
$6
$7
$7
$8" | /usr/bin/openssl req -new -key /etc/httpd/conf/ssl.key/server.key -x509 -days 365 -out /etc/httpd/conf/ssl.crt/server.crt >/dev/null