%define name	tilitin
%define version	0.6.8
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Free Finnish bookkeeping software
Group:		Office
License:	GPLv3+
URL:		http://helineva.net/tilitin/
Source:		http://helineva.net/tilitin/%{name}-%{version}-src.zip
Source1:	%{name}
Source2:	%{name}.desktop
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	locales
BuildRequires:	ant
BuildRequires:	crimson
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
