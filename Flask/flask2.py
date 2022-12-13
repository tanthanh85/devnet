from flask import Flask,request
from IOSXE import IOSXE
from flask_restx import Resource, Api, reqparse, fields

iosxe = IOSXE()
app = Flask(__name__)

api = Api(app,version='1.0', title='SIMPLE IOSXE FLASK APP', description="This is a simple IOSXE Flask app")
ns = api.namespace('IOSXE Flask sample', description="Flask sample")


parser = api.parser()
parser.add_argument("area_id", type=str, required=True, help="OSPF Area ID example: 0, 1, 2, ...", location="form")
parser.add_argument("int_id", type=str, required=True, help="GigabitEthernet Interface ID: 1, 2, ...", location="form")



# @ns.route('/')
# def hello_world():
#     return "hello world"

@ns.route('/getospf')
@api.doc(response={404: 'not found'})
@api.doc(response={200: 'successful'})
class QueryInterfaces(Resource):
    def get(self):
        uri = 'Cisco-IOS-XE-native:native/interface/GigabitEthernet=1/ip/Cisco-IOS-XE-ospf:router-ospf/ospf/process-id'
        response = iosxe.get_data(uri)
#         return response.json()

@ns.route('/int_to_ospf')
@api.doc(responses={403: "failed to create"})
@api.doc(responses={201: "success"})
class InterfaceToOSPF(Resource):
    @api.doc(parser=parser)
    def patch(self):
        args = parser.parse_args()
        int_id = args['int_id']
        area_id = args['area_id']
        payload = {
        "Cisco-IOS-XE-ospf:process-id": [
            {
            "id": 1,
            "area": [
                {
                "area-id": area_id
                }
            ]
            }
        ]
        }
        uri = 'Cisco-IOS-XE-native:native/interface/GigabitEthernet={id}/ip/Cisco-IOS-XE-ospf:router-ospf/ospf/process-id'.format(id=int_id)
        response = iosxe.patch_data(uri=uri,payload=payload)
        if response == 204:
            return "successfully added interface GigabitEthernet{id} to OSPF in area {area} ".format(id=int_id, area=area_id)
        else:
            return "Failed with " + str(response)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)