#!/usr/bin/perl
#Reverse IP script.

use LWP::UserAgent;
while (!$ARGV[0]) {
print "Usage: $0 IP \n"; exit;}
$a = 1;
$ua = new LWP::UserAgent(timeout => 15, agent => "Mozilla/5.0 (x11; u; linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7)" );

$req = $ua->get('http://whois.webhosting.info/' . $ARGV[0] . '?pi=1&ob=SLD&oo=ASC');
if (!($req->is_success)) {

die $req->status_line; }
else {
$output = $req->as_string;
until ($output =~ /(.*?)IP\sDetails\s-\sN\/A\./) {
$req = $ua->get('http://whois.webhosting.info/' . $ARGV[0] . '?pi=' . $a . '&ob=SLD&oo=ASC');
if (!($req->is_success)) { die $req->status_line; }
$output = $req->as_string;

while ($output =~ /<td><a\shref=\"http:\/\/whois.webhosting.info\/(.*?)\">/g){
my($crap,$yes)=split(/info\/(.*?)\.\"\>/,$&);
print "$yes\n";
}
sleep 5;
$a++;
}
print "Done!\n";
} 
