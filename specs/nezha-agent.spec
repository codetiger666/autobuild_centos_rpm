Name:           nezha_agent
Version:        codetiger_version
Release:        1%{?dist}
Summary:        哪吒监控agent编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/nezhahq/agent/releases/download/v%{version}/nezha-agent_linux_amd64.zip
Source1:        nezha-agent.service
Source2:        nezha-agent.sh
Source3:        agent.conf

%description


%prep
rm -rf %{_builddir}/*
cp %{SOURCE0} %{_builddir}
unzip -d %{name}-%{version} %{SOURCE0}

%pre
if [ $1 == 1 ]; then
    id 3000 &> /dev/null
    if [ $? -ne 0 ]
    then
    groupadd -g 3000 onedrive 2> /dev/null
    useradd -u 3000 -g onedrive onedrive -s /sbin/nologin 2> /dev/null
    fi
fi

%install
%{__mkdir} -p %{buildroot}/usr/local/nezha
cp %{name}-%{version}/nezha-agent %{buildroot}/usr/local/nezha/nezha-agent
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_usr}/lib/systemd/system/nezha-agent.service
%{__install} -p -D -m 0755 %{SOURCE2} %{buildroot}/usr/local/nezha/nezha-agent.sh

# 安装后操作
%post
if [ $1 == 1 ]; then
    chown -R 3000:3000 /usr/local/nezha
fi

%files
%{_usr}/local/nezha/nezha-agent
%{_usr}/local/nezha/nezha-agent.sh
%{_usr}/lib/systemd/system/nezha-agent.service
%config(noreplace) %{_usr}/local/nezha/agent.conf
%doc

%changelog
