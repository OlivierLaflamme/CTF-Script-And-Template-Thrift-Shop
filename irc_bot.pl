#!/usr/bin/perl
use strict();
use warnings();
use IO::Socket;


#default Options
my $network = "irc.freenodel.org"; #Network to connect to
my @channels = ("#trea"); #Channels to join in
my $op = "bla.vhost.at"; #Admin Vhost
my $nick = "aBot"; #Nick bot uses
my $user = "abot \"localhost\" \"".$network."\" :aBot"; #Username
my $chancount = 0; #How much channels are default ?!

sub send_pong;
sub join_chans;
sub parse_cmds;
sub do_command;
sub send_raw;

my $socket = IO::Socket::INET->new
            (PeerAddr => $network,
                PeerPort => 6667,
                Proto => "tcp",
                Type => SOCK_STREAM) or die("Can't Connect");
send_raw ("user $user\n");
send_raw ("nick $nick\n");
while(<$socket>) {
   parse_cmds($_);
   if($_ =~ '376')
   {
      print "[!] End of MOTD reached\n";
      print "[!] Joining Channels\n";
      join_chans($_);
   }
}
      
close($socket);

sub do_command{
   ($name_, $to_, $host_, $cmd_) = @_;
   if($cmd_ =~ /^!help/){
      send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :#User Commands\n");
      send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :  !help - shows help menu\n");   
      send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :  !chancount - shows how much channels needs me\n");   
      send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :  !chanlist - shows in wich channels im\n");
      send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :  !sqrt - prints the root of the given number;example: 9 is 3\n");
   }
   if($cmd_ =~ /^!sqrt (\d*)/){
      $root = $1;
      send_raw("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :".$root." is ".sqrt($root)."\n");
   }
   if($cmd_ =~ /^!chancount/){
      send_raw("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :im in $chancount Channel(s)\n");
      send_raw("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :write !chanlist if you want to see in wich channels im\n");
   }
   if($cmd_ =~ /^!chanlist/){
      send_raw("PRIVMSG ".$name_." :im in:\n");
      foreach $chanl (@channels){
         send_raw("PRIVMSG ".$name_." :".$chanl.", \n");
      }
   }
   if($host_ eq $op){
      if($cmd_ =~ /^!help/){
         send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :#Adminstrative Commands\n");
         send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :  !kick <chan> <nick> - kicks a user outta a channel\n");
         send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :  !kickban <chan> <nick> - kickban's a user outta a channel\n");
         send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :  !op <+/-> <chan> :<nick> - give operator/take operator rights from a user\n");
         send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :  !voice <+/-> <chan> :<nick> - give voice/take voice rights from a user\n");
         send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :  !chanmode <mode(s)> - set channel modes\n");
      }
      if($cmd_ =~ /^!chanmode (.*)/ ){
         $mode = $1;
      send_raw("MODE $to_ $mode\n");
      }
      if($cmd_ =~ /^!voice (.+?) (.+?) \:(.*)/){
         $chan = $2;
         $who = $3;
         $mode = $1;
         
         if($chan !~ /^#(.*)/){
            send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :arg1 is no channel\n");
            return;
         }
         if($mode eq "+"){
            send_raw("MODE ".$chan." +v ".$who."\n");
         }
         elsif($mode eq "-"){
            send_raw("MODE ".$chan." -v ".$who."\n");
         }
      }
      if($cmd_ =~ /^!op (.+?) (.+?) \:(.*)/){
         $chan = $2;
         $who = $3;
         $mode = $1;
         if($chan !~ /#(.*)/){
            send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :arg1 is no channel\n");
            return;
         }
         if($mode eq "+"){
            send_raw("MODE ".$chan." +o ".$who."\n");
         }
         elsif($mode eq "-"){
            send_raw("MODE ".$chan." -o ".$who."\n");
         }
      }
      if($cmd_ =~ /^!eval (.*)/){
         eval $1;
      }   
      if($cmd_ =~ /^!join (.*)/){
         if($1 !~ /#(.*)/){
            send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :arg1 is no channel\n");
            return;
         }
         else   {
            $channels[$chancount] = "#".$1;
            print "[!] Joining Channel: ".$channels[$chancount]."\n";
            send_raw ("JOIN ".$channels[$chancount]."\n");
            $chancount++;
         }
      }
      if($cmd_ =~ /!kick (.*) (.*)/){
         $kchan = $1;
         $knick = $2;
         if($1 !~ /#(.*)/){
            send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :arg1 is no channel\n");
            return;
         }
         else{
            send_raw("KICK $kchan $knick\n");
         }
      }
      if($cmd_ =~ /^!kickban (.*) (.*)/){
         $kchan = $1;
         $knick = $2;
         if($1 !~ /#(.*)/){
            send_raw ("PRIVMSG ".(($to_ =~/#(.*)/)? $to_ : $name_)." :arg1 is no channel\n");
            return;
         }
         else{
            send_raw("MODE ".$kchan." +b ".$knick."\n");
            send_raw("KICK $kchan $knick\n");
         }
      }
   }
}

sub parse_cmds{
   $cmds = shift;
   if($cmds =~ /^PING/){
      send_pong($_);
   }
   elsif ($cmds =~ /^\:(.+?)\!(.+?)\@(.+?) PRIVMSG (.+?) \:(.+)/){
      my $name=$1; my $host=$3; my $from=$4; my $args=$5;
      if ($args =~ /^VERSION$/) {
               send_raw ("PRIVMSG ".$name." :Dont disturb me!\n");
            }
      if($args =~ /^\!(.*)/)
      {
         do_command($name, $from, $host, $args);      
      }
   }
}

sub join_chans{

   foreach $jchan (@channels){
      send_raw("join $jchan\n");
   $chancount++;
   printf "[!] Joining Channel: ".$jchan."\n";

   }
}

sub send_raw{
   my $tosend = shift;
   print $socket "$tosend";
}

sub send_pong{
   $pong = shift;
   if($pong =~ /^PING (.*)/){
      send_raw("PONG $1");
   }
}
