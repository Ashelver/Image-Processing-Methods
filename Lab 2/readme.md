Libraries used: numpy, matplotlib, math, cv2, json

For lab3_1, you can modify the `3x3` filter settings using json file similar with:
```json
{
    "filter": [
        [0.11, 0.11, 0.11],
        [0.11, 0.11, 0.11],
        [0.11, 0.11, 0.11]
    ]
}
```

```shell
Lab2-1: Exmaple Usage: 
    python './src/lab2_1.py' log './img/Fig3.08(a).jpg' './result/lab2_1_log(30).jpg' 30
    python './src/lab2_1.py' log './img/Fig3.08(a).jpg' './result/lab2_1_power(15,0.5).jpg' 15 0.5
Lab2-2: Exmaple Usage: 
    python './src/lab2_2.py' './img/Fig3.08(a).jpg' './result/lab2_2_enhanced_img.jpg'
Lab2-3: Exmaple Usage: 
    python './src/lab2_3.py' add './img/Fig3.08(a).jpg' './result/lab2_2_enhanced_img.jpg' './result/lab2_3_add_example.jpg'
Lab3-1: Exmaple Usage: 
    python './src/lab3_1.py' './conf/Lowpass_filter.json' './img/Fig3.37(a).jpg' './result/lab3_1_blur.jpg'
    python './src/lab3_1.py' './conf/Highpass_filter1.json' './img/Fig3.38(a)1.jpg' './result/lab3_1_sharpen1.jpg' 'True'
    python './src/lab3_1.py' './conf/Highpass_filter2.json' './img/Fig3.38(a)1.jpg' './result/lab3_1_sharpen2.jpg' 
```
OR

```shell
python ./src/main.py
```