%if 0%{?fedora}
%global with_python3 1
%endif

%define srcname notario

Name:           python-notario
Version:        0.0.8
Release:        1%{?dist}
Summary:        A dictionary validator
License:        MIT
URL:            http://github.com/alfredodeza/notario
Source0:        http://pypi.python.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

Patch0001: 0001-create-a-utility-to-extract-proper-assert-messages.patch
Patch0002: 0002-use-the-new-utility-to-fix-broken-tests.patch

Source1:        https://raw.githubusercontent.com/alfredodeza/notario/master/LICENSE
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  pytest
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%endif # with_python3

%description
Notario is flexible and succinct Python dictionary validator with the ability
to validate against both keys and values. Schemas are smaller and readable
representations of data being validated.

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Notario is flexible and succinct Python dictionary validator with the ability
to validate against both keys and values. Schemas are smaller and readable
representations of data being validated.

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3

%description -n python3-%{srcname}
Notario is flexible and succinct Python dictionary validator with the ability
to validate against both keys and values. Schemas are smaller and readable
representations of data being validated.
%endif # with_python3

%prep
%autosetup -p1 -n %{srcname}-%{version}

cp -a %{SOURCE1} .

%build
%{py2_build}

%if 0%{?with_python3}
%{py3_build}
%endif # with_python3

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif # with_python3

%check
py.test-%{python2_version} -v notario/tests

%if 0%{?with_python3}
py.test-%{python3_version} -v notario/tests
%endif # with_python3

%files -n python2-%{srcname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
%endif # with_python3

%changelog
* Fri Feb 05 2016 Ken Dreyer <kdreyer@redhat.com> 0.0.8-1
- Initial package
