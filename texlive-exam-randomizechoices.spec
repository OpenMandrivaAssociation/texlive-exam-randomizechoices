Name:		texlive-exam-randomizechoices
Version:	61719
Release:	2
Summary:	Randomize mc choices using the exam class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exam-randomizechoices
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-randomizechoices.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-randomizechoices.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is an extension to the exam document class. It
provides the user with four new multiple choice typesetting
environments which place their content in a random order. It
can (only) be used in combination with the exam class. It can
only randomize the placement of choices in multiple choice
questions. The questions themselves cannot be randomized with
this package. Furthermore, the package provides a simple answer
key table typesetter and has a command for writing the answer
keys to an external file.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/exam-randomizechoices
%doc %{_texmfdistdir}/doc/latex/exam-randomizechoices

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
