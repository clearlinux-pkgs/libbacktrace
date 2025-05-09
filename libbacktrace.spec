#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v25
# autospec commit: 9594167
#
%define keepstatic 1
Name     : libbacktrace
Version  : 793921876c981ce49759114d7bb89bb89b2d3a2d
Release  : 2
URL      : https://github.com/ianlancetaylor/libbacktrace/archive/793921876c981ce49759114d7bb89bb89b2d3a2d.tar.gz
Source0  : https://github.com/ianlancetaylor/libbacktrace/archive/793921876c981ce49759114d7bb89bb89b2d3a2d.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libbacktrace-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# libbacktrace
A C library that may be linked into a C/C++ program to produce symbolic backtraces

%package dev
Summary: dev components for the libbacktrace package.
Group: Development
Provides: libbacktrace-devel = %{version}-%{release}
Requires: libbacktrace = %{version}-%{release}

%description dev
dev components for the libbacktrace package.


%package license
Summary: license components for the libbacktrace package.
Group: Default

%description license
license components for the libbacktrace package.


%package staticdev
Summary: staticdev components for the libbacktrace package.
Group: Default
Requires: libbacktrace-dev = %{version}-%{release}

%description staticdev
staticdev components for the libbacktrace package.


%prep
%setup -q -n libbacktrace-793921876c981ce49759114d7bb89bb89b2d3a2d
cd %{_builddir}/libbacktrace-793921876c981ce49759114d7bb89bb89b2d3a2d

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1745533294
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure
make  %{?_smp_mflags}

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1745533294
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libbacktrace
cp %{_builddir}/libbacktrace-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libbacktrace/555657fe7ff5be9969fa3387d8e465e0a1afa2f4 || :
export GOAMD64=v2
GOAMD64=v2
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/backtrace-supported.h
/usr/include/backtrace.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libbacktrace/555657fe7ff5be9969fa3387d8e465e0a1afa2f4

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libbacktrace.a
