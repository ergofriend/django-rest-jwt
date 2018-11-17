# REST API SERVER

## PATH

- admin/
- api/
- api/auth

## Tips

### models.py

#### タイムスタンプ

created と modified を提供 [django-model-utils](https://django-model-utils.readthedocs.io/en/latest/models.html#timestampedmodel)

```python
from model_utils.models import TimeStampedModel
# models.Modelの代わりに
class Ticket(TimeStampedModel):
```

## 参考にしたサイト

[REST framework 公式ドキュメント](https://www.django-rest-framework.org)

[djoser 公式ドキュメント](https://djoser.readthedocs.io)

[Building An API With Django 2.0: Part I](https://tag1consulting.com/blog/building-api-django-20-part-i)

[Django 2.0 リリース！ 最新の Django で作るカンバンボードアプリ ～ モデルの定義と Django REST framework の実装](https://codezine.jp/article/detail/10722)
