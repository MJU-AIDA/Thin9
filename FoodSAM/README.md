## Install with Anaconda
### System Requirements and Prerequisite

OS : Ubuntu

GPU : RTX3090

Install anaconda or miniconda

### git clone

`git clone https://github.com/MJU-AIDA/Thin9.git`

### Change Directory to FoodSAM

`cd Thin9/FoodSAM`

### Create Conda env and activate it

`conda create -n test python=3.7.16 -y`

`conda activate test`

### Install Stated Version of torch and torchvision

`bash torch.sh`

### Install Others

`pip install -r requirement.txt`

### Download Model parameter files (3.3GB)

`wget --load-cookies ~/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies ~/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1ejJsY6WFAH48WgnEPmUV08zd40cXd9U6' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1ejJsY6WFAH48WgnEPmUV08zd40cXd9U6" -O ckpts.zip && rm -rf ~/cookies.txt`

`unzip ckpts.zip`

### Check Model execution


`source activate`

`conda activate test`

`python FoodSAM/panoptic.py --img_path dataset/images/27.jpg --output output_panoptic`

### Check FastAPI execution

`uvicorn FoodSAM.app:app --reload`
