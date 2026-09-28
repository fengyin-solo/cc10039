"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class AircraftEntry(BaseModel):
    """航空器明细结构。"""

    field_0: str | None = None  # 机号
    field_1: str | None = None  # 机型
    field_2: str | None = None  # 发动机型号
    field_3: str | None = None  # 总飞行小时
    field_4: str | None = None  # 总起落循环
    field_5: str | None = None  # 所属基地
    field_6: str | None = None  # 引进日期
    field_7: str | None = None  # 航空器状态

class AdEntry(BaseModel):
    """适航指令明细结构。"""

    field_0: str | None = None  # 指令编号
    field_1: str | None = None  # 适用机型
    field_2: str | None = None  # 指令来源
    field_3: str | None = None  # 执行要求
    field_4: str | None = None  # 截止日期
    field_5: str | None = None  # 责任工段
    field_6: str | None = None  # 执行说明
    field_7: str | None = None  # 指令状态

class TimeditemEntry(BaseModel):
    """时控项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 适用机型
    field_2: str | None = None  # 项目名称
    field_3: str | None = None  # 间隔小时
    field_4: str | None = None  # 间隔日历日
    field_5: str | None = None  # 上次执行日
    field_6: str | None = None  # 下次到期日
    field_7: str | None = None  # 项目状态

class LinemaintEntry(BaseModel):
    """航线维护单明细结构。"""

    field_0: str | None = None  # 维护单号
    field_1: str | None = None  # 机号
    field_2: str | None = None  # 维护类别
    field_3: str | None = None  # 执行工段
    field_4: str | None = None  # 放行人员
    field_5: str | None = None  # 执行日期
    field_6: str | None = None  # 发现问题数
    field_7: str | None = None  # 维护状态

class CheckpackEntry(BaseModel):
    """定检工作包明细结构。"""

    field_0: str | None = None  # 工作包编号
    field_1: str | None = None  # 机号
    field_2: str | None = None  # 定检级别
    field_3: str | None = None  # 包含工卡数
    field_4: str | None = None  # 计划开始日
    field_5: str | None = None  # 计划工时
    field_6: str | None = None  # 责任工段
    field_7: str | None = None  # 工作包状态

class CardEntry(BaseModel):
    """维修工卡明细结构。"""

    field_0: str | None = None  # 工卡编号
    field_1: str | None = None  # 关联工作包
    field_2: str | None = None  # 工卡名称
    field_3: str | None = None  # 工序步骤数
    field_4: str | None = None  # 标准工时
    field_5: str | None = None  # 执行人
    field_6: str | None = None  # 执行日期
    field_7: str | None = None  # 工卡状态

class MaterialEntry(BaseModel):
    """航材领用单明细结构。"""

    field_0: str | None = None  # 领用单号
    field_1: str | None = None  # 航材件号
    field_2: str | None = None  # 航材名称
    field_3: str | None = None  # 领用数量
    field_4: str | None = None  # 适用机型
    field_5: str | None = None  # 领用工段
    field_6: str | None = None  # 领用日期
    field_7: str | None = None  # 领用状态

class LicenseEntry(BaseModel):
    """维修人员执照明细结构。"""

    field_0: str | None = None  # 人员编号
    field_1: str | None = None  # 人员姓名
    field_2: str | None = None  # 执照类别
    field_3: str | None = None  # 机型签署
    field_4: str | None = None  # 发证机构
    field_5: str | None = None  # 有效期至
    field_6: str | None = None  # 所属工段
    field_7: str | None = None  # 执照状态

class RecordEntry(BaseModel):
    """维修记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 关联工卡
    field_2: str | None = None  # 机号
    field_3: str | None = None  # 维修项目
    field_4: str | None = None  # 执行人
    field_5: str | None = None  # 完成日期
    field_6: str | None = None  # 签署人
    field_7: str | None = None  # 记录状态

