#!/usr/bin/perl

# shellcode generator

 print "shellcode: ";
 $x1=<>;
 my $data = "$x1";
 chomp($data);
 my @values = split(undef,$data);

 foreach my $val (@values) {

   chomp($val);
   print '\x';
   print unpack(H8,"$val");

}

 print "\n";
 exit 0;
