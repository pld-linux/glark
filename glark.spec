Summary:	Text search application
Summary(pl):	Aplikacja do przeszukiwania tekstu
Name:		glark
Version:	1.7.10
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/glark/%{name}-%{version}.tar.gz
# Source0-md5:	d8093215231b2ed3801675bed36fc580
URL:		http://glark.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Similar to grep, glark performs searching of text files, using
Perl/Ruby regular expressions, highlighting of matches, context around
matches, complex expressions (``and'' and ``or''), and automatic
exclusion of non-text files.

%description -l pl
glark, podobnie do grepa, przeszukuje pliki tekstowe przy u¿yciu
wyra¿eñ regularnych Perla/Ruby'ego, pod¶wietlaj±c dopasowania,
obs³uguj±c kontekst w otoczeniu dopasowania, z³o¿one wyra¿enia ("i"
oraz "lub"), a tak¿e automatycznie wykluczaj±c pliki nietekstowe.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glark
%{_mandir}/man1/glark.1*
%{_datadir}/%{name}
