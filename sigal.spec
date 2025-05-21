Name:           sigal
Version:        2.5
Release:        2%{?dist}
Summary:        Static gallery generator
License:        MIT
Url:            https://github.com/saimn/sigal
Source:         https://files.pythonhosted.org/packages/source/s/%{name}/%{name}-%{version}.tar.gz
Patch1:         sigal-2.4-no-mp4.patch
Patch2:         sigal-2.5-no-heic.patch
BuildRequires:  git-core
BuildRequires:  python3-devel
# satisfied by ffmpeg-free from Fedora or by ffmpeg from RPMFusion
BuildRequires:  /usr/bin/ffmpeg
Requires:       /usr/bin/ffmpeg
Suggests:       python3-boto
Suggests:       python3-cssmin

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
%autosetup -S git

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{name}

%check
%tox


%files
%license LICENSE
%doc AUTHORS README.rst
%{_bindir}/%{name}
%{python3_sitelib}/*


%changelog
* Wed May 21 2025 Dan Horák <dan[at]danny.cz> - 2.5-2
- skip HEIC related tests

* Sat Mar 15 2025 Dan Horák <dan[at]danny.cz> - 2.5-1
- updated to 2.5

* Fri Nov 03 2023 Dan Horák <dan[at]danny.cz> - 2.4-1
- updated to 2.4

* Fri Jun 30 2023 Dan Horák <dan[at]danny.cz> - 2.3-4
- fix tests with newer ffmpeg

* Fri Jun 30 2023 Dan Horák <dan[at]danny.cz> - 2.3-3
- rebuild

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
