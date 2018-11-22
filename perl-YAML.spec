%define modname	YAML
%define modver 1.27

Summary:	YAML Ain't Markup Language (tm)

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/YAML
Source0:	http://www.cpan.org/modules/by-module/%{modname}/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-Test-Base >= 0.47
BuildRequires:	perl-devel
Provides:	perl-YAML-parser
BuildArch:	noarch

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
#we dont have the deps
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/YAML*
# %{perl_vendorlib}/Test/YAML*
%{_mandir}/man3/*
