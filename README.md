# 🧪 Azure AI Custom Evaluators 範例
本範例說明如何在本機執行2個自訂的客製指標（Clarity、Helpfulness），並針對指定的 LLM Response 資料集（`dataset.jsonl`）進行評估，其評估結果會上傳至Azure AI Foundry Project中作呈現。請依下列步驟完成環境設定與範例程式碼執行。

## 專案結構
```text
azure-ai-custom-evaluators/
├─ clarity.py                     # Clarity 客製指標實作（句長、冗長比例等）
├─ clarity_evaluation.py          # Clarity 客製指標範例
├─ helpfulness.py                 # Helpfulness 客製指標（透過 promptflow + LLM）
├─ helpfulness_evaluation.py      # Helpfulness 客製指標範例
├─ helpfulness.prompty            # Helpfulness 的 promptflow 定義
├─ local_evaluation.py            # 對 dataset.jsonl 執行批次評估並輸出結果
├─ dataset.jsonl                  # 測試資料（JSONL）
├─ requirements.txt               # pip 依賴
├─ pyproject.toml                 # 專案定義（含 Python 版本要求）
├─ sample_env_rename_it           # 環境變數樣板，請另存為 .env
└─ myevalresults.json             # 執行後產生的本機評估結果（檔案不存在時會新增）
```

## 資料集格式（dataset.jsonl）
- 檔案類型為 JSON Lines；每行至少包含：
  - `id`: 範例識別碼
  - `response`: 要評估的答案文字
- 範例內容：
  ```jsonl
  {"id": "1", "response": "The process has three steps. First, submit your form online..."}
  {"id": "2", "response": "In order to achieve the objective, it is necessary that the applicant..."}
  ```

## 步驟一：準備環境
- Python 環境
  - Python 版本至少 3.8
    - 此專案的 `pyproject.toml` 是指定 `requires-python == 3.11.12`，僅供參考
    - 檢查 Python 版本，以 Windows 環境為例，透過 PowerShell 執行
        ```powershell
        python --version
        ```

- Azure AI Foundry 資源
    - 前往 Azure AI Foundry Portal：[https://ai.azure.com/](https://ai.azure.com/) 
    - 新增或找到既有的 AI 專案，並進入專案頁面
    - 前往「Endpoints and keys」或「端點與金鑰」查看，如下圖所示
        ![complete](azure-ai-get-language-endpoint-and-key.png)

    - 取得 Azure AI Services 的 Endpoint 與 Key，將於步驟五中使用
        - `AZURE_AI_FOUNDRY_PROJECT_ENDPOINT`
        - `AZURE_OPENAI_ENDPOINT`
        - `AZURE_AI_KEY`
        - `MODEL_EVALUATION_DEPLOYMENT_NAME`
        - `MODEL_GENAIAPP_DEPLOYMENT_NAME`

## 步驟二：取得或切換到此資料夾
- 使用 Git：
    ```powershell
    git clone https://github.com/ownway22/azure-ai-custom-evaluators.git
    cd <你的-repo資料夾>/azure-pii-sample-code
    ```

- 或直接將本資料夾下載到本機。

## 步驟三：啟動虛擬環境
- 在 `<你的-repo資料夾>/azure-pii-sample-code` 目錄下執行：
    ```powershell
    python -m venv .venv                # 建立虛擬環境
    .venv\Scripts\Activate              # 啟動虛擬環境
    ```

## 步驟四：安裝相依套件
- 本專案提供 `requirements.txt` 和 `pyproject.toml` 做安裝
- 以 `requirements.txt` 為例
    ```powershell
    python -m pip install --upgrade pip # 升級 pip
    pip install -r requirements.txt     # 安裝相依套件
    ```

## 步驟五：準備環境變數
- 將 `.env_example` 另存為 `.env`
- 貼上步驟一的5個環境變數

## 步驟六：執行範例與評估
你可以選擇單獨執行客製指標的範例，或直接執行批次評估。

1) 客製指標範例1 - 「清晰度（Clarity）」
    ```powershell
    python .\clarity_evaluation.py

    # 或使用 uv（若已安裝）
    uv run .\clarity_evaluation.py
    ```

2) 客製指標範例2 - 「有用性（Helpfulness）」
    ```powershell
    python .\helpfulness_evaluation.py

    # 或使用 uv（若已安裝）
    uv run .\helpfulness_evaluation.py
    ```

3) 以上述兩個指標針對 LLM Response 資料集（`dataset.jsonl`）進行評估，並將評估結果存成 `myevalresults.json`
    ```powershell
    # 使用 python
    python .\local_evaluation.py

    # 或使用 uv（若已安裝）
    uv run .\local_evaluation.py
    ```

## 輸出結果
- 批次評估會在專案根目錄輸出 `myevalresults.json`。
- 若 `.env` 內提供且有效的 `AZURE_AI_FOUNDRY_PROJECT_ENDPOINT`，結果也會嘗試上傳至 Azure AI Studio 專案。
  - 若上傳失敗（例如 404/Resource not found），指令會顯示警告並自動改為僅本機輸出，不會中斷流程。

## 疑難排解（Troubleshooting）
- 遙測上傳 404／Resource not found：
  - 檢查 `AZURE_AI_FOUNDRY_PROJECT_ENDPOINT` 是否為有效的 HTTP(S) URL，且確實指向你要上傳的 Azure AI Studio 專案。
  - 若仍失敗，指令會自動退回本機輸出 `myevalresults.json`。

- Helpfulness 客製指標失敗或回傳空分數：
  - 確認 `.env` 已填入 `AZURE_OPENAI_ENDPOINT`、`MODEL_EVALUATION_DEPLOYMENT_NAME`、`AZURE_AI_KEY`。
  - 確認你的模型部署可用，且帳戶具備呼叫權限。
  - 檢查 `helpfulness.prompty` 是否存在且可被 `promptflow` 載入。

- 套件安裝問題：
  - 優先確認已啟動本資料夾下的 `.venv` 後再安裝。
  - 若使用 `pip` 仍遇到相依衝突，可嘗試 `uv pip install -r requirements.txt`。

## Reference
1. [Custom evaluators - Azure AI Foundry | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/custom-evaluators)

2. [Building Your Own Custom Evaluator for GenAI Apps, Agents, and Models Using Azure AI Foundry SDK - DEV Community](https://dev.to/icebeam7/building-your-own-custom-evaluator-for-genai-apps-agents-and-models-using-azure-ai-foundry-sdk-1okg)