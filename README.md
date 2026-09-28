# 民航机务航线维护平台

面向航空器适航状态、时控项目到期、定检工作包编排、维修放行签署与维修差错整改的一体化机务维修后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 航空器 | `aircraft` | 航空器 | 机号、机型、发动机型号 |
| 适航指令 | `ad` | 适航指令 | 指令编号、适用机型、指令来源 |
| 时控项目 | `timeditem` | 时控项目 | 项目编号、适用机型、项目名称 |
| 航线维护 | `linemaint` | 航线维护单 | 维护单号、机号、维护类别 |
| 定检工作包 | `checkpack` | 定检工作包 | 工作包编号、机号、定检级别 |
| 维修工卡 | `card` | 维修工卡 | 工卡编号、关联工作包、工卡名称 |
| 航材领用 | `material` | 航材领用单 | 领用单号、航材件号、航材名称 |
| 维修人员执照 | `license` | 维修人员执照 | 人员编号、人员姓名、执照类别 |
| 维修记录 | `record` | 维修记录 | 记录编号、关联工卡、机号 |
| 缺陷保留 | `defecthold` | 缺陷保留单 | 保留编号、机号、缺陷描述 |
| 放行签署 | `release` | 放行签署单 | 放行单号、机号、放行类别 |
| 试车检查 | `enginetest` | 试车检查单 | 试车编号、机号、发动机序号 |
| 无损探伤 | `ndt` | 无损探伤单 | 探伤编号、机号、探伤部位 |
| 客舱维护 | `cabin` | 客舱维护单 | 维护单号、机号、客舱区域 |
| 发动机孔探 | `borescope` | 发动机孔探单 | 孔探编号、机号、发动机序号 |
| 起落架维护 | `gear` | 起落架维护单 | 维护编号、机号、起落架位置 |
| 维修差错 | `error` | 维修差错单 | 差错编号、机号、差错类型 |
| 维修单位资质 | `org` | 维修单位资质 | 单位编号、单位名称、许可证号 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
