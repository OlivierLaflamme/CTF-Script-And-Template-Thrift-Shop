#!/usr/bin/perl
use LWP::Simple;
$site=$ARGV[0];
$kac=$ARGV[1];
if(@ARGV<2){&usage}
else{
if(int($kac)){
for($i=0;$i<=$kac;$i++){
get($site) || die "Site adresi yanlis\n";
}
print "$kac tane hiti artirilmisitir";
}
else {print "Numeric bir sayi girin";}
}
sub usage{
print q[
WebClicker Perl Version
Coded by h4ckinger
usageerl webclicker.pl http://www.hackinger.org <hit>
exmerl webclicker.pl http://www.hackinger.org 20
];
