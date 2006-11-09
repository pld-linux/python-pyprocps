%define	module	pyprocps

Summary:	Python module for gathering process information from /proc on Linux systems
Name:		python-%{module}
Version:	0.2
Release:	1
License:	PSF
Group:		Libraries/Python
Source0:	http://eli.criffield.net/pyprocps/pyprocps-%{version}.tar.gz
# Source0-md5:	834f5954ee4904afbbee3f33cbeea62c
BuildRequires:	python-devel >= 2.2.1
%pyrequires_eq	python
URL:		http://eli.criffield.net/pyprocps/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses the information in /proc on Linux systems and
presents it.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
