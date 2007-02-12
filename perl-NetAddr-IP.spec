#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	NetAddr
%define	pnam	IP
Summary:	NetAddr::IP - Manages IPv4 and IPv6 addresses and subnets
Summary(pl.UTF-8):   NetAddr::IP - zarządzanie adresami i podsieciami IPv4 i IPv6
Name:		perl-NetAddr-IP
Version:	4.004
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f0ef938abf0b1e43ca96fb0068381df
URL:		http://search.cpan.org/dist/NetAddr-IP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More)
BuildRequires:	perl-Math-BigInt
BuildRequires:	perl-Module-Signature
%endif
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
%{perl_vendorarch}/NetAddr/IP.pm
%dir %{perl_vendorarch}/NetAddr/IP
%{perl_vendorarch}/NetAddr/IP/Lite.pm
%{perl_vendorarch}/NetAddr/IP/Util.pm
%{perl_vendorarch}/NetAddr/IP/UtilPP.pm
%{perl_vendorarch}/NetAddr/IP/Util_IS.pm
%dir %{perl_vendorarch}/auto/NetAddr/IP/Util
%{perl_vendorarch}/auto/NetAddr/IP/Util/Util.bs
%attr(755,root,root) %{perl_vendorarch}/auto/NetAddr/IP/Util/Util.so
%{perl_vendorarch}/auto/NetAddr/IP/Util/autosplit.ix
%{perl_vendorarch}/auto/NetAddr/IP/Util/*.al
%dir %{perl_vendorarch}/auto/NetAddr/IP/UtilPP
%{perl_vendorarch}/auto/NetAddr/IP/UtilPP/autosplit.ix
%{perl_vendorarch}/auto/NetAddr/IP/UtilPP/*.al
%{perl_vendorarch}/auto/NetAddr/IP/autosplit.ix
%{perl_vendorarch}/auto/NetAddr/IP/*.al
%{_mandir}/man3/*
