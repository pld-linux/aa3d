# $Revision: 1.9 $Date: 2003-05-26 16:24:19 $
Summary:	ASCII-Art stereogram generator
Summary(pl):	Generator stereogramów w postaci ASCII Art
Name:		aa3d
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/aa-project/%{name}-%{version}.tar.gz
# Source0-md5:	fa0d1547b68b75d83ca3fe37d625584e
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
