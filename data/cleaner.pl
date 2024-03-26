#!/usr/bin/env perl

package main;
use strict;
use warnings;
use 5.010;
use utf8;
use Const::Fast;
use Data::Dumper;
our $VERSION = 'v0.0.1';

sub convline
{
    my ($word, $definition) = shift =~ /^([^=]+)=\s?(.+)$/;
    return '' unless defined $definition;
    $definition =~ s/=/-/g;
    $definition =~ s/\.$//g;
    chop $word and $word = ucfirst $word;
    $definition = ucfirst $definition;

    return "$word; $definition\n";
}

sub main
{
    binmode STDOUT, ':encoding(UTF-8)';
    const my $filename => $ARGV[0];
    die "Usage: $0 <input filename>"  unless -e $filename;
    die "Unable to open $filename $!" unless open my $fd, '<', $filename;
    print convline $_ while <$fd>;
    die "$!" unless close $fd;
    return 0;
}

main();

1;
# vim: set ft = perl
__END__
