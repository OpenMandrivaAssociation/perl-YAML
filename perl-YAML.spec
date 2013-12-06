%define modname	YAML
%define modver	0.84

Summary:	YAML Ain't Markup Language (tm)
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/YAML/%{modname}-%{modver}.tar.gz
Buildarch:	noarch
BuildRequires:	perl-Test-Base >= 0.47
BuildRequires:	perl-devel
Provides:	perl-YAML-parser

%description
The YAML.pm module implements a YAML Loader and Dumper based on the YAML 1.0
specification. http://www.yaml.org/spec/

YAML is a generic data serialization language that is optimized for human
readability. It can be used to express the data structures of most modern
programming languages. (Including Perl!!!)

For information on the YAML syntax, please refer to the YAML specification.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/YAML*
%{perl_vendorlib}/Test/YAML*
%{_mandir}/man3/*

