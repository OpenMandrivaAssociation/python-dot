%define modname dot
%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

Name:		python-%{modname}
Version:	0.9.10
Release:	%mkrel 7
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





%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9.10-7mdv2010.0
+ Revision: 442099
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.9.10-6mdv2009.0
+ Revision: 259581
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9.10-5mdv2009.0
+ Revision: 247406
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.9.10-3mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 23 2007 Jérôme Soyer <saispo@mandriva.org> 0.9.10-3mdv2007.0
+ Revision: 125235
- Add BR
- Rebuild for python 2.5
- Rebuild for latest python

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - import python-dot-0.9.10-1mdv2007.0

* Sun May 28 2006 Jerome Soyer <saispo@mandriva.org> 0.9.10-1mdv2007.0
- First mandriva package

