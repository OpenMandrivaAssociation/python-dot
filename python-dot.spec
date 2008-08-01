%define modname dot
%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

Name:		python-%{modname}
Version:	0.9.10
Release:	%mkrel 6
License:	MIT
Group:		Development/Python
Summary:	Python interface to Graphviz's Dot language
URL:		http://dkbza.org/pydot.html
Source0:	http://dkbza.org/data/py%{modname}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	python-parsing python-devel
BuildRequires:	graphviz, python-parsing
Requires:	graphviz, python-parsing
BuildArch:	noarch
Provides:	py%{modname}

%description
An interface for creating both directed and non directed graphs from Python. 
Currently all attributes implemented in the Dot language are supported (up 
to Graphviz 1.16).

Output can be inlined in Postscript into interactive scientific environments 
like TeXmacs, or output in any of the format's supported by the Graphviz 
tools dot, neato, twopi.

%prep
%setup -q -n py%{modname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE ChangeLog PKG-INFO README
%{python_sitelib}/*



