#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	NetAddr
%define	pnam	IP
Summary:	NetAddr::IP - Manages IPv4 and IPv6 addresses and subnets
Summary(pl):	NetAddr::IP - zarz±dzanie adresami i podsieciami IPv4 i IPv6
Name:		perl-NetAddr-IP
Version:	3.21
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c6033bdadf356daf4bd4658247f5362e
URL:		http://search.cpan.org/dist/NetAddr-IP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Math::BigInt)
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an object-oriented abstraction on top of IP
addresses or IP subnets, that allows for easy manipulations.

%description -l pl
Ten modu³ dostarcza obiektowo zorientowan± abstrakcjê dla adresów lub
podsieci IP pozwalaj±c± na ³atwe operacje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/NetAddr/IP

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO *.htm
%{perl_vendorlib}/NetAddr/*.pm
%dir %{perl_vendorlib}/NetAddr/IP
%{_mandir}/man3/*
