# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.135
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


# Variables with simple values

DRSUAPI_ATTID_accountExpires = 589983
DRSUAPI_ATTID_adminDescription = 131298
DRSUAPI_ATTID_adminDisplayName = 131266
DRSUAPI_ATTID_attributeID = 131102
DRSUAPI_ATTID_attributeSyntax = 131104
DRSUAPI_ATTID_auxiliaryClass = 131423
DRSUAPI_ATTID_badPwdCount = 589836
DRSUAPI_ATTID_cn = 3
DRSUAPI_ATTID_codePage = 589840
DRSUAPI_ATTID_comment = 589980
DRSUAPI_ATTID_countryCode = 589849
DRSUAPI_ATTID_currentValue = 589851
DRSUAPI_ATTID_dBCSPwd = 589879
DRSUAPI_ATTID_description = 13
DRSUAPI_ATTID_displayName = 131085
DRSUAPI_ATTID_dMDLocation = 131108
DRSUAPI_ATTID_dNSHostName = 590443
DRSUAPI_ATTID_fSMORoleOwner = 590193
DRSUAPI_ATTID_governsID = 131094
DRSUAPI_ATTID_gPLink = 590715
DRSUAPI_ATTID_groupType = 590574
DRSUAPI_ATTID_hasMasterNCs = 131086
DRSUAPI_ATTID_homeDirectory = 589868
DRSUAPI_ATTID_homeDrive = 589869
DRSUAPI_ATTID_initialAuthIncoming = 590363
DRSUAPI_ATTID_initialAuthOutgoing = 590364
DRSUAPI_ATTID_instanceType = 131073
DRSUAPI_ATTID_INVALID = -1
DRSUAPI_ATTID_invocationId = 131187
DRSUAPI_ATTID_isDeleted = 131120
DRSUAPI_ATTID_isMemberOfPartialAttributeSet = 590463
DRSUAPI_ATTID_isRecycled = 591882
DRSUAPI_ATTID_isSingleValued = 131105
DRSUAPI_ATTID_lastKnownParent = 590605
DRSUAPI_ATTID_lastLogoff = 589875
DRSUAPI_ATTID_lastLogon = 589876
DRSUAPI_ATTID_lDAPDisplayName = 131532
DRSUAPI_ATTID_lmPwdHistory = 589984
DRSUAPI_ATTID_logonCount = 589993
DRSUAPI_ATTID_logonHours = 589888
DRSUAPI_ATTID_mayContain = 131097
DRSUAPI_ATTID_member = 31

DRSUAPI_ATTID_msDS_Behavior_Version = 591283

DRSUAPI_ATTID_msDS_HasDomainNCs = 591644
DRSUAPI_ATTID_msDS_hasMasterNCs = 591660
DRSUAPI_ATTID_msDS_KeyVersionNumber = 591606

