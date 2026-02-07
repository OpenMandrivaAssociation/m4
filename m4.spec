%ifarch %{armx}
%define _disable_rebuild_configure 1
%endif

%if %{cross_compiling}
%bcond_with pgo
%else
# (tpg) enable PGO build
%bcond_without pgo
%endif

Summary:	The GNU macro processor
Name:		m4
Version:	1.4.21
Release:	1
License:	GPLv3+
Group:		Development/Other
Url:		https://www.gnu.org/software/m4/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc

BuildRequires:	slibtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	libsigsegv-devel
BuildRequires:	hostname
BuildRequires:	make
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
%autosetup -p1

%build
export gl_cv_func_strtod_works=no

%if %{with pgo}
export LD_LIBRARY_PATH="$(pwd)"

CFLAGS="%{optflags} -fprofile-generate" \
CXXFLAGS="%{optflags} -fprofile-generate" \
LDFLAGS="%{build_ldflags} -fprofile-generate" \
%configure \
    --without-included-regex \
    --with-libsigsegv-prefix=%{_prefix}

%make_build
make check ||:
unset LD_LIBRARY_PATH
llvm-profdata merge --output=%{name}-llvm.profdata $(find . -name "*.profraw" -type f)
PROFDATA="$(realpath %{name}-llvm.profdata)"
rm -f *.profraw
make clean

CFLAGS="%{optflags} -fprofile-use=$PROFDATA" \
CXXFLAGS="%{optflags} -fprofile-use=$PROFDATA" \
LDFLAGS="%{build_ldflags} -fprofile-use=$PROFDATA" \
%endif
%configure \
    --without-included-regex \
    --with-libsigsegv-prefix=%{_prefix}

%make_build

%check
%define Werror_cflags %{nil}
make check CFLAGS="%{optflags}" ||:

%install
%make_install infodir=%{_datadir}/info

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README THANKS
%{_bindir}/%{name}
%doc %{_infodir}/*
%doc %{_mandir}/man1*/*
