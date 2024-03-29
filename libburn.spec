%define tbpostfix pl00

Name:           libburn
Version:        0.7.0
Release:        1%{?dist}
Summary:        Library for reading, mastering and writing optical discs

Group:          System Environment/Libraries
License:        GPLv2
URL:            http://libburnia-project.org/
Source0:        http://files.libburnia-project.org/releases/%{name}-%{version}.%{tbpostfix}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:   libtool intltool gettext doxygen graphviz


%description
Libburn is an open-source library for reading, mastering and writing
optical discs. For now this means only CD-R and CD-RW.

The project comprises of several more or less interdependent parts which
together strive to be a usable foundation for application development.
These are libraries, language bindings, and middleware binaries which emulate
classical (and valuable) Linux tools.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n     cdrskin
Summary:        Limited cdrecord compatibility wrapper to ease migration to libburn
Group:          Applications/Multimedia
Requires:       %{name} = %{version}-%{release}

%description -n cdrskin
A limited cdrecord compatibility wrapper which allows to use some libburn 
features from the command line.


%prep
%setup -q


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
doxygen doc/doxygen.conf


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT README
%{_libdir}/%{name}*.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc
%doc doc/html

%files -n cdrskin
%defattr(-,root,root,-)
%{_mandir}/*/*
%{_bindir}/cdrskin


%changelog
* Wed Sep 30 2009 Denis Leroy <denis@poolshark.org> - 0.7.0-1
- Update to upstream 0.7.0
- Fixed binary installation
- Removed rpath

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Denis Leroy <denis@poolshark.org> - 0.6.0-2
- Updating to pl01 tarball from upstream
- Fixed project URL

* Wed Jan 07 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.0-1
- New upstream version

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.8-2
- fix license tag

* Wed Jun 11 2008 Denis Leroy <denis@poolshark.org> - 0.4.8-1
- Update to upstream 0.4.8

* Thu Feb 14 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-2
- Autorebuild for GCC 4.3

* Thu Dec 13 2007 Denis Leroy <denis@poolshark.org> - 0.4.0-1
- Update to 0.4.0

* Wed Oct 10 2007 Jesse Keating <jkeating@redhat.com> - 0.3.8-2
- Rebuild for BuildID

* Fri Aug 10 2007 Denis Leroy <denis@poolshark.org> - 0.3.8-1
- Update to upstream 0.3.8
- Fixed project URL

* Sun Mar 25 2007 Denis Leroy <denis@poolshark.org> - 0.2.6.3-3
- Fixed unowned include directory (#233860)

* Tue Mar 20 2007 Denis Leroy <denis@poolshark.org> - 0.2.6.3-2
- Moved documentation into devel package, #228372
- Updated source URL to new upstream location

* Tue Jan 02 2007 Jesse Keating <jkeating@redhat.com> - 0.2.6.3-1
- Update to 0.2.6.3
- Remove libisofs stuff as it's packaged seperately now.
- Add a manpage for cdrskin

* Sat Oct 21 2006 Jesse Keating <jkeating@redhat.com> - 0.2-2-2
- Point to a real URL in source, now that we have a tarball

* Fri Oct 20 2006 Jesse Keating <jkeating@redhat.com> - 0.2-2-1
- 0.2.2 release

* Tue Sep 12 2006 Jesse Keating <jkeating@redhat.com> - 0.2-5.20060808svn
- Create doxygen docs

* Fri Sep  8 2006 Jesse Keating <jkeating@redhat.com> - 0.2-4.20060808svn
- rebuild with new snapshot

* Sun Aug 27 2006 Jesse Keating <jkeating@redhat.com> - 0.2-3.20060823svn
- don't install dupe headers in -devel packages
- libisofs requires libburn devel for directory ownership

* Sun Aug 27 2006 Jesse Keating <jkeating@redhat.com> - 0.2-2.20060823svn
- Fix cdrskin require
- Fix tabs
- Added doc files

* Wed Aug 23 2006 Jesse Keating <jkeating@redhat.com> - 0.2-1.20060823svn
- Initial package for review
