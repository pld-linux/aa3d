# $Revision: 1.2.2.1 $Date: 2003-07-11 12:00:19 $
Summary:	ASCII-Art stereogram generator
Summary(pl):	Generator stereogramów w postaci ASCII Art
Name:		aa3d
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	ftp://download.sourceforge.net/pub/sourceforge/aa-project/%{name}-%{version}.tar.gz
URL:		http://aa-project.sourceforge.net/aa3d/
BuildRequires:	aalib-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	XFree86-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ASCII-Art stereogram generator.

%description -l pl
Generator stereogramów w ASCII Art.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install aa3d $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README logo pyramid

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
