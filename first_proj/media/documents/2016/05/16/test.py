binary_file = open("zdl.zdl", "rb")
_bytes = binary_file.read()
print("%d bytes read." % (len(_bytes)), _bytes)

data = _bytes.encode("hex")
print ("\n\n Trial \n\n ", data)

binary_file.close()


# from transform import ringBuffer


# class ringTrial(object):
# 	def __init__(self, body={}):
# 		self.body = body

# payload = {
# 	  "event": {
# 	    "esn": 0,
# 	    "latitude": 0,
# 	    "longitude": 0,
# 	    "odometer": 0,
# 	    "timestamp": "",
# 	    "vin": "",
# 	    "v2jDataSource": {
# 	      "serial": ""
# 	    },
# 	    "faultTrigger": {
# 	      "j1939Fault": {
# 		"fmi": "",
# 		"sa": "",
# 		"spn": "",
# 		"timestamp": ""
# 	      }
# 	    }
# 	  },
# 	  "faults": [
# 	    {
# 	      "j1939Fault": {
# 		"timestamp": "",
# 		"sa": 0,
# 		"spn": 0,
# 		"fmi": 0,
# 		"ocurrenceCount": 0
# 	      }
# 	    }
# 	  ],
# 	  "j1939Message": {
# 	    "fmi": "",
# 	    "sa": "",
# 	    "spn": "",
# 	    "timestamp": ""
# 	  }
# 	}

# t = ringTrial(payload)
# esn = "r"
# byte_collection = "e"
# r = ringBuffer()
# print (r.transF(t, esn, byte_collection))