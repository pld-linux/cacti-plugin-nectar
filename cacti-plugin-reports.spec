%define		namesrc	reports
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Reports
Summary(pl):	Wtyczka do Cacti - Reports
Name:		cacti-plugin-reports
Version:	0.1b
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version in name
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	775098a64f02a89569c239d57886d06b
URL:		http://www.cactiusers.org/
#BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - allows you to send graphs that you specify to users
that you specify at a specified time. A simple wizard guides you
through the whole process. Currently works, but lacks a little polish
and some much needed options.

%description -l pl
Wtyczka do Cacti.

%prep
%setup -q -n %{namesrc}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc
%{webcactipluginroot}
