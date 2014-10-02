# based on PLD Linux spec git://git.pld-linux.org/packages/.git
Summary:	A perfect hash function generator
Name:		gperf
Version:	3.0.4
Release:	6
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/gperf/%{name}-%{version}.tar.gz
# Source0-md5:	c1f1db32fb6598d6a93e6e88796a8632
Patch0:		%{name}-no_dvi_html.patch
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gperf is a perfect hash function generator written in C++. Simply
stated, a perfect hash function is a hash function and a data
structure that allows recognition of a key word in a set of words
using exactly one probe into the data structure.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/gperf
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*

