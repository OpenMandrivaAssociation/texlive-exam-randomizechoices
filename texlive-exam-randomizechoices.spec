%global tl_name exam-randomizechoices
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Randomize mc choices using the exam class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exam-randomizechoices
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-randomizechoices.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-randomizechoices.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is an extension to the exam document class. It provides the
user with four new multiple choice typesetting environments which place
their content in a random order. It can (only) be used in combination
with the exam class. It can only randomize the placement of choices in
multiple choice questions. The questions themselves cannot be randomized
with this package. Furthermore, the package provides a simple answer key
table typesetter and has a command for writing the answer keys to an
external file.