DRSUAPI_ATTID_mustContain = 131096
DRSUAPI_ATTID_name = 589825
DRSUAPI_ATTID_nCName = 131088
DRSUAPI_ATTID_ntPwdHistory = 589918
DRSUAPI_ATTID_ntSecurityDescriptor = 131353
DRSUAPI_ATTID_objectCategory = 590606
DRSUAPI_ATTID_objectClass = 0
DRSUAPI_ATTID_objectSid = 589970
DRSUAPI_ATTID_objectVersion = 131148
DRSUAPI_ATTID_oMSyntax = 131303
DRSUAPI_ATTID_options = 590131
DRSUAPI_ATTID_ou = 11
DRSUAPI_ATTID_possSuperiors = 131080
DRSUAPI_ATTID_primaryGroupID = 589922
DRSUAPI_ATTID_priorValue = 589924
DRSUAPI_ATTID_profilePath = 589963
DRSUAPI_ATTID_pwdLastSet = 589920
DRSUAPI_ATTID_rangeLower = 131106
DRSUAPI_ATTID_rangeUpper = 131107
DRSUAPI_ATTID_rDNAttId = 131098
DRSUAPI_ATTID_sAMAccountName = 590045
DRSUAPI_ATTID_sAMAccountType = 590126
DRSUAPI_ATTID_schemaIDGUID = 589972
DRSUAPI_ATTID_scriptPath = 589886
DRSUAPI_ATTID_searchFlags = 131406
DRSUAPI_ATTID_serverReference = 590339
DRSUAPI_ATTID_serverReferenceBL = 590340
DRSUAPI_ATTID_servicePrincipalName = 590595
DRSUAPI_ATTID_showInAdvancedViewOnly = 131241
DRSUAPI_ATTID_subClassOf = 131093
DRSUAPI_ATTID_supplementalCredentials = 589949
DRSUAPI_ATTID_systemAuxiliaryClass = 590022
DRSUAPI_ATTID_systemFlags = 590199
DRSUAPI_ATTID_systemMayContain = 590020
DRSUAPI_ATTID_systemMustContain = 590021
DRSUAPI_ATTID_systemPossSuperiors = 590019
DRSUAPI_ATTID_transportAddressAttribute = 590719
DRSUAPI_ATTID_trustAuthIncoming = 589953
DRSUAPI_ATTID_trustAuthOutgoing = 589959
DRSUAPI_ATTID_unicodePwd = 589914
DRSUAPI_ATTID_userAccountControl = 589832
DRSUAPI_ATTID_userParameters = 589962
DRSUAPI_ATTID_userPrincipalName = 590480
DRSUAPI_ATTID_userWorkstations = 589910
DRSUAPI_ATTID_wellKnownObjects = 590442
DRSUAPI_ATTID_whenCreated = 131074

DRSUAPI_CH_REFTYPE_CROSS = 3
DRSUAPI_CH_REFTYPE_NSSR = 2
DRSUAPI_CH_REFTYPE_SUBORDINATE = 1
DRSUAPI_CH_REFTYPE_SUPERIOR = 0

DRSUAPI_COMPRESSION_TYPE_MSZIP = 2
DRSUAPI_COMPRESSION_TYPE_XPRESS = 3

DRSUAPI_DC_CONNECTION_CTR_01 = -1

DRSUAPI_DC_INFO_CTR_1 = 1
DRSUAPI_DC_INFO_CTR_2 = 2
DRSUAPI_DC_INFO_CTR_3 = 3

DRSUAPI_DIRERR_ATTRIBUTE = 1
DRSUAPI_DIRERR_NAME = 2
DRSUAPI_DIRERR_OK = 0
DRSUAPI_DIRERR_REFERRAL = 3
DRSUAPI_DIRERR_SECURITY = 4
DRSUAPI_DIRERR_SERVICE = 5
DRSUAPI_DIRERR_SYSTEM = 7
DRSUAPI_DIRERR_UPDATE = 6

DRSUAPI_DRS_ADD_REF = 4

DRSUAPI_DRS_ASYNC_OP = 1
DRSUAPI_DRS_ASYNC_REP = 256

DRSUAPI_DRS_CRITICAL_ONLY = 1024

DRSUAPI_DRS_DEL_REF = 8

DRSUAPI_DRS_DISABLE_AUTO_SYNC = 67108864

DRSUAPI_DRS_DISABLE_PERIODIC_SYNC = 134217728

DRSUAPI_DRS_FULL_SYNC_IN_PROGRESS = 65536

DRSUAPI_DRS_FULL_SYNC_NOW = 32768
DRSUAPI_DRS_FULL_SYNC_PACKET = 131072

DRSUAPI_DRS_GETCHG_CHECK = 2

DRSUAPI_DRS_GET_ALL_GROUP_MEMBERSHIP = 2147483648

DRSUAPI_DRS_GET_ANC = 2048

DRSUAPI_DRS_GET_NC_SIZE = 4096

DRSUAPI_DRS_IGNORE_ERROR = 256

DRSUAPI_DRS_INIT_SYNC = 32

DRSUAPI_DRS_INIT_SYNC_NOW = 8388608

DRSUAPI_DRS_LOCAL_ONLY = 4096

DRSUAPI_DRS_MAIL_REP = 128

DRSUAPI_DRS_NEVER_NOTIFY = 536870912
DRSUAPI_DRS_NEVER_SYNCED = 2097152

