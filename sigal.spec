Name:           sigal
Version:        2.3
Release:        2%{?dist}
Summary:        Static gallery generator
License:        MIT
Url:            https://github.com/saimn/sigal
Source:         https://files.pythonhosted.org/packages/source/s/%{name}/%{name}-%{version}.tar.gz
Patch0:         sigal-2.3-no-mp4.patch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# test requirements
BuildRequires:  python3-jinja2
BuildRequires:  python3-markdown
BuildRequires:  python3-pillow
BuildRequires:  python3-blinker
BuildRequires:  python3-click
BuildRequires:  python3-pilkit
BuildRequires:  python3-pytest
BuildRequires:  python3-natsort
BuildRequires:  python3-feedgenerator
BuildRequires:  python3-brotli
BuildRequires:  python3-cryptography
# satisfied by ffmpeg-free from Fedora or by ffmpeg from RPMFusion
BuildRequires:  /usr/bin/ffmpeg
Requires:       /usr/bin/ffmpeg
Suggests:       python-boto
Suggests:       python-cssmin
BuildArch:      noarch

%description
Sigal is a static gallery generator written in Python with the following
features:

* Generates HTML pages using jinja2 templates.
* Emits relative links for a portable output.
* Supports themes, videos, EXIF tags, and ZIP downloading.
* Processes directories recursively and files in parallel.

The idea behind Sigal is to ease the use of the JavaScript libraries like
galleria_. These libraries display the images, Sigal on the other hand does
image resizing, thumbnail creation and HTML page generation.

%prep
%autosetup -p1

%build
%{py3_build}


%install
%{py3_install}

%check
%pytest tests -k "not (test_build)"


%files
%license LICENSE
%doc AUTHORS README.rst
%{_bindir}/%{name}
%{python3_sitelib}/*

%changelog
* Mon Jun 20 2022 Dan Horák <dan[at]danny.cz> - 2.3-2
- allow using ffmpeg-free

* Wed Jun 15 2022 Dan Horák <dan[at]danny.cz> - 2.3-1
- updated to 2.3

* Sat Aug 28 2021 Dan Horák <dan[at]danny.cz> - 2.2-1
- updated to 2.2

* Thu Aug 20 2020 Dan Horák <dan[at]danny.cz> - 2.1.1-1
- updated to 2.1.1

* Thu Jul 16 2020 Dan Horák <dan[at]danny.cz> - 2.1-1
- updated to 2.1

* Sun May 10 2020 Dan Horák <dan[at]danny.cz> - 2.0-1
- initial Fedora version
