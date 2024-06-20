Name:           alist
Version:        codetiger_version
Release:        1%{?dist}
Summary:        alist网盘

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/alist-org/alist/releases/download/alist.tar.gz
Source1:        alist.service
Source2:        alist.sh

%description


%prep
rm -rf %{_builddir}/*
cp %{SOURCE0} %{_builddir}
tar -xf -C %{name}-%{version} %{SOURCE0}

%pre
if [ $1 == 1 ]; then
    id alist &> /dev/null
    if [ $? -ne 0 ]
    then
    useradd alist -s /sbin/nologin 2> /dev/null
    fi
fi

%install
%{__mkdir} -p %{buildroot}/usr/local/alist
cp %{name}-%{version}/alist %{buildroot}/usr/local/nezha/alist
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_usr}/lib/systemd/system/alist.service
%{__install} -p -D -m 0755 %{SOURCE2} %{buildroot}/usr/local/nezha/alist.sh

# 安装后操作
%post
if [ $1 == 1 ]; then
    chown -R alist:alist /usr/local/alist
fi

%files
%{_usr}/local/alist/alist
%{_usr}/local/alist/alist
%{_usr}/lib/systemd/system/alist.service
%doc

%changelog
