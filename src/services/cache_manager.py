# app/services/cache_manager.py
import time

class InMemoryCacheManger:
    def __init__(self, default_ttl=3600):
        '''
        default_ttl=3600 seconds (1 hour), free API updates < 2 hours.
        '''
        self.cache_store = {} # Location : (data, timestamp)
        self.default_ttl = default_ttl

    def get_cached_data(self, location : str):
        '''
        return data if cache is valid else return nun
        '''''
        cache_entry = self.cache_store.get(location)
        if not cache_entry:
            return None
        data, exp_time = cache_entry
        if(time.time() < exp_time):
            return data
        else:
            #expired cache
            del self.cache_store[location]
            return None

    def set_cached_data(self, location : str, data, ttl=None):
        #Store data in cache via TTL, if none provided use default(API key)
        ttl = ttl or self.default_ttl
        expiration = time.time() + ttl
        self.cache_store[location] = (data, expiration)

    def is_cache_valid(self, location : str):
        cache_entry = self.cache_store.get(location)
        if not cache_entry:
            return False
        _, exp_time = cache_entry
        return time.time() < exp_time


# cache_test.py
if __name__ == "__main__":
    cache = InMemoryCacheManger(default_ttl=5)  # 5 seconds
    cache.set_cached_data("London", {"temp": 20})
    print(cache.get_cached_data("London"))  # Should print {'temp': 20}
    time.sleep(6)
    print(cache.get_cached_data("London"))  # Should print None (expired)
