import dns

import dns.resolver

result = dns.resolver.resolve('ivytech.edu','A')

for ipval in result:
    print("IP", ipval.to_text())