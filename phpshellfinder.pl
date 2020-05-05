#!/usr/bin/perl

use strict;
use warnings;
use LWP::UserAgent;

usage() unless $ARGV[2];

my @searchTerm;
my @checkTerm;

if(lc($ARGV[0]) eq "r57") {
        push(@searchTerm, "inurl:r57.php");
        push(@searchTerm, "\"[ phpinfo ]  [ php.ini ]  [ cpu ]  [ mem ]  [ users ]  [ tmp ]  [ delete ]\"");
        push(@searchTerm, "intitle:r57shell");
        push(@checkTerm, "r57");
        push(@checkTerm, "safe_mode");
} elsif(lc($ARGV[0]) eq "c99") {
        push(@searchTerm, "inurl:c99.php");
        push(@searchTerm, "\"Encoder    Tools    Proc.    FTP brute    Sec.    SQL    PHP-code    Update    Feedback    Self remove    Logout\"");
        push(@searchTerm, "intitle:\" - phpshell\"");
        push(@searchTerm, "intitle:\" - c99shell\"");
        push(@checkTerm, "c99");
        push(@checkTerm, "Safe-mode");
} elsif(lc($ARGV[0]) eq "mys") {
        push(@searchTerm, "\"Auto error traping enabled\"");
        push(@searchTerm, "intitle:\"MyShell 1.1.0 build 20010923\"");
        push(@checkTerm, "MyShell");
        push(@checkTerm, "Echo commands");
} elsif(lc($ARGV[0]) eq "phs") {
        push(@searchTerm, "intitle:\"PHP Shell 1.5\"");
        push(@searchTerm, "intitle:\"PHP Shell 1.6\"");
        push(@searchTerm, "intitle:\"PHP Shell 1.7\"");
        push(@searchTerm, "\"Enable stderr-trapping?\"");
        push(@checkTerm, "PHP Shell");
        push(@checkTerm, "Choose new working");
} elsif(lc($ARGV[0]) eq "phm") {
        push(@searchTerm, "\"PHPShell by Macker\"");
        push(@searchTerm, "\"[ Main Menu ]      [ PHPKonsole ]      [ Haxplorer ]\"");
        push(@checkTerm, "Haxplorer");
        push(@checkTerm, "PHPKonsole");
} elsif(lc($ARGV[0]) eq "rem") {
        push(@searchTerm, "intitle:\"phpRemoteView: \"");
        push(@searchTerm, "\"REMVIEW TOOLS\"");
        push(@checkTerm, "phpRemoteView");
        push(@checkTerm, "perms");
}

if(!@searchTerm) {
        print "Error: [shell to find] is a unknown shell\n" and die;
}

my $outputOn;

if(lc($ARGV[1]) eq "on") {
        $outputOn = 1;
} elsif(lc($ARGV[1]) eq "off") {
        $outputOn = 0;
} else {
        print "Error: [screen output] must be \"on\" or \"off\"\n" and die;
}

my $outputFile;

if(index(lc($ARGV[2]), ".htm") > 0) {
        $outputFile = $ARGV[2];
} else {
        print "Error: [output HTML file] must be *.htm or *.html\n" and die;
}

open(FILEHANDLE, ">$outputFile");
print FILEHANDLE "<html><head><title>PHP Shell's</title></head><body>\n";
close FILEHANDLE;

my $userAgent = LWP::UserAgent->new;
$userAgent->agent("User-Agent=Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.5) Gecko/20061201 Firefox/2.0.0.5");

my @resultLinks;

foreach(@searchTerm) {
        print "[*] Query for \"$_\"\n" if($outputOn == 1);
       
        my $isLastPage = 0;
       
        for(my $gPage = 0; ; $gPage++) {
                if($isLastPage == 1) { last; }
               
                my $gRequest =  HTTP::Request->new(GET => "http://www.google.de/search?q=$_&start=$gPage"."0");
                my $gResource = $userAgent->request($gRequest);
               
                if($gResource->is_success) {
                        my @gContent = split("<div class=g>", $gResource->content);
                        if(@gContent < 10) { $isLastPage = 1; };
                       
                        for(my $gPiece = 1; $gPiece < @gContent; $gPiece++) {
                                my $shellLink = substr($gContent[$gPiece], index($gContent[$gPiece], "href=\"") + 6);
                                $shellLink = substr($shellLink, 0, index($shellLink, "\""));
                               
                                print "[*] Check status of site \"$shellLink\"\n" if($outputOn == 1);
                               
                                my $sRequest = HTTP::Request->new(GET => $shellLink);
                                my $sResource = $userAgent->request($sRequest);
                               
                                if($sResource->is_success) {
                                        if(index($sResource->content, $checkTerm[0]) != -1 && index($sResource->content, $checkTerm[1]) != -1) {
                                                open(FILEHANDLE, ">>$outputFile");
                                                print FILEHANDLE "Link: <a href=\"$shellLink\">$shellLink</a><br>\n";
                                                print FILEHANDLE "Search Term: <i>$_</i><br><br>\n";
                                                close FILEHANDLE;
                                               
                                                print "[+] Found shell: $shellLink\n" if($outputOn == 1);
                                        } else {
                                                print "[-] No shell\n" if($outputOn == 1);
                                        }
                                } else {
                                        print "[-] Offline\n" if($outputOn == 1);
                                }
                        }
                       
                        sleep 20; #wait 20 seconds so google dont think we are a bot
                } else {
                        print "Unable to query google\n" and die;
                }
        }
}

open(FILEHANDLE, ">>$outputFile");
print FILEHANDLE "<br><br><center><small><a href=\"http://www.vx-dia.de.vu\">Find PHP Shells via Google - by DiA/RRLF</a></small></center></body></html>";
close FILEHANDLE;

sub usage {
        print qq(
Find PHP Shells via Google - by DiA/RRLF (http://www.vx-dia.de.vu)
       
Usage:   perl $0 [shell to find] [screen output] [output HTML file]
                  [shell to find] can be:
                        r57 - find r57shell
                        c99 - find c99shell
                        mys - find MyShell
                        phs - find PHP Shell
                        phm - find PHPShell (Macker)
                        rem - find phpRemoteView
                  [screen output] can be:
                        on  - every step the script doas get printed on the screen
                        off - no output, the script just writes to the output file
                  [output HTML file] must be:
                        *.htm or *.html
                                                           
Example: perl $0 c99 on c99shells.htm
         perl $0 mys off manyshells.htm

)       and exit;
} 
