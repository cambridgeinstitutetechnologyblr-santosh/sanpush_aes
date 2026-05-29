# AES S-Box Accelerator using SKY130 OpenLane Flow

## Overview

This project implements an AES (Advanced Encryption Standard) S-Box Accelerator in Verilog HDL and demonstrates its physical implementation using the SKY130 open-source ASIC design flow.

The AES S-Box is a nonlinear substitution block used in the SubBytes stage of AES encryption. It accepts an 8-bit input and produces an 8-bit substituted output according to the AES substitution table.

This project was developed and verified using the Tiny Tapeout framework and OpenLane physical design flow.

---

## Features

- 8-bit AES S-Box implementation
- Verilog RTL design
- Tiny Tapeout compatible interface
- SKY130 ASIC implementation
- OpenLane synthesis and place-and-route flow
- Cocotb-based verification

---

## Interface

### Inputs

| Signal | Width | Description |
|----------|----------|-------------|
| ui_in | 8 | AES input byte |

### Outputs

| Signal | Width | Description |
|----------|----------|-------------|
| uo_out | 8 | AES S-Box output byte |

### Unused Signals

| Signal |
|----------|
| uio_in |
| uio_out |
| uio_oe |
| clk |
| rst_n |

---

## Example Mappings

| Input (Hex) | Output (Hex) |
|-------------|--------------|
| 00 | 63 |
| 01 | 7C |
| 02 | 77 |
| 03 | 7B |
| 04 | F2 |
| 05 | 6B |
| 06 | 6F |
| 07 | C5 |

---

## Verification

The design is verified using Cocotb testbenches.

Test vectors include:

```text
0x00 → 0x63
0x01 → 0x7C
0x02 → 0x77
0x03 → 0x7B
0x04 → 0xF2
```

---

## Physical Design Flow

The design was implemented using:

- Tiny Tapeout
- OpenLane
- SKY130 PDK
- OpenROAD
- Magic
- Netgen

Flow stages:

1. RTL Design
2. Functional Simulation
3. Synthesis
4. Floorplanning
5. Placement
6. Clock Tree Synthesis
7. Routing
8. DRC/LVS Verification
9. GDSII Generation

---

## Project Title

**Design and Physical Implementation of AES S-Box Accelerator using SKY130 OpenLane Flow**

---

## Author

Santosh
