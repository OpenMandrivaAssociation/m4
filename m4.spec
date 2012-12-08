Summary:	The GNU macro processor
Name:		m4
Version:	1.4.16
Release:	6
License:	GPLv3+
Group:		Development/Other
URL:		http://www.gnu.org/software/m4/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2.sig
BuildRequires:	libsigsegv-devel

%description
A GNU implementation of the traditional UNIX macro processor.  M4 is
useful for writing text files which can be logically parsed, and is used
by many programs as part of their build process.  M4 has built-in
functions for including files, running shell commands, doing arithmetic,
etc.  The autoconf program needs m4 for generating configure scripts, but
not for running configure scripts.

m4 is most likely needed if you want to compile or develop software.

%prep

%setup -q

%build
export gl_cv_func_strtod_works=no 
%configure2_5x
%make

%check
%define Werror_cflags %nil
make check CFLAGS="%optflags"

%install
%makeinstall_std infodir=%{_datadir}/info

%files
%defattr(-,root,root)
%doc NEWS README BACKLOG THANKS ChangeLog
%{_bindir}/%{name}
%{_infodir}/*
%{_mandir}/man1*/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.16-3mdv2011.0
+ Revision: 666353
- mass rebuild

* Wed Mar 02 2011 Funda Wang <fwang@mandriva.org> 1.4.16-2
+ Revision: 641269
- BR sigsegv
- update to new version 1.4.16

* Wed Sep 01 2010 Funda Wang <fwang@mandriva.org> 1.4.15-1mdv2011.0
+ Revision: 574992
- update to new version 1.4.15

* Thu Feb 25 2010 Funda Wang <fwang@mandriva.org> 1.4.14-1mdv2010.1
+ Revision: 511038
- disable format check when running test
- new version 1.4.14

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 1.4.13-1mdv2010.0
+ Revision: 369861
- New version 1.4.13

* Wed Oct 29 2008 Funda Wang <fwang@mandriva.org> 1.4.12-1mdv2009.1
+ Revision: 298554
- New version 1.4.12

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.4.11-2mdv2009.0
+ Revision: 265036
- rebuild early 2009.0 package (before pixel changes)

* Fri Apr 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.11-1mdv2009.0
+ Revision: 195587
- make the tests pass
- 1.4.11

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.4.10-3mdv2008.1
+ Revision: 152890
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.4.10-2mdv2008.1
+ Revision: 152889
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jul 14 2007 Funda Wang <fwang@mandriva.org> 1.4.10-1mdv2008.0
+ Revision: 51975
- New version

* Sat Jul 07 2007 Funda Wang <fwang@mandriva.org> 1.4.9-1mdv2008.0
+ Revision: 49330
- New version


* Sun Dec 10 2006 Emmanuel Andry <eandry@mandriva.org> 1.4.8-1mdv2007.0
+ Revision: 94417
- New version 1.4.8
- Import m4

* Fri Jan 06 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.4.4-1mdk
- 1.4.4
- %%mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.4.3-2mdk
- Rebuild

* Wed Jun 08 2005 Abel Cheung <deaddog@mandriva.org> 1.4.3-1mdk
- 1.4.3
- Can makeinstall_std now
- Prereq -> Requires
- Use bz2 again since it is readily available in mirror (with signature)
- Fix URL

* Wed Nov 10 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4.2-1mdk
- 1.4.2
- cosmetics

* Fri Jun 11 2004 Abel Cheung <deaddog@deaddog.org> 1.4.1-1mdk
- Finally, after 10 years...
- Patch not needed
- Use tar.gz instead, package is signed

