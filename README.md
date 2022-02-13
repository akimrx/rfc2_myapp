![Role tests](https://github.com/akimrx/rfc2_myapp/actions/workflows/ci.yml/badge.svg)

Role Name
=========

Example myapp role.

Role Variables
--------------

See `defaults/main.yml`

| Variable | Default | Description |
|----------|---------|-------------|
| `myapp_port` | `8080` | listening port |



Running tests locally
---------------------
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
ansible-galaxy collection install community.docker

molecule -v test
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
      - rfc2_myapp
```

License
-------

MIT

Author Information
------------------

akimrx
