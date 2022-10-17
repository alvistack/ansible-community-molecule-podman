# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-molecule-podman
Epoch: 100
Version: 2.0.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Molecule Podman plugin
License: BSD-3-Clause
URL: https://github.com/ansible-community/molecule-podman/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Molecule Podman Plugin is designed to allow use podman containers for
provisioning test resources.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-molecule-podman
Summary: Molecule Podman plugin
Requires: python3
Requires: python3-ansible-compat >= 2.2.0
Requires: python3-molecule >= 4.0.0
Requires: python3-podman
Provides: python3-molecule-podman = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule-podman) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule-podman = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule-podman) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule-podman = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule-podman) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-molecule-podman
Molecule Podman Plugin is designed to allow use podman containers for
provisioning test resources.

%files -n python%{python3_version_nodots}-molecule-podman
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-molecule-podman
Summary: Molecule Podman plugin
Requires: python3
Requires: python3-ansible-compat >= 2.2.0
Requires: python3-molecule >= 4.0.0
Requires: python3-podman
Provides: python3-molecule-podman = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule-podman) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule-podman = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule-podman) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule-podman = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule-podman) = %{epoch}:%{version}-%{release}

%description -n python3-molecule-podman
Molecule Podman Plugin is designed to allow use podman containers for
provisioning test resources.

%files -n python3-molecule-podman
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
