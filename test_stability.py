import pytest
from network_monitor import NetworkMonitor

@pytest.fixture
def monitor():
    """Setup a NetworkMonitor instance for testing."""
    return NetworkMonitor(target_host="8.8.8.8")

def test_network_connection_status(monitor):
    """Test Case 1: Verify that the target host is reachable."""
    latency = monitor.check_latency()
    assert latency is not None, "Error: Target host is unreachable. Possible network outage."

def test_latency_threshold(monitor):
    """Test Case 2: Ensure latency is within the acceptable industrial threshold (< 100ms)."""
    latency = monitor.check_latency()
    if latency:
        assert latency < 100, f"Alert: High latency detected ({latency:.2f}ms). Real-time safety might be compromised."

def test_stability_logic(monitor):
    """Test Case 3: Validate the system stability logic under normal conditions."""
    # With a high threshold (e.g., 500ms), the system should normally return True
    assert monitor.is_stable(threshold_ms=500) is True, "Logic Error: System failed stability check even with high threshold."