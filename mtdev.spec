%define major	1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
 
Name:           mtdev
Version:        1.1.3
Release:        1
License:        MIT
Summary:        Kernel multi-touch transformation library
Url:            http://edge.launchpad.net/mtdev
Group:          System/Libraries
Source0:        https://launchpad.net/mtdev/trunk/1.1.3/+download/%{name}-%{version}.tar.gz
 
%description
The mtdev library transforms all variants of kernel MT (multi-touch) events to
the slotted type B protocol. The events put into mtdev may be from any MT
device, specifically type A without contact tracking, type A with contact
tracking, or type B with contact tracking. See the kernel documentation for
further details.
 
%package -n %{libname}
Summary:        Kernel multi-touch transformation library
Group:          System/Libraries
 
%description -n %{libname}
The mtdev library transforms all variants of kernel MT (multi-touch) events to
the slotted type B protocol. The events put into mtdev may be from any MT
device, specifically type A without contact tracking, type A with contact
tracking, or type B with contact tracking. See the kernel documentation for
further details.
 
%package -n %{develname}
Summary:        Development files for mtdev
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:		%{name}-devel = %{version}-%{release}
 
%description -n %{develname}
The mtdev library transforms all variants of kernel MT (multi-touch) events to
the slotted type B protocol. The events put into mtdev may be from any MT
device, specifically type A without contact tracking, type A with contact
tracking, or type B with contact tracking. See the kernel documentation for
further details.
 
This package provides the development files for mtdev.
 
%prep
%setup -q
 
%build
%configure2_5x \
  --disable-static
%make
 
%install
%makeinstall_std
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
 
%files
%doc ChangeLog README COPYING
%{_bindir}/mtdev-test
 
%files -n %{libname}
%{_libdir}/*.so.%{major}*
 
%files -n %{develname}
%{_includedir}/mtdev*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
