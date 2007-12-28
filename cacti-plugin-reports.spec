%define		namesrc	reports
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Reports
Summary(pl.UTF-8):	Wtyczka do Cacti - Reports
Name:		cacti-plugin-reports
Version:	0.3a
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	%{namesrc}-%{version}.zip
# Source0-md5:	ccd09c76b80c2346d86a739ee1cc2794
URL:		http://www.cactiusers.org/forums
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - allows you to send graphs that you specify to users
that you specify at a specified time. A simple wizard guides you
through the whole process. Currently works, but lacks a little polish
and some much needed options.

%description -l pl.UTF-8
Wtyczka do Cacti pozwalająca wysyłać określone wykresy do określonych
użytkowników o określonym czasie. Prosty wizard prowadzi przez cały
proces konfiguracji. Aktualnie działa, ale wymaga jeszcze dopracowania
i dodania kilku najbardziej potrzebnych opcji.

%prep
%setup -q -n %{namesrc}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -a * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README reports.txt
%{webcactipluginroot}