DRSUAPI_DRS_NONGC_RO_REP = 8192

DRSUAPI_DRS_NO_DISCARD = 1048576
DRSUAPI_DRS_NO_SOURCE = 32768

DRSUAPI_DRS_PER_SYNC = 64

DRSUAPI_DRS_PREEMPTED = 16777216

DRSUAPI_DRS_REF_GCSPN = 1048576
DRSUAPI_DRS_REF_OK = 16384

DRSUAPI_DRS_SPECIAL_SECRET_PROCESSING = 4194304

DRSUAPI_DRS_SYNC_ALL = 8
DRSUAPI_DRS_SYNC_BYNAME = 16384
DRSUAPI_DRS_SYNC_FORCED = 33554432
DRSUAPI_DRS_SYNC_PAS = 1073741824
DRSUAPI_DRS_SYNC_REQUEUE = 262144
DRSUAPI_DRS_SYNC_URGENT = 524288

DRSUAPI_DRS_TWOWAY_SYNC = 512

DRSUAPI_DRS_UPDATE_ADDRESS = 2
DRSUAPI_DRS_UPDATE_FLAGS = 1
DRSUAPI_DRS_UPDATE_NOTIFICATION = 2
DRSUAPI_DRS_UPDATE_SCHEDULE = 4

DRSUAPI_DRS_USE_COMPRESSION = 268435456

DRSUAPI_DRS_WRIT_REP = 16

DRSUAPI_DS_BIND_GUID = 'e24d201a-4fd6-11d1-a3da-0000f875ae0d'

DRSUAPI_DS_BIND_GUID_W2K = '6abec3d1-3054-41c8-a362-5a0c5b7d5d71'
DRSUAPI_DS_BIND_GUID_W2K3 = '6afab99c-6e26-464a-975f-f58f105218bc'

DRSUAPI_DS_EXECUTE_KCC_ASYNCHRONOUS_OPERATION = 1

DRSUAPI_DS_EXECUTE_KCC_DAMPED = 2

DRSUAPI_DS_LINKED_ATTRIBUTE_FLAG_ACTIVE = 1

DRSUAPI_DS_MEMBERSHIP_FLAG_GROUP_ATTR = 1

DRSUAPI_DS_MEMBERSHIP_TYPE_DOMAIN_GROUPS = 3
DRSUAPI_DS_MEMBERSHIP_TYPE_DOMAIN_GROUPS2 = 7

DRSUAPI_DS_MEMBERSHIP_TYPE_DOMAIN_LOCAL_GROUPS = 2
DRSUAPI_DS_MEMBERSHIP_TYPE_DOMAIN_LOCAL_GROUPS2 = 4

DRSUAPI_DS_MEMBERSHIP_TYPE_GROUPMEMBERS = 6

DRSUAPI_DS_MEMBERSHIP_TYPE_UNIVERSAL_AND_DOMAIN_GROUPS = 1

DRSUAPI_DS_MEMBERSHIP_TYPE_UNIVERSAL_GROUPS = 5

DRSUAPI_DS_NAME_FLAG_EVAL_AT_DC = 2

DRSUAPI_DS_NAME_FLAG_GCVERIFY = 4

DRSUAPI_DS_NAME_FLAG_NO_FLAGS = 0

DRSUAPI_DS_NAME_FLAG_SYNTACTICAL_ONLY = 1

DRSUAPI_DS_NAME_FLAG_TRUST_REFERRAL = 8

DRSUAPI_DS_NAME_FORMAT_ALT_SECURITY_IDENTITIES_NAME = -11

DRSUAPI_DS_NAME_FORMAT_CANONICAL = 7

DRSUAPI_DS_NAME_FORMAT_CANONICAL_EX = 9

DRSUAPI_DS_NAME_FORMAT_DISPLAY = 3

DRSUAPI_DS_NAME_FORMAT_DNS_DOMAIN = 12

DRSUAPI_DS_NAME_FORMAT_FQDN_1779 = 1

DRSUAPI_DS_NAME_FORMAT_GUID = 6

DRSUAPI_DS_NAME_FORMAT_LIST_DOMAINS = -9

