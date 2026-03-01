# Security Guidelines

## API Token Security

### ✓ DO:
1. Store your Kaggle API token in `.env` file
2. Keep `.env` in `.gitignore` (already configured)
3. Use environment variables to access tokens
4. Regenerate tokens if accidentally exposed
5. Use `.env.example` as a template (without real tokens)

### ✗ DON'T:
1. Never commit `.env` file to git
2. Never hardcode tokens in source code
3. Never share your token in chat/email
4. Never push tokens to GitHub/GitLab
5. Never store tokens in notebooks

## File Security Status

### Protected Files (in .gitignore):
- `.env` - Your actual API token
- `.env.local` - Local environment overrides
- `*.env` - Any environment files
- `kaggle.json` - Legacy Kaggle credentials

### Safe to Commit:
- `.env.example` - Template without real tokens
- All source code files
- Notebooks (ensure no tokens in output cells)
- Documentation

## Token Exposure Response

If you accidentally expose your token:

1. **Immediately revoke it** on Kaggle:
   - Go to https://www.kaggle.com/settings
   - Delete the exposed token
   - Generate a new one

2. **Update your .env file** with the new token

3. **Check git history**:
   ```bash
   git log --all --full-history -- .env
   ```

4. **If committed to git**, use git-filter-branch or BFG Repo-Cleaner to remove it

## Environment Variable Setup

### Option 1: Using .env file (Recommended)
```bash
# In project root
echo "KAGGLE_API_TOKEN=your_token_here" > .env
```

### Option 2: Shell environment variable
```bash
# In ~/.bashrc or ~/.zshrc
export KAGGLE_API_TOKEN=your_token_here
```

### Option 3: Temporary session
```bash
# Current terminal session only
export KAGGLE_API_TOKEN=your_token_here
python scripts/download_dataset.py
```

## Verification

Check if token is properly secured:
```bash
# Should NOT show your token
git status

# Should show .env is ignored
git check-ignore .env

# Should return: .env
```

## Additional Security Measures

1. **File permissions** (Linux/Mac):
   ```bash
   chmod 600 .env  # Only you can read/write
   ```

2. **Regular token rotation**:
   - Regenerate tokens every 3-6 months
   - Update .env file with new token

3. **Monitor usage**:
   - Check Kaggle account for unexpected API usage
   - Review access logs periodically
