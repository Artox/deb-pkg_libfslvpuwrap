Name: libfslvpuwrap
Version: 1.0.46
Release: 1
License: TODO
Group: Productivity/Multimedia/Other
Summary: Freescale VPU wrapper
Source: %{name}-%{version}.tar.gz
Source1: libfslvpuwrap-1.0.46.bin
Source10: rpmlintrc
BuildRequires: python
BuildRequires: libvpu-imx6-devel
BuildRequires: pkg-config

%description
Provides Freescale's VPU wrapper library.

%package devel
Group: Development/Libraries/C and C++
Summary: Development files for libfslvpuwrap
Requires: %{name} = %{version}-%{release}
%description devel
Provides development files for building against the VPU wrapper library for Freescale i.MX SoCs.

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%prep
%setup -q
chmod +x %{SOURCE1}
%{SOURCE1} --auto-accept --force

%build
cd libfslvpuwrap-1.0.46
%configure
make

%install
cd libfslvpuwrap-1.0.46
%make_install

%files
%defattr(-,root,root)
/usr/lib/*.so.*
/usr/share/doc/libfslvpuwrap

%files devel
%defattr(-,root,root)
/usr/lib/*.so
/usr/lib/*.a
/usr/lib/*.la
/usr/lib/pkgconfig/*.pc
/usr/include/imx-mm
/usr/share/imx-mm

%changelog
