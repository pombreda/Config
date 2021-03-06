# encoding: utf-8
# module samba.dsdb
# from /usr/lib/python2.7/dist-packages/samba/dsdb.so
# by generator 1.135
""" Python bindings for the directory service databases. """
# no imports

# Variables with simple values

ATYPE_DISTRIBUTION_GLOBAL_GROUP = 268435457

ATYPE_DISTRIBUTION_LOCAL_GROUP = 536870913

ATYPE_DISTRIBUTION_UNIVERSAL_GROUP = 268435457

ATYPE_INTERDOMAIN_TRUST = 805306370

ATYPE_NORMAL_ACCOUNT = 805306368

ATYPE_SECURITY_GLOBAL_GROUP = 268435456

ATYPE_SECURITY_LOCAL_GROUP = 536870912

ATYPE_SECURITY_UNIVERSAL_GROUP = 268435456

ATYPE_WORKSTATION_TRUST = 805306369

DSDB_CONTROL_DBCHECK = '1.3.6.1.4.1.7165.4.3.19'

DSDB_CONTROL_DBCHECK_MODIFY_RO_REPLICA = '1.3.6.1.4.1.7165.4.3.19.1'

DSDB_SYNTAX_BINARY_DN = '1.2.840.113556.1.4.903'

DSDB_SYNTAX_OR_NAME = '1.2.840.113556.1.4.1221'

DSDB_SYNTAX_STRING_DN = '1.2.840.113556.1.4.904'

DS_DOMAIN_FUNCTION_2000 = 0
DS_DOMAIN_FUNCTION_2003 = 2

DS_DOMAIN_FUNCTION_2003_MIXED = 1

DS_DOMAIN_FUNCTION_2008 = 3

DS_DOMAIN_FUNCTION_2008_R2 = 4

DS_FLAG_ATTR_IS_CONSTRUCTED = 4

DS_FLAG_ATTR_NOT_REPLICATED = 1

DS_FLAG_ATTR_REQ_PARTIAL_SET_MEMBER = 2

DS_GUID_COMPUTERS_CONTAINER = 'AA312825768811D1ADED00C04FD8D5CD'

DS_GUID_DELETED_OBJECTS_CONTAINER = '18E2EA80684F11D2B9AA00C04F79F805'

DS_GUID_DOMAIN_CONTROLLERS_CONTAINER = 'A361B2FFFFD211D1AA4B00C04FD7D83A'

DS_GUID_FOREIGNSECURITYPRINCIPALS_CONTAINER = '22B70C67D56E4EFB91E9300FCA3DC1AA'

DS_GUID_INFRASTRUCTURE_CONTAINER = '2FBAC1870ADE11D297C400C04FD8D5CD'

DS_GUID_LOSTANDFOUND_CONTAINER = 'AB8153B7768811D1ADED00C04FD8D5CD'

DS_GUID_MICROSOFT_PROGRAM_DATA_CONTAINER = 'F4BE92A4C777485E878E9421D53087DB'

DS_GUID_NTDS_QUOTAS_CONTAINER = '6227F0AF1FC2410D8E3BB10615BB5B0F'

DS_GUID_PROGRAM_DATA_CONTAINER = '09460C08AE1E4A4EA0F64AEE7DAA1E5A'

DS_GUID_SYSTEMS_CONTAINER = 'AB1D30F3768811D1ADED00C04FD8D5CD'

DS_GUID_USERS_CONTAINER = 'A9D1CA15768811D1ADED00C04FD8D5CD'

DS_NTDSDSA_OPT_DISABLE_INBOUND_REPL = 2

DS_NTDSDSA_OPT_DISABLE_NTDSCONN_XLATE = 8

DS_NTDSDSA_OPT_DISABLE_OUTBOUND_REPL = 4

DS_NTDSDSA_OPT_DISABLE_SPN_REGISTRATION = 16

DS_NTDSDSA_OPT_IS_GC = 1

DS_NTDSSETTINGS_OPT_FORCE_KCC_WHISTLER_BEHAVIOR = 64

DS_NTDSSETTINGS_OPT_IS_AUTO_TOPOLOGY_DISABLED = 1

DS_NTDSSETTINGS_OPT_IS_GROUP_CACHING_ENABLED = 32

DS_NTDSSETTINGS_OPT_IS_INTER_SITE_AUTO_TOPOLOGY_DISABLED = 16

DS_NTDSSETTINGS_OPT_IS_RAND_BH_SELECTION_DISABLED = 256

DS_NTDSSETTINGS_OPT_IS_REDUNDANT_SERVER_TOPOLOGY_ENABLED = 1024

DS_NTDSSETTINGS_OPT_IS_SCHEDULE_HASHING_ENABLED = 512

DS_NTDSSETTINGS_OPT_IS_TOPL_CLEANUP_DISABLED = 2

