



CONFIG_SECTIONS = [
    # TODO : reconsider 2-tier / 3-tier sections
    "access_control/telnet",
    "access_control/pam",
    "access_control/ssh",
    "access_control/webui",
    "access_control/cli",
    "access_control/security",
    "access_control/security/attempts",
    "apn_database/config",
    "attack_prevention/http",
    "attack_prevention/https",
    "attack_prevention/port_scan",
    "attack_prevention/icmp",
    "attack_prevention/ssh",
    "attack_prevention/syn_flood",
    "auto_reboot/scheduler",
    "auto_reboot/ping_wget",
    "azure_iot_hub",
    # "backup" - only 'status' for backup, not 'config'
    "bacnet",
    "bacnet/bip",
    "bacnet/mstp",
    # "bgp" - there is no 'config' for bgp, only 'global' and 'instance'
    "bgp/instance",
    # "bgp/instance/{id}/peer" 'config' doesn't fit the scheme for now
    # "bgp/instance/{id}/peer_group" 'config'
    "bgp/access", # Returns all BGP access configurations
    "bgp/maps", # Returns all BGP route maps configurations
    "bgp/map_filters", # Returns all BGP map filters configurations
    # "bgp/instance/{id}/map_filters" 🤷‍♂️
    # "call_utilities" - 'global'
    "call_utilities/rules",
    "certificates",
    "certificates/certs",
    "certificates/ca",
    "certificates/client",
    "certificates/server",
    "certificates/keys",
    "certificates/dh",
    "certificates/root_ca",
    "cloud_of_things",
    "console",
    "cumulocity",
    "uscripts", # user scripts
    "data_limit",
    "data_to_server/collections",
    "data_to_server/data",
    "data_to_server/servers", # Returns all Data to Server Server Plugins configuration
    # data_usage/{interval}/status - Returns SIM card usage data for specified interval
    "date_time/ntpd",
    "date_time/ntp/client",
    "date_time/ntp/time_servers",
    "ddns",
    "dfota",
    "dhcp/static_leases/ipv4",
    "dhcp/static_leases/ipv6",
    "dhcp/servers/ipv4",
    "dhcp/servers/ipv6",
    # "dhcp/leases/ipv4", - status
    # diagnostics/actions/ping - action only
    # "dlms" - global / "enabled": "string"
    "dlms/connections",
    "dlms/devices",
    "dlms/cosem_group",
    # "dlms/cosem_group/{id}/cosem" - config
    "minidlna",
    "dmvpn",
    "dmz",
    "dnp3/tcp",
    # "dnp3/tcp/{id}/requests"
    "dnp3/serial",
    # "dnp3/serial/{id}/requests"
    "dnp3/outstation",
    "dnp3/serial_outstation",
    "dns",
    "eigrp",
    "email_relay",
    "esim",
    "events_log",
    "events_reporting",
    "failover/mode",
    "failover/interfaces",
    "failover/policies",
    "failover/rules",
    "failover/members",
    "firewall/custom_rules",
    # "firewall/global"
    "firewall/nat_rules",
    "firewall/port_forwards",
    "firewall/traffic_rules",
    "firewall/zones",
    # "firmware/device/status"
    "fota",
    # "gps/global"
    "gps/nmea",
    "gps/nmea/rules",
    "gps/https",
    "gps/https/tavl_rules",
    "gps/avl",
    "gps/avl/main_rules",
    "gps/avl/secondary_rules",
    "gps/avl/tavl_rules",
    "gps/avl/io_rules",
    "gps/geofencing",
    "gre",
    # "gre/{id}/routes"
    "hotspot",
    "hotspot/users",
    "hotspot/users/config",
    # "hotspot/themes/global"
    "hotspot/themes",
    "hotspot/groups",
    "hotspot/user_management",
    "hotspot2",
    # "hotspot2/{id}/venues"
    # "hotspot2/{id}/3gpp"
    # "hotspot2/{id}/nai"
    # "hotspot2/{id}/names"
    # "hotspot2/{id}/capabilities"
    "igmp_proxy",
    "igmp_proxy/routes",
    # "io/juggler/global"
    "io/juggler/conditions",
    "io/juggler/operations",
    "io/juggler/inputs",
    "io/post_get",
    # "io/scheduler/global"
    "io/scheduler",
    "interfaces",
    # "internet_connection/global"
    # "ip_neighbors/ipv4/status"
    "ip_routes/ipv4",
    "ip_routes/ipv6",
    "ip_rules/ipv4",
    "ipsec",
    "ipsec/secrets",
    "l2tp/client",
    "l2tp/server",
    "l2tp/users",
    "l2tpv3",
    "logging",
    # "messages/status" - Returns all SMS Messages
    "messages/storage",
    # "modbus/client/global"
    "modbus/client/tcp",
    # "modbus/client/tcp/{id}/requests"
    # "modbus/client/tcp/{id}/alarms"
    "modbus/client/serial",
    "modbus/client/serial/servers",
    "modbus/client/serial/servers/{id}/requests",
    "modbus/client/serial/servers/{id}/alarms",
    "modbus/server/serial",
    "modbus/server/tcp",
    "modbus/tcp_over_serial",
    "modbus/tcp_over_serial/{id}/filters",
    "modbus/gateway",
    "modbus/serial_gateway",
    "modem_control",
    "mqtt/broker",
    "mqtt/bridge",
    "mqtt/bridge/topics",
    "mqtt/publisher",
    # "nat_offloading/global"
    "network/devices",
    "network/devices/bridge",
    "network/devices/ethernet/",
    "nhrp",
    "nhrp/interface",
    # nhrp/interface/{id}/mapping
    "ntrip",
    "opcua/destination_server",
    "opcua/server",
    # opcua/server/{id}/nodes
    # opcua/group/{id}/values
    "opcua/group",
    # opcua/global
    "openvpn",
    # openvpn/{id}/clients
    "operator_lists",
    "ospf",
    "ospf/interface",
    "ospf/neighbor",
    "ospf/area",
    "ospf/network",
    "overip",
    # "overip/{id}/filters"
    "package_manager/restore",
    # package_manager/all_packages/status
    "port_based_vlan",
    "ports_settings",
    "pptp/client",
    "pptp/server",
    "profiles",
    # profiles/scheduler/global
    "profiles/scheduler",
    "qos/interfaces",
    "qos/rules",
    "recipients/phone_groups",
    "recipients/email_users",
    "relayd",
    # "rip/global"
    "rip/interface",
    "rip/access",
    "rms",
    "routing_tables",
    # "samba/global"
    "samba/shares",
    "samba/users",
    # serial/status
    # services/status
    "sim_cards",
    "sim_idle_protection",
    "sim_switch",
    "smpp",
    "sms_gateway/post_get",
    "sms_gateway/auto_reply",
    "sms_gateway/sms_forwarding/to_http",
    "sms_gateway/sms_forwarding/to_sms",
    "sms_gateway/sms_forwarding/to_smtp",
    "sms_gateway/email_to_sms",
    "sms_utilities/rules",
    "snmp/agent",
    "snmp/system",
    "snmp/users",
    "snmp/communities",
    "snmp/communities_v6",
    # snmp/trap/global
    "snmp/trap",
    "speedtest",
    "sqm",
    "sshfs",
    "sstp",
    # stunnel/global
    "stunnel",
    # system/device/status
    # system/device/usage/status
    # system/device/load/status
    "system",
    "system/led",
    "system/buttons",
    "thingworx",
    "tinc",
    # tinc/{id}/hosts
    # topology/status
    "tr069",
    "ulog/available_interfaces",
    "ulog",
    "ulog/ftp",
    "troubleshoot",
    # troubleshoot/system/status - Returns system log contents
    # troubleshoot/kernel/status - Returns kernel log contents
    "udprelay",
    # unauthorized/status
    # "upnp/global",
    "upnp/acls",
    "upnp/redirects",
    # usb_tools/memory_expansion/status
    "usb_tools",
    "usb_tools/mount",
    "usb_tools/p910nd",
    "users",
    "users/groups",
    # users/acls/options
    "vrf",
    "vrrp",
    "wol/global",
    "wol",
    # webfilter/global
    "webfilter",
    "webfilter/privoxy",
    "wifi_scanner",
    "wireguard",
    # wireguard/{id}/peers
    "wireless/multi_ap",
    "wireless/devices",
    "wireless/interfaces",
    # wireless/interfaces/status
    "zerotier",
    # zerotier/{id}/networks
]