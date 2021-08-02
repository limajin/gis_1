from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    # 연결된 유저객체가 삭제 됐을 때 작성자 미상의 글로 남겨두겠다
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    # 긴문자열 TextField

    created_at = models.DateField(auto_now_add=True, null=True)
    # 시간 정보 자동 입력되게