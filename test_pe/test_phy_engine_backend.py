# -*- coding: utf-8 -*-
import os
import unittest
from pathlib import Path
from typing import Optional

_IMPORT_ERROR: Optional[BaseException] = None
try:
    from physicsLab import Experiment, ExperimentType, OpenMode
    from physicsLab.circuit import Battery_Source, Ground_Component, Resistor, crt_wire
    from physicsLab.circuit.phy_engine import (
        PhyEngineNotAvailableError,
        PhyEngineUnsupportedElementError,
        analyze_experiment_with_phy_engine,
        resolve_phyengine_library_path,
    )
except ModuleNotFoundError as e:
    # `physicsLab` depends on `typing_extensions` (and `requests`) at import time.
    _IMPORT_ERROR = e


def _try_get_lib_path() -> Optional[Path]:
    try:
        return resolve_phyengine_library_path()
    except PhyEngineNotAvailableError:
        return None


class TestPhyEngineBackend(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if _IMPORT_ERROR is not None:
            name = getattr(_IMPORT_ERROR, "name", None)
            if name in {"typing_extensions", "requests"}:
                raise unittest.SkipTest(
                    f"Missing runtime dependency: {name}. Install deps or run via the repo venv."
                )
            raise _IMPORT_ERROR

    def test_dc_voltage_divider_like_loop(self):
        lib_path = _try_get_lib_path()
        if lib_path is None:
            self.skipTest("Phy-Engine dynamic library not available")

        with Experiment(
            OpenMode.crt,
            "__test_phyengine_dc__",
            ExperimentType.Circuit,
            force_crt=True,
        ) as expe:
            v = Battery_Source(0, 0, 0, voltage=5)
            r = Resistor(1, 0, 0, resistance=1000)
            g = Ground_Component(2, 0, 0)

            crt_wire(v.red, r.red)
            crt_wire(r.black, v.black)
            crt_wire(v.black, g.i)

            sample = analyze_experiment_with_phy_engine(expe, analyze_type="DC", lib_path=lib_path)

            # Resistor pins should be at ~5V and ~0V.
            self.assertIn(r, sample.pin_voltage)
            self.assertEqual(len(sample.pin_voltage[r]), 2)
            self.assertAlmostEqual(sample.pin_voltage[r][0], 5.0, places=6)
            self.assertAlmostEqual(sample.pin_voltage[r][1], 0.0, places=6)

            expe.close(delete=True)

    def test_env_var_override(self):
        lib_path = _try_get_lib_path()
        if lib_path is None:
            self.skipTest("Phy-Engine dynamic library not available")

        old = os.environ.get("PHYSICSLAB_PHYENGINE_LIB")
        try:
            os.environ["PHYSICSLAB_PHYENGINE_LIB"] = str(lib_path)

            with Experiment(
                OpenMode.crt,
                "__test_phyengine_env_override__",
                ExperimentType.Circuit,
                force_crt=True,
            ) as expe:
                v = Battery_Source(0, 0, 0, voltage=5)
                r = Resistor(1, 0, 0, resistance=1000)
                g = Ground_Component(2, 0, 0)

                crt_wire(v.red, r.red)
                crt_wire(r.black, v.black)
                crt_wire(v.black, g.i)

                sample = analyze_experiment_with_phy_engine(expe, analyze_type="DC")
                self.assertAlmostEqual(sample.pin_voltage[r][0], 5.0, places=6)
                self.assertAlmostEqual(sample.pin_voltage[r][1], 0.0, places=6)

                expe.close(delete=True)
        finally:
            if old is None:
                os.environ.pop("PHYSICSLAB_PHYENGINE_LIB", None)
            else:
                os.environ["PHYSICSLAB_PHYENGINE_LIB"] = old

    def test_unsupported_element_raises(self):
        lib_path = _try_get_lib_path()
        if lib_path is None:
            self.skipTest("Phy-Engine dynamic library not available")

        from physicsLab.circuit.elements.otherCircuit import Buzzer

        with Experiment(
            OpenMode.crt,
            "__test_phyengine_unsupported__",
            ExperimentType.Circuit,
            force_crt=True,
        ) as expe:
            Buzzer(0, 0, 0)
            with self.assertRaises(PhyEngineUnsupportedElementError):
                analyze_experiment_with_phy_engine(expe, analyze_type="DC", lib_path=lib_path)
            expe.close(delete=True)
