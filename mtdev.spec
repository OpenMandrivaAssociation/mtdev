%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%global optflags %{optflags} -Oz

Summary:	Kernel multi-touch transformation library
Name:		mtdev
Version:	1.1.7
Release:	1
License:	MIT
Group:		System/Libraries
Url:		https://edge.launchpad.net/mtdev
Source0:	https://launchpad.net/mtdev/trunk/%{version}/+download/%{name}-%{version}.tar.gz
 
%description
The mtdev library transforms all variants of kernel MT (multi-touch) events to
the slotted type B protocol. The events put into mtdev may be from any MT
device, specifically type A without contact tracking, type A with contact
tracking, or type B with contact tracking. See the kernel documentation for
further details.

%package -n %{libname}
Summary:	Kernel multi-touch transformation library
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development files for mtdev
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the development files for mtdev.

%prep
%autosetup -p1

%build
%configure \
	--disable-static
%make_build

%install
%make_install

%files
%doc ChangeLog README COPYING
%{_bindir}/mtdev-test

%files -n %{libname}
%{_libdir}/libmtdev.so.%{major}*

%files -n %{devname}
%{_includedir}/mtdev*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
