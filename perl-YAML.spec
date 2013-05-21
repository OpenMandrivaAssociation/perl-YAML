%define upstream_name YAML
%define upstream_version 0.84

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	YAML Ain't Markup Language (tm)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/YAML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Test-Base >= 0.47
BuildRequires:	perl-devel
Provides:	perl-YAML-parser
Buildarch:	noarch

%description
The YAML.pm module implements a YAML Loader and Dumper based on the YAML 1.0
specification. http://www.yaml.org/spec/

YAML is a generic data serialization language that is optimized for human
readability. It can be used to express the data structures of most modern
programming languages. (Including Perl!!!)

For information on the YAML syntax, please refer to the YAML specification.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.780.0-2mdv2012.0
+ Revision: 765879
- rebuilt for perl-5.14.2

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.780.0-1
+ Revision: 764934
- 0.78

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.730.0-3
+ Revision: 764397
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.730.0-2
+ Revision: 763121
- rebuild

* Fri Apr 29 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.730.0-1
+ Revision: 660540
- new version

* Fri Sep 03 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.720.0-1mdv2011.0
+ Revision: 575599
- update to 0.72

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 0.710.0-2mdv2011.0
+ Revision: 556988
- rebuild

* Sun Jan 03 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.710.0-1mdv2010.1
+ Revision: 485808
- update to 0.71

* Sun Aug 16 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.700.0-1mdv2010.0
+ Revision: 416976
- update to 0.70

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.680.0-1mdv2010.0
+ Revision: 401810
- rebuild using %%perl_convert_version
- fixed license field

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.68-2mdv2009.1
+ Revision: 324628
- provides virtual package perl-YAML-parser

* Mon Dec 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.68-1mdv2009.1
+ Revision: 311964
- update to new version 0.68

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.67-1mdv2009.1
+ Revision: 309335
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.66-2mdv2009.0
+ Revision: 224679
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.66-1mdv2008.1
+ Revision: 97607
- update to new version 0.66

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.65-1mdv2008.0
+ Revision: 46535
- update to new version 0.65


* Tue Jul 04 2006 Scott Karns <scottk@mandriva.org> 0.62-1mdv2007.0
- Version 0.62 -- Upstream incorporation blessed ref LoadFile/DumpFile
  patch

* Mon Jul 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.61-2mdv2007.0
- Patch 0: Allow to use LoadFile/DumpFile on filenames that are blessed
  references with overloaded stringification.

* Sun Jul 02 2006 Scott Karns <scottk@mandriva.org> 0.61-1mdv2007.0
- 0.61

* Fri Feb 17 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.58-1mdk
- 0.58

* Thu Feb 02 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.57-1mdk
- 0.57

* Tue Jan 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.53-1mdk
- 0.53
- Update BuildRequires

* Thu Jan 19 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.52-1mdk
- 0.52

* Wed Jan 18 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.51-2mdk
- Add BuildRequires : perl-Test-Base

* Wed Jan 18 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.51-1mdk
- 0.51

* Tue Jan 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.50-1mdk
- 0.50

* Wed Apr 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdk 
- new release
- spec cleanup
- disable test, we need a more recent Test module in core

* Mon Jan 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.36-1mdk
- 0.36
- add tests

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.35-3mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.35-2mdk 
- rpmbuildupdate aware

* Fri Dec 05 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.35-1mdk
- first mdk release

