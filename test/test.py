# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):

    dut._log.info("Starting AES S-Box Test")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 10)

    dut.rst_n.value = 1

    # AES S-Box vectors matching the entries currently in project.v
    test_vectors = [
        (0x00, 0x63),
        (0x01, 0x7C),
        (0x02, 0x77),
        (0x03, 0x7B),
        (0x04, 0xF2),
        (0x05, 0x6B),
        (0x06, 0x6F),
        (0x07, 0xC5),
        (0x08, 0x30),
        (0x09, 0x01),
        (0x0A, 0x67),
        (0x0B, 0x2B),
        (0x0C, 0xFE),
        (0x0D, 0xD7),
        (0x0E, 0xAB),
        (0x0F, 0x76)
    ]

    for inp, expected in test_vectors:

        dut.ui_in.value = inp

        await ClockCycles(dut.clk, 1)

        result = int(dut.uo_out.value)

        dut._log.info(
            f"Input=0x{inp:02X}, Output=0x{result:02X}, Expected=0x{expected:02X}"
        )

        assert result == expected, \
            f"FAILED: Input=0x{inp:02X}, Got=0x{result:02X}, Expected=0x{expected:02X}"

    dut._log.info("AES S-Box Test Passed")
