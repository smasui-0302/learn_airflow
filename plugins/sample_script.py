import sys
from datetime import datetime
import argparse
import logging

# ロガーの設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

def check_future_date(target_date_str):
    try:
        target_date = datetime.strptime(target_date_str, '%Y-%m-%d')
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return target_date > today
    except ValueError:
        logger.error("日付は'YYYY-MM-DD'形式で入力してください")
        sys.exit(1)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='指定された日付が未来の日付かどうかをチェックします')
    parser.add_argument('--date', type=str, required=True, help='チェックする日付 (YYYY-MM-DD形式)')
    
    args = parser.parse_args()
    result = check_future_date(args.date)
    logger.info("指定された日付は未来の日付です" if result else "指定された日付は過去の日付です")
    logger.debug(f"結果: {result}")
    print(result)
