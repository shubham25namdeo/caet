"""

Module to support Fault.consume

"""

from honeybadger.new_service import BaseService, launch_service


class FaultConsumer(BaseService):

    """

    Fault Consumer primary class



    :param config_path:

    :param instance_number:

    :return:

    """

    service_name = 'viper.fault.consume'



    def consume_message(self, incoming_message, outgoing_message):

        """

        Convert the Fault message to DTNA acceptable payload



        :param incoming_message:

        :param outgoing_message:

        :return:



        """



        message_parts = incoming_message.body

        key = message_parts.get('key', "")

        esn = key.get('esn', "") # waiting for the other source(corvid.jackdaw)

        trouble_code = message_parts.get('trouble_code', "")

        location = trouble_code.get('location', "")

        latitude = location.get('lat', "")

        longitude = location.get('lon', "")

        odometer = trouble_code.get('odometer', "")

        timestamp = trouble_code.get('ts', "")

        spn = trouble_code.get('spn', "")

        fmi = trouble_code.get('fmi_id', "")

        occurrence_count = trouble_code.get('occurrence_count', "")

        address = trouble_code.get('source_address', "")

        sa = address.get('sa', "")

        vin = key.get('vin', "") # waiting for the source(corvid.jackdaw)

        serial = key.get('gpssn', "")







        payload = {

            "event": {

                "esn": esn,

                "latitude": latitude,

                "longitude": longitude,

                "odometer": odometer,

                "timestamp": timestamp,

                "vin": vin,

                "v2jDataSource": {

                    "serial": serial

                }

            },

            "faultTrigger": {

                "j1939fault": {

                    "fmi": str(fmi),

                    "sa": str(sa),

                    "spn": str(spn),

                    "timestamp": timestamp

                }

            },

            "faults":[



                {"j1939faults": {

                    "timestamp": timestamp,

                    "sa": int(sa),

                    "spn": int(spn),

                    "fmi": fmi,

                    "ocurrencecount": occurrence_count

               }

              }

            ]

        }





        outgoing_message.body = payload

        self.publish(outgoing_message)

        #return payload



if __name__ == '__main__':

    launch_service(FaultConsumer)