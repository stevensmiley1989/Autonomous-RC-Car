# Autonomous-RC-Car
RC Car's Remote Control Autonomously Controlled by Servos using AI. 

![GIF](https://github.com/stevensmiley1989/Autonomous-RC-Car/blob/main/misc/SMHX8455.GIF)

Hardware
------------------

   1x [RC Tank](https://www.amazon.com/Control-Military-Vehicles-Rotating-Channels/dp/B08GLD5SWN/ref=asc_df_B08GLD5SWN/?tag=hyprod-20&linkCode=df0&hvadid=475772725632&hvpos=&hvnetw=g&hvrand=7369787069368498144&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9005083&hvtargid=pla-1186391619299&psc=1)
   
   1x [Jetson Orin AGX](https://www.amazon.com/NVIDIA-Jetson-AGX-Orin-Developer/dp/B09WGRQP4B/ref=asc_df_B09WGRQP4B/?tag=hyprod-20&linkCode=df0&hvadid=598250021259&hvpos=&hvnetw=g&hvrand=12826577717783760631&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9005083&hvtargid=pla-1687956090664&psc=1)

   1x [Android Phone](https://www.amazon.com/SAMSUNG-Smartphone-Unlocked-Android-Battery/dp/B09XP9FX25/ref=sr_1_5?keywords=galaxy+a53&qid=1669601798&sr=8-5)
   
   2x [60kg Servos](https://www.amazon.com/gp/product/B07S96K29Z/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
   
   1x [Arduino Nano](https://www.amazon.com/gp/product/B07WK4VG58/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
   
   1x [Bread Board](https://www.amazon.com/gp/product/B07KG823W9/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
   
   2x [Brass Cylinders](https://www.amazon.com/gp/product/B07Z9B4441/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
   
   1x [Bag of Zip ties](https://www.amazon.com/gp/product/B0777LWBD9/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
   
   1x [Box of Wood Screws](https://www.amazon.com/WoodPro-Fasteners-AP9X212-1-Purpose-Construction/dp/B00EDMHKYU/ref=sxin_17_ac_d_rm?ac_md=3-3-Y29uc3RydWN0aW9uIHNjcmV3cw%3D%3D-ac_d_rm_rm_rm&content-id=amzn1.sym.568df61d-e115-4cb1-a96a-ba070b8f0935%3Aamzn1.sym.568df61d-e115-4cb1-a96a-ba070b8f0935&cv_ct_cx=wood+screws&keywords=wood+screws&pd_rd_i=B00EDMHKYU&pd_rd_r=af4f8e93-c136-4b44-b82f-39f49a03f778&pd_rd_w=iadQa&pd_rd_wg=bu2UR&pf_rd_p=568df61d-e115-4cb1-a96a-ba070b8f0935&pf_rd_r=K5BEW0TEK51EJJ78F69Z&psc=1&qid=1669601473&sr=1-4-7d9bfb42-6e38-4445-b604-42cab39e191b)
   
   1x [12"x12"x"1/2" ply wood](https://www.amazon.com/Premium-Baltic-Birch-Plywood-Grade/dp/B07F1WGHQW/ref=sr_1_5?crid=3T63MY5ELNOLI&keywords=plywood+12x12x1%2F2&qid=1669601546&s=hi&sprefix=plywood+12x12x1%2F2%2Ctools%2C85&sr=1-5)
   
   1x [Wires](https://www.amazon.com/gp/product/B01EV70C78/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
   
   1x [12v Battery](https://www.amazon.com/gp/product/B01M7Z9Z1N/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
   
   1x [Voltage Regulator](https://www.amazon.com/gp/product/B07JZ2GQJF/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
   

   
   

Prerequisites
------------------

Yolov7 should be installed from (https://github.com/WongKinYiu/yolov7).  A version controlled fork is shown in these instructions below.


~~~~~~~

Yolov7
.. code:: shell
    cd ~/
    #git clone https://github.com/WongKinYiu/yolov7.git
    git clone https://github.com/stevensmiley1989/yolov7.git
    cd yolov7
    git switch smiley #if using smiley branch, this is a version control method
    pip3 install -r requirements.txt #you might need to adjust things manually here for versions of PyTorch    
~~~~~~~


Download COCO weights for YOLOv7 from here and put in weights directory as
[best.pt](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt)

Installation
------------------
~~~~~~~

Arduino Nano
.. Use Arduino IDE and upload code in Arduino_Nano_Code directory
~~~~~~~
~~~~~~~
Jetson Orin AGX

Python 3 + Tkinter
.. code:: shell
    cd ~/
    python3 -m venv venv_RC
    source venv_RC/bin/activate
    
    cd ~/Autonomous-RC-Car
    pip3 install -r requirements.txt
    python3 main.py
~~~~~~~

![layout.JPG](https://raw.githubusercontent.com/stevensmiley1989/Autonomous-RC-Car/main/misc/layout.JPG)

## Contact-Info<a class="anchor" id="4"></a>

Feel free to contact me to discuss any issues, questions, or comments.

* Email: [stevensmiley1989@gmail.com](mailto:stevensmiley1989@gmail.com)
* GitHub: [stevensmiley1989](https://github.com/stevensmiley1989)
* LinkedIn: [stevensmiley1989](https://www.linkedin.com/in/stevensmiley1989)
* Kaggle: [stevensmiley](https://www.kaggle.com/stevensmiley)

### License <a class="anchor" id="5"></a>
MIT License

Copyright (c) 2022 Steven Smiley

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

*I am providing code and resources in this repository to you under an open source license.  Because this is my personal repository, the license you receive to my code and resources is from me and not my employer. 
