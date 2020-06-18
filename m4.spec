# For __muloti4
%global optflags %{optflags} --rtlib=compiler-rt

%ifarch %{armx}
%define _disable_rebuild_configure 1
%endif

# (tpg) enable PGO build
%ifnarch riscv64
%bcond_without pgo
%else
%bcond_with pgo
%endif

Summary:	The GNU macro processor
Name:		m4
Version:	1.4.18
Release:	12
License:	GPLv3+
Group:		Development/Other
Url:		http://www.gnu.org/software/m4/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
Patch0:		m4-1.4.18-clang.patch
Patch1:		0002-Fix-build-with-glibc-2.18.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsigsegv-devel
BuildRequires:	hostname
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
export LLVM_PROFILE_FILE=%{name}-%p.profile.d
export LD_LIBRARY_PATH="$(pwd)"
CFLAGS="%{optflags} -fprofile-instr-generate" \
CXXFLAGS="%{optflags} -fprofile-instr-generate" \
FFLAGS="$CFLAGS" \
FCFLAGS="$CFLAGS" \
LDFLAGS="%{ldflags} -fprofile-instr-generate" \
%configure \
    --without-included-regex \
    --with-libsigsegv-prefix=%{_prefix}

%make_build
make check ||:
unset LD_LIBRARY_PATH
unset LLVM_PROFILE_FILE
llvm-profdata merge --output=%{name}.profile $(find . -type f -name "*.profile.d")
rm -f *.profile.d
make clean

CFLAGS="$RPM_OPT_FLAGS -fprofile-instr-use=$(realpath %{name}.profile)" \
CXXFLAGS="%{optflags} -fprofile-instr-use=$(realpath %{name}.profile)" \
FFLAGS="$CFLAGS" \
FCFLAGS="$CFLAGS" \
LDFLAGS="%{ldflags} -fprofile-instr-use=$(realpath %{name}.profile)" \
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

%files
%doc NEWS README BACKLOG THANKS
%{_bindir}/%{name}
%{_infodir}/*
%{_mandir}/man1*/*
