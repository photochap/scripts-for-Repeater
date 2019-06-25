#/etc/init.d/ircddbgateway {start|stop|status|restart|force-reload}
"""
ircddbgateway.service - LSB: ircDDBGateway
   Loaded: loaded (/etc/init.d/ircddbgateway; generated; vendor preset: enabled)
   Active: active (running) since Wed 2018-08-01 13:59:34 CEST; 11min ago
     Docs: man:systemd-sysv-generator(8)
  Process: 23150 ExecStop=/etc/init.d/ircddbgateway stop (code=exited, status=0/SUCCESS)
  Process: 23342 ExecStart=/etc/init.d/ircddbgateway start (code=exited, status=0/SUCCESS)
   CGroup: /system.slice/ircddbgateway.service
           +-23442 /usr/bin/ircddbgatewayd -daemon -logdir /var/log/opendv

août 01 13:59:24 PHOTOCHAP_DStar systemd[1]: Starting LSB: ircDDBGateway...
août 01 13:59:25 PHOTOCHAP_DStar ircddbgateway[23342]: Stopping ntp (via systemctl): ntp.service.
août 01 13:59:31 PHOTOCHAP_DStar ircddbgateway[23342]:  1 Aug 13:59:31 ntpdate[23373]: adjust time server 95.81.173.74 offset -0.001710 sec
août 01 13:59:32 PHOTOCHAP_DStar ircddbgateway[23342]: Starting ntp (via systemctl): ntp.service.
août 01 13:59:34 PHOTOCHAP_DStar systemd[1]: Started LSB: ircDDBGateway.
Hint: Some lines were ellipsized, use -l to show in full.
"""
#
