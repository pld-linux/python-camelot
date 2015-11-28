%define 	module	camelot
Summary:	A python GUI framework on top of  Sqlalchemy  and PyQt
Summary(pl.UTF-8):	Szkielet graficznego interfejsu użytkownika na bazie Sqlalchemy i PyQt
Name:		python-%{module}
Version:	09.07.17
Release:	3
License:	GPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/C/Camelot/Camelot-%{version}.tar.gz
# Source0-md5:	4452cc2e4536e283117a153a907979dc
URL:		http://www.conceptive.be/projects/camelot/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-SQLAlchemy >= 0.4
Requires:	python-elixir >= 0.6
Conflicts:	python-SQLAlchemy >= 0.5
Conflicts:	python-elixir >= 0.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A python GUI framework on top of Sqlalchemy and PyQt, inspired by the
Django admin interface.

%description -l pl.UTF-8
Szkielet graficznego interfejsu użytkownika na bazie Sqlalchemy,
elixir i PyQt, zainspirowany interfejsem administracyjnym Django.

%prep
%setup -q -n Camelot-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%doc example
%{py_sitescriptdir}/%{module}
# %{py_sitedir}/*.py[co]
# %{py_sitescriptdir}/%{module}
# %attr(755,root,root) %{py_sitedir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Camelot-*.egg-info
%endif
%attr(755,root,root) %{_bindir}/*
