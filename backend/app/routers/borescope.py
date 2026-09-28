"""发动机孔探接口：维护发动机孔探单，覆盖提交孔探、判定正常、登记损伤等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.borescope import BorescopeService

router = APIRouter(prefix="/api/borescope", tags=["发动机孔探"])

service = BorescopeService()

LIST_FIELDS = ["孔探编号", "机号", "发动机序号", "孔探级别", "检查部位", "孔探人员", "孔探日期", "孔探状态"]
STATUSES = ["待孔探", "孔探中", "结论正常", "发现损伤"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按孔探编号检索"),
    status: str | None = Query(default=None, description="待孔探、孔探中、结论正常、发现损伤"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按孔探编号与状态过滤发动机孔探列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条发动机孔探单明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"发动机孔探单 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条发动机孔探单，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="发动机孔探单已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条发动机孔探单执行提交孔探、判定正常、登记损伤；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出发动机孔探清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "borescope", "total": total, "items": items}
