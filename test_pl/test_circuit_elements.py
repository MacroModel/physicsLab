import unittest
from physicsLab import Experiment, OpenMode, ExperimentType
from physicsLab.circuit.elements import *


class TestSensor(unittest.TestCase):
    def test_accelerometer(self):
        with Experiment(OpenMode.crt, "__test_sensor_accelerometer__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Accelerometer(0, 0, 0, ranges=2, shifting=0.75, response_factor=0.229)
            expe.close(delete=True)

    def test_analog_joystick(self):
        with Experiment(OpenMode.crt, "__test_sensor_analog_joystick__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Analog_Joystick(0, 0, 0)
            expe.close(delete=True)

    def test_attitude_sensor(self):
        with Experiment(OpenMode.crt, "__test_sensor_attitude_sensor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Attitude_Sensor(0, 0, 0, ranges=180, shifting=2.5, response_factor=0.0125)
            expe.close(delete=True)

    def test_gravity_sensor(self):
        with Experiment(OpenMode.crt, "__test_sensor_gravity_sensor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Gravity_Sensor(0, 0, 0, ranges=2, shifting=0.75, response_factor=0.229)
            expe.close(delete=True)

    def test_gyroscope(self):
        with Experiment(OpenMode.crt, "__test_sensor_gyroscope__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Gyroscope(0, 0, 0, ranges=150, shifting=2.5, response_factor=0.0125)
            expe.close(delete=True)

    def test_linear_accelerometer(self):
        with Experiment(OpenMode.crt, "__test_sensor_linear_accelerometer__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Linear_Accelerometer(0, 0, 0, ranges=2, shifting=0.75, response_factor=0.229)
            expe.close(delete=True)

    def test_magnetic_field_sensor(self):
        with Experiment(OpenMode.crt, "__test_sensor_magnetic_field_sensor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Magnetic_Field_Sensor(0, 0, 0, ranges=0.04, shifting=3.2, response_factor=80)
            expe.close(delete=True)

    def test_photodiode(self):
        with Experiment(OpenMode.crt, "__test_sensor_photodiode__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Photodiode(0, 0, 0)
            expe.close(delete=True)

    def test_photoresistor(self):
        with Experiment(OpenMode.crt, "__test_sensor_photoresistor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Photoresistor(0, 0, 0)
            expe.close(delete=True)

    def test_proximity_sensor(self):
        with Experiment(OpenMode.crt, "__test_sensor_proximity_sensor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Proximity_Sensor(0, 0, 0)
            expe.close(delete=True)


class TestOtherCircuit(unittest.TestCase):
    def test_buzzer(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_buzzer__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Buzzer(0, 0, 0)
            expe.close(delete=True)

    def test_spark_gap(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_spark_gap__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Spark_Gap(0, 0, 0)
            expe.close(delete=True)

    def test_tesla_coil(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_tesla_coil__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Tesla_Coil(0, 0, 0)
            expe.close(delete=True)

    def test_color_light_emitting_diode(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_color_led__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Color_Light_Emitting_Diode(0, 0, 0)
            expe.close(delete=True)

    def test_dual_light_emitting_diode(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_dual_led__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Dual_Light_Emitting_Diode(0, 0, 0)
            expe.close(delete=True)

    def test_electric_bell(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_electric_bell__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Electric_Bell(0, 0, 0)
            expe.close(delete=True)

    def test_musical_box(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_musical_box__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Musical_Box(0, 0, 0)
            expe.close(delete=True)

    def test_resistance_law(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_resistance_law__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Resistance_Law(0, 0, 0)
            expe.close(delete=True)

    def test_solenoid(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_solenoid__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Solenoid(0, 0, 0)
            expe.close(delete=True)

    def test_electric_fan(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_electric_fan__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Electric_Fan(0, 0, 0)
            expe.close(delete=True)

    def test_simple_instrument(self):
        with Experiment(OpenMode.crt, "__test_other_circuit_simple_instrument__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Simple_Instrument(0, 0, 0, pitches=[60, 64, 67])
            expe.close(delete=True)


class TestLogicCircuit(unittest.TestCase):
    def test_logic_input(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_logic_input__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Logic_Input(0, 0, 0, output_status=True)
            expe.close(delete=True)

    def test_logic_output(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_logic_output__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Logic_Output(0, 0, 0)
            expe.close(delete=True)

    def test_yes_gate(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_yes_gate__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Yes_Gate(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_no_gate(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_no_gate__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = No_Gate(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_or_gate(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_or_gate__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Or_Gate(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_and_gate(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_and_gate__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = And_Gate(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_nor_gate(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_nor_gate__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Nor_Gate(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_nand_gate(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_nand_gate__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Nand_Gate(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_xor_gate(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_xor_gate__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Xor_Gate(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_xnor_gate(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_xnor_gate__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Xnor_Gate(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_imp_gate(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_imp_gate__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Imp_Gate(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_nimp_gate(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_nimp_gate__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Nimp_Gate(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_half_adder(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_half_adder__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Half_Adder(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_full_adder(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_full_adder__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Full_Adder(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_half_subtractor(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_half_subtractor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Half_Subtractor(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_full_subtractor(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_full_subtractor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Full_Subtractor(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_multiplier(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_multiplier__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Multiplier(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_d_flipflop(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_d_flipflop__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = D_Flipflop(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_t_flipflop(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_t_flipflop__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = T_Flipflop(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_real_t_flipflop(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_real_t_flipflop__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Real_T_Flipflop(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_jk_flipflop(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_jk_flipflop__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = JK_Flipflop(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_counter(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_counter__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Counter(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_random_generator(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_random_generator__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Random_Generator(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_eight_bit_input(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_eight_bit_input__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Eight_Bit_Input(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_eight_bit_display(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_eight_bit_display__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Eight_Bit_Display(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)

    def test_schmitt_trigger(self):
        with Experiment(OpenMode.crt, "__test_circuit_elements_schmitt_trigger__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Schmitt_Trigger(0, 0, 0, high_level=5, low_level=0)
            expe.close(delete=True)


class TestArtificialCircuit(unittest.TestCase):
    def test_ne555(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_ne555__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = NE555(0, 0, 0)
            expe.close(delete=True)

    def test_basic_capacitor(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_basic_capacitor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Basic_Capacitor(0, 0, 0)
            expe.close(delete=True)

    def test_basic_inductor(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_basic_inductor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Basic_Inductor(0, 0, 0)
            expe.close(delete=True)

    def test_basic_diode(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_basic_diode__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Basic_Diode(0, 0, 0)
            expe.close(delete=True)

    def test_light_emitting_diode(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_light_emitting_diode__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Light_Emitting_Diode(0, 0, 0)
            expe.close(delete=True)

    def test_ground_component(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_ground_component__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Ground_Component(0, 0, 0)
            expe.close(delete=True)

    def test_transformer(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_transformer__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Transformer(0, 0, 0)
            expe.close(delete=True)

    def test_tapped_transformer(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_tapped_transformer__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Tapped_Transformer(0, 0, 0)
            expe.close(delete=True)

    def test_mutual_inductor(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_mutual_inductor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Mutual_Inductor(0, 0, 0)
            expe.close(delete=True)

    def test_rectifier(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_rectifier__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Rectifier(0, 0, 0)
            expe.close(delete=True)

    def test_transistor(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_transistor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Transistor(0, 0, 0)
            expe.close(delete=True)

    def test_comparator(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_comparator__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Comparator(0, 0, 0)
            expe.close(delete=True)

    def test_operational_amplifier(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_operational_amplifier__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Operational_Amplifier(0, 0, 0)
            expe.close(delete=True)

    def test_relay_component(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_relay_component__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Relay_Component(0, 0, 0)
            expe.close(delete=True)

    def test_n_mosfet(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_n_mosfet__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = N_MOSFET(0, 0, 0)
            expe.close(delete=True)

    def test_p_mosfet(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_p_mosfet__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = P_MOSFET(0, 0, 0)
            expe.close(delete=True)

    def test_current_source(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_current_source__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Current_Source(0, 0, 0)
            expe.close(delete=True)

    def test_sinewave_source(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_sinewave_source__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Sinewave_Source(0, 0, 0)
            expe.close(delete=True)

    def test_square_source(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_square_source__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Square_Source(0, 0, 0)
            expe.close(delete=True)

    def test_triangle_source(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_triangle_source__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Triangle_Source(0, 0, 0)
            expe.close(delete=True)

    def test_sawtooth_source(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_sawtooth_source__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Sawtooth_Source(0, 0, 0)
            expe.close(delete=True)

    def test_pulse_source(self):
        with Experiment(OpenMode.crt, "__test_artificial_circuit_pulse_source__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Pulse_Source(0, 0, 0)
            expe.close(delete=True)


class TestBasicCircuit(unittest.TestCase):
    def test_simple_switch(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_simple_switch__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Simple_Switch(0, 0, 0)
            expe.close(delete=True)

    def test_spdt_switch(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_spdt_switch__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = SPDT_Switch(0, 0, 0)
            expe.close(delete=True)

    def test_dpdt_switch(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_dpdt_switch__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = DPDT_Switch(0, 0, 0)
            expe.close(delete=True)

    def test_push_switch(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_push_switch__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Push_Switch(0, 0, 0)
            expe.close(delete=True)

    def test_air_switch(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_air_switch__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Air_Switch(0, 0, 0)
            expe.close(delete=True)

    def test_incandescent_lamp(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_incandescent_lamp__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Incandescent_Lamp(0, 0, 0)
            expe.close(delete=True)

    def test_battery_source(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_battery_source__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Battery_Source(0, 0, 0)
            expe.close(delete=True)

    def test_student_source(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_student_source__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Student_Source(0, 0, 0)
            expe.close(delete=True)

    def test_resistor(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_resistor__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Resistor(0, 0, 0)
            expe.close(delete=True)

    def test_fuse_component(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_fuse_component__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Fuse_Component(0, 0, 0)
            expe.close(delete=True)

    def test_slide_rheostat(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_slide_rheostat__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Slide_Rheostat(0, 0, 0)
            expe.close(delete=True)

    def test_multimeter(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_multimeter__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Multimeter(0, 0, 0)
            expe.close(delete=True)

    def test_galvanometer(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_galvanometer__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Galvanometer(0, 0, 0)
            expe.close(delete=True)

    def test_microammeter(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_microammeter__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Microammeter(0, 0, 0)
            expe.close(delete=True)

    def test_electricity_meter(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_electricity_meter__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Electricity_Meter(0, 0, 0)
            expe.close(delete=True)

    def test_resistance_box(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_resistance_box__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Resistance_Box(0, 0, 0)
            expe.close(delete=True)

    def test_simple_ammeter(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_simple_ammeter__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Simple_Ammeter(0, 0, 0)
            expe.close(delete=True)

    def test_simple_voltmeter(self):
        with Experiment(OpenMode.crt, "__test_basic_circuit_simple_voltmeter__", ExperimentType.Circuit, force_crt=True) as expe:
            _ = Simple_Voltmeter(0, 0, 0)
            expe.close(delete=True)
