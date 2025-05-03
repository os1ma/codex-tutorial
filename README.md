# python-project-template
## サンプル: Todo リスト CLI

JSONファイル(`tasks.json`)にタスクを保存するシンプルなCLIです。以下のサブコマンドを提供します:

```bash
# タスクを追加
python -m todo add "牛乳を買う"
# タスク一覧を表示
python -m todo list
# タスク1を完了にマーク
python -m todo done 1
# タスク1を削除
python -m todo delete 1
```

実行するとカレントディレクトリに`tasks.json`が作成・更新されます。
