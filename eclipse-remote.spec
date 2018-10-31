%{?_javapackages_macros:%_javapackages_macros}
# Release has not been tagged, but this commit comprised the release
# See https://bugs.eclipse.org/bugs/show_bug.cgi?id=445422
%global git_tag 137f306ed56470a5be5367b49df5422b2ac83c9a

Name:           eclipse-remote
Version:        1.1.0
Release:        1.4
Group:		Development/Java
Summary:        Eclipse Remote Services plug-in
License:        EPL
URL:            https://www.eclipse.org/ptp/

Source0:        http://git.eclipse.org/c/ptp/org.eclipse.remote.git/snapshot/org.eclipse.remote-%{git_tag}.tar.bz2

BuildArch:      noarch

BuildRequires:    tycho
BuildRequires:    tycho-extras
BuildRequires:    jsch
BuildRequires:    eclipse-pde >= 1:4.3.2
BuildRequires:    eclipse-license

Requires:         jsch
Requires:         eclipse-platform >= 1:4.3.2

%description
Remote Services provides an extensible remote services framework.

%prep
%setup -q -n org.eclipse.remote-%{git_tag}

find -name *.jar -exec rm -rf {} \;
find -name *.class -exec rm -rf {} \;

%build
%mvn_build  -j -- -f releng/org.eclipse.remote.build/pom.xml

%install
%mvn_install

%files -f .mfiles
%doc features/org.eclipse.remote-feature/epl-v10.html

%changelog
* Tue Sep 30 2014 Mat Booth <mat.booth@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Thu Sep 25 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-3
- Rebuild to regenerate auto requires

* Fri Sep 12 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-2
- Build/install with xmvn

* Fri Jun 27 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-1
- Update to upstream released version
- Add BR on eclipse-license

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.5.git19f4d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.4.git19f4d9
- Drop requirement on jpackage-utils

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.3.git19f4d9
- Update to latest upstream.

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.2.gite09793
- Don't include the cdt feature.

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.1.gite09793
- Initial package.
