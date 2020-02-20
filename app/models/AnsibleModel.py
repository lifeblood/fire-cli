from bootstrap import app


class AnsibleModel(object):

    def __init__(self):
        pass

    sh_separator = ' && '
    sql_separator = ' '

    @classmethod
    def _prepared_command(cls, role_name=None, json_data=None, dry_run=False, verbose=None):
        lists = [
            'ansible-playbook',
            '-i ' + app.config().get('ansible::inventory'),
            'playbooks/' + role_name + '.yml',
            '-e ' + json_data
        ]
        if dry_run is True:
            lists.append('--check')
        if verbose is not None:
            lists.append(verbose)
        return lists

    @classmethod
    def run_playbooks(cls, role_name, json_data, verbose=None):
        lists = cls._prepared_command(role_name=role_name, json_data=json_data, dry_run=False, verbose=verbose)
        cmd = cls.sql_separator.join(lists)
        app.utils().subprocess_check_call(cmd)

    @classmethod
    def dry_run_playbooks(cls, role_name, json_data, verbose=None):
        lists = cls._prepared_command(role_name=role_name, json_data=json_data, dry_run=True, verbose=verbose)
        cmd = cls.sql_separator.join(lists)
        app.utils().subprocess_check_call(cmd)

    @staticmethod
    def get_inventory(lists=None, host=None):
        if lists is not None:
            print(lists)
        elif host is not None:
            print(host)
        else:
            print('None!')

