Name:           pgsnap
Version:        1.0
Release:        1%{?dist}
Summary:        A small tool to take a backup of PostgreSQL

License:        MIT
URL:            https://github.com/sikevux/pgsnap
Source0:        https://github.com/sikevux/pgsnap/archive/pgsnap-%{version}.tar.gz

BuildRequires:  bash
Requires:       bash

%description
A small tool to make backups of PostgreSQL databases.
Really crude. Lots of dragons

%prep
%setup -q

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 pgsnap %{buildroot}%{_bindir}

%files
%attr(0755,root,root) %{_bindir}/pgsnap


%changelog
* Mon Jan  9 2017 Patrik Greco <sikevux@sikevux.se> - 1.0-1
- Initial release
