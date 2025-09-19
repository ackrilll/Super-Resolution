import os

def rename_files_in_directory(directory_path):
    """
    지정된 디렉토리의 파일 이름을 순서대로 숫자로 변경하는 스크립트.
    directory_path (str): 파일이 있는 디렉토리 경로
    """
    try:
        # 1. 디렉토리 내 모든 파일 목록 가져오기
        files = os.listdir(directory_path)

        # 2. 파일 이름 순서대로 정렬
        files.sort()

        # 3. 각 파일의 이름을 순차적인 숫자로 변경
        for index, filename in enumerate(files):
            # 원본 파일 경로
            original_file_path = os.path.join(directory_path, filename)

            # 파일인지 확인 (디렉토리 제외)
            if os.path.isfile(original_file_path):
                # 파일의 확장자 가져오기
                file_extension = os.path.splitext(filename)[1]

                # 새로운 파일 이름 (1부터 시작하는 숫자)
                new_filename = f"{index + 1}{file_extension}"

                # 새로운 파일 경로
                new_file_path = os.path.join(directory_path, new_filename)

                # 파일 이름 변경
                os.rename(original_file_path, new_file_path)
                print(f"'{filename}' -> '{new_filename}'로 변경되었습니다.")

    except FileNotFoundError:
        print(f"오류: '{directory_path}' 경로를 찾을 수 없습니다.")
    except Exception as e:
        print(f"파일 이름 변경 중 오류가 발생했습니다: {e}")
# 예: 'C:/Users/Username/Desktop/images'
target_directory = '.\\Dataset4K'
# 함수 호출
rename_files_in_directory(target_directory)