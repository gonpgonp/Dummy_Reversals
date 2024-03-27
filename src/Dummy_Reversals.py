from ctypes import windll
from struct import pack, unpack
import os
import time
import keyboard

import sub_dr as sub
import cfg_dr as cfg

sub.ex_cmd_enable()
os.system('mode con: cols=36 lines=5')
os.system('cls')
os.system('title Dummy Reversal')
print('\x1b[1;1H' + '\x1b[?25l')
windll.winmm.timeBeginPeriod(1)  # タイマー精度を1msec単位にする

sub.get_base_address()

while 1:
    
    time.sleep(0.001)
    
    if keyboard.is_pressed("="):
        time.sleep(0.2)
        cfg.rev_setting = (cfg.rev_setting + 1)%3
    
    if keyboard.is_pressed("-"):
        time.sleep(0.2)
        cfg.rev_pat = sub.r_mem(0x155C3C, cfg.p2_pat_buf)
        cfg.rev_stance = sub.r_mem(0x155F47, cfg.p2_rev_stance_buf)
    
    cfg.timer = sub.r_mem(0x162A40, cfg.timer_buf)
    cfg.p2_mot = sub.r_mem(0x1581CC, cfg.p2_mot_buf)
    cfg.p2_no_combo = sub.r_mem(0x155C90, cfg.p2_no_combo_buf)
    cfg.p2_stance = sub.r_mem(0x155F47, cfg.p2_stance_buf)
    
    if cfg.p2_no_combo == 0 or cfg.rev_setting == 2:
        cfg.do_reversal = True
        
    
    if (cfg.p2_mot == 0 and cfg.p2_mot != cfg.last_mot and cfg.rev_setting > 0
        and cfg.timer > 1 and cfg.rev_stance%2 == cfg.p2_stance%2):
        if cfg.do_reversal:
            sub.w_mem(0x155F38, pack('h', cfg.rev_pat))
            if cfg.rev_setting == 1:
                cfg.do_reversal = False
                time.sleep(0.2)
    
    cfg.last_mot = cfg.p2_mot
    
    sub.view()
