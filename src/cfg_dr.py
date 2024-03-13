from ctypes import create_string_buffer

pid = 0
h_pro = 0
base_ad = 0

rev_pat = 0
p2_mot = 0
timer = 0

p2_mot_buf = create_string_buffer(4)
p2_pat_buf = create_string_buffer(2)
timer_buf = create_string_buffer(4)

rev_setting = False
last_mot = 0