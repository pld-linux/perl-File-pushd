#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	File
%define	pnam	pushd
Summary:	File::pushd - change directory temporarily for a limited scope
Summary(pl.UTF-8):	File::pushd - tymczasowa zmiana katalogu dla ograniczonego kontekstu
Name:		perl-File-pushd
Version:	1.016
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1480e0d4813a8990c003e78338f00955
URL:		http://search.cpan.org/dist/File-pushd/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::pushd does a temporary chdir that is easily and automatically
reverted, similar to pushd in some Unix command shells.

%description -l pl.UTF-8
File::pushd dokonuje tymczasowej zmiany katalogu, którą można łatwo
cofnąć - podobnie, jak polecenie pushd w niektórych powłokach
uniksowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Todo
%{perl_vendorlib}/File/pushd.pm
%{_mandir}/man3/File::pushd.3pm*
%{_examplesdir}/%{name}-%{version}
