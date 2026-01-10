# Phy-Engine (optional backend for `physicsLab`)

This repo vendors / references `Phy-Engine` as an optional circuit solver backend. `physicsLab` can call it through a small `ctypes` wrapper (no hard dependency at import time).

## Clone with git submodule

If you are cloning `physicsLab` (the parent repo) and `Phy-Engine` is configured as a submodule:

```bash
git clone --recurse-submodules <PHYSICSLAB_REPO_URL>
# or after cloning:
git submodule update --init --recursive
```

If you are adding `Phy-Engine` as a submodule to your `physicsLab` checkout:

```bash
git submodule add https://github.com/MacroModel/Phy-Engine.git third-parties/Phy-Engine
git submodule update --init --recursive
```

## Build the shared library (native)

`Phy-Engine` ships a C ABI in `include/phy_engine/dll_api.h` and builds a shared library from `src/dll_main.cpp`.

### macOS / Linux

```bash
cmake -S third-parties/Phy-Engine/src -B third-parties/Phy-Engine/build -DCMAKE_BUILD_TYPE=Release
cmake --build third-parties/Phy-Engine/build -j
```

Outputs (typical):
- macOS: `third-parties/Phy-Engine/build/libphyengine.dylib`
- Linux: `third-parties/Phy-Engine/build/libphyengine.so`

### Windows (MSVC)

```bat
cmake -S third-parties/Phy-Engine/src -B third-parties/Phy-Engine/build -G "Visual Studio 17 2022" -A x64
cmake --build third-parties/Phy-Engine/build --config Release
```

Outputs (typical):
- `third-parties/Phy-Engine/build/Release/phyengine.dll`

## Install the runtime shared library for `physicsLab`

`physicsLab` searches for the `Phy-Engine` shared library in:

1) `PHYSICSLAB_PHYENGINE_LIB` (full file path), then
2) `physicsLab/native/` (recommended), then
3) a few development build folders under `third-parties/Phy-Engine/`.

Recommended installation is to copy the built shared library into `physicsLab/native/`:

- macOS:
  - copy `libphyengine.dylib` to `physicsLab/native/libphyengine.dylib`
- Linux:
  - copy `libphyengine.so` to `physicsLab/native/libphyengine.so`
- Windows:
  - copy `phyengine.dll` to `physicsLab/native/phyengine.dll`

If you prefer to keep it elsewhere, set:

```bash
export PHYSICSLAB_PHYENGINE_LIB=/full/path/to/libphyengine.dylib   # macOS
export PHYSICSLAB_PHYENGINE_LIB=/full/path/to/libphyengine.so      # Linux
setx PHYSICSLAB_PHYENGINE_LIB "C:\full\path\to\phyengine.dll"      # Windows
```

## Call from `physicsLab`

The wrapper lives in `physicsLab/circuit/phy_engine.py` and is exposed via `physicsLab.circuit`.

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
    print("Resistor pin voltages:", sample.pin_voltage[r])
```

### Supported elements (current mapping)

The mapping is intentionally small and will raise `PhyEngineUnsupportedElementError` for unsupported `ModelID`s. Currently supported `ModelID`s include:

- Analog: `Resistor`, `Basic Capacitor`, `Basic Inductor`, `Battery Source`, `Simple Switch`, `Push Switch`, `Air Switch`, `Transformer`, `Mutual Inductor`, `Rectifier`, `Ground Component`
- Digital: `Logic Input`, `Logic Output`, `Yes Gate`, `No Gate`, `And Gate`, `Or Gate`, `Xor Gate`, `Xnor Gate`, `Nand Gate`, `Nor Gate`, `Imp Gate`, `Nimp Gate`, `Half Adder`, `Full Adder`, `Half Subtractor`, `Full Subtractor`, `Multiplier`, `D Flipflop`, `T Flipflop`, `Real-T Flipflop`, `JK Flipflop`

Notes:
- `Battery Source` internal resistance is not modeled; add an explicit `Resistor` if needed.
- The current C ABI sampler returns real-valued node voltages only.

