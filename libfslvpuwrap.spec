#
# spec file for package libfslvpuwrap
#
# Copyright (c) 2014 Josua Mayer <privacy@not.given>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

Name: libfslvpuwrap
Version: 1.0.46
Release: 1
License: Freescale IP
Group: Productivity/Multimedia/Other
Summary: Freescale VPU wrapper
Source: %{name}-%{version}.tar.gz
Source1: libfslvpuwrap-1.0.46.bin
Source10: rpmlintrc
Patch0: libtoolize.patch
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
#%%patch0 -p1 -d libfslvpuwrap-1.0.46
patch -d libfslvpuwrap-1.0.46 -p1 < %{PATCH0}

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
%doc libfslvpuwrap-1.0.46/EULA.txt

%files devel
%defattr(-,root,root)
/usr/lib/*.so
/usr/lib/*.a
/usr/lib/*.la
/usr/lib/pkgconfig/*.pc
/usr/include/imx-mm
/usr/share/imx-mm

%changelog
