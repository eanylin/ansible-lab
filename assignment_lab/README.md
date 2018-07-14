**Background**

MitziCom, a telecommunications company, provides hosting and cloud services to a variety of clients, from medium-sized companies to enterprise giants.

MitziCom has requested a proof-of-concept using Red Hat Ansible Tower. The purpose of the POC is to determine the feasibility of using Ansible Tower as a CI/CD tool for automating continuous deployment of an internal three-tier application on QA and production environments.

**Environment**

- OpenStack Platform Workstation: workstation-7655.rhpds.opentlc.com
- Production Bastion/Jump-Server: bastion.0b75.example.opentlc.com
- Ansible Tower (Cluster): https://tower1.ffe9.example.opentlc.com, https://tower2.ffe9.example.opentlc.com, https://tower3.ffe9.example.opentlc.com

**Ansible Tower Setup Steps**
1. Add public key (http://www.opentlc.com/download/ansible_bootcamp/openstack_keys/openstack.pub) to authorized_keys of the cloud-user on the OpenStack Platform Workstation
2. Create *Advanced_Ansible_Lab* inventory in Ansible Tower
    - Create *osp_workstation* host
3. Create *cloud-user* credentials (Machine Login) in Ansible Tower using private key from http://www.opentlc.com/download/ansible_bootcamp/openstack_keys/openstack.pem 
4. Create new project, i.e. *Advanced_Ansible_Lab_Assignment* using Git SCM Type, pointing to https://github.com/eanylin/ansible-lab
    - Set SCM Update Option to *Clean* and *Update on Launch*
5. Create new Job Template, i.e. Provision_QA_Environment with the following settings:
    - Inventory: Advanced_Ansible_Lab
    - Project: Advanced_Ansible_Lab_Assignment
    - Playbook: assignment_lab/provision_osp.yml
    - Credential: cloud-user (Machine)
    - Verbosity: 2
6. Create new Job Template, i.e. Deploy_3_Tier_App_QA with the following settings:
    - Inventory: Advanced_Ansible_Lab
    - Project: Advanced_Ansible_Lab_Assignment
    - Playbook: assignment_lab/configure_3TA_OSP.yml
    - Credential: cloud-user (Machine)
    - Verbosity: 2
7. Create new Job Template, i.e. Clean_Up_OpenStack with the following settings:
    - Inventory: Advanced_Ansible_Lab
    - Project: Advanced_Ansible_Lab_Assignment
    - Playbook: assignment_lab/cleanup_OSP.yml
    - Credential: cloud-user (Machine)
    - Verbosity: 2
8. Create new Job Template, i.e. Provision_Prod_Environment with the following settings:
    - Inventory: Advanced_Ansible_Lab
    - Project: Advanced_Ansible_Lab_Assignment
    - Playbook: assignment_lab/provision_prod.yml
    - Credential: aws 
    - Verbosity: 2
9. Create new Job Template, i.e. Create_3_Tier_Prod_Key with the following settings:
    - Inventory: Advanced_Ansible_Lab
    - Project: Advanced_Ansible_Lab_Assignment
    - Playbook: assignment_lab/create_3TA_prod_key.yml
    - Credential: aws
    - Verbosity: 2
10. Create new Job Template, i.e. Deploy_3_Tier_App_Prod with the following settings:
    - Inventory: Advanced_Ansible_Lab
    - Project: Advanced_Ansible_Lab_Assignment
    - Playbook: assignment_lab/configure_3TA_AWS.yml
    - Credential: aws 
    - Verbosity: 2
11. Create new Job Template, i.e. Clean_Up_3_Tier_App_Prod with the following settings:
    - Inventory: Advanced_Ansible_Lab
    - Project: Advanced_Ansible_Lab_Assignment
    - Playbook: assignment_lab/cleanup_3TA.yml
    - Credential: aws 
    - Verbosity: 2
12. Create a new workflow job template, i.e. Ansible_CICD and update the workflow editor as follows:
