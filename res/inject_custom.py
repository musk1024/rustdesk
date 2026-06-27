# Injects self-hosted server config at build time from environment variables.
# No secrets are stored in the repo; values come from GitHub Actions secrets.
import os
rdv = os.environ.get("RS_RENDEZVOUS", "").strip()
key = os.environ.get("RS_PUB_KEY", "").strip()
api = os.environ.get("RS_API", "").strip()
cfg = "libs/hbb_common/src/config.rs"
s = open(cfg, encoding="utf-8").read()
if rdv:
    s = s.replace('&["rs-ny.rustdesk.com"]', '&["%s"]' % rdv)
if key:
    s = s.replace("OeVuKk5nlHiXp+APNn0Y3pC1Iwpwn44JGqrQCsWqmBw=", key)
open(cfg, "w", encoding="utf-8").write(s)
com = "src/common.rs"
s = open(com, encoding="utf-8").read()
if api:
    s = s.replace('"https://admin.rustdesk.com".to_owned()', '"%s".to_owned()' % api)
open(com, "w", encoding="utf-8").write(s)
print("inject done: rendezvous=%s pubkey=%s api=%s" % (bool(rdv), bool(key), bool(api)))
