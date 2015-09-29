#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pixman
Version  : 0.32.8
Release  : 12
URL      : http://cairographics.org/releases/pixman-0.32.8.tar.gz
Source0  : http://cairographics.org/releases/pixman-0.32.8.tar.gz
Summary  : The pixman library (version 1)
Group    : Development/Tools
License  : MIT
Requires: pixman-lib
BuildRequires : pkgconfig(libpng)

%description
Pixman is a library that provides low-level pixel manipulation
features such as image compositing and trapezoid rasterization.

%package dev
Summary: dev components for the pixman package.
Group: Development
Requires: pixman-lib
Provides: pixman-devel

%description dev
dev components for the pixman package.


%package lib
Summary: lib components for the pixman package.
Group: Libraries

%description lib
lib components for the pixman package.


%prep
%setup -q -n pixman-0.32.8

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export CFLAGS="$CFLAGS -flto -fno-semantic-interposition -O3 -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -flto -fno-semantic-interposition -O3 -ffunction-sections "
%configure --disable-static --disable-gtk
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pixman-1/pixman-version.h
/usr/include/pixman-1/pixman.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
