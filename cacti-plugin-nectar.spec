%define		plugin	nectar
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti - Send Graphs and Text to given mail address(es)
Name:		cacti-plugin-%{plugin}
Version:	0.35a
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:%{plugin}-v%{version}.tgz
# Source0-md5:	f9e9e706141ac0965574a1ebab4f3d07
URL:		http://docs.cacti.net/plugin:nectar
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti
Requires:	cacti(pia) >= 2.9
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-gd
Requires:	php-mysql
Requires:	php-pcre
Requires:	php-session
Obsoletes:	cacti-plugin-reports
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
This plugin allows you to email graphs on a given and selectable
interval

Features:
- allow both users and admins to create reports
- include tree's, text, horizontal rules, and graphs into reports
- allows filtering of tree and host content on trees by regular
  expression
- allow basic formmatting
- allow custom css and html to be integrated into the reports
- specify different timespans for graphs
- schedule reports using different scheduling intervals
- basic png2jpeg conversion using php-gd, verified with Linux only

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{plugindir}
