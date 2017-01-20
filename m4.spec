Summary:	The GNU macro processor
Name:		m4
Version:	1.4.18
Release:	1
License:	GPLv3+
Group:		Development/Other
Url:		http://www.gnu.org/software/m4/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
BuildRequires:	autoconf
BuildRequires:	automake
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
# (tpg) build with GCC
#/tmp/lto-llvm-3aa0ac.o:ld-temp.o:function main: error: undefined reference to '__muloti4'
#/tmp/lto-llvm-3aa0ac.o:ld-temp.o:function make_room_for: error: undefined reference to '__muloti4'
#/tmp/lto-llvm-3aa0ac.o:ld-temp.o:function at_fatal_signal: error: undefined reference to '__muloti4'
export CC=gcc
export CXX=g++

export gl_cv_func_strtod_works=no
%configure
%make

%check
%define Werror_cflags %{nil}
make check CFLAGS="%{optflags}"

%install
%makeinstall_std infodir=%{_datadir}/info

%files
%doc NEWS README BACKLOG THANKS
%{_bindir}/%{name}
%{_infodir}/*
%{_mandir}/man1*/*
