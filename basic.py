# 프로그램 운영시 중요한 부분을 로그로 남기는 것,
# 단순한 에러인지, 출력인지 등을 관리하는 모듈
import logging

# logging.debug('debug')
# logging.info('INFO')
# logging.warning('WARNING')
# logging.error('error')
# logging.critical('critical')

# print(logging.DEBUG) # 필요한 정보를 기록
# logging.setLevel(logging.INFO) # 정보 알림
# print(logging.WARNING) # 작동은 하지만 예상치 못한 일이 발생할 것으로 예측, 기본값
# logging.setLevel(logging.ERROR) # 에러
# logging.setLevel(logging.CRITICAL) # 심각한 오류

# 1. 로거 생성
logger = logging.getLogger('테스트')
# 1-2 레벨 설정
logger.setLevel(logging.DEBUG)

# 2. 파일 핸들러 생성
f1 = logging.FileHandler('data\\default.log', encoding='utf-8')
f2 = logging.FileHandler('data\\secret.log', encoding='utf-8')

# 2-2. 레벨 설정, 설정 안하면 WARNING 부터
f1.setLevel(logging.WARNING)

logger.addHandler(f1)
logger.addHandler(f2)

# 3. 포매터 생성
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
f1.setFormatter(formatter)
f2.setFormatter(formatter)


# print(3)
# logger.debug('프로그램 디버그')
# logger.info('프로그램 인포')
# logger.warning('프로그램 워닝')
# logger.error('에러가 발생했어요')
# logger.critical('심각한 오류')