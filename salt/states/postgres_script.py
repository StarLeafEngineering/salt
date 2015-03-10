import logging

log = logging.getLogger(__name__)

def run(name,
        source,
        dbname=None,
        host=None,
        port=None,
        password=None,
        runas=None,
        user=None,
        **kwargs):

    log.debug("Running postgres_script on {0} from {1}".format(source, __env__))

    if __opts__['test']:
        return {
            'changes': {},
            'comment': 'Postgres script {0} needs to be run'.format(source),
            'name': name,
            'result': None,
        }

    mret = __salt__['postgres_ext.run_script'](
        source=source,
        saltenv=__env__,
        dbname=dbname,
        host=host,
        port=port,
        password=password,
        runas=runas,
        user=user,
    )
    return {
        'changes': mret,
        'comment': 'Postgres script {0} {1}'.format(
            source,
            "Succeeded" if mret['retcode'] == 0 else "Failed"
        ),
        'name': name,
        'result': mret['retcode'] == 0,
    }
