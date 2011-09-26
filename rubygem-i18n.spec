%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname i18n
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

%define enable_check 0

Summary:	New wave Internationalization support for Ruby
Name:		rubygem-%{gemname}
Version:	0.5.0
Release:	%mkrel 1
Group:		Development/Ruby
License:	MIT and (GPLv2 or Ruby)
URL:		http://github.com/svenfuchs/i18n
Source0:	http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires:	rubygems
Requires:	ruby(abi) = 1.8
BuildRequires:	ruby(abi) = 1.8
BuildRequires:	rubygems
BuildRequires:	ruby-rdoc
%if %{enable_check} > 0
BuildRequires:	rubygem(mocha)
# test_declarative is not available in Fedora yet.
BuildRequires:	rubygem(test_declarative)
%endif
BuildArch:	noarch
Provides:	rubygem(%{gemname}) = %{version}

%description
Ruby Internationalization and localization solution.


%package doc
Summary: Documentation for %{name}
Group:		Development/Ruby
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force --rdoc %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/
chmod -x %{buildroot}%{geminstdir}/MIT-LICENSE
chmod -x %{buildroot}%{geminstdir}/lib/i18n.rb

%if %{enable_check} > 0
%check
pushd .%{geminstdir}

# Bundler just complicates everything in our case, remove it.
sed -i -e "s|require 'bundler/setup'||" test/test_helper.rb

RUBYOPT="rubygems I%{buildroot}%{geminstdir}/lib" testrb test/all.rb

popd
%endif

%files
%defattr(-, root, root, -)
%dir %{geminstdir}
%{geminstdir}/lib
%doc %{geminstdir}/README.textile
%doc %{geminstdir}/MIT-LICENSE
%doc %{geminstdir}/CHANGELOG.textile
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-, root, root, -)
%{geminstdir}/ci
%{geminstdir}/test
%doc %{gemdir}/doc/%{gemname}-%{version}
