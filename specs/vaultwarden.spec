Name:           vaultwarden
Version:        codetiger_version
Release:        1%{?dist}
Summary:        vaultwarden编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/czyt/vaultwarden-binary/releases/download/codetiger_version-extracted/vaultwarden
Source1:        vaultwarden.sh
Source2:        .env
Source3:        vaultwarden.service

%description


# 安装
%install
%{__mkdir} -p %{buildroot}/usr/local/vaultwarden
%{__install} -p -D -m 0755 %{SOURCE0} %{buildroot}%{_usr}/local/vaultwarden/vaultwarden
%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}%{_usr}/local/vaultwarden/vaultwarden.sh
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_usr}/local/vaultwarden/.env
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}%{_usr}/lib/systemd/system/vaultwarden.service

# 安装后操作
%post
if [ $1 == 1 ]; then
    useradd -u 3000 -o vaultwarden 2>/dev/null
    chown -R vaultwarden:3000 /usr/local/vaultwarden
fi

# 卸载前准备
%preun
if [ $1 == 0 ]; then
    %if 0%{?use_systemd}
        if [ -f /usr/lib/systemd/system/vaultwarden.service ]; then
        %systemd_preun vaultwarden.service
        fi
    %endif
fi

# 文件列表
%files
%{_usr}/local/vaultwarden/vaultwarden
%{_usr}/local/vaultwarden/vaultwarden.sh
%{_usr}/lib/systemd/system/vaultwarden.service
%config
%{_usr}/local/vaultwarden/.env
%doc

%changelog