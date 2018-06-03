
# 针对区块链app应用的改进

改进了block属性，以与记忆app（一款基于区块链的心情分享、漂流瓶社交应用）配合。

```
    def new_block(self, proof: int, my_message: str, previous_hash: Optional[str]) -> Dict[str, Any]:
        """
        生成新块

        :参数proof: 工作量证明算法给出的证明
        :参数previous_hash: 上一个块的哈希值
        :return: 一个新块
        """

        block = {
            'index': len(self.chain) + 1,
            'my_message': my_message,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
```

# 以下是原作者的README

# 用Python从零开始创建区块链

本文是博客：[用Python从零开始创建区块链](http://learnblockchain.cn/2017/10/27/build_blockchain_by_python/) 的源码. 
翻译自[Building a Blockchain](https://medium.com/p/117428612f46)

[博客地址](http://learnblockchain.cn/2017/10/27/build_blockchain_by_python/)| [英文README](https://github.com/xilibi2003/blockchain/blob/master/README-en.md) 

## 安装

1. 安装 [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. 安装 [pipenv](https://github.com/kennethreitz/pipenv). 

```
$ pip install pipenv 
```

3. 创建virtual env. 

```
$ pipenv --python=python3.6
```

4. 安装依赖.  

```
$ pipenv install 
``` 

5. 运行节点:
    * `$ pipenv run python blockchain.py` 
    * `$ pipenv run python blockchain.py -p 5001`
    * `$ pipenv run python blockchain.py --port 5002`
    
## Docker运行

另一种方式是使用Docker运行：

1. 克隆库
2. 构建docker容器

```
$ docker build -t blockchain .
```

3. 运行

```
$ docker run --rm -p 80:5000 blockchain
```

4. 添加多个节点:

```
$ docker run --rm -p 81:5000 blockchain
$ docker run --rm -p 82:5000 blockchain
$ docker run --rm -p 83:5000 blockchain
```

## 贡献
[深入浅出区块链](http://learnblockchain.cn/) 想做好的区块链学习博客。
[博客地址](https://github.com/xilibi2003/learnblockchain) 欢迎大家一起参与贡献，一起推动区块链技术发展。




