import json
import urllib.request

# あなたのColab APIエンドポイント
API_URL = "https://33b6-34-83-133-36.ngrok-free.app/predict"

def handler(event, context):
    try:
        # ユーザーの入力メッセージを取得（最後の発言を使用）
        message = event['messages'][-1]['content']

        # APIに送るリクエストデータをJSONでエンコード
        data = json.dumps({"input": message}).encode("utf-8")

        # HTTPリクエストの作成
        req = urllib.request.Request(
            API_URL,
            data=data,
            headers={'Content-Type': 'application/json'},
            method='POST'
        )

        # リクエスト送信とレスポンスの読み取り
        with urllib.request.urlopen(req) as res:
            res_body = res.read()
            result = json.loads(res_body)['output']  # APIの返答から 'output' を取り出す

        # チャットアプリが期待する形式で返す
        return {
            'statusCode': 200,
            'body': json.dumps({
                'reply': result
            })
        }

    except Exception as e:
        # エラーハンドリング
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
