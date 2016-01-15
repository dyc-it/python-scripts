import sys
import keystoneclient.v2_0.client as ksclient
from neutronclient.v2_0 import client as neutronclient


def initSecurityGroupRules(auth_url, username, password, tenant_name, isClearingSecurintGroupRules):
    neutron = neutronclient.Client(auth_url=auth_url,
                           username=username,
                           password=password,
                           tenant_name=tenant_name)

    group = neutron.list_security_groups(name="default")
    groupID=group['security_groups'][0]['id']

    if isClearingSecurintGroupRules==True:
        for rule in group['security_groups'][0]['security_group_rules']:
            #print rule
            neutron.delete_security_group_rule(rule['id'])

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

    out_80 = {
                     "security_group_rule": {
                            "direction": "egress",
                            "port_range_min": "80",
                            "ethertype": "IPv4",
                            "port_range_max": "80",
                            "protocol": "tcp",
                            "security_group_id": groupID
                      }
                 }

    in_22 = {
                     "security_group_rule": {
                            "direction": "ingress",
                            "port_range_min": "22",
                            "ethertype": "IPv4",
                            "port_range_max": "22",
                            "protocol": "tcp",
                            "security_group_id": groupID
                      }
                 }

    out_22 = {
                     "security_group_rule": {
                            "direction": "egress",
                            "port_range_min": "22",
                            "ethertype": "IPv4",
                            "port_range_max": "22",
                            "protocol": "tcp",
                            "security_group_id": groupID
                      }
                 }
    in_icmp = {
                     "security_group_rule": {
                            "direction": "ingress",
                            "ethertype": "IPv4",
                            "protocol": "icmp",
                            "security_group_id": groupID
                      }
                 }

    out_icmp = {
                     "security_group_rule": {
                            "direction": "egress",
                            "ethertype": "IPv4",
                            "protocol": "icmp",
                            "security_group_id": groupID
                      }
                 }
    print 'add ingress and egress of port 80'
    try:
        neutron.create_security_group_rule(in_80)
    except Exception:
        pass
    try:
        neutron.create_security_group_rule(out_80)
    except Exception:
        pass

    print 'add ingress and egress of port 22'
    try:
        neutron.create_security_group_rule(in_22)
    except Exception:
        pass
    try:
        neutron.create_security_group_rule(out_22)
    except Exception:
        pass

    print 'add ingress and egress of icmp protocol'
    try:
        neutron.create_security_group_rule(in_icmp)
    except Exception:
        pass
    try:
        neutron.create_security_group_rule(out_icmp)
    except Exception:
        pass


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print len(sys.argv)
        print 'usage: python createTenant.py tenantName userName password'
        exit(1)
    tenant_name=sys.argv[1]
    user_name=sys.argv[2]
    password=sys.argv[3]


    ADMIN_OS_AUTH_URL= 'http://haproxy:35357/v2.0'
    NORMAL_OS_AUTH_URL='http://haproxy:5000/v2.0'
    OS_USERNAME='admin'
    OS_PASSWORD='cdf9a6f98269180d64b3'
    OS_TENANT_NAME='admin'
    OS_REGION_NAME=''

    keystone = ksclient.Client(auth_url=ADMIN_OS_AUTH_URL,
                               username=OS_USERNAME,
                               password=OS_PASSWORD,
                               tenant_name=OS_TENANT_NAME)
    tenant=None
    user=None

    isTenantExists=True
    isClearingSecurintGroupRules=False
    try:
        tenant=keystone.tenants.find(name=tenant_name)
        print 'tenant "%s" exists' % tenant_name
    except Exception:
        isTenantExists=False
        # if tenant not exist, clear the default security groups rules in the new tenant
        isClearingSecurintGroupRules=True

    isUserExists=True
    try:
        user=keystone.users.find(name=user_name)
        print 'user "%s" exists' % user_name
    except Exception:
        isUserExists=False

    if isUserExists==False:
        print 'create user "%s"' % user_name
        user=keystone.users.create(name=user_name,password=password)

    if isTenantExists==False:
        print 'create tenant "%s"' % tenant_name
        tenant=keystone.tenants.create(tenant_name=tenant_name)
        isTenantExists=True

    # add user in tenant with normal role
    try:
        role=keystone.roles.find(name='_member_')
        print 'Add user "%s" in tenant "%s"' % (user_name, tenant_name)
        keystone.roles.add_user_role(user=user,role=role,tenant=tenant)
    except Exception:
        pass


    if isUserExists==True and isTenantExists==True:
        # whether the password of user is correct
        try:
            keystone = ksclient.Client(auth_url=NORMAL_OS_AUTH_URL,
                               username=user_name,
                               password=password,
                               tenant_name=tenant_name)
        except Exception:
            print 'Error:the password of user is incorrect, cannot add security group rules'
            sys.exit(1)



    # add default security group rules
    initSecurityGroupRules(auth_url=NORMAL_OS_AUTH_URL, username=user_name,
                           password=password, tenant_name=tenant_name,
                           isClearingSecurintGroupRules=isClearingSecurintGroupRules)







