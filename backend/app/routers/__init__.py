"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import aircraft as router_aircraft
from app.routers import ad as router_ad
from app.routers import timeditem as router_timeditem
from app.routers import linemaint as router_linemaint
from app.routers import checkpack as router_checkpack
from app.routers import card as router_card
from app.routers import material as router_material
from app.routers import license as router_license
from app.routers import record as router_record
from app.routers import defecthold as router_defecthold
from app.routers import release as router_release
from app.routers import enginetest as router_enginetest
from app.routers import ndt as router_ndt
from app.routers import cabin as router_cabin
from app.routers import borescope as router_borescope
from app.routers import gear as router_gear
from app.routers import error as router_error
from app.routers import org as router_org

ROUTERS = [router_aircraft, router_ad, router_timeditem, router_linemaint, router_checkpack, router_card, router_material, router_license, router_record, router_defecthold, router_release, router_enginetest, router_ndt, router_cabin, router_borescope, router_gear, router_error, router_org]
