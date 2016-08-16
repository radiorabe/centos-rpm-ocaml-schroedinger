Name:     ocaml-schroedinger

Version:  0.1.1
Release:  1
Summary:  OCaml bindings for schroedinger
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-schroedinger
Source0:  https://github.com/savonet/ocaml-schroedinger/releases/download/%{version}/ocaml-schroedinger-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-bytes
BuildRequires: ocaml-ogg
BuildRequires: schroedinger-devel
BuildRequires: libogg-devel
Requires:      schroedinger
Requires:      libogg

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/schroedinger/META
/usr/lib64/ocaml/schroedinger/schroedinger.a
/usr/lib64/ocaml/schroedinger/schroedinger.cma
/usr/lib64/ocaml/schroedinger/schroedinger.cmi
/usr/lib64/ocaml/schroedinger/schroedinger.cmxa
/usr/lib64/ocaml/schroedinger/schroedinger.mli
/usr/lib64/ocaml/schroedinger/libschroedinger_stubs.a
/usr/lib64/ocaml/stublibs/dllschroedinger_stubs.so
/usr/lib64/ocaml/stublibs/dllschroedinger_stubs.so.owner

%description
OCAML bindings for schroedinger


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-schroedinger.spec
