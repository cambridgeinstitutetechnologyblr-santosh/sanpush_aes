/*
 * Copyright (c) 2024
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_santosh_aes_sbox (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

reg [7:0] sbox_out;

always @(*) begin
    case (ui_in)

        8'h00: sbox_out = 8'h63;
        8'h01: sbox_out = 8'h7C;
        8'h02: sbox_out = 8'h77;
        8'h03: sbox_out = 8'h7B;
        8'h04: sbox_out = 8'hF2;
        8'h05: sbox_out = 8'h6B;
        8'h06: sbox_out = 8'h6F;
        8'h07: sbox_out = 8'hC5;
        8'h08: sbox_out = 8'h30;
        8'h09: sbox_out = 8'h01;
        8'h0A: sbox_out = 8'h67;
        8'h0B: sbox_out = 8'h2B;
        8'h0C: sbox_out = 8'hFE;
        8'h0D: sbox_out = 8'hD7;
        8'h0E: sbox_out = 8'hAB;
        8'h0F: sbox_out = 8'h76;

        // For now we implement first 16 entries
        // and return input for remaining values

        default: sbox_out = ui_in;
    endcase
end

assign uo_out = sbox_out;

assign uio_out = 8'b0;
assign uio_oe  = 8'b0;

wire _unused = &{ena, clk, rst_n, uio_in, 1'b0};

endmodule
