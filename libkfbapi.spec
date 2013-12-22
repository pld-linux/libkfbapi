Summary:	Library to access to Facebook services
Name:		libkfbapi
Version:	1.0
Release:	1
License:	GPL v2+
Group:		Development/Libraries
URL:		http://projects.kde.org/libkfbapi
Source0:	ftp://ftp.kde.org/pub/kde/stable/libkfbapi/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	05ce3213a1383796a02115705c2bf829
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	kde4-kdepimlibs-devel
BuildRequires:	qjson-devel >= 0.7

%description
Library to access to Facebook services, this package is needed by
kdepim-runtime to build akonadi-facebook resources.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdepimlibs-devel

%description devel
Libraries and header files for developing applications that use
akonadi-facebook resources.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkfbapi.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkfbapi.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/libkfbapi
%{_pkgconfigdir}/LibKFbAPI.pc
%attr(755,root,root) %{_libdir}/libkfbapi.so
%{_libdir}/cmake/LibKFbAPI
