import nmap

nm = nmap.PortScanner()
print("nm", nm)
results = nm.scan('49.43.33.180', '1-1024')
print("results", results)
for host in results['scan']:
    print(f'{host}: {results["scan"][host]["tcp"].keys()}')