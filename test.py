from zxcvbn import zxcvbn
result = zxcvbn("password123")
print(result['score'])
