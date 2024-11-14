#!/usr/bin/perl
use strict;
use warnings;
use Lingua::EN::Opinion;
use Term::ANSIColor;
use File::Slurp;

# Funzione per analizzare il sentimento
sub analyze_sentiment
{
    my ($text) = @_;
    my $opinion = Lingua::EN::Opinion->new(text => $text, stem => 1);
    my $scores;
    eval
	{
        $scores = $opinion->analyze();
    };
    if ($@)
	{
        die "Error analyzing sentiment: $@";
    }

    my ($positive, $negative, $neutral) = (0, 0, 0);
    foreach my $score (@$scores)
	{
        $positive++ if $score == 1;
        $negative++ if $score == -1;
        $neutral++ if $score == 0;
    }

    return ($positive, $negative, $neutral);
}

# Funzione per interpretare il sentimento
sub interpret_sentiment
{
    my ($positive, $negative, $neutral) = @_;
    if ($positive > $negative && $positive > $neutral)
	{
        return "Positivo", 'green';
    }
	elsif ($negative > $positive && $negative > $neutral)
	{
        return "Negativo", 'red';
    }
	else {
        return "Neutro", 'yellow';
    }
}

# Funzione principale
sub main {
    my @files = ("Elezioni_positivo.txt", "Elezioni_neutro.txt", "Elezioni_negativo.txt");

    foreach my $file_name (@files)
	{
        if (-e $file_name)
		{
            my $content = read_file($file_name);

            my ($positive, $negative, $neutral) = analyze_sentiment($content);
            my ($overall_sentiment, $color) = interpret_sentiment($positive, $negative, $neutral);

            print color('bold blue'), "\n" . "=" x 50, color('reset'), "\n";
            print color('bold blue'), "Analisi del file: $file_name", color('reset'), "\n";
            print color('bold blue'), "=" x 50, color('reset'), "\n";
            print "Polarita: ", color("bold $color"), "$overall_sentiment", color('reset'), "\n";
            print "Positivo: ", color('bold green'), "$positive", color('reset'), "\n";
            print "Neutro: ", color('bold yellow'), "$neutral", color('reset'), "\n";
            print "Negativo: ", color('bold red'), "$negative", color('reset'), "\n";

            print "\nPremi Invio per continuare...";
            <STDIN>;
        }
		else
		{
            print color('bold red'), "Errore: Il file $file_name non è stato trovato.", color('reset'), "\n";
        }
    }

    print color('bold blue'), "\nAnalisi completata!", color('reset'), "\n";
}

# Esegui la funzione principale
main();