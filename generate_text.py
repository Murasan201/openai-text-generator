import os
import openai

# 環境変数から API キーを取得して設定
oai_key = os.getenv("OPENAI_API_KEY")
if not oai_key:
    raise RuntimeError("環境変数 OPENAI_API_KEY が設定されていません")
openai.api_key = oai_key


def generate_text(prompt: str) -> str:
    """
    ChatCompletion API を用いて o4-mini モデルから応答を取得する関数。

    Args:
        prompt (str): ユーザーからのプロンプト文字列
    Returns:
        str: モデルからの生成テキスト
    """
    response = openai.chat.completions.create(
        model="o4-mini",
        messages=[
            {"role": "system", "content": (
                "あなたは親切で知識豊富なアシスタントです。ユーザーの質問に対して明確で分かりやすい回答を提供してください。"
                "常に具体的な内容を含む回答をし、空の応答は絶対に返さないでください。"
            )},
            {"role": "user", "content": prompt}
        ],
        max_completion_tokens=1000,
    )
    # デバッグ用ログを出力（必要に応じてコメントアウト）
    print("DEBUG:", response)
    # 生成されたテキストを返却
    content = response.choices[0].message.content
    if not content:
        return "応答が生成されませんでした。再度お試しください。"
    return content.strip()


if __name__ == "__main__":
    sample_prompt = "LLMの最新の技術動向について簡潔に教えてください。"
    print("=" * 60)
    print("OpenAI o4-mini モデル テキスト生成デモ")
    print("=" * 60)
    print(f"プロンプト: {sample_prompt}")
    print("-" * 60)
    print("LLM応答:")
    print("-" * 60)
    generated_text = generate_text(sample_prompt)
    print(generated_text)
    print("=" * 60)
