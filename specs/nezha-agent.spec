Name:           nezha_agent
Version:        codetiger_version
Release:        1%{?dist}
Summary:        哪吒监控agent编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/nezhahq/agent/releases/download/v%{version}/nezha-agent_linux_amd64.zip
Source1:        nezha-agent.service
Source2:        nezha-agent.sh

%description


%prep
rm -rf %{_builddir}/*
cp %{SOURCE0} %{_builddir}
unzip -d %{name}-%{version} %{SOURCE0}

%install
%{__mkdir} -p %{buildroot}/usr/local/nezha
cp %{name}-%{version}/nezha-agent %{buildroot}/usr/local/nezha/nezha-agent
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_usr}/lib/systemd/system/nezha-agent.service
%{__install} -p -D -m 0755 %{SOURCE2} %{buildroot}/usr/local/nezha/nezha-agent.sh

%files
%{_usr}/local/nezha/nezha-agent
%{_usr}/local/nezha/nezha-agent.sh
%{_usr}/lib/systemd/system/nezha-agent.service
%doc

%changelog
