import keystoneclient.v2_0.client as ksclient
from neutronclient.v2_0 import client as neutronclient

ADMIN_OS_AUTH_URL= 'http://haproxy:35357/v2.0'
NORMAL_OS_AUTH_URL='http://haproxy:5000/v2.0'
OS_USERNAME='admin'
OS_PASSWORD='cdf9a6f98269180d64b3'
OS_TENANT_NAME='admin'
OS_REGION_NAME=''

tenant_name="dyc"
user_name="dyc"
password="dyc"



keystone = ksclient.Client(auth_url=ADMIN_OS_AUTH_URL,
                           username=OS_USERNAME,
                           password=OS_PASSWORD,
                           tenant_name=OS_TENANT_NAME)



# res=keystone.tenants.find(name=tenant_name)
# print res

# tenant=keystone.tenants.create(tenant_name=tenant_name)
# user=keystone.users.create(name=user_name,password=password)
# role=keystone.roles.find(name='_member_')
# keystone.roles.add_user_role(user=user,role=role,tenant=tenant)


neutron = neutronclient.Client(auth_url=NORMAL_OS_AUTH_URL,
                           username=user_name,
                           password=password,
                           tenant_name=tenant_name)





group = neutron.list_security_groups(name="default")
groupID=group['security_groups'][0]['id']
# print groupID
for rule in group['security_groups'][0]['security_group_rules']:
    print rule
    # neutron.delete_security_group_rule(rule['id'])

in_80 = {
                 "security_group_rule": {
                        "direction": "ingress",
                        "port_range_min": "80",
                        "ethertype": "IPv4",
                        "port_range_max": "80",
                        "protocol": "tcp",
                        "security_group_id": groupID
                  }
             }



print body_value
# in_80='{ "security_group_rule": { "direction": "ingress", "port_range_min": "80", "ethertype": "IPv4", "port_range_max": "80", "protocol": "tcp","security_group_id": "{{security-group-id}}"}}'
# out_80='{ "security_group_rule": { "direction": "egress", "port_range_min": "80", "ethertype": "IPv4", "port_range_max": "80", "protocol": "tcp","security_group_id": "{{security-group-id}}"}}'


neutron.create_security_group_rule(body_value)









