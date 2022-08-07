from config import OSM_URL_PRIMARY, OSM_URL_SECONDARY_ONE, OSM_URL_SECONDARY_TWO


def switchover():

  try:
   result = call_something(OSM_URL_PRIMARY)
  except Exception:
    result = call_something(OSM_URL_SECONDARY_TWO)
  except Exception:
    result = call_something(OSM_URL_SECONDARY_TWO)
  except Exception:
    raise Exception("Unable to get a final result")

  return result

def call_something(url):
  pass
