# browser_back

The English version is the second half 
このスクリプトは、毎朝9:00（日本時間）に指定したページでブラウザバックを行うものです。

1. **Pythonのインストール**  
このスクリプトを実行するためには、Pythonがインストールされている環境が必要です。Pythonがまだインストールされていない場合は、[公式サイト](https://www.python.org/downloads/)からインストールしてください。 

2. **必要なライブラリをインストールする**
```bash
pip install selenium webdriver-manager pytz
```

3.  **URLの設定**  
   スクリプト内の `url` 変数に、最初にアクセスしたいページのURLを指定します（デフォルトは `"https://example.com"` ですが、任意のURLに変更してください）。

4. **スクリプトの実行**  
   ```bash
   python browser_back.py
   ```

5. **スクリプトの停止**

スクリプトを終了したいときは、ターミナルで **Ctrl + C** を押すと停止します。これにより、ブラウザも自動的に閉じられます。

### 注意事項

- **スクリプトは常時実行が必要です**: 毎朝9:00に実行するため、このスクリプトは一日中実行されている必要があります。スリープモードやシャットダウンすると動作しなくなりますので注意してください。
- **タイムゾーン設定**: `Asia/Tokyo`タイムゾーン（日本標準時）に設定されていますが、他のタイムゾーンで使いたい場合は、適切なタイムゾーンに置き換えることができます。

---
This script automatically performs a browser back action on the specified page every morning at 9:00 AM (Japan Standard Time).

1. **Install Python**  
   To run this script, make sure Python is installed. If it is not yet installed, download it from the [official website](https://www.python.org/downloads/).

2. **Install necessary libraries**  
   ```bash
   pip install selenium webdriver-manager pytz
   ```

3. **Specify the URL**  
   In the script, set the `url` variable to the page you want to open initially (the default is `"https://example.com"`; you can change it to any URL).

4. **Run the script**  
   ```bash
   python browser_back.py
   ```

5. **Stop the script**  
   To stop the script, press **Ctrl + C** in the terminal. This will close the browser automatically.

### Important Notes

- **The script needs to run continuously**: Since it performs the action daily at 9:00 AM, this script needs to stay active. It will not work if your computer goes to sleep or shuts down, so keep this in mind.
- **Timezone setting**: The script is set to `Asia/Tokyo` timezone (Japan Standard Time), but if you want to use it in another timezone, simply replace it with the appropriate timezone setting.
