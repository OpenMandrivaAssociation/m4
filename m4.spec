# For __muloti4
%global optflags %{optflags} --rtlib=compiler-rt

%ifarch %{armx}
%define _disable_rebuild_configure 1
%endif

Summary:	The GNU macro processor
Name:		m4
Version:	1.4.18
Release:	5
License:	GPLv3+
Group:		Development/Other
Url:		http://www.gnu.org/software/m4/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
Patch0:		m4-1.4.18-clang.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsigsegv-devel
BuildRequires:	git-core
Requires:	/bin/sh

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
%autopatch -p1

%build
export gl_cv_func_strtod_works=no
%configure
%make_build

%check
%define Werror_cflags %{nil}
make check CFLAGS="%{optflags}"

%install
%make_install infodir=%{_datadir}/info

%files
%doc NEWS README BACKLOG THANKS
%{_bindir}/%{name}
%{_infodir}/*
%{_mandir}/man1*/*
