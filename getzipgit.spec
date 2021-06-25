Name:           getzipgit
Version:        0.0.1
Release:        1%{?dist}
Summary:        Download icons from a private DAV and push to public Git
License:        GPLv3+
URL:            http://www.slackermedia.info
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
Requires:       git

%description
A script to fetch releases of a particular set of openly licensed icons from a remote DAV server and to push to a public Git repository.

%define debug_package %{nil}

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md LICENSE
%{_mandir}/man8/%{name}.8.gz

%changelog
* Thu Jun 24 2021 Seth Kenlon <skenlon@redhat.com> - 0.0.1-1
- Initial RPM release.
