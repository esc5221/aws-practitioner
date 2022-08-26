### Markdown에서 Toggle 사용
``` html
<details>
<summary>정답</summary>

</details>
```

### 정답 선택 regex pattern
```
(?<=\n)[A-E](,\s[A-Z])?.*(?<!\.|\?)\n
(?<=\n)[A-E](\s|,\s[A-Z]).*(?<!\.|\?|[a-z])\n
(?<=\n)[A-E](?=\n|\,\s[A-Z]).*(?<!\.|\?|[a-z])\n
```