#!/usr/bin/perl

use strict;
use warnings;

# New author details
my $new_author = 'alessiotucci';
my $new_email = 'alessiotucci33@gmail.com';

# Start the interactive rebase
system("git rebase -i --root");

# Modify each commit
while (<DATA>) {
    chomp;
    if ($_ =~ /^pick\s+(\S+)\s+(.*)$/) {
        my $commit = $1;
        my $message = $2;
        # Amend the commit
        system("git commit --amend --author='$new_author <$new_email>' --no-edit");
        # Continue the rebase
        system("git rebase --continue");
    }
}

__DATA__
# List of commit hashes and messages
# Replace this section with your commit hashes and messages

