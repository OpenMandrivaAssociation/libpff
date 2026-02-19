%define major 1
%define libname %mklibname pff
%define devname %mklibname pff -d
%global optflags %{optflags} -I%{_builddir}/%{name}-%{version}/libcerror -I%{_builddir}/%{name}-%{version}/libcnotify -I%{_builddir}/%{name}-%{version}/libclocale -I%{_builddir}/%{name}-%{version}/libuna -I%{_builddir}/%{name}-%{version}/libcsplit -I%{_builddir}/%{name}-%{version}/libcthread -I%{_builddir}/%{name}-%{version}/libcdata -I%{_builddir}/%{name}-%{version}/libcfile -I%{_builddir}/%{name}-%{version}/libcpath -I%{_builddir}/%{name}-%{version}/libfcache -I%{_builddir}/%{name}-%{version}/libfdatetime -I%{_builddir}/%{name}-%{version}/libfguid -I%{_builddir}/%{name}-%{version}/libfwnt -I%{_builddir}/%{name}-%{version}/libbfio -I%{_builddir}/%{name}-%{version}/libfdata -I%{_builddir}/%{name}-%{version}/libfmapi -I%{_builddir}/%{name}-%{version}/libfvalue

Name:		libpff
Version:	20231205
Release:	1
Source0:	https://github.com/libyal/libpff/releases/download/%{version}/libpff-alpha-%{version}.tar.gz
Summary:	Library and tools to access the PFF and OFF formats
URL:		https://github.com/libyal/libpff
License:	LGPL-3.0
Group:		System/Libraries
BuildRequires:	autoconf automake slibtool
BuildRequires:	pkgconfig(zlib)
# Can't go the declarative route yet because
# libpff doesn't support out-
BuildSystem:	autotools

%description
Library and tools to access the Personal Folder File (PFF)
and Offline Folder File (OFF) file formats used by Outlook
to store email, contacts and other data

%package -n %{libname}
Summary:	Library and tools to access the PFF and OFF formats
Group:		System/Libraries

%description -n %{libname}
Library and tools to access the Personal Folder File (PFF)
and Offline Folder File (OFF) file formats used by Outlook
to store email, contacts and other data

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep -a
find . -name Makefile.am |xargs sed -i -e 's,-I../,-I$(top_srcdir)/,g'
slibtoolize --force
aclocal
autoheader
automake -a
autoconf

%files
%{_bindir}/*
%{_mandir}/man1/*.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*.3*
