# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SmartCard-Audit
GUID : 09ac07b9-6ac9-43bc-a50f-58419a797c69
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("09ac07b9-6ac9-43bc-a50f-58419a797c69"), event_id=100, version=0)
class Microsoft_Windows_SmartCard_Audit_100_0(Etw):
    pattern = Struct(
        "Process" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("09ac07b9-6ac9-43bc-a50f-58419a797c69"), event_id=101, version=0)
class Microsoft_Windows_SmartCard_Audit_101_0(Etw):
    pattern = Struct(
        "Process" / WString,
        "ProcessId" / Int32ul
    )

