import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port, timeout=1):
    """Attempt to connect to a given host/port and return the port if open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            return port if result == 0 else None
    except Exception:
        return None

def network_scan(host, port_range=(1, 1024), max_threads=100, timeout=1):
    """Scan ports on a given host within the specified port range."""
    open_ports = []
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [
            executor.submit(scan_port, host, port, timeout)
            for port in range(port_range[0], port_range[1] + 1)
        ]
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)
    return sorted(open_ports)

if __name__ == "__main__":
    # ======= STATIC CONFIG (edit these) =======
    target_host = "127.0.0.1"     # e.g., "127.0.0.1", "192.168.1.10" or "example.com"
    start_port = 1
    end_port = 1024
    max_threads = 100
    timeout_seconds = 1
    # ==========================================

    print(f"Scanning {target_host} ports {start_port}-{end_port} (threads={max_threads})...")
    results = network_scan(
        target_host,
        port_range=(start_port, end_port),
        max_threads=max_threads,
        timeout=timeout_seconds,
    )

    if results:
        print("Open ports found:", results)
    else:
        print("No open ports found.")