DRSUAPI_DS_NAME_FORMAT_LIST_DOMAINS_IN_SITE = -3

DRSUAPI_DS_NAME_FORMAT_LIST_GLOBAL_CATALOG_SERVERS = -15

DRSUAPI_DS_NAME_FORMAT_LIST_INFO_FOR_SERVER = -5

DRSUAPI_DS_NAME_FORMAT_LIST_NCS = -10
DRSUAPI_DS_NAME_FORMAT_LIST_ROLES = -6

DRSUAPI_DS_NAME_FORMAT_LIST_SERVERS_FOR_DOMAIN_IN_SITE = -4

DRSUAPI_DS_NAME_FORMAT_LIST_SERVERS_IN_SITE = -2

DRSUAPI_DS_NAME_FORMAT_LIST_SERVERS_WITH_DCS_IN_SITE = -13

DRSUAPI_DS_NAME_FORMAT_LIST_SITES = -1

DRSUAPI_DS_NAME_FORMAT_MAP_SCHEMA_GUID = -8

DRSUAPI_DS_NAME_FORMAT_NT4_ACCOUNT = 2

DRSUAPI_DS_NAME_FORMAT_NT4_ACCOUNT_NAME_SANS_DOMAIN = -7

DRSUAPI_DS_NAME_FORMAT_NT4_ACCOUNT_NAME_SANS_DOMAIN_EX = -16

DRSUAPI_DS_NAME_FORMAT_SERVICE_PRINCIPAL = 10

DRSUAPI_DS_NAME_FORMAT_SID_OR_SID_HISTORY = 11

DRSUAPI_DS_NAME_FORMAT_STRING_SID_NAME = -12

DRSUAPI_DS_NAME_FORMAT_UNKNOWN = 0

DRSUAPI_DS_NAME_FORMAT_UPN_AND_ALTSECID = -17

DRSUAPI_DS_NAME_FORMAT_UPN_FOR_LOGON = -14

DRSUAPI_DS_NAME_FORMAT_USER_PRINCIPAL = 8

DRSUAPI_DS_NAME_STATUS_DOMAIN_ONLY = 5

DRSUAPI_DS_NAME_STATUS_NOT_FOUND = 2
DRSUAPI_DS_NAME_STATUS_NOT_UNIQUE = 3

DRSUAPI_DS_NAME_STATUS_NO_MAPPING = 4

DRSUAPI_DS_NAME_STATUS_NO_SYNTACTICAL_MAPPING = 6

DRSUAPI_DS_NAME_STATUS_OK = 0

DRSUAPI_DS_NAME_STATUS_RESOLVE_ERROR = 1

DRSUAPI_DS_NAME_STATUS_TRUST_REFERRAL = 7

DRSUAPI_DS_REPLICA_GET_INFO = 1
DRSUAPI_DS_REPLICA_GET_INFO2 = 2

DRSUAPI_DS_REPLICA_INFO_ATTRIBUTE_VALUE_METADATA = 6
DRSUAPI_DS_REPLICA_INFO_ATTRIBUTE_VALUE_METADATA2 = 10

DRSUAPI_DS_REPLICA_INFO_CLIENT_CONTEXTS = -4

DRSUAPI_DS_REPLICA_INFO_CURSORS = 1
DRSUAPI_DS_REPLICA_INFO_CURSORS2 = 7
DRSUAPI_DS_REPLICA_INFO_CURSORS3 = 8

DRSUAPI_DS_REPLICA_INFO_KCC_DSA_CONNECT_FAILURES = 3

DRSUAPI_DS_REPLICA_INFO_KCC_DSA_LINK_FAILURES = 4

DRSUAPI_DS_REPLICA_INFO_NEIGHBORS = 0

DRSUAPI_DS_REPLICA_INFO_OBJ_METADATA = 2
DRSUAPI_DS_REPLICA_INFO_OBJ_METADATA2 = 9

DRSUAPI_DS_REPLICA_INFO_PENDING_OPS = 5

DRSUAPI_DS_REPLICA_INFO_REPSTO = -2

DRSUAPI_DS_REPLICA_INFO_SERVER_OUTGOING_CALLS = -6

