# Created by pyp2rpm-3.3.2
%global pypi_name jasypt4py

Name:           python-%{pypi_name}
Version:        0.0.3
Release:        1%{?dist}
Summary:        Cipher functions that produce Jasypt/Bouncycastle compatible password encryption

License:        Apache License 2.0
URL:            https://github.com/fareliner/jasypt4py
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2-crypto
BuildRequires:  python2-nose
BuildRequires:  python2-setuptools
 
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-crypto
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
UNKNOWN

%package -n     python2-%{pypi_name}
Summary:        Cipher functions that produce Jasypt/Bouncycastle compatible password encryption
 
Requires:       python2-crypto
%description -n python2-%{pypi_name}
UNKNOWN

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Cipher functions that produce Jasypt/Bouncycastle compatible password encryption
 
Requires:       python%{python3_pkgversion}-crypto
%description -n python%{python3_pkgversion}-%{pypi_name}
UNKNOWN


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build
%{__python3} setup.py build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%{__python3} setup.py install --skip-build --root %{buildroot}
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%doc README.md
%{python2_sitelib}/jasypt4py/encryptor.py*
%{python2_sitelib}/jasypt4py/exceptions.py*
%{python2_sitelib}/jasypt4py/generator.py*
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%dir %{python3_sitelib}/jasypt4py/__pycache__/
%{python3_sitelib}/jasypt4py/__pycache__/*
%{python3_sitelib}/jasypt4py/encryptor.py
%dir %{python3_sitelib}/jasypt4py/__pycache__/
%{python3_sitelib}/jasypt4py/__pycache__/*
%{python3_sitelib}/jasypt4py/exceptions.py
%dir %{python3_sitelib}/jasypt4py/__pycache__/
%{python3_sitelib}/jasypt4py/__pycache__/*
%{python3_sitelib}/jasypt4py/generator.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Jul 22 2019 mockbuilder - 0.0.3-1
- Initial package.
