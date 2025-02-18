from lab2_1 import lab2_1
from lab2_2 import lab2_2
from lab2_3 import lab2_3
from lab3_1 import lab3_1
lf = [0.11, 0.11, 0.11,
       0.11, 0.11, 0.11,
       0.11, 0.11, 0.11]

hf1 = [-1, -1, -1,
       -1, 8, -1,
       -1, -1, -1]

hf2 = [-1, -1, -1,
       -1, 9, -1,
       -1, -1, -1]



if __name__ == "__main__":
    p1 = lab2_1()
    p2 = lab2_2()
    p3 = lab2_3()

    # 2-1
    p1.log_transform('./img/Fig3.08(a).jpg', './result/lab2_1_log(30).jpg', 30)
    p1.power_law_transform('./img/Fig3.08(a).jpg', './result/lab2_1_power(15,0.5).jpg', 15, 0.5)
    
    # 2-2
    p2.process_image('./img/Fig3.08(a).jpg', './result/lab2_2_enhanced_img.jpg')
    
    # 2-3
    p3.add_images('./img/Fig3.08(a).jpg', './result/lab2_2_enhanced_img.jpg', './result/lab2_3_add_example.jpg')
    
    # 3-1
    lowpass = lab3_1(*lf)
    highpass1 = lab3_1(*hf1, scaling=True)
    highpass2 = lab3_1(*hf2)

    lowpass.apply_filter('./img/Fig3.37(a).jpg','./result/lab3_1_blur.jpg')
    highpass1.apply_filter('./img/Fig3.38(a)1.jpg','./result/lab3_1_sharpen1.jpg')
    highpass2.apply_filter('./img/Fig3.38(a)1.jpg','./result/lab3_1_sharpen2.jpg')