DS_NTDSSETTINGS_OPT_IS_TOPL_DETECT_STALE_DISABLED = 8

DS_NTDSSETTINGS_OPT_IS_TOPL_MIN_HOPS_DISABLED = 4

ENC_ALL_TYPES = 31

ENC_CRC32 = 1

ENC_HMAC_SHA1_96_AES128 = 8
ENC_HMAC_SHA1_96_AES256 = 16

ENC_RC4_HMAC_MD5 = 4

ENC_RSA_MD5 = 2

GPLINK_OPT_DISABLE = 1
GPLINK_OPT_ENFORCE = 2

GPO_BLOCK_INHERITANCE = 1

GPO_FLAG_MACHINE_DISABLE = 2

GPO_FLAG_USER_DISABLE = 1

GPO_INHERIT = 0

GTYPE_DISTRIBUTION_DOMAIN_LOCAL_GROUP = 4

GTYPE_DISTRIBUTION_GLOBAL_GROUP = 2

GTYPE_DISTRIBUTION_UNIVERSAL_GROUP = 8

GTYPE_SECURITY_BUILTIN_LOCAL_GROUP = 2147483653

GTYPE_SECURITY_DOMAIN_LOCAL_GROUP = 2147483652

GTYPE_SECURITY_GLOBAL_GROUP = 2147483650

GTYPE_SECURITY_UNIVERSAL_GROUP = 2147483656

INSTANCE_TYPE_IS_NC_HEAD = 1

INSTANCE_TYPE_NC_ABOVE = 8
INSTANCE_TYPE_NC_COMING = 16
INSTANCE_TYPE_NC_GOING = 32

INSTANCE_TYPE_UNINSTANT = 2
INSTANCE_TYPE_WRITE = 4

NTDSCONN_KCC_GC_TOPOLOGY = 1

NTDSCONN_KCC_INTERSITE_GC_TOPOLOGY = 32

NTDSCONN_KCC_INTERSITE_TOPOLOGY = 64

NTDSCONN_KCC_MINIMIZE_HOPS_TOPOLOGY = 4

NTDSCONN_KCC_OSCILLATING_CONNECTION_TOPOLOGY = 16

NTDSCONN_KCC_REDUNDANT_SERVER_TOPOLOGY = 512

NTDSCONN_KCC_RING_TOPOLOGY = 2

NTDSCONN_KCC_SERVER_FAILOVER_TOPOLOGY = 128

NTDSCONN_KCC_SITE_FAILOVER_TOPOLOGY = 256

NTDSCONN_KCC_STALE_SERVERS_TOPOLOGY = 8

NTDSCONN_OPT_DISABLE_INTERSITE_COMPRESSION = 16

NTDSCONN_OPT_IS_GENERATED = 1

NTDSCONN_OPT_OVERRIDE_NOTIFY_DEFAULT = 4

NTDSCONN_OPT_RODC_TOPOLOGY = 64

NTDSCONN_OPT_TWOWAY_SYNC = 2

NTDSCONN_OPT_USER_OWNED_SCHEDULE = 32

NTDSCONN_OPT_USE_NOTIFY = 8

NTDSSITELINK_OPT_DISABLE_COMPRESSION = 4

NTDSSITELINK_OPT_TWOWAY_SYNC = 2

NTDSSITELINK_OPT_USE_NOTIFY = 1

SEARCH_FLAG_ANR = 4
SEARCH_FLAG_ATTINDEX = 1
SEARCH_FLAG_CONFIDENTIAL = 128
SEARCH_FLAG_COPY = 16
SEARCH_FLAG_NEVERVALUEAUDIT = 256
SEARCH_FLAG_PDNTATTINDEX = 2
SEARCH_FLAG_PRESERVEONDELETE = 8

SEARCH_FLAG_RODC_ATTRIBUTE = 512

SEARCH_FLAG_SUBTREEATTRINDEX = 64
SEARCH_FLAG_TUPLEINDEX = 32

SYSTEM_FLAG_ATTR_IS_RDN = 32

SYSTEM_FLAG_CONFIG_ALLOW_LIMITED_MOVE = 268435456

SYSTEM_FLAG_CONFIG_ALLOW_MOVE = 536870912
SYSTEM_FLAG_CONFIG_ALLOW_RENAME = 1073741824

SYSTEM_FLAG_CR_NTDS_DOMAIN = 2
SYSTEM_FLAG_CR_NTDS_NC = 1

SYSTEM_FLAG_CR_NTDS_NOT_GC_REPLICATED = 4

SYSTEM_FLAG_DISALLOW_DELETE = 2147483648

SYSTEM_FLAG_DISALLOW_MOVE_ON_DELETE = 33554432

SYSTEM_FLAG_DOMAIN_DISALLOW_MOVE = 67108864
SYSTEM_FLAG_DOMAIN_DISALLOW_RENAME = 134217728

SYSTEM_FLAG_SCHEMA_BASE_OBJECT = 16

