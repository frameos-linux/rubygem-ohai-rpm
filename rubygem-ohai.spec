# Generated from ohai-0.5.8.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname ohai
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Ohai profiles your system and emits JSON
Name: rubygem-%{gemname}
Version: 0.6.10
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://wiki.opscode.com/display/ohai
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(yajl-ruby) 
Requires: rubygem(systemu) >= 2.2
Requires: rubygem(mixlib-cli) >= 0
Requires: rubygem(mixlib-config) >= 0
Requires: rubygem(mixlib-log) >= 0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Ohai profiles your system and emits JSON


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/ohai
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct 24 2011 Sergio Rubio <rubiojr@frameos.org> - 0.6.10-1
- Upstream update
- Bump systemu dep to 2.2.0

* Fri Oct 07 2011 Sergio Rubio <rubiojr@frameos.org> - 0.6.8-1
- upstream update

* Tue Oct 04 2011 Sergio Rubio <rubiojr@frameos.org> - 0.6.6-1
- upstream 0.6.6

* Fri Apr 29 2011 Sergio Rubio <rubiojr@frameos.org> - 0.6.4-2
- upstream update

* Fri Apr 15 2011 Sergio Rubio <rubiojr@frameos.org> - 0.6.2-1
- bumped version

* Thu Apr 14 2011 Sergio Rubio <rubiojr@frameos.org> - 0.6.0-1
- bumped version
- removed json and extlib deps
- added rubygem-yajl-ruby deps

* Sun Dec 19 2010 Sergio Rubio <rubiojr@frameos.org> - 0.5.8-1
- Initial package
