# untar script by yufei liu (yl2515)

if (@ARGV < 2) {
	print "Usage: perl untar.pl [hwk directory with tars] [grade report master]\n";
	exit;
}

my $hw_dir = shift(@ARGV);
my $report = shift(@ARGV);

# make sure hw_dir ends in slash
$hw_dir = $hw_dir . "/" if ($hw_dir !~ m/^*.\/$/);

my @files = glob($hw_dir . "*.tar.gz");

for (@files) {

		$_ = substr($_, length($hw_dir));

    if ($_ =~ m/([a-z]{2,3}[0-9]{1,4})\-.*/) {
			my $uni = $1;
			my $fn = $hw_dir . $uni . '.tar.gz';

			if (-e $fn) {
				unlink($fn);
			}

			print "processed $_ \n";

			system("mv " . $hw_dir . $_ . " " . $fn);
    }
}

# untar
@files = glob($hw_dir . "*.tar.gz");

for (@files) {

		$_ = substr($_, length($hw_dir));

	if ($_ =~ m/^(.*).tar.gz$/) {
		print "untarring uni $1\n";
		system("mkdir " . $hw_dir . $1);
		system("tar -C " . $hw_dir . $1 . "/ -zxvf " . $hw_dir . $_);
		print "Copying grade report for $1\n";
		system("cp $report " . $hw_dir . "/" . $1 . ".txt");

		unlink($hw_dir . $_);
	}
}

print "\nDone!\n";
