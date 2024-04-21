"""
也可以在\后面跟Unicode字符编码来表示字符，例如\u9a86\u660a代表的是中文“骆昊”。

如果不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明，再看看下面的代码又会输出什么。

right-justified 使靠右对齐右对齐
justify 
    adj. 正当的; (做某事)有正当理由的; 
    v. 为…辩解(或辩护); 对…作出解释; 证明…正确(或正当、有理);
        使齐行; 调整使全行排满; 使每行排齐使…对齐
        

f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数

f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间

print(set1 ^ set2)
# print(set1.symmetric_difference(set2))



sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                    '*', sentence, flags=re.IGNORECASE)
print(purified)  # 你丫是*吗? 我*你大爷的. * you.


poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentence_list = re.split(r'[，。, .]', poem)
while '' in sentence_list:
    sentence_list.remove('')
print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']

https://deerchao.cn/tutorials/regex/regex.htm

\b	匹配单词的边界	
[^] 匹配不在字符集中的任意单一字符	

*?	重复任意次，但尽可能少重复	a.*b
a.*?b	将正则表达式应用于aabab，前者会匹配整个字符串aabab，后者会匹配aab和ab两个字符串
+?	重复1次或多次，但尽可能少重复		
??	重复0次或1次，但尽可能少重复		
{M,N}?	重复M到N次，但尽可能少重复		
{M,}?	重复M次以上，但尽可能少重复

"""

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
print(s1.rjust(40, ' '))
a, b = 5, 10
list1 = [1, 3, 5, 7, 100]
# 清空列表元素
list1.clear()

from queue import Queue
q = Queue()
q.put(1)
q.put(2)
q.put(3)
print(q.qsize())
print(q.empty())
q.queue.clear()
print(q.empty())
