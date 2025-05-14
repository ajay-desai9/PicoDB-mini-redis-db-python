from picodb import Client
import time

def test_basic_operations():
    # Create a client instance
    client = Client()
    
    print("Testing basic operations...")
    
    # Test SET and GET
    print("\n1. Testing SET and GET:")
    client.set("name", "John")
    print(f"GET name: {client.get('name')}")
    
    # Test multiple operations
    print("\n2. Testing multiple operations:")
    client.set("age", "30")
    client.set("city", "New York")
    print(f"GET age: {client.get('age')}")
    print(f"GET city: {client.get('city')}")
    
    # Test MGET
    print("\n3. Testing MGET:")
    values = client.mget("name", "age", "city")
    print(f"MGET name, age, city: {values}")
    
    # Test MSET
    print("\n4. Testing MSET:")
    client.mset("country", "USA", "occupation", "Developer")
    print(f"GET country: {client.get('country')}")
    print(f"GET occupation: {client.get('occupation')}")
    
    # Test DELETE
    print("\n5. Testing DELETE:")
    client.delete("occupation")
    print(f"GET occupation after delete: {client.get('occupation')}")
    
    # Test FLUSH
    print("\n6. Testing FLUSH:")
    print(f"Number of keys before flush: {len(client.mget('name', 'age', 'city', 'country'))}")
    client.flush()
    print(f"GET name after flush: {client.get('name')}")

if __name__ == "__main__":
    # Make sure the server is running before executing tests
    print("Starting PicoDB tests...")
    print("Make sure the server is running in a separate terminal!")
    print("You can start the server by running: python picodb.py")
    
    try:
        test_basic_operations()
        print("\nAll tests completed successfully!")
    except Exception as e:
        print(f"\nError during testing: {str(e)}") 