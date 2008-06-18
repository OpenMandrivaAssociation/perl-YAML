%define module	YAML
%define name	perl-%{module}
%define version 0.66
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	YAML Ain't Markup Language (tm)
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/YAML/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%{name}-%{version}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.6.1
%endif
BuildRequires:	perl-Test-Base >= 0.47
Buildarch:	noarch

%description
The YAML.pm module implements a YAML Loader and Dumper based on the YAML 1.0
specification. http://www.yaml.org/spec/

YAML is a generic data serialization language that is optimized for human
readability. It can be used to express the data structures of most modern
programming languages. (Including Perl!!!)

For information on the YAML syntax, please refer to the YAML specification.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes COMPATIBILITY README
%{_bindir}/*
%{perl_vendorlib}/YAML*
%{perl_vendorlib}/Test/YAML*
%{_mandir}/*/*

