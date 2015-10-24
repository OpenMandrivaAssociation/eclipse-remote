%{?_javapackages_macros:%_javapackages_macros}
%global eclipse_dropin %{_datadir}/eclipse/dropins
%global git_tag 19f4d9867863f5a60b379d737c8ce409f151a600

Name:           eclipse-remote
Version:        1.0.0
Release:        0.4.git19f4d9%{?dist}
Summary:        Eclipse Remote Services plug-in
License:        EPL
URL:            https://www.eclipse.org/ptp/

Source0:        http://git.eclipse.org/c/ptp/org.eclipse.remote.git/snapshot/org.eclipse.remote-%{git_tag}.tar.bz2

BuildArch:      noarch

BuildRequires:    maven-local
BuildRequires:    tycho
BuildRequires:    tycho-extras
BuildRequires:    feclipse-maven-plugin
BuildRequires:    jsch
BuildRequires:    eclipse-pde >= 1:4.3.1
BuildRequires:    java-1.7.0-openjdk-devel
BuildConflicts:	  java-1.8.0-openjdk-devel

Requires:         jsch
Requires:         eclipse-platform >= 1:4.3.1

%description
Remote Services provides an extensible remote services framework.

%prep
%setup -q -n org.eclipse.remote-%{git_tag}

find -name *.jar -exec rm -rf {} \;
find -name *.class -exec rm -rf {} \;

%build
xmvn -o clean verify -f releng/org.eclipse.remote.build/pom.xml

%install
xmvn -o org.fedoraproject:feclipse-maven-plugin:install \
  -Dfeatures=org.eclipse.remote \
  -DsourceRepo=releng/org.eclipse.remote.repo/target/repository \
  -DtargetLocation=%{buildroot}%{eclipse_dropin}/remote/eclipse

%files
%doc features/org.eclipse.remote-feature/*.html
%{eclipse_dropin}/remote

%changelog
* Wed May 07 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.4.git19f4d9
- Drop requirement on jpackage-utils

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.3.git19f4d9
- Update to latest upstream.

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.2.gite09793
- Don't include the cdt feature.

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.1.gite09793
- Initial package.

