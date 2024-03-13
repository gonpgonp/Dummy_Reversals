from ctypes import windll
from struct import pack, unpack
import os
import time
import keyboard

import sub_dr as sub
import cfg_dr as cfg

sub.ex_cmd_enable()
os.system('mode con: cols=36 lines=4')
os.system('cls')
os.system('title Dummy Reversal')
print('\x1b[1;1H' + '\x1b[?25l')
windll.winmm.timeBeginPeriod(1)  # タイマー精度を1msec単位にする

sub.get_base_address()

while 1:
    
    time.sleep(0.001)
    
    if keyboard.is_pressed("="):
        time.sleep(0.1)
        cfg.rev_setting = not cfg.rev_setting
    
    if keyboard.is_pressed("-"):
        time.sleep(0.1)
        cfg.rev_pat = sub.r_mem(0x155C3C, cfg.p2_pat_buf)
    
    cfg.timer = sub.r_mem(0x162A40, cfg.timer_buf)
    cfg.p2_mot = sub.r_mem(0x1581CC, cfg.p2_mot_buf)
    
    if (cfg.p2_mot == 0 and cfg.p2_mot != cfg.last_mot and cfg.rev_setting and cfg.timer > 1):
        sub.w_mem(0x155F38, pack('h', cfg.rev_pat))
    
    cfg.last_mot = cfg.p2_mot
    
    sub.view()
