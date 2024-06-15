"""
# logに関するクラス
- モジュールとして呼び出す際はloggerの名前は__name__想定
- 引数
  - logger_name  ロガー作成時の名前基本は「__name__」想定
  - log_file     指定することでログファイルを出力
  - log_level    デフォルトですべて出力(CRITICAL:50, ERROR:40, WARNING:30, INFO:20, DEBUG:10, NOTSET:0)
  - debug_mode   True明示指定でコンソールに出力
  - max_bytes    ログファイルの最大バイト数
  - backup_cout  最大バイト超えたときに保持しておくファイル数
  - encoding     文字コード指定
"""

import logging 
from logging.handlers import RotatingFileHandler as r_handler

class LogHandler():
    def __init__(self, logger_name, log_file=None, log_level=10, debug_mode=False, max_bytes=10000, backup_count=2, encoding="utf-8"):
        # フォーマット（ファイル）
        self.log_file_format = logging.Formatter("[%(levelname)s] %(asctime)s -%(message)s <場所：%(filename)s/%(funcName)s/%(lineno)d行目>")
        # フォーマット（コンソール）
        self.log_console_format = logging.Formatter("[%(levelname)s] %(asctime)s -%(message)s <場所：%(filename)s/%(funcName)s/%(lineno)d行目>")
        # loggerの作成
        self.logger = logging.getLogger(logger_name)
        # logレベル設定
        self.logger.setLevel(log_level)
        
        # logファイル出力先とファイルの最大バイト数、ファイル数設定
        if log_file:
            file_handler = r_handler(log_file, maxBytes=max_bytes, backupCount=backup_count, encoding=encoding)
            file_handler.setFormatter(self.log_file_format)
            self.logger.addHandler(file_handler) 

        if debug_mode:
            console_handler = logging.StreamHandler() 
            console_handler.setFormatter(self.log_console_format) # コンソール出力時フォーマット 
            self.logger.addHandler(console_handler) # 設定したハンドラーセット

if __name__ == "__main__":
    log = LogHandler(__name__, "log.txt", log_level=10, debug_mode=True)
    log.logger.debug("test")