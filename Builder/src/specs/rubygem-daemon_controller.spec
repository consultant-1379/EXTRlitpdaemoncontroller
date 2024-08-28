%global realversion 1.1.8
%global rpmversion <rpm.version>
%global packager <ericsson.rstate>
%global realname rubygem-rack

%global gemname daemon_controller

%global gemdir /usr/share/gems
%global geminstdir %{gemdir}/gems/%{gemname}-%{realversion}
%global gemspecdir %{gemdir}/specifications/
%global gemcachedir %{gemdir}/cache/

Summary: Library for robust daemon management
Name: EXTRlitpdaemoncontroller_CXP9031033
Version: %{rpmversion}
Release: 1
Group: Development/Languages
License: MIT
URL: http://www.ericsson.com/
Source0: %{gemname}-%{realversion}.tar.gz
Requires: ruby(runtime_executable) >= 2.0.0
Requires: ruby(runtime_executable) < 2.1.0
Requires: ruby(rubygems)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{realversion}
Provides: rubygem-%{gemname} = %{realversion}
Packager:  %{packager}

%description
Library which implements daemon management capabilities.
repackaged by Ericsson from GitHUB source code.


%prep
%setup -q -c -T
mkdir -p .%{gemdir}

%build

%install
%{__install} -d -m0755 %{buildroot}%{geminstdir}
%{__install} -d -m0755 %{buildroot}%{gemspecdir}
cp -a  %{_builddir}%{gemname}-release-%{realversion}/* %{buildroot}%{geminstdir}
cp -a  %{_builddir}%{gemname}-release-%{realversion}/daemon_controller-1.1.8.gemspec %{buildroot}%{gemspecdir}

%files
%defattr(-,root,root,0755)
%{geminstdir}
%{gemspecdir}
