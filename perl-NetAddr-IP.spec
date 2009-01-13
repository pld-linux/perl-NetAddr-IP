#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	NetAddr
%define	pnam	IP
Summary:	NetAddr::IP - Manages IPv4 and IPv6 addresses and subnets
Summary(pl.UTF-8):	NetAddr::IP - zarządzanie adresami i podsieciami IPv4 i IPv6
Name:		perl-NetAddr-IP
Version:	4.022
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1cc73e524b244435c172a9f7dbc39bea
URL:		http://search.cpan.org/dist/NetAddr-IP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More)
BuildRequires:	perl-Math-BigInt
BuildRequires:	perl-Module-Signature
%endif
Obsoletes:	perl-NetAddr-IP-Lite <= 0:1.01
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an object-oriented abstraction on top of IP
addresses or IP subnets, that allows for easy manipulations.

%description -l pl.UTF-8
Ten moduł dostarcza obiektowo zorientowaną abstrakcję dla adresów lub
podsieci IP pozwalającą na łatwe operacje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%dir %{perl_vendorarch}/NetAddr
%dir %{perl_vendorarch}/NetAddr/IP
%{perl_vendorarch}/NetAddr/*.pm
%{perl_vendorarch}/NetAddr/IP/*.pm
%dir %{perl_vendorarch}/auto/NetAddr
%dir %{perl_vendorarch}/auto/NetAddr/IP
%dir %{perl_vendorarch}/auto/NetAddr/IP/Util
%attr(755,root,root) %{perl_vendorarch}/auto/NetAddr/IP/Util/*.so
%{perl_vendorarch}/auto/NetAddr/IP/Util/*.ix
%{perl_vendorarch}/auto/NetAddr/IP/Util/*.al
%dir %{perl_vendorarch}/auto/NetAddr/IP/UtilPP
%{perl_vendorarch}/auto/NetAddr/IP/UtilPP/*.ix
%{perl_vendorarch}/auto/NetAddr/IP/UtilPP/*.al
%{perl_vendorarch}/auto/NetAddr/IP/*.ix
%{perl_vendorarch}/auto/NetAddr/IP/*.al
%{_mandir}/man3/*
