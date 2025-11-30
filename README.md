# openai-in-action
Source code for the book OpenAI in Action by KnoDAX

# 🔑 How to Set Up Your OpenAI API Key
To run the examples in this repository, you must configure an **OpenAI API key**. This key authenticates your requests to OpenAI’s GPT models. Follow the steps below to create, store, and securely use your key.

---

## ✅ 1. Create or Log In to Your OpenAI Account

1. Go to [https://platform.openai.com](https://platform.openai.com)
2. Click **Sign Up** if you don’t have an account
3. Click **Log In** if you already have one

---

## ✅ 2. Navigate to the API Keys Page

In your OpenAI dashboard:

* Open the **User menu**
* Select **API Keys**
* This is where you manage, create, or delete keys

---

## ✅ 3. Generate a New API Key

1. Click **Create New Secret Key**
2. Copy the key immediately — it will only appear once
3. Store it securely (password manager recommended)

If you misplace it, generate a new one.

---

# ⚙️ 4. Configure Your Application

## Install the OpenAI Python Library

```bash
pip install openai
```

## Use the API Key in Python (not recommended for production)

```python
import openai

openai.api_key = "your-api-key"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="What is AI?",
    max_tokens=50
)

print(response.choices[0].text.strip())
```

---

# 🔐 5. Recommended: Store Your Key as an Environment Variable

Hardcoding your key in notebooks or scripts can expose it.
Instead, store it using environment variables.

---

## 🖥️ macOS / Linux

### Temporary (session only)

```bash
export OPENAI_API_KEY="your-api-key"
```

Verify:

```bash
echo $OPENAI_API_KEY
```

### Permanent (recommended)

Edit your shell config:

```bash
nano ~/.zshrc   # or ~/.bashrc
```

Add:

```bash
export OPENAI_API_KEY="your-api-key"
```

Apply changes:

```bash
source ~/.zshrc
```

---

## 🪟 Windows

1. Open **Environment Variables**

2. Under *User variables*, click **New**

3. Add:

   * Variable name: `OPENAI_API_KEY`
   * Variable value: `your-api-key`

4. Save and close

5. Verify in PowerShell or CMD:

```cmd
echo %OPENAI_API_KEY%
```

---

# 🧪 6. Test Your Setup

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
print(f"Your API key is: {api_key}")
```

If your key prints correctly, everything is configured.

---

# 📊 7. Manage and Monitor API Keys

In your OpenAI dashboard:

* Monitor usage
* Delete unused keys
* Regenerate keys regularly
* Immediately revoke compromised keys

---

# 🎉 Your OpenAI API Key Is Ready to Use

You can now run all examples, notebooks, and projects in the **OpenAI in Action** repository.

