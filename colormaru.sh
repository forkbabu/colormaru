cd /content/
git clone https://github.com/forkbabu/qq.git DeOldify
cd DeOldify
pip install fire
pip install -r colab_requirements.txt
mkdir -p 'models'
wget -nc https://data.deepai.org/deoldify/ColorizeVideo_gen.pth -O ./models/ColorizeVideo_gen.pth
wget -nc https://media.githubusercontent.com/media/jantic/DeOldify/master/resource_images/watermark.png -O ./resource_images/watermark.png
python3 /content/colormaru/set.py --vid=$1
