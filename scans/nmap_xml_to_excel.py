# nmap_xml_to_excel.py
import sys, xml.etree.ElementTree as ET
import pandas as pd

xmlfile = sys.argv[1]    # e.g., scans/target_full.xml
xlsxfile = sys.argv[2]   # e.g., scans/target_full.xlsx

tree = ET.parse(xmlfile)
root = tree.getroot()
rows = []
for host in root.findall('host'):
    addr_el = host.find('address')
    if addr_el is None: continue
    ip = addr_el.get('addr')
    ports = host.findall('.//port')
    for p in ports:
        portid = p.get('portid')
        proto = p.get('protocol')
        state = p.find('state').get('state') if p.find('state') is not None else ''
        svc = p.find('service')
        name = svc.get('name') if svc is not None and 'name' in svc.attrib else ''
        product = svc.get('product') if svc is not None and 'product' in svc.attrib else ''
        version = svc.get('version') if svc is not None and 'version' in svc.attrib else ''
        rows.append({'ip':ip,'port':portid,'proto':proto,'state':state,'service':name,'product':product,'version':version})
df = pd.DataFrame(rows)
df.to_excel(xlsxfile,index=False)
print("Saved", xlsxfile)
