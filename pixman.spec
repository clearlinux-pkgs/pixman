#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
%define keepstatic 1
Name     : pixman
Version  : 0.42.2
Release  : 56
URL      : https://cairographics.org/releases/pixman-0.42.2.tar.gz
Source0  : https://cairographics.org/releases/pixman-0.42.2.tar.gz
Summary  : The pixman library (version 1)
Group    : Development/Tools
License  : MIT
Requires: pixman-lib = %{version}-%{release}
Requires: pixman-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libpng-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32pixman-1)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : zlib-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: fmv.patch
Patch2: avx2.patch
Patch3: avx2-2.patch

%description
Pixman
======
Pixman is a library that provides low-level pixel manipulation
features such as image compositing and trapezoid rasterization.

%package dev
Summary: dev components for the pixman package.
Group: Development
Requires: pixman-lib = %{version}-%{release}
Provides: pixman-devel = %{version}-%{release}
Requires: pixman = %{version}-%{release}

%description dev
dev components for the pixman package.


%package dev32
Summary: dev32 components for the pixman package.
Group: Default
Requires: pixman-lib32 = %{version}-%{release}
Requires: pixman-dev = %{version}-%{release}

%description dev32
dev32 components for the pixman package.


%package lib
Summary: lib components for the pixman package.
Group: Libraries
Requires: pixman-license = %{version}-%{release}

%description lib
lib components for the pixman package.


%package lib32
Summary: lib32 components for the pixman package.
Group: Default
Requires: pixman-license = %{version}-%{release}

%description lib32
lib32 components for the pixman package.


%package license
Summary: license components for the pixman package.
Group: Default

%description license
license components for the pixman package.


%package staticdev
Summary: staticdev components for the pixman package.
Group: Default
Requires: pixman-dev = %{version}-%{release}

%description staticdev
staticdev components for the pixman package.


%package staticdev32
Summary: staticdev32 components for the pixman package.
Group: Default
Requires: pixman-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the pixman package.


%prep
%setup -q -n pixman-0.42.2
cd %{_builddir}/pixman-0.42.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a pixman-0.42.2 build32
popd
pushd ..
cp -a pixman-0.42.2 buildavx2
popd
pushd ..
cp -a pixman-0.42.2 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685570759
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}" %reconfigure  --disable-gtk \
--disable-mmx \
--disable-sse2 \
--disable-ssse3 \
--enable-static
make  %{?_smp_mflags}

make check || :
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}" %reconfigure  --disable-gtk \
--disable-mmx \
--disable-sse2 \
--disable-ssse3 \
--enable-static
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure  --disable-gtk \
--disable-mmx \
--disable-sse2 \
--disable-ssse3 \
--enable-static  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%reconfigure  --disable-gtk \
--disable-mmx \
--disable-sse2 \
--disable-ssse3 \
--enable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%reconfigure  --disable-gtk \
--disable-mmx \
--disable-sse2 \
--disable-ssse3 \
--enable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :
cd ../buildavx512;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1685570759
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pixman
cp %{_builddir}/pixman-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pixman/3b90aaf730fa20460f8fe3fd20c16daf3acaba59 || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pixman-1/pixman-version.h
/usr/include/pixman-1/pixman.h
/usr/lib64/libpixman-1.so
/usr/lib64/pkgconfig/pixman-1.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpixman-1.so
/usr/lib32/pkgconfig/32pixman-1.pc
/usr/lib32/pkgconfig/pixman-1.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpixman-1.so.0.42.2
/V4/usr/lib64/libpixman-1.so.0.42.2
/usr/lib64/libpixman-1.so.0
/usr/lib64/libpixman-1.so.0.42.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpixman-1.so.0
/usr/lib32/libpixman-1.so.0.42.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pixman/3b90aaf730fa20460f8fe3fd20c16daf3acaba59

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libpixman-1.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libpixman-1.a
