import sys
from datetime import datetime
import argparse

def check_future_date(target_date_str):
    try:
        target_date = datetime.strptime(target_date_str, '%Y-%m-%d')
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return target_date > today
    except ValueError:
        print("日付は'YYYY-MM-DD'形式で入力してください")
        sys.exit(1)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='指定された日付が未来の日付かどうかをチェックします')
    parser.add_argument('--date', type=str, required=True, help='チェックする日付 (YYYY-MM-DD形式)')
    
    args = parser.parse_args()
    result = check_future_date(args.date)
    print("指定された日付は未来の日付です" if result else "指定された日付は過去の日付です")
    print(result)
