Summary:	The GNU macro processor
Name:		m4
Version:	1.4.17
Release:	10
License:	GPLv3+
Group:		Development/Other
Url:		http://www.gnu.org/software/m4/
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
%apply_patches
 
%build
export gl_cv_func_strtod_works=no 
%configure2_5x
%make

%check
%define Werror_cflags %{nil}
make check CFLAGS="%optflags"

%install
%makeinstall_std infodir=%{_datadir}/info

%files
%doc NEWS README BACKLOG THANKS ChangeLog
%{_bindir}/%{name}
%{_infodir}/*
%{_mandir}/man1*/*

