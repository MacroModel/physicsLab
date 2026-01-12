# 通过`physicsLab`使用物实网络API

## class User

`User`类是对一个真实的物实用户的封装

* 匿名用户登录:

```python
from physicsLab import web
user = web.anonymous_login()
```

* 通过邮箱密码登录:

```python
from physicsLab import web
user = web.email_login(YOUR_EMAIL, YOUR_PASSWORD)
```

* 通过`Token`, `AuthCode`登录:

```python
from physicsLab import *
user = web.token_login(
    token=YOUR_TOKEN,
    auth_code=YOUR_AUTH_CODE,
)
```

一个`User`的对象有以下属性:

* is_binded: 该账号是否绑定了邮箱或第三方关联账号
* user_id: 用户id
* gold: 金币
* level: 等级
* device_id: 硬件指纹
* avatar_region
* decoration
* nickname: 用户昵称
* signature: 用户签名
* avatar: 当前头像的索引
* avatar_region
* decoration
* verification
~~为什么有些属性没写是什么意思呢? 因为我也不知道()~~

`User`类也提供了一些方法, 这些方法是对物实网络api的封装:
> 注: 以`async_`开头的方法为协程风格的api

详见[user-method.md](./docsgen/user-method.md)

## 上传实验（.sav -> 物实）

发布/更新实验的高层接口在 `Experiment.upload()` / `Experiment.update()`（见 `docs/experiment.md`），它们内部会调用 WebAPI（`/Contents/SubmitExperiment`、`/Contents/ConfirmExperiment` 等）。

下面示例把本地 `.sav` 存档通过网络发布到物实（需要非匿名账号）：

```python
from physicsLab import Category, Experiment, OpenMode, web

user = web.email_login(YOUR_EMAIL, YOUR_PASSWORD)
intro = open("docs/rv32i_intro.md", "r", encoding="utf-8").read().strip()

with Experiment(OpenMode.load_by_filepath, "riscv_pe_to_pl.sav") as expe:
    expe.edit_publish_info(title="RV32I", introduction=intro)
    expe.upload(user, Category.Experiment)
```

如果你不想把密码写进代码，推荐用 `token_login()` 或在终端用环境变量传入（例如 `PL_EMAIL` / `PL_PASSWORD`）。

本仓库也提供了一个命令行脚本：`cmd/upload_experiment.py`（会从环境变量读取登录信息，不足时再交互输入密码）。

常用命令：

```bash
# 查看 .sav 是否已发布（Summary.ID 是否存在）
.venv/bin/python cmd/upload_experiment.py inspect --sav riscv_pe_to_pl.sav

# 按 RV32I 预设发布（标题 RV32I，简介读取 docs/rv32i_intro.md）
export PL_EMAIL="your@email.com"
.venv/bin/python cmd/upload_experiment.py publish-rv32i --sav riscv_pe_to_pl.sav

# 只演练（不发起任何网络请求）
.venv/bin/python cmd/upload_experiment.py publish-rv32i --dry-run --sav riscv_pe_to_pl.sav
```
