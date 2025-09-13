# Cyber Security Base – Module 5.1 Project

## Project Overview

This project demonstrates practical cybersecurity attacks in a controlled virtual lab environment. The target is **Metasploitable3** with **DVWA (Damn Vulnerable Web Application)**, and the attacker machine is **Kali Linux**. The project aims to identify, exploit, and document common vulnerabilities, and apply threat modeling using **STRIDE** and **OWASP Top 10** frameworks.

**Note:** This project contains only the results of the experiments and is **not able to be cloned**.

## Attacks Demonstrated

1. **SQL Injection** – Bypassing authentication and extracting user data.
2. **XSS Reflected** – Injecting JavaScript into input fields.
3. **Command Injection** – Executing system commands via DVWA.
4. **SSH Weak Authentication** – Logging in with default credentials.
5. **Telnet Weak Authentication** – Logging in with default credentials.

## Tools Used

* Kali Linux (attacker VM)
* Metasploitable3 (target VM)
* DVWA for web vulnerabilities
* Nmap for port scanning
* Dirb/Gobuster for directory and file enumeration
* Snort for intrusion detection (optional)
* Excel/Python for threat modeling analysis


## Threat Modeling

Threat modeling was done using STRIDE and OWASP Top 10 to assess risk and impact for each attack.

## Usage Instructions

1. Review the `scans/` outputs and `PoC_DVWA/` for proof of concept.
2. Open `threat_model.xlsx` to analyze threat modeling results.
3. View `Cybersecurity_Report.pdf` for the detailed project report.
4. Open `Threat_Model_Dashboard.png` to visualize the threat model.

**Note:** This project is for educational purposes only and should only be executed in a controlled virtual lab environment.
