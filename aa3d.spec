# $Revision: 1.7 $Date: 2003-05-06 11:30:20 $
Summary:	ASCII-Art stereogram generator
Summary(pl):	Generator stereogramów w postaci ASCII Art
Name:		aa3d
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/aa-project/%{name}-%{version}.tar.gz
URL:		http://aa-project.sourceforge.net/aa3d/
BuildRequires:	XFree86-devel
BuildRequires:	aalib-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.2
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README logo pyramid 
%attr(755,root,root) %{_bindir}/*
