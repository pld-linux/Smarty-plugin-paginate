%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.0.0
Summary:	Smarty plugin for data set pagination
Name:		Smarty-plugin-paginate
Version:	1.6
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/PHP
Source0:	http://www.phpinsider.com/php/code/SmartyPaginate/SmartyPaginate-%{version}.tar.gz
# Source0-md5:	1407027bd2cc319cdb3b8535a498289d
URL:		http://www.phpinsider.com/php/code/SmartyPaginate/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	Smarty
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_smartydir	%{_datadir}/php/Smarty

%description
SmartyPaginate is a data pagination class for the Smarty template
engine.

Often times when you display a large result set on a web page (such as
a database query), you will want to break it up across multiple pages
with "previous" and "next" links that aid in navigating through the
data. SmartyPaginate automates the task of keeping track of the
pagination and displaying pagination navigation links.

%prep
%setup -q -n SmartyPaginate-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_smartydir}/plugins,%{php_data_dir}}
cp -a libs/SmartyPaginate.class.php $RPM_BUILD_ROOT%{php_data_dir}
cp -a plugins/*.php $RPM_BUILD_ROOT%{_smartydir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{php_data_dir}/*.class.php
%{_smartydir}/plugins/*.php