DRSUAPI_DS_REPLICA_INFO_UPTODATE_VECTOR_V1 = -5

DRSUAPI_DS_REPLICA_OBJECT_DYNAMIC = 2

DRSUAPI_DS_REPLICA_OBJECT_FROM_MASTER = 1

DRSUAPI_DS_REPLICA_OBJECT_REMOTE_MODIFY = 65536

DRSUAPI_DS_REPLICA_OP_TYPE_ADD = 1
DRSUAPI_DS_REPLICA_OP_TYPE_DELETE = 2
DRSUAPI_DS_REPLICA_OP_TYPE_MODIFY = 3
DRSUAPI_DS_REPLICA_OP_TYPE_SYNC = 0

DRSUAPI_DS_REPLICA_OP_TYPE_UPDATE_REFS = 4

DRSUAPI_DS_SPN_OPERATION_ADD = 0
DRSUAPI_DS_SPN_OPERATION_DELETE = 2
DRSUAPI_DS_SPN_OPERATION_REPLACE = 1

DRSUAPI_EXOP_ERR_ACCESS_DENIED = 15

DRSUAPI_EXOP_ERR_COULDNT_CONTACT = 11

DRSUAPI_EXOP_ERR_DIR_ERROR = 13

DRSUAPI_EXOP_ERR_EXCEPTION = 5

DRSUAPI_EXOP_ERR_FMSO_PENDING_OP = 9

DRSUAPI_EXOP_ERR_FSMO_MISSING_SETTINGS = 14

DRSUAPI_EXOP_ERR_FSMO_NOT_OWNER = 3

DRSUAPI_EXOP_ERR_FSMO_OWNER_DELETED = 8

DRSUAPI_EXOP_ERR_FSMO_REFUSING_ROLES = 12

DRSUAPI_EXOP_ERR_MISMATCH = 10
DRSUAPI_EXOP_ERR_NONE = 0

DRSUAPI_EXOP_ERR_PARAM_ERROR = 16

DRSUAPI_EXOP_ERR_RID_ALLOC = 7

DRSUAPI_EXOP_ERR_SUCCESS = 1

DRSUAPI_EXOP_ERR_UNKNOWN_CALLER = 6
DRSUAPI_EXOP_ERR_UNKNOWN_OP = 2

DRSUAPI_EXOP_ERR_UPDATE_ERR = 4

DRSUAPI_EXOP_FSMO_ABANDON_ROLE = 5

DRSUAPI_EXOP_FSMO_REQ_PDC = 4
DRSUAPI_EXOP_FSMO_REQ_ROLE = 1

DRSUAPI_EXOP_FSMO_RID_ALLOC = 2

DRSUAPI_EXOP_FSMO_RID_REQ_ROLE = 3

DRSUAPI_EXOP_NONE = 0

DRSUAPI_EXOP_REPL_OBJ = 6
DRSUAPI_EXOP_REPL_SECRET = 7

DRSUAPI_NT4_CHANGELOG_GET_CHANGELOG = 1

DRSUAPI_NT4_CHANGELOG_GET_SERIAL_NUMBERS = 2

DRSUAPI_NTDSDSA_KRB5_SERVICE_GUID = 'E3514235-4B06-11D1-AB04-00C04FC2DCD2'

DRSUAPI_OBJECTCLASS_attributeSchema = 196622
DRSUAPI_OBJECTCLASS_classSchema = 196621
DRSUAPI_OBJECTCLASS_top = 65536

DRSUAPI_SECBUFFER_DATA = 1
DRSUAPI_SECBUFFER_EMPTY = 0
DRSUAPI_SECBUFFER_EXTRA = 5
DRSUAPI_SECBUFFER_MISSING = 4

DRSUAPI_SECBUFFER_PKG_PARAMS = 3

DRSUAPI_SECBUFFER_READONLY = -2147483648

DRSUAPI_SECBUFFER_STREAM_HEADER = 7
DRSUAPI_SECBUFFER_STREAM_TRAILER = 6

DRSUAPI_SECBUFFER_TOKEN = 2

