Summary:	Simple encoder that uses OpenQuicktime library
Summary(pl.UTF-8):	Prosty koder korzystający z biblioteki OpenQuicktime
Name:		oqtencoder
Version:	0.1
Release:	1
License:	LGPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/openquicktime/%{name}-%{version}.tgz
# Source0-md5:	9e4e3c5eb87e106144dff52dcb6c8ccd
URL:		http://openquicktime.sourceforge.net/
BuildRequires:	openquicktime-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OQTEncoder is simple encoder that uses OpenQuicktime library.

%description -l pl.UTF-8
OQTEncoder jest prostym koderem korzystającym z biblioteki
OpenQuicktime.

%prep
%setup -q -n OQTEncoder-%{version}

%build
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install oqtencoder $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme
%attr(755,root,root) %{_bindir}/*
