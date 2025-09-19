import cv2
import os
import random

def transform_image(folder_path, target_size, output_folder=None):
    """
    다양한 보간법을 사용하여 이미지 크기를 변환하고 결과를 표시합니다.

    Args:
        image_path (str): 원본 이미지 파일의 경로.
        target_size (tuple): 변환 후 이미지의 (너비, 높이).
        save_path (str, optional): 변환된 이미지를 저장할 경로. None이면 저장하지 않습니다.
    """
    try:
        files = os.listdir(folder_path)
        print(files)
        print(f'해당 폴더에 이미지가 {len(files)} 장 있습니다')

        for file in files:
            print(file)
            file_path = os.path.join(folder_path, file)
            original_image = cv2.imread(file_path)
            random_number = random.randint(1, 3)

            if random_number == 1:
                transformed_image = cv2.resize(
                    original_image,
                    dsize=target_size,
                    interpolation=cv2.INTER_CUBIC
                )
                print("쌍삼차 보간법 적용")
            elif random_number==2:
                transformed_image = cv2.resize(
                    original_image,
                    dsize=target_size,
                    interpolation=cv2.INTER_NEAREST
                )
                print("최근접 이웃 보간법 적용")
            else:
                transformed_image = cv2.resize(
                    original_image,
                    dsize=target_size,
                    interpolation=cv2.INTER_LINEAR
                )
                print("쌍선형 보간법 적용")



            # 3. 변환된 이미지 저장 (경로가 지정된 경우)
            if output_folder:
                transformed_image_path = os.path.join(output_folder,file)
                print(transformed_image_path)
                cv2.imwrite(transformed_image_path, transformed_image)


            # 사용자가 키를 누를 때까지 대기 후 창 닫기
            cv2.waitKey(0)
            cv2.destroyAllWindows()


    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


# --- 사용 예시 ---
# 여기에 자신의 이미지 경로와 저장 경로를 지정하세요.
folder_path = '.\\Dataset4K'
output_folder = '.\\DownscaleImages'

# 목표 크기 지정 (예: 원본 크기의 0.25배로 축소)
target_size_downscale = (960,540)  # (너비, 높이)

transform_image(folder_path, target_size_downscale, output_folder)