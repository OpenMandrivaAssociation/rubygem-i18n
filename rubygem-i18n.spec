# Generated from i18n-0.6.0.gem by gem2rpm5 0.6.6 -*- rpm-spec -*-
%define	rbname	i18n

Summary:	New wave Internationalization support for Ruby
Name:		rubygem-%{rbname}

Version:	0.6.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/svenfuchs/i18n
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems >= 1.3.5
BuildArch:	noarch

%description
New wave Internationalization support for Ruby.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/backend
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/backend/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/core_ext
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/core_ext/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/core_ext/kernel
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/core_ext/kernel/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/core_ext/string
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/core_ext/string/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/gettext
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/gettext/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/interpolate
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/interpolate/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/locale
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/locale/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/locale/tag
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/locale/tag/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/tests
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/tests/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/tests/localization
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/i18n/tests/localization/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