DRSUAPI_SE_CHOICE_BASE_ONLY = 0

DRSUAPI_SE_CHOICE_IMMED_CHLDRN = 1

DRSUAPI_SE_CHOICE_WHOLE_SUBTREE = 2

DRSUAPI_SUPPORTED_EXTENSION_ADAM = 1
DRSUAPI_SUPPORTED_EXTENSION_ADDENTRY = 128

DRSUAPI_SUPPORTED_EXTENSION_ADDENTRYREPLY_V3 = 134217728

DRSUAPI_SUPPORTED_EXTENSION_ADDENTRY_V2 = 512

DRSUAPI_SUPPORTED_EXTENSION_ADD_SID_HISTORY = 262144

DRSUAPI_SUPPORTED_EXTENSION_ASYNC_REPLICATION = 2

DRSUAPI_SUPPORTED_EXTENSION_BASE = 1

DRSUAPI_SUPPORTED_EXTENSION_CRYPTO_BIND = 8192

DRSUAPI_SUPPORTED_EXTENSION_DCINFO_V01 = 65536
DRSUAPI_SUPPORTED_EXTENSION_DCINFO_V1 = 32
DRSUAPI_SUPPORTED_EXTENSION_DCINFO_V2 = 2048

DRSUAPI_SUPPORTED_EXTENSION_GETCHGREPLY_V5 = 33554432
DRSUAPI_SUPPORTED_EXTENSION_GETCHGREPLY_V6 = 67108864
DRSUAPI_SUPPORTED_EXTENSION_GETCHGREPLY_V7 = 134217728

DRSUAPI_SUPPORTED_EXTENSION_GETCHGREQ_V10 = 536870912
DRSUAPI_SUPPORTED_EXTENSION_GETCHGREQ_V5 = 1048576
DRSUAPI_SUPPORTED_EXTENSION_GETCHGREQ_V6 = 4194304
DRSUAPI_SUPPORTED_EXTENSION_GETCHGREQ_V8 = 16777216

DRSUAPI_SUPPORTED_EXTENSION_GETCHG_COMPRESS = 16

DRSUAPI_SUPPORTED_EXTENSION_GET_MEMBERSHIPS2 = 2097152

DRSUAPI_SUPPORTED_EXTENSION_GET_REPL_INFO = 16384

DRSUAPI_SUPPORTED_EXTENSION_INSTANCE_TYPE_NOT_REQ_ON_MOD = 4096

DRSUAPI_SUPPORTED_EXTENSION_KCC_EXECUTE = 256

DRSUAPI_SUPPORTED_EXTENSION_LH_BETA2 = 2

DRSUAPI_SUPPORTED_EXTENSION_LINKED_VALUE_REPLICATION = 1024

DRSUAPI_SUPPORTED_EXTENSION_MOVEREQ_V2 = 8

DRSUAPI_SUPPORTED_EXTENSION_NONDOMAIN_NCS = 8388608

DRSUAPI_SUPPORTED_EXTENSION_POST_BETA3 = 524288

DRSUAPI_SUPPORTED_EXTENSION_RECYCLE_BIN = 4

DRSUAPI_SUPPORTED_EXTENSION_REMOVEAPI = 4

DRSUAPI_SUPPORTED_EXTENSION_RESERVED_PART2 = 1073741824
DRSUAPI_SUPPORTED_EXTENSION_RESERVED_PART3 = 2147483648

DRSUAPI_SUPPORTED_EXTENSION_RESTORE_USN_OPTIMIZATION = 64

DRSUAPI_SUPPORTED_EXTENSION_STRONG_ENCRYPTION = 32768

DRSUAPI_SUPPORTED_EXTENSION_TRANSITIVE_MEMBERSHIP = 131072

DRSUAPI_SUPPORTED_EXTENSION_VERIFY_OBJECT = 134217728

DRSUAPI_SUPPORTED_EXTENSION_XPRESS_COMPRESS = 268435456

# no functions
# classes

