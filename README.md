# MPTCP NIDS Evasion Tests

## Contents
1. [Overview](#overview)
2. [NIDS](#nids)
    1. [Suricata Rules](#suricata-rules)
    2. [Snort Rules](#snort-rules) 
3. [Test Cases](#test-cases)
4. [Test Scenarios](#test-scenarios)
    1. [(scenario1/baseline) TCP Fragmentation](#scenario1) 
    2. [(scenario2) MPTCP Fragmentation in a single subflow](#scenario2)
    3. [(scenario3) PTCP Fragmentation across a single IDS](#scenario3)
    4. [(scenario4) MPTCP Fragmentation across multiple IDS](#scenario4)

---

## Overview
This repository contains tests conducted in order to demonstrate how it's possible to evade Network Intrusion Detection Systems(NIDS) using MPTCP connections. 
The tests were conducted in an emulation environment using [`CORE v5.5.1`](https://github.com/coreemu/core). During the tests execution traffic was recorded in the relevant interfaces. Those captures were later used to generate the NIDSs analysis. 

The machine used for the tests was running `Linux Kernel 5.14`.


The MPTCP configurations and the topologies were created using [mptcp_test_bed](https://github.com/RuiCunhaM/mptcp_test_bed).

As for the web server, that acted as the target of the attacks, a [small altered version](https://github.com/RuiCunhaM/mini_httpd/tree/mptcp-detailed-logs) of [mini_httpd](https://github.com/peter-leonov/mini_httpd) was used in order to support MPTCP.

For each individual test it's possible to consult a variety of data:
  - Topology configuration files
  - The scripts used to generate the attacks
  - Logs from the web server.
  - NIDSs reports
  - Pcaps at the relevant nodes

**Note:** When reproducing these tests, in order for the python scripts to work, they require a Python version compatible with MPTCP. This is officially supported since **Python 3.10**. But there is also a 3.9 compatible [fork](https://github.com/RuiCunhaM/cpython/tree/3.9-mptcp).  

---

## NIDS

The NIDSs used to inspect the traffic in these tests were [`Suricata v6.0.3`](https://suricata.io/) and [`Snort3`](https://www.snort.org/snort3).


### Suricata Rules 
The Suricata rules used were acquired from the following sources:

```
- oisf/trafficid
- sslbl/ssl-fp-blacklist
- sslbl/ja3-fingerprints
- tgreen/hunting
- etnetera/aggressive
- ptresearch/attackdetection
- malsilo/win-malware
- et/open
```

### Snort Rules
As for Snort rules, besides the builtin, the following sets were also used:
```
- snort3-community-rules.tar.gz
- snortrules-snapshot-31150.tar.gz (Registered)
```
---

## Test Cases
The first test case consist of a [**SQL Injection**](SQL_Injection/) attempt, and is aimed to simply show how this technique is effective, and it also helps to easily understand how it works.
 
The second test case is a complete [**Web Scanning**](Web_Scanning/) attempt, where the database from [Nikto2](https://cirt.net/Nikto2) is used to evaluate if its possible to achieve a lower detection rate when combined with this technique.

---

## Test Scenarios
Each test case was executed in four different scenarios. These scenarios have different purposed and are are used to demonstrate different situations where the MPTCP Fragmentation can be achieved.

<a name="scenario1"></a>
### TCP Fragmentation (scenario1/baseline)
This first scenario uses common TCP, and its purpose is to prove that even when splitting an HTTP Request across different TCP segments, NIDS are still able to put the requests together and detect the threats. This is also considered as the baseline for the next scenarios.

---

<a name="scenario2"></a>
### MPTCP Fragmentation in a single subflow (scenario2)
This scenario is very similar to the previous one, however this time instead of a simple TCP connection we have a MPTCP connection with a single subflow. This aims to demonstrate that the NIDS are still able to detect the threats if only one MPTCP subflow is used. This behaviour is completely expected, since MPTCP is technically just an extra TCP option, therefore, to the eyes of the NIDS this is exactly the same to the previous scenario with a normal TCP connection.

---

<a name="scenario3"></a>
### MPTCP Fragmentation across a single IDS (scenario3)
In this scenario, the **A**ttacker has two interfaces in two different subnets, meanwhile the **T**arget is only connected to one subnet and has only one interface. Here the request is splitted across the two subflows, which causes the NIDS to see data arriving from different MPTCP subflows/TCP Connections but that belong to the same overall MPTCP connection.

---

<a name="scenario4"></a>
### MPTCP Fragmentation across multiple IDS (scenario4)
This last scenario is similar to the previous, however this time the **T**arget server is the one using two network interfaces. Here two different NIDS analysis are conducted, one for each subnet that the target is connected to. In this scenario, by splitting the request across the subflows, only a fraction of the total data goes through each network, therefore it is not possible for the NIDS to have a complete picture of the attack. 

[Back to top](#contents)


