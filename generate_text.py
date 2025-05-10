import os
import openai

# 環境変数から API キーを取得して設定
oai_key = os.getenv("OPENAI_API_KEY")
if not oai_key:
    raise RuntimeError("環境変数 OPENAI_API_KEY が設定されていません")
openai.api_key = oai_key


def generate_text(prompt: str) -> str:
    """
    ChatCompletion API を用いて GPT-4 モデルから応答を取得する関数。

    Args:
        prompt (str): ユーザーからのプロンプト文字列
    Returns:
        str: モデルからの生成テキスト
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": (
                "You are a helpful assistant who provides detailed and informative responses. "
                "Please elaborate on the latest technological trends with examples when possible. "
                "Ensure your response is complete and not empty."
            )},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
    )
    # デバッグ用ログを出力
    print("DEBUG:", response)
    # 生成されたテキストを返却
    return response.choices[0].message["content"].strip()


if __name__ == "__main__":
    sample_prompt = "LLMの最新の技術動向について200文字程度で教えてください。"
    print("Prompt:", sample_prompt)
    generated_text = generate_text(sample_prompt)
    print("Generated Text:")
    print(generated_text)
