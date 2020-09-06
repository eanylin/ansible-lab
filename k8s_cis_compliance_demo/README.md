# K8s CIS Compliance Using Ansible Tower and Kube-Bench

Ansible has been used to perform compliance checks on various Operating Systems such as Linux, Unix and Windows Servers. It has also been used in recent days to perform CIS compliance checks on network equipment such as Cisco, Juniper routers/switches.

While most of the end targets are usually physical servers, network equipment and/or virtual machines, it is also possible to make use of Ansible to perform compliance checks against Kubernetes platforms. This playbook makes use of kube-bench (refer to [kube-bench](https://github.com/aquasecurity/kube-bench) for more information) to perform CIS Compliance on Kubernetes platform.

The Ansible [Community Kubernetes Collections](https://galaxy.ansible.com/community/kubernetes) is also used to retrieve logs from the pod as part of the playbook run. Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins (refer to this [user guide](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more information on Ansible Collection)

[Ansible Tower](https://www.ansible.com/products/tower) 3.7.2 and [Engine](https://github.com/ansible/ansible) 2.9.13 were used to execute the playbook (the YouTube demo video recording can be found at the following [link](https://youtu.be/6jNuK0jdB_c)). Playbook testing was performed against vanilla kubernetes built using kubeadm. The target node is as follows

```
# kubectl get nodes -o wide
NAME                 STATUS   ROLES    AGE     VERSION   INTERNAL-IP      EXTERNAL-IP   OS-IMAGE                KERNEL-VERSION                CONTAINER-RUNTIME
centos7.domain.com   Ready    master   2d21h   v1.19.0   192.168.56.145   <none>        CentOS Linux 7 (Core)   3.10.0-1127.19.1.el7.x86_64   docker://19.3.12
```

```
# kubectl get pods -n kube-system
NAME                                         READY   STATUS    RESTARTS   AGE
coredns-f9fd979d6-9c2cl                      1/1     Running   2          2d21h
coredns-f9fd979d6-cgh8d                      1/1     Running   2          2d21h
etcd-centos7.domain.com                      1/1     Running   2          2d21h
kube-apiserver-centos7.domain.com            1/1     Running   2          2d21h
kube-controller-manager-centos7.domain.com   1/1     Running   3          2d21h
kube-proxy-qt64c                             1/1     Running   2          2d21h
kube-scheduler-centos7.domain.com            1/1     Running   3          2d21h
```

```
# kubectl get pods -n calico-system
NAME                                       READY   STATUS    RESTARTS   AGE
calico-kube-controllers-67f6c9d576-xqcww   1/1     Running   0          5m8s
calico-node-sgm5l                          1/1     Running   2          2d21h
calico-typha-6c9c786b77-wt6qg              1/1     Running   0          5m8s
```
