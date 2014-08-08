%define dialogsubversion 20140219

Summary:	    A utility for creating interactive TTY boxes from shell script
Name:		    dialog
Version:	    1.2
Release:	    0
License:	    LGPL-2.1
Group:		    Base/Utilities
URL:		    http://invisible-island.net/dialog/dialog.html
Source:		    ftp://invisible-island.net/dialog/%{name}-%{version}-%{dialogsubversion}.tgz
Source1001:	    %{name}.manifest
BuildRequires:	    findutils
BuildRequires:	    gettext
BuildRequires:	    libtool
BuildRequires:	    ncurses-devel
Requires(post):	    /sbin/ldconfig
Requires(postun):   /sbin/ldconfig


%description
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces.  Dialog is called
from within a shell script.  The following dialog boxes are implemented:
yes/no, menu, input, message, text, info, checklist, radiolist, and
gauge.

Install dialog if you would like to create TTY dialog boxes.

%package devel
Summary:	    Development files for building applications with the dialog library
Group:		    Development/Libraries
Requires:	    %{name}-%{version} = %{version}
Requires:	    ncurses-devel
Requires(post):	    /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description devel
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces. This package
contains the files needed for developing applications, which use the
dialog library.


%prep
%setup -q -n %{name}-%{version}-%{dialogsubversion}
cp %{SOURCE1001} .

%build
%configure \
	--includedir=%{_includedir}/dialog \
	--enable-included-msgs \
	--enable-nls \
	--enable-widec \
	--with-libtool \
	--with-ncurses \
	--with-ncursesw
make %{?_smp_mflags}


%install
%make_install
rm -rf %{buildroot}%{_mandir}

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig

%lang_package

%files -f %{name}.lang
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/dialog
%{_libdir}/libdialog.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/dialog-config
%{_includedir}/dialog
%{_libdir}/libdialog.so
