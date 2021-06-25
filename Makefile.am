AUTOMAKE_OPTIONS = foreign subdir-objects
dist_bin_SCRIPTS = bin/getzipgit
dist_man_MANS = man/getzipgit.8

all-am: getzipgit

getzipgit: bin/getzipgit
	@echo "Found getzipgit"
	@echo "You may now run \'make dist\'"

nuke:
	@rm config.status configure config.log
	@rm Makefile 
	@rm -r autom4te.cache/
	@rm aclocal.m4 
	@rm compile install-sh missing Makefile.in
	@rm config.guess
	@rm config.sub
