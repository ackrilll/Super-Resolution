import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import os
import numpy as np
from model import FSRCNN

def generate_high_res_image(model_path, LOW_RES_FOLDER_PATH, OUTPUT_FOLDER_PATH, scale_factor=4):
    """
    훈련된 모델을 사용하여 저해상도 이미지를 고화질로 변환하고 저장합니다.
    """
    try:
        # 1. 장치 설정 (GPU 또는 CPU)
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        # 2. 모델 불러오기
        model = FSRCNN(scale_factor=scale_factor).to(device)
        model.load_state_dict(torch.load(model_path))
        model.eval()  # 모델을 추론 모드로 설정

        # 3. 저해상도 이미지 불러와 텐서로 변환
        for file in os.listdir(LOW_RES_FOLDER_PATH):
            low_res_image_path = os.path.join(LOW_RES_FOLDER_PATH,file)
            lr_image = Image.open(low_res_image_path).convert('RGB')
            lr_tensor = transforms.ToTensor()(lr_image).unsqueeze(0).to(device)

            # 4. 이미지 생성 (추론)
            with torch.no_grad():  # 그라디언트 계산 비활성화
                hr_output_tensor = model(lr_tensor)

            # 5. 텐서를 이미지로 변환
            hr_output_image = hr_output_tensor.squeeze(0).cpu()  # 텐서에서 배치 차원 제거
            hr_output_image = transforms.ToPILImage()(hr_output_image)

            # 6. 이미지 저장
            output_path = os.path.join(OUTPUT_FOLDER_PATH,file)
            hr_output_image.save(output_path)
            print(f"고화질 이미지가 '{output_path}'에 성공적으로 저장되었습니다.")


    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


# --- 사용 예시 ---
# 훈련된 모델 가중치 파일 경로
TRAINED_MODEL_PATH = '.\\params/fsrcnn_4x_model.pth'

# 고화질로 변환할 저해상도 이미지 폴더
LOW_RES_FOLDER_PATH = '.\\DownScaleTwiceImages'

# 생성된 고화질 이미지를 저장할 경로
OUTPUT_FOLDER_PATH = '.\\inference'

generate_high_res_image(TRAINED_MODEL_PATH, LOW_RES_FOLDER_PATH, OUTPUT_FOLDER_PATH)