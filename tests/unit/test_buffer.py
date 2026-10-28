import pytest
from dcp_service.buffer import BoundedBuffer

def test_buffer_is_fifo():
    buffer = BoundedBuffer[int](2)
    assert buffer.put(1)
    assert buffer.put(2)
    assert buffer.get() == 1
    assert buffer.get() == 2
    assert buffer.get() is None

def test_buffer_rejects_overflow():
    buffer = BoundedBuffer[int](1)
    assert buffer.put(1)
    assert not buffer.put(2)

def test_zero_capacity_is_invalid():
    with pytest.raises(ValueError):
        BoundedBuffer(0)