class DefectholdEntry(BaseModel):
    """缺陷保留单明细结构。"""

    field_0: str | None = None  # 保留编号
    field_1: str | None = None  # 机号
    field_2: str | None = None  # 缺陷描述
    field_3: str | None = None  # 保留类别
    field_4: str | None = None  # 放行限制
    field_5: str | None = None  # 批准人
    field_6: str | None = None  # 复查期限
    field_7: str | None = None  # 保留状态

class ReleaseEntry(BaseModel):
    """放行签署单明细结构。"""

    field_0: str | None = None  # 放行单号
    field_1: str | None = None  # 机号
    field_2: str | None = None  # 放行类别
    field_3: str | None = None  # 放行人员
    field_4: str | None = None  # 执照编号
    field_5: str | None = None  # 签署时间
    field_6: str | None = None  # 限制条件
    field_7: str | None = None  # 放行状态

class EnginetestEntry(BaseModel):
    """试车检查单明细结构。"""

    field_0: str | None = None  # 试车编号
    field_1: str | None = None  # 机号
    field_2: str | None = None  # 发动机序号
    field_3: str | None = None  # 试车项目
    field_4: str | None = None  # 推力参数
    field_5: str | None = None  # 试车员
    field_6: str | None = None  # 试车日期
    field_7: str | None = None  # 试车状态

class NdtEntry(BaseModel):
    """无损探伤单明细结构。"""

    field_0: str | None = None  # 探伤编号
    field_1: str | None = None  # 机号
    field_2: str | None = None  # 探伤部位
    field_3: str | None = None  # 探伤方法
    field_4: str | None = None  # 探伤标准
    field_5: str | None = None  # 探伤人员
    field_6: str | None = None  # 探伤日期
    field_7: str | None = None  # 探伤状态

class CabinEntry(BaseModel):
    """客舱维护单明细结构。"""

    field_0: str | None = None  # 维护单号
    field_1: str | None = None  # 机号
    field_2: str | None = None  # 客舱区域
    field_3: str | None = None  # 座椅数量
    field_4: str | None = None  # 维护项目
    field_5: str | None = None  # 执行班组
    field_6: str | None = None  # 执行日期
    field_7: str | None = None  # 客舱状态

class BorescopeEntry(BaseModel):
    """发动机孔探单明细结构。"""

    field_0: str | None = None  # 孔探编号
    field_1: str | None = None  # 机号
    field_2: str | None = None  # 发动机序号
    field_3: str | None = None  # 孔探级别
    field_4: str | None = None  # 检查部位
    field_5: str | None = None  # 孔探人员
    field_6: str | None = None  # 孔探日期
    field_7: str | None = None  # 孔探状态

class GearEntry(BaseModel):
    """起落架维护单明细结构。"""

    field_0: str | None = None  # 维护编号
    field_1: str | None = None  # 机号
    field_2: str | None = None  # 起落架位置
    field_3: str | None = None  # 检查项目
    field_4: str | None = None  # 轮胎磨损量
    field_5: str | None = None  # 刹车片厚度
    field_6: str | None = None  # 执行人
    field_7: str | None = None  # 维护状态

class ErrorEntry(BaseModel):
    """维修差错单明细结构。"""

    field_0: str | None = None  # 差错编号
    field_1: str | None = None  # 机号
    field_2: str | None = None  # 差错类型
    field_3: str | None = None  # 差错等级
    field_4: str | None = None  # 发生日期
    field_5: str | None = None  # 责任工段
    field_6: str | None = None  # 整改措施
    field_7: str | None = None  # 差错状态

class OrgEntry(BaseModel):
    """维修单位资质明细结构。"""

    field_0: str | None = None  # 单位编号
    field_1: str | None = None  # 单位名称
    field_2: str | None = None  # 许可证号
    field_3: str | None = None  # 许可项目
    field_4: str | None = None  # 机型能力
    field_5: str | None = None  # 有效期至
    field_6: str | None = None  # 审核日期
    field_7: str | None = None  # 资质状态
