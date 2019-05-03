

```python
import pycorrector
```


```python
corrected_sent, detail = pycorrector.correct('你菛不跟我我就送')
print(corrected_sent, detail)
```

    你们不跟我我就送 [['菛', '们', 1, 2]]



```python
corrected_sent, detail = pycorrector.correct('我等你表演中路等你表演。')
print(corrected_sent, detail)
```

    我等你表演中路等你表演。 []



```python
corrected_sent, detail = pycorrector.correct('讼我鲁班的皮肤')
print(corrected_sent, detail)
```

    送我鲁班的皮肤 [['讼', '送', 0, 1]]



```python
corrected_sent, detail = pycorrector.correct('踒方有一个送了十个人头')
print(corrected_sent, detail)
```

    我放有一个送了十个人头 [['踒', '我', 0, 1], ['方有', '放有', 1, 3]]



```python
corrected_sent, detail = pycorrector.correct('安琪拉再送屻头的话，我就举报他。')
print(corrected_sent, detail)
```

    安琪拉在送人头的话，我就举报他。 [['再', '在', 3, 4], ['屻', '人', 5, 6]]



```python
corrected_sent, detail = pycorrector.correct('你先送我几个人头，我不会帵他。')
print(corrected_sent, detail)
```

    你先送我几个人头，我不会完他。 [['帵', '完', 12, 13]]

