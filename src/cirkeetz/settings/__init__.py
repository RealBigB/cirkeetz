# -*- coding:utf-8 -*
import os


_here = os.path.dirname(os.path.abspath(__file__))
_envname = os.getenv("CIRKEETZ_ENV", None)
if _envname:
    _settings = os.path.join(_here, "%s.py" % _envname)
    if not os.path.exists(_settings):
        raise RuntimeError("found $CIRKEETS_ENV='%s' but no matching settings file '%s'" % (_envname, _settings))
else:
    _nodename = os.uname()[1].lower().replace(" ", "").replace(".", "_")
    _settings = os.path.join(_here, "%s.py" % _nodename)
    if not os.path.exists(_settings):
        raise RuntimeError("no node settings file '%s' found for node '%s'" % (_settings, _nodename))
    
execfile(_settings)
