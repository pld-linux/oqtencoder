Summary:	Simple encoder that uses OpenQuicktime library
Summary(pl):	Prosty koder korzystaj±cy z biblioteki OpenQuicktime
Name:		oqtencoder
Version:	0.1
Release:	1
License:	LGPL
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Group(pt):	Aplicações/Gráficos
Source0:	http://prdownloads.sourceforge.net/openquicktime/%{name}-%{version}.tgz
URL:		http://openquicktime.sourceforge.net/
BuildRequires:	openquicktime-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OQTEncoder is simple encoder that uses OpenQuicktime library.

%description -l pl
OQTEncoder jest prostym koderem korzystaj±cym z biblioteki
OpenQuicktime.

%prep
%setup -q -n OQTEncoder-%{version}

%build
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install oqtencoder $RPM_BUILD_ROOT%{_bindir}

gzip -9nf readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.gz
%attr(755,root,root) %{_bindir}/*
