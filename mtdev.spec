%define major	1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
 
Summary:	Kernel multi-touch transformation library
Name:		mtdev
Version:	1.1.4
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://edge.launchpad.net/mtdev
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
%setup -q
 
%build
%configure2_5x \
	--disable-static
%make
 
%install
%makeinstall_std
 
%files
%doc ChangeLog README COPYING
%{_bindir}/mtdev-test
 
%files -n %{libname}
%{_libdir}/libmtdev.so.%{major}*
 
%files -n %{devname}
%{_includedir}/mtdev*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

