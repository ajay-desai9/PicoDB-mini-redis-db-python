from picodb  import Client

c = Client()

print("Set foo => bar:", c.set("foo", "bar"))
print("Get foo:", c.get("foo"))
print("MGET foo, missing_key:", c.mget("foo", "missing_key"))
print("MSET a 1 b 2:", c.mset("a", "1", "b", "2"))
print("Get a:", c.get("a"))
print("Flush all keys:", c.flush())
print("Get foo after flush:", c.get("foo"))  