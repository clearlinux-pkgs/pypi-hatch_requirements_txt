#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-hatch_requirements_txt
Version  : 0.4.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/03/a9/478750388ddf54be886abb7cdb032e3b5a23c8886a8b1953fb66cd98c908/hatch_requirements_txt-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/03/a9/478750388ddf54be886abb7cdb032e3b5a23c8886a8b1953fb66cd98c908/hatch_requirements_txt-0.4.0.tar.gz
Summary  : Hatchling plugin to read project dependencies from requirements.txt
Group    : Development/Tools
License  : MIT
Requires: pypi-hatch_requirements_txt-license = %{version}-%{release}
Requires: pypi-hatch_requirements_txt-python = %{version}-%{release}
Requires: pypi-hatch_requirements_txt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
BuildRequires : pypi(packaging)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=======================
hatch-requirements-txt
=======================
.. start short_desc

%package license
Summary: license components for the pypi-hatch_requirements_txt package.
Group: Default

%description license
license components for the pypi-hatch_requirements_txt package.


%package python
Summary: python components for the pypi-hatch_requirements_txt package.
Group: Default
Requires: pypi-hatch_requirements_txt-python3 = %{version}-%{release}

%description python
python components for the pypi-hatch_requirements_txt package.


%package python3
Summary: python3 components for the pypi-hatch_requirements_txt package.
Group: Default
Requires: python3-core
Provides: pypi(hatch_requirements_txt)
Requires: pypi(hatchling)
Requires: pypi(packaging)

%description python3
python3 components for the pypi-hatch_requirements_txt package.


%prep
%setup -q -n hatch_requirements_txt-0.4.0
cd %{_builddir}/hatch_requirements_txt-0.4.0
pushd ..
cp -a hatch_requirements_txt-0.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678749371
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-hatch_requirements_txt
cp %{_builddir}/hatch_requirements_txt-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-hatch_requirements_txt/1d9dba11f7812c15429ba2e119b272157c291bfb || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-hatch_requirements_txt/1d9dba11f7812c15429ba2e119b272157c291bfb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
