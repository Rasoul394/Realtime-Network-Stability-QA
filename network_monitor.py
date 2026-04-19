import time
from ping3 import ping

class NetworkMonitor:
    """
    Utility class to monitor network stability and latency for industrial systems.
    """
    def __init__(self, target_host="8.8.8.8", timeout=2):
        self.target_host = target_host
        self.timeout = timeout

    def check_latency(self):
        """
        Measures network latency in milliseconds.
        Returns None if the host is unreachable.
        """
        # ping() returns seconds, multiply by 1000 for milliseconds
        latency = ping(self.target_host, timeout=self.timeout)
        if latency is None:
            return None  # Connection timed out or host unreachable
        return latency * 1000

    def is_stable(self, threshold_ms=100):
        """
        Determines if the network is stable based on a specific threshold.
        Industrial standard for real-time systems is often < 100ms.
        """
        latency = self.check_latency()
        if latency is None or latency > threshold_ms:
            return False
        return True