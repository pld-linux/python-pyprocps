%define	module	pyprocps

Summary:	Python module for gathering process information from /proc on Linux systems
Summary(pl.UTF-8):	Moduł Pythona do zbierania informacji o procesach z linuksowego katalogu /proc
Name:		python-%{module}
Version:	0.4
Release:	4
License:	PSF
Group:		Libraries/Python
Source0:	http://eli.criffield.net/pyprocps/pyprocps-%{version}.tar.gz
# Source0-md5:	be7b45655285875bf782fff3e948040e
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
URL:		http://eli.criffield.net/pyprocps/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses the information in /proc on Linux systems and
presents it.

%description -l pl.UTF-8
Ten moduł analizuje i obrazuje informacje z katalogu /proc w systemach
linuksowych.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.egg-info