from drsuapi import drsuapi
from DsaAddressListItem_V1 import DsaAddressListItem_V1
from DsAddEntryCtr2 import DsAddEntryCtr2
from DsAddEntryCtr3 import DsAddEntryCtr3
from DsAddEntryErrorInfoX import DsAddEntryErrorInfoX
from DsAddEntryErrorInfo_Attr_V1 import DsAddEntryErrorInfo_Attr_V1
from DsAddEntryErrorInfo_Name_V1 import DsAddEntryErrorInfo_Name_V1
from DsAddEntryErrorInfo_Referr_V1 import DsAddEntryErrorInfo_Referr_V1
from DsAddEntryRequest2 import DsAddEntryRequest2
from DsAddEntryRequest3 import DsAddEntryRequest3
from DsAddEntry_AttrErrListItem_V1 import DsAddEntry_AttrErrListItem_V1
from DsAddEntry_AttrErr_V1 import DsAddEntry_AttrErr_V1
from DsAddEntry_ErrData_V1 import DsAddEntry_ErrData_V1
from DsAddEntry_RefErrListItem_V1 import DsAddEntry_RefErrListItem_V1
from DsAttributeValue import DsAttributeValue
from DsAttributeValueCtr import DsAttributeValueCtr
from DsBindInfo24 import DsBindInfo24
from DsBindInfo28 import DsBindInfo28
from DsBindInfo48 import DsBindInfo48
from DsBindInfoCtr import DsBindInfoCtr
from DsBindInfoFallBack import DsBindInfoFallBack
from DsExecuteKCC1 import DsExecuteKCC1
from DsGetDCConnection01 import DsGetDCConnection01
from DsGetDCConnectionCtr01 import DsGetDCConnectionCtr01
from DsGetDCInfo1 import DsGetDCInfo1
from DsGetDCInfo2 import DsGetDCInfo2
from DsGetDCInfo3 import DsGetDCInfo3
from DsGetDCInfoCtr1 import DsGetDCInfoCtr1
from DsGetDCInfoCtr2 import DsGetDCInfoCtr2
from DsGetDCInfoCtr3 import DsGetDCInfoCtr3
from DsGetDCInfoRequest1 import DsGetDCInfoRequest1
from DsGetMemberships2Ctr1 import DsGetMemberships2Ctr1
from DsGetMemberships2Request1 import DsGetMemberships2Request1
from DsGetMembershipsCtr1 import DsGetMembershipsCtr1
from DsGetMembershipsRequest1 import DsGetMembershipsRequest1
from DsGetNCChangesCtr1 import DsGetNCChangesCtr1
from DsGetNCChangesCtr1TS import DsGetNCChangesCtr1TS
from DsGetNCChangesCtr2 import DsGetNCChangesCtr2
from DsGetNCChangesCtr6 import DsGetNCChangesCtr6
from DsGetNCChangesCtr6TS import DsGetNCChangesCtr6TS
from DsGetNCChangesCtr7 import DsGetNCChangesCtr7
from DsGetNCChangesMSZIPCtr1 import DsGetNCChangesMSZIPCtr1
from DsGetNCChangesMSZIPCtr6 import DsGetNCChangesMSZIPCtr6
from DsGetNCChangesRequest10 import DsGetNCChangesRequest10
from DsGetNCChangesRequest5 import DsGetNCChangesRequest5
from DsGetNCChangesRequest8 import DsGetNCChangesRequest8
from DsGetNCChangesXPRESSCtr1 import DsGetNCChangesXPRESSCtr1
from DsGetNCChangesXPRESSCtr6 import DsGetNCChangesXPRESSCtr6
from DsGetNT4ChangeLogInfo1 import DsGetNT4ChangeLogInfo1
from DsGetNT4ChangeLogRequest1 import DsGetNT4ChangeLogRequest1
from DsNameCtr1 import DsNameCtr1
from DsNameInfo1 import DsNameInfo1
from DsNameRequest1 import DsNameRequest1
from DsNameString import DsNameString
from DsPartialAttributeSet import DsPartialAttributeSet
from DsRemoveDSServerRequest1 import DsRemoveDSServerRequest1
from DsRemoveDSServerResult1 import DsRemoveDSServerResult1
from DsReplica06 import DsReplica06
from DsReplica06Ctr import DsReplica06Ctr
from DsReplicaAddRequest1 import DsReplicaAddRequest1
from DsReplicaAddRequest2 import DsReplicaAddRequest2
from DsReplicaAttribute import DsReplicaAttribute
from DsReplicaAttributeCtr import DsReplicaAttributeCtr
from DsReplicaAttrValMetaData import DsReplicaAttrValMetaData
from DsReplicaAttrValMetaData2 import DsReplicaAttrValMetaData2
from DsReplicaAttrValMetaData2Ctr import DsReplicaAttrValMetaData2Ctr
from DsReplicaAttrValMetaDataCtr import DsReplicaAttrValMetaDataCtr
from DsReplicaConnection04 import DsReplicaConnection04
from DsReplicaConnection04Ctr import DsReplicaConnection04Ctr
from DsReplicaCursor import DsReplicaCursor
from DsReplicaCursor2 import DsReplicaCursor2
from DsReplicaCursor2Ctr import DsReplicaCursor2Ctr
from DsReplicaCursor2CtrEx import DsReplicaCursor2CtrEx
from DsReplicaCursor3 import DsReplicaCursor3
from DsReplicaCursor3Ctr import DsReplicaCursor3Ctr
from DsReplicaCursorCtr import DsReplicaCursorCtr
from DsReplicaCursorCtrEx import DsReplicaCursorCtrEx
from DsReplicaDelRequest1 import DsReplicaDelRequest1
from DsReplicaGetInfoRequest1 import DsReplicaGetInfoRequest1
from DsReplicaGetInfoRequest2 import DsReplicaGetInfoRequest2
from DsReplicaHighWaterMark import DsReplicaHighWaterMark
from DsReplicaKccDsaFailure import DsReplicaKccDsaFailure
from DsReplicaKccDsaFailuresCtr import DsReplicaKccDsaFailuresCtr
from DsReplicaLinkedAttribute import DsReplicaLinkedAttribute
from DsReplicaMetaData import DsReplicaMetaData
from DsReplicaMetaDataCtr import DsReplicaMetaDataCtr
from DsReplicaModRequest1 import DsReplicaModRequest1
from DsReplicaNeighbour import DsReplicaNeighbour
from DsReplicaNeighbourCtr import DsReplicaNeighbourCtr
from DsReplicaObject import DsReplicaObject
from DsReplicaObjectIdentifier import DsReplicaObjectIdentifier
from DsReplicaObjectIdentifier2 import DsReplicaObjectIdentifier2
from DsReplicaObjectIdentifier3 import DsReplicaObjectIdentifier3
from DsReplicaObjectIdentifier3Binary import DsReplicaObjectIdentifier3Binary
from DsReplicaObjectListItem import DsReplicaObjectListItem
from DsReplicaObjectListItemEx import DsReplicaObjectListItemEx
from DsReplicaObjMetaData import DsReplicaObjMetaData
from DsReplicaObjMetaData2 import DsReplicaObjMetaData2
from DsReplicaObjMetaData2Ctr import DsReplicaObjMetaData2Ctr
from DsReplicaObjMetaDataCtr import DsReplicaObjMetaDataCtr
from DsReplicaOID import DsReplicaOID
from DsReplicaOIDMapping import DsReplicaOIDMapping
from DsReplicaOIDMapping_Ctr import DsReplicaOIDMapping_Ctr
from DsReplicaOp import DsReplicaOp
from DsReplicaOpCtr import DsReplicaOpCtr
from DsReplicaSyncRequest1 import DsReplicaSyncRequest1
from DsReplicaUpdateRefsRequest1 import DsReplicaUpdateRefsRequest1
from DsSiteCostInfo import DsSiteCostInfo
from DsWriteAccountSpnRequest1 import DsWriteAccountSpnRequest1
from DsWriteAccountSpnResult1 import DsWriteAccountSpnResult1
from NameResOp_V1 import NameResOp_V1
from QuerySitesByCostCtr1 import QuerySitesByCostCtr1
from QuerySitesByCostRequest1 import QuerySitesByCostRequest1
from SecBuffer import SecBuffer
from SecBufferDesc import SecBufferDesc
