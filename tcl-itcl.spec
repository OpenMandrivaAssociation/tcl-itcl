%define oname   itcl

Summary:        Object oriented extensions to Tcl and Tk
Name:           tcl-%{oname}
Version:        4.3.2
Release:        1
License:        TCL
Group:          System/Libraries
URL:            https://core.tcl-lang.org/itcl/home
Source0:        https://downloads.sourceforge.net/tcl/%{oname}%{version}.tar.gz
#Source0:        https://downloads.sourceforge.net/incrtcl/itcl%{version}.tar.gz
Patch1:         %{name}-libdir.patch
Patch2:         %{name}-soname.patch

BuildRequires:  tcl-devel

Requires:       tcl(abi) = %{tcl_version}

%rename	%{oname}
%rename	%{oname}ib

%description
[incr Tcl] is Tcl extension that provides object-oriented features that are
missing from the Tcl language.

%files
%dir %{tcl_sitearch}/%{oname}%{version}
%{tcl_sitearch}/%{oname}%{version}/*.tcl
%{tcl_sitearch}/%{oname}%{version}/*.so
%{_mandir}/mann/*.n*
%license license.terms
%doc README releasenotes.txt

#--------------------------------------------------------------------

%package devel
Summary:  Development headers and libraries for linking against itcl
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers and libraries for linking against itcl.

%files devel
%{_includedir}/*.h
%{tcl_sitearch}/%{oname}%{version}/*.a
%{tcl_sitearch}/%{oname}%{version}/itclConfig.sh

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}%{version}

%build
%configure
%make_build

%install
%make_install

# Patch the updated location of the stub library
#sed -i -e "s#%{_libdir}/%{oname}%{version}#%{tcl_sitearch}/%{oname}%{version}#" \
#        $RPM_BUILD_ROOT%{_libdir}/itclConfig.sh

%check
make test

