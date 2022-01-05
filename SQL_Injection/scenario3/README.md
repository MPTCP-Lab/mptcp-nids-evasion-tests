# TCP Segmentation - Scenario3

![Topology](topology.png)

- [Script](script.py) used to generate the attack attempt
- Suricata [analysis](suricata/)
- Snort [analysis](snort)
- r3 [pcap](r3_eth2.pcapng)
- [Server logs](httpd.log)
- Topology [configuration](topology.toml)

## Commands Executed

- At **T**arget node
```
./mini_httpd -l httpd.log
```

- At **A**ttacker node
```
python3 script.py 10.0.4.20 eth0
```

---
- Suricata analysis generated with 
```
suricata -r r3_eth2.pcapng > summary.txt
```

- Snort analysis generated with
```
snort -r r3_eth2.pcapng -A alert_fast -R /etc/snort/rules/snort.rules -c /etc/snort/snort.lua > summary.txt
```
