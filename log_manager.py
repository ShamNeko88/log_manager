"""
Summaly:
    - logのファイル出力等の操作を簡易的に行う

Example:
    - log.txt及びコンソールにログを出力

    ```
    import log_manager
    log = log_manager.LogHandler(
        __name__, "log.txt", log_level=10, debug_mode=True
    )
    log.logger.debug("test")
    ```
"""
import logging
from logging.handlers import RotatingFileHandler as r_handler


class LogHandler():
    """
    Summary:
        - ログのファイル出力等を簡易的にする

    Args:
        - logger_name:   基本は「__name__」想定
          - log_file:    指定することでログファイルを出力
          - log_level:   デフォルトですべて出力(CRITICAL:50, ERROR:40, WARNING:30, INFO:20, DEBUG:10, NOTSET:0)
          - debug_mode:  True明示指定でコンソールに出力
          - max_bytes:   ログファイルの最大バイト数
          - backup_cout: 最大バイト超えたときに保持しておくファイル数
          - encoding:    文字コード指定
    """
    def __init__(self, logger_name: str,
                 log_file: str = None,
                 log_level: int = 10,
                 debug_mode=False,
                 max_bytes: int = 10000,
                 backup_count: int = 2,
                 encoding: str = "utf-8"):
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
            file_handler = r_handler(log_file, maxBytes=max_bytes,
                                     backupCount=backup_count,
                                     encoding=encoding)
            file_handler.setFormatter(self.log_file_format)
            self.logger.addHandler(file_handler)

        if debug_mode:
            console_handler = logging.StreamHandler()
            # コンソール出力時フォーマット
            console_handler.setFormatter(self.log_console_format)
            # 設定したハンドラーセット
            self.logger.addHandler(console_handler)


if __name__ == "__main__":
    import log_manager
    log = log_manager.LogHandler(
        __name__, "log.txt", log_level=10, debug_mode=True
    )
    log.logger.debug("test")
