"""
Module to support ringbuffer.transform
"""
from honeybadger.new_service import BaseService, launch_service


class ringBuffer(BaseService):
	"""
	ringbuffer transform primary class

	:param config_path:
	:param instance_number:
	:return:

	"""
	service_name = 'viper.ringbuffer.transform'

	def _parse_esn(self, esn):
		esn_regex_pattern = config.get("file_worker","esn_pattern")
		log.debug("Parsing ESN \'%s\' with pattern: %s" % (esn, esn_regex_pattern))
		match = re.search(esn_regex_pattern, esn, re.I + re.M)
		if match is not None:
		    for m_str in match.groups():
		        if m_str is not None and isinstance(m_str, str) and len(m_str) >= 1:
		            log.debug("Located ESN:  %s" % m_str)
		            return m_str
		else:
		    log.debug("ESN could not be parsed.")
		return esn



	def _parse_value(self, byte_collection):
		"""
		@param byte_collection:   the bytes representing the header
		@type byte_collection:    byte string.
		"""
		NULL_BYTE = "\x00"
		self.value = None
		try:
			bc = byte_collection[self.offset:self.num_bytes+self.offset]
			self.value = "".join([str(i) for i in struct.unpack(self.format, bc) if i is not NULL_BYTE])

			if self.name == 'odometer':
				self.value = str(int(self.value) * 125)
		except:
			log.error(tb.format_exception(*sys.exc_info()))
		return self.value

	def transF(self):
		"""
		This transformation fuction is written,
		based on the schema supplied.
		Will be edited,	when further instructed.
		"""
		service_name = 'viper.ringbuffer.transform'

		message_parts = incoming_message.body

		location = trouble_code.get('location', "")

		latitude = location.get('lat', "")

		longitude = location.get('lon', "")

		odometer = trouble_code.get('odometer', "")

		spn = trouble_code.get('spn', "")

		fmi = trouble_code.get('fmi_id', "")

		occurrenceCount = trouble_code.get('occurrence_count', "")

		sa = address.get('sa', "")

		vin = key.get('vin', "") # waiting for the source(corvid.jackdaw)

		serial = key.get('gpssn', "")

		payload = {
			"event": {
				"esn": self._parse_esn(self, esn),
				"latitude": latitude,
				"longitude": longitude,
				"odometer": self._parse_value(self, byte_collection),
				"timestamp": timestamp,
				"vin": vin,
				"v2jDataSource": {
					"serial": serial
				},
				"faultTrigger": {
					"j1939Fault": {
						"fmi": str(fmi),
						"sa": str(sa),
						"spn": str(spn),
						"timestamp": timestamp
					}
				}
			},
			"faults": [
			{
			  "j1939Fault": {
			    "timestamp": timestamp,
			    "sa": int(sa),
			    "spn": int(spn),
			    "fmi": fmi,
			    "ocurrenceCount": ocurrenceCount
			  }
			}
			],
			  "j1939Message": {
			    "fmi": str(fmi),
			    "sa": str(sa),
			    "spn": str(spn),
			    "timestamp": str(timestamp)
			  }
			}


# send data to publish function
        self.publish(payload)










# 	#taking default values in variables.

# 	esn = None
# 	latitude = None
# 	longitude = None
# 	odometer = None
# 	timestamp = ""
# 	vin = ""
# 	serial = ""

# 	ftrgr_fmi = ""
# 	ftrgr_sa = ""
# 	ftrgr_spn = ""
# 	ftrgr_timestamp = ""

# 	flts_timestamp = ""
# 	flts_sa = None
# 	flts_spn = None
# 	flts_fmi = None
# 	flts_ocurrenceCount = None

# 	jMsg_fmi = ""
# 	jMsg_sa = ""
# 	jMsg_spn = ""
# 	jMsg_timestamp = ""


if __name__ == '__main__':

	launch_service(ringBuffer)