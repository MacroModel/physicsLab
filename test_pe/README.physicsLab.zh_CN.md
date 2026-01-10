# Phy-Engine（`physicsLab` 的可选电路计算后端）

本仓库以第三方方式引入（vendor / submodule）`Phy-Engine`，作为 `physicsLab` 的**可选**电路求解后端。`physicsLab` 通过 `ctypes` 调用其动态库（导出 C ABI），因此不会在 `import physicsLab` 时产生强制依赖。

## 通过 git submodule 克隆

如果你在克隆 `physicsLab`（父仓库）时已配置 `Phy-Engine` 为 submodule：

```bash
git clone --recurse-submodules <PHYSICSLAB_REPO_URL>
# 或者克隆后执行：
git submodule update --init --recursive
```

如果你要把 `Phy-Engine` 作为 submodule 添加到当前 `physicsLab` 工作区：

```bash
git submodule add https://github.com/MacroModel/Phy-Engine.git third-parties/Phy-Engine
git submodule update --init --recursive
```

## 在本机编译动态库（native）

`Phy-Engine` 的 C ABI 头文件位于 `include/phy_engine/dll_api.h`，动态库由 `src/dll_main.cpp` 构建生成。

### macOS / Linux

```bash
cmake -S third-parties/Phy-Engine/src -B third-parties/Phy-Engine/build -DCMAKE_BUILD_TYPE=Release
cmake --build third-parties/Phy-Engine/build -j
```

常见输出：
- macOS：`third-parties/Phy-Engine/build/libphyengine.dylib`
- Linux：`third-parties/Phy-Engine/build/libphyengine.so`

### Windows（MSVC）

```bat
cmake -S third-parties/Phy-Engine/src -B third-parties/Phy-Engine/build -G "Visual Studio 17 2022" -A x64
cmake --build third-parties/Phy-Engine/build --config Release
```

常见输出：
- `third-parties/Phy-Engine/build/Release/phyengine.dll`

## 安装运行时动态库（`physicsLab` 从哪里加载）

`physicsLab` 会按以下顺序查找 `Phy-Engine` 的动态库：

1) 环境变量 `PHYSICSLAB_PHYENGINE_LIB`（必须是动态库文件的**完整路径**）
2) `physicsLab/native/`（推荐）
3) 一些开发期默认路径（`third-parties/Phy-Engine/` 下的若干 build 目录）

推荐做法：将编译产物拷贝到 `physicsLab/native/`：

- macOS：拷贝 `libphyengine.dylib` 到 `physicsLab/native/libphyengine.dylib`
- Linux：拷贝 `libphyengine.so` 到 `physicsLab/native/libphyengine.so`
- Windows：拷贝 `phyengine.dll` 到 `physicsLab/native/phyengine.dll`

如果你希望放在其它位置，请设置环境变量：

```bash
export PHYSICSLAB_PHYENGINE_LIB=/full/path/to/libphyengine.dylib   # macOS
export PHYSICSLAB_PHYENGINE_LIB=/full/path/to/libphyengine.so      # Linux
setx PHYSICSLAB_PHYENGINE_LIB "C:\full\path\to\phyengine.dll"      # Windows
```

## 在 `physicsLab` 中调用

封装入口在 `physicsLab/circuit/phy_engine.py`，并通过 `physicsLab.circuit` 暴露。

```python
from physicsLab import Experiment, OpenMode, ExperimentType
from physicsLab.circuit import (
    Battery_Source,
    Resistor,
    Ground_Component,
    crt_wire,
    analyze_experiment_with_phy_engine,
)

with Experiment(OpenMode.crt, "phyengine-demo", ExperimentType.Circuit, force_crt=True) as ex:
    v = Battery_Source(0, 0, 0, voltage=5)
    r = Resistor(1, 0, 0, resistance=1000)
    g = Ground_Component(2, 0, 0)

    crt_wire(v.red, r.red)
    crt_wire(r.black, v.black)
    crt_wire(v.black, g.i)

    sample = analyze_experiment_with_phy_engine(ex, analyze_type="DC")
    print("Resistor 引脚电压：", sample.pin_voltage[r])
```

### 当前支持的元件（映射范围）

此后端目前只做了一个**小范围**的 `ModelID -> Phy-Engine element code` 映射；遇到未支持元件会抛出 `PhyEngineUnsupportedElementError`。

当前已支持的 `ModelID`（部分）：

- 模拟电路：`Resistor`、`Basic Capacitor`、`Basic Inductor`、`Battery Source`、`Simple Switch`、`Push Switch`、`Air Switch`、`Transformer`、`Mutual Inductor`、`Rectifier`、`Ground Component`
- 数字电路：`Logic Input`、`Logic Output`、`Yes Gate`、`No Gate`、`And Gate`、`Or Gate`、`Xor Gate`、`Xnor Gate`、`Nand Gate`、`Nor Gate`、`Imp Gate`、`Nimp Gate`、`Half Adder`、`Full Adder`、`Half Subtractor`、`Full Subtractor`、`Multiplier`、`D Flipflop`、`T Flipflop`、`Real-T Flipflop`、`JK Flipflop`

注意：
- `Battery Source` 的“内阻”目前不会自动建模；需要时请显式添加一个 `Resistor`。
- 当前采样接口只返回实数电压（complex 的虚部不在该封装中暴露）。

