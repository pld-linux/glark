Summary:	Text search application
Name:		glark
Version:	1.6.5
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Similar to grep, glark performs searching of text files, using
Perl/Ruby regular expressions, highlighting of matches, context around
matches, complex expressions (``and'' and ``or''), and automatic
exclusion of non-text files.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glark
%{_mandir}/man1/glark.1*
