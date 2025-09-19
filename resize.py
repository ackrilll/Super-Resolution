#이미지 크기 일괄적으로 같게 만들어주는 스크립트
import cv2
import os
def resize(folder_path, target_size):
    count = 0
    #1. 폴더에 있는 이미지 하나씩 가져오기
    for i in range(len(os.listdir(folder_path))):
        file_path = os.path.join(folder_path,os.listdir(folder_path)[i])
        original_image = cv2.imread(file_path)
        width, hight = original_image.shape[1], original_image.shape[0]
        if (width != target_size[0]) or (hight != target_size[1]):
            count += 1
            transformed_image = cv2.resize(
                original_image,
                dsize=target_size,
                interpolation=cv2.INTER_CUBIC
            )
            cv2.imwrite(file_path, transformed_image)
            print(f'변형 전 이미지 모양: {original_image.shape}')
            print(f'변형 후 이미지 모양: {transformed_image.shape}')
            print(count)
    print(f'총 {count} 개의 이미지를 변형하였습니다')


resize('.\\Dataset4K',(3840,2160))

