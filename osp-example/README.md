main.yaml

> Configure SSH keys on Jumpbox

```
ssh -i ./.ssh/yourprivatekey userid@workstation-${GUID}.rhpds.opentlc.com
wget http://www.opentlc.com/download/ansible_bootcamp/openstack_keys/openstack.pub
cat openstack.pub  >> ~/.ssh/authorized_keys
```

> Configure laptop or bastion host for ssh proxy

```
wget http://www.opentlc.com/download/ansible_bootcamp/openstack_keys/openstack.pem -O ~/.ssh/openstack.pem
chmod 400 ~/.ssh/openstack.pem


cat << EOF > /etc/ansible/openstack_ssh_config
Host workstation-${GUID}.rhpds.opentlc.com
 Hostname workstation-${GUID}.rhpds.opentlc.com
 IdentityFile ~/.ssh/openstack.pem
 ForwardAgent yes
 User cloud-user
 StrictHostKeyChecking no
 PasswordAuthentication no

Host 10.10.10.*
 User cloud-user
 IdentityFile ~/.ssh/openstack.pem
 ProxyCommand ssh -F ~/.ssh/openstack_ssh_config cloud-user@workstation-${GUID}.rhpds.opentlc.com -W %h:%p -vvv
 StrictHostKeyChecking no
EOF


cat << EOF > osp_test_inventory
[jumpbox]
workstation-${GUID}.rhpds.opentlc.com ansible_ssh_user=root ansible_ssh_private_key_file=~/.ssh/openstack.pem
EOF

ansible -i osp_test_inventory all -m ping


ansible -i osp_test_inventory jumpbox -m os_user_facts -a cloud=ospcloud -v

cat << EOF > ssh_ansible.yaml
- hosts: localhost
  tasks:
  - name: Add ssh_args in ansible.cfg to point to the user's SSH config
    lineinfile:
      path: /etc/ansible/ansible.cfg
      insertafter: '^#ssh_args '
      line: 'ssh_args = -F /etc/ansible/openstack_ssh_config -o ControlMaster=auto -o ControlPersist=5m -o LogLevel=QUIET'
EOF
```


 
Step 1: Deploy Insfrastructure on OSP 10

>roles/osp-instances/vars/frontend.yaml
```
instance_name: frontend
group: frontends
deployment: dev
security_group_name: frontend_servers
```

>roles/osp-instances/vars/app1.yaml
```
instance_name: app1
group: apps
deployment: dev
security_group_name: app_servers
```

>roles/osp-instances/vars/app2.yaml
```
instance_name: app2
group: apps
deployment: dev
security_group_name: app_servers
```

>roles/osp-instances/vars/db.yaml
```
instance_name: db
group: appdbs
deployment: dev
security_group_name: db_servers
```
Step 2: Configure Instances 

Step 3: Deploy example APP
