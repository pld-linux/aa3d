Summary:	ASCII-Art stereogram generator
Summary(pl.UTF-8):   Generator stereogramów w postaci ASCII Art
Name:		aa3d
Version:	1.0
Release:	3
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/aa-project/%{name}-%{version}.tar.gz
# Source0-md5:	fa0d1547b68b75d83ca3fe37d625584e
URL:		http://aa-project.sourceforge.net/aa3d/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ASCII-Art stereogram generator.

%description -l pl.UTF-8
Generator stereogramów w ASCII Art.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

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
