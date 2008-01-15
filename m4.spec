%define	name	m4
%define	version	1.4.10
%define	release	%mkrel 3

Summary:	The GNU macro processor
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
Url:		http://www.gnu.org/software/m4/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2.sig
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post,preun):	info-install

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
%configure2_5x
%make

make check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std infodir=%{_datadir}/info

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README BACKLOG THANKS ChangeLog
%{_bindir}/%{name}
%{_infodir}/*
%{_mandir}/man1*/*
