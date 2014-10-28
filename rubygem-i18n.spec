# Generated from i18n-0.6.0.gem by gem2rpm5 0.6.6 -*- rpm-spec -*-
%define	rbname	i18n

Summary:	New wave Internationalization support for Ruby
Name:		rubygem-%{rbname}

Version:	0.6.9
Release:	4
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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/backend
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/backend/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/core_ext
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/core_ext/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/core_ext/kernel
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/core_ext/kernel/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/core_ext/string
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/core_ext/string/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/gettext
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/gettext/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/interpolate
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/interpolate/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/locale
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/locale/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/locale/tag
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/locale/tag/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/tests
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/tests/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/tests/localization
%{gem_dir}/gems/%{rbname}-%{version}/lib/i18n/tests/localization/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{gem_dir}/doc/%{rbname}-%{version}

