### ログ管理モジュール

- Summaly:
    - logのファイル出力等の操作を簡易的に行う

- Example:
    - log.txt及びコンソールにログを出力

    ```Python
    import log_manager
    log = log_manager.LogHandler(
        __name__, "log.txt", log_level=10, debug_mode=True
    )
    log.logger.debug("test")
    ```