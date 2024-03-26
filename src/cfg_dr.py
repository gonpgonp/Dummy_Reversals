from ctypes import create_string_buffer

pid = 0
h_pro = 0
base_ad = 0

rev_pat = 0
rev_stance = 0
p2_mot = 0
p2_no_combo = 1
p2_stance = 0
timer = 0

p2_mot_buf = create_string_buffer(4)
p2_pat_buf = create_string_buffer(2)
p2_no_combo_buf = create_string_buffer(1)
p2_rev_stance_buf = create_string_buffer(1)
p2_stance_buf = create_string_buffer(1)
timer_buf = create_string_buffer(4)

buffer = create_string_buffer(4)

rev_setting = 0
do_reversal = False
last_mot = 0