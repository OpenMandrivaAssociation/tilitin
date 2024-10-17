%define name	tilitin
%define version	0.14.0
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Free Finnish bookkeeping software
Group:		Office
License:	GPLv3+
URL:		https://helineva.net/tilitin/
Source:		http://helineva.net/tilitin/%{name}-%{version}-src.zip
Source1:	%{name}
Source2:	%{name}.desktop
BuildRequires:	locales
BuildRequires:	ant
#BuildRequires:	crimson
BuildRequires:	java-rpmbuild
Requires:	java >= 1.6.0
Requires:	javasqlite
BuildArch:	noarch

%description
Tilitin is a free Finnish bookkeeping software for Windows and Linux.

%prep
%setup -q

%build 
LC_ALL=UTF-8 %ant

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}/tilikarttamallit
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
install -D -m 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 644 dist/tilitin.jar %{buildroot}%{_datadir}/%{name}/
install -D -m 644 lib/* %{buildroot}%{_datadir}/%{name}/
install -D -m 644 tilikarttamallit/* %{buildroot}%{_datadir}/%{name}/tilikarttamallit/

# Install hicolor icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{24x24,32x32,48x48}/apps
install -D -m 644 src/kirjanpito/ui/resources/tilitin-24x24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
install -D -m 644 src/kirjanpito/ui/resources/tilitin-32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m 644 src/kirjanpito/ui/resources/tilitin-48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsbasedir}/*/apps/%{name}.png


%changelog
* Tue Apr 05 2011 Jani Välimaa <wally@mandriva.org> 0.14.0-1mdv2011.0
+ Revision: 650722
- new version 0.14.0
- drop buildroot definition

* Tue Mar 22 2011 Jani Välimaa <wally@mandriva.org> 0.13.0-1
+ Revision: 647665
- new version 0.13.0

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.12.0-2
+ Revision: 640487
- rebuild to obsolete old packages

* Wed Feb 16 2011 Jani Välimaa <wally@mandriva.org> 0.12.0-1
+ Revision: 638063
- new version 0.12.0
- build without crimson

* Tue Feb 08 2011 Jani Välimaa <wally@mandriva.org> 0.11.3-1
+ Revision: 636931
- new version 0.11.3

* Tue Jan 25 2011 Jani Välimaa <wally@mandriva.org> 0.11.0-1
+ Revision: 632543
- new version 0.11.0

* Wed Jan 19 2011 Jani Välimaa <wally@mandriva.org> 0.10.1-1
+ Revision: 631672
- new version 0.10.1

* Wed Dec 29 2010 Jani Välimaa <wally@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 625974
- new version 0.10.0

* Tue Dec 21 2010 Jani Välimaa <wally@mandriva.org> 0.9.0-1mdv2011.0
+ Revision: 623609
- new version 0.9.0
- fix desktop file

* Mon Nov 29 2010 Jani Välimaa <wally@mandriva.org> 0.8.10-1mdv2011.0
+ Revision: 603127
- new version 0.8.10

* Tue Nov 16 2010 Jani Välimaa <wally@mandriva.org> 0.8.9-1mdv2011.0
+ Revision: 598117
- new version 0.8.9

* Wed Oct 27 2010 Jani Välimaa <wally@mandriva.org> 0.8.8-1mdv2011.0
+ Revision: 589613
- new version 0.8.8

* Tue Oct 26 2010 Jani Välimaa <wally@mandriva.org> 0.8.7-1mdv2011.0
+ Revision: 589457
- new version 0.8.7

* Mon Oct 04 2010 Jani Välimaa <wally@mandriva.org> 0.8.6-1mdv2011.0
+ Revision: 582931
- new version 0.8.6

* Sun Oct 03 2010 Jani Välimaa <wally@mandriva.org> 0.8.5-1mdv2011.0
+ Revision: 582643
- new version 0.8.5

* Tue Aug 31 2010 Jani Välimaa <wally@mandriva.org> 0.8.4-1mdv2011.0
+ Revision: 574701
- new version 0.8.4

* Thu Aug 19 2010 Jani Välimaa <wally@mandriva.org> 0.8.3-1mdv2011.0
+ Revision: 571326
- new version 0.8.3

* Wed Aug 04 2010 Jani Välimaa <wally@mandriva.org> 0.8.2-1mdv2011.0
+ Revision: 565870
- new versio 0.8.2

* Fri Jul 23 2010 Jani Välimaa <wally@mandriva.org> 0.8.1-1mdv2011.0
+ Revision: 557288
- new version 0.8.1

* Sat Jul 10 2010 Jani Välimaa <wally@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 550016
- new version 0.8.0
- fix desktop file (again)

* Sun May 02 2010 Jani Välimaa <wally@mandriva.org> 0.6.8-2mdv2010.1
+ Revision: 541645
- fix desktop file

* Tue Apr 13 2010 Jani Välimaa <wally@mandriva.org> 0.6.8-1mdv2010.1
+ Revision: 534596
- new version 0.6.8

* Thu Apr 08 2010 Jani Välimaa <wally@mandriva.org> 0.6.7-1mdv2010.1
+ Revision: 532881
- new version 0.6.7
- fix .desktop file

* Thu Mar 18 2010 Jani Välimaa <wally@mandriva.org> 0.6.6-1mdv2010.1
+ Revision: 524936
- new version 0.6.6

* Wed Mar 10 2010 Jani Välimaa <wally@mandriva.org> 0.6.5-1mdv2010.1
+ Revision: 517358
- new version 0.6.5

* Sat Mar 06 2010 Jani Välimaa <wally@mandriva.org> 0.6.4-1mdv2010.1
+ Revision: 515287
- add missing BR
- modify summary and description
- fix build (use %%ant instead of ant)
- import tilitin


* Wed Feb 24 2010 Jani Välimaa <wally@mandriva-fi.org> 0.6.4-1mdv2010.0
- new version 0.6.4

* Wed Feb 02 2010 Jani Välimaa <wally@mandriva-fi.org> 0.6.3-1mdv2010.0
- new version 0.6.3

* Wed Jan 20 2010 Jani Välimaa <wally@mandriva-fi.org> 0.6.2-1mdv2010.0
- new version 0.6.2

* Sun Jan 10 2010 Jani Välimaa <wally@mandriva-fi.org> 0.6.1-1mdv2010.0
- new version 0.6.1

* Sat Jan 09 2010 Jani Välimaa <wally@mandriva-fi.org> 0.6.0-1mdv2010.0
- new version 0.6.0

* Mon Nov 16 2009 Jani Välimaa <wally@mandriva-fi.org> 0.5.3-1mdv2010.0
- Initial release for Mandriva