UF_00000004 = 4
UF_00000400 = 1024
UF_00004000 = 16384
UF_00008000 = 32768
UF_ACCOUNTDISABLE = 2

UF_DONT_EXPIRE_PASSWD = 65536

UF_DONT_REQUIRE_PREAUTH = 4194304

UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED = 128

UF_HOMEDIR_REQUIRED = 8

UF_INTERDOMAIN_TRUST_ACCOUNT = 2048

UF_LOCKOUT = 16

UF_MNS_LOGON_ACCOUNT = 131072

UF_NORMAL_ACCOUNT = 512

UF_NOT_DELEGATED = 1048576

UF_NO_AUTH_DATA_REQUIRED = 33554432

UF_PARTIAL_SECRETS_ACCOUNT = 67108864

UF_PASSWD_CANT_CHANGE = 64

UF_PASSWD_NOTREQD = 32

UF_PASSWORD_EXPIRED = 8388608

UF_SCRIPT = 1

UF_SERVER_TRUST_ACCOUNT = 8192

UF_SMARTCARD_REQUIRED = 262144

UF_TEMP_DUPLICATE_ACCOUNT = 256

UF_TRUSTED_FOR_DELEGATION = 524288

UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION = 16777216

UF_USE_DES_KEY_ONLY = 2097152

UF_WORKSTATION_TRUST_ACCOUNT = 4096

# functions

def _am_pdc(*args, **kwargs): # real signature unknown
    pass

def _am_rodc(*args, **kwargs): # real signature unknown
    pass

def _dsdb_convert_schema_to_openldap(*args, **kwargs): # real signature unknown
    """
    dsdb_convert_schema_to_openldap(ldb, target_str, mapping) -> str
    Create an OpenLDAP schema from a schema.
    """
    pass

def _dsdb_DsReplicaAttribute(*args, **kwargs): # real signature unknown
    pass

def _dsdb_get_attid_from_lDAPDisplayName(*args, **kwargs): # real signature unknown
    pass

def _dsdb_get_backlink_from_lDAPDisplayName(*args, **kwargs): # real signature unknown
    pass

def _dsdb_get_lDAPDisplayName_by_attid(*args, **kwargs): # real signature unknown
    pass

def _dsdb_get_linkId_from_lDAPDisplayName(*args, **kwargs): # real signature unknown
    pass

def _dsdb_get_nc_root(*args, **kwargs): # real signature unknown
    pass

def _dsdb_get_oid_from_attid(*args, **kwargs): # real signature unknown
    pass

def _dsdb_get_partitions_dn(*args, **kwargs): # real signature unknown
    pass

def _dsdb_get_syntax_oid_from_lDAPDisplayName(*args, **kwargs): # real signature unknown
    pass

def _dsdb_get_systemFlags_from_lDAPDisplayName(*args, **kwargs): # real signature unknown
    pass

def _dsdb_get_wellknown_dn(*args, **kwargs): # real signature unknown
    pass

def _dsdb_load_partition_usn(*args, **kwargs): # real signature unknown
    """ get uSNHighest and uSNUrgent from the partition @REPLCHANGED """
    pass

def _dsdb_normalise_attributes(*args, **kwargs): # real signature unknown
    pass

def _dsdb_set_am_rodc(*args, **kwargs): # real signature unknown
    pass

def _dsdb_set_global_schema(*args, **kwargs): # real signature unknown
    pass

def _dsdb_set_ntds_invocation_id(*args, **kwargs): # real signature unknown
    pass

def _dsdb_set_schema_from_ldb(*args, **kwargs): # real signature unknown
    pass

def _dsdb_set_schema_from_ldif(*args, **kwargs): # real signature unknown
    pass

def _dsdb_write_prefixes_from_schema_to_ldb(*args, **kwargs): # real signature unknown
    pass

def _samdb_get_domain_sid(*args, **kwargs): # real signature unknown
    """
    samdb_get_domain_sid(samdb)
    Get SID of domain in use.
    """
    pass

def _samdb_ntds_invocation_id(*args, **kwargs): # real signature unknown
    """ get the NTDS invocation ID GUID as a string """
    pass

def _samdb_ntds_objectGUID(*args, **kwargs): # real signature unknown
    """ get the NTDS objectGUID as a string """
    pass

def _samdb_server_site_name(*args, **kwargs): # real signature unknown
    """ Get the server site name as a string """
    pass

def _samdb_set_domain_sid(*args, **kwargs): # real signature unknown
    """
    samdb_set_domain_sid(samdb, sid)
    Set SID of domain to use.
    """
    pass

def _samdb_set_ntds_settings_dn(*args, **kwargs): # real signature unknown
    """
    samdb_set_ntds_settings_dn(samdb, ntds_settings_dn)
    Set NTDS Settings DN for this LDB (allows it to be set before the DB fully exists).
    """
    pass

# no classes
