import hashlib

class HashTable:
    def __init__(self):
        # 해시 테이블 초기화
        self.hash_table = [0 for i in range(8)]
        
    # 문자열을 정수로 바꿔 Key가 되게끔 함
    def get_key(self, data):
        # SHA-256 알고리즘 사용(hashlib 라이브러리)
        hash_convert = hashlib.sha256()
        hash_convert.update(data.encode())
        # 16진수로 return
        return int(hash_convert.hexdigest(), 16)
    
    # 나머지를 이용한 해시 함수
    def hash_function(self, key):
        return key % 8
    
    # 데이터를 해시 테이블에 저장하는 함수
    def save(self, data, value):
        # 키 생성
        key = self.get_key(data)
        # 생성된 키를 해시 함수에 넣음
        hash_value = self.hash_function(key)
        
        # 해시 테이블의 해당 해시 값 부분이 비어있지 않으면(같은 해시 값이 있을 경우)
        if self.hash_table[hash_value] != 0:
            for index in range(len(self.hash_table[hash_value])):
                # 한 hash address 안에 리스트가 있고, 그 리스트 안에는
                # key와 value값으로 이루어진 리스트가 또 존재함
                # ([key, value])를 요소로 가지는 연결 리스트
                # 해시 값이 같을 때, chaining 기법으로 연결된 연결 리스트를 순회
                # key값도 같다면 해당 key의 value 를 update
                
                # hash값과 key 값이 같은경우 update
                if self.hash_table[hash_value][index][0] == key:
                    self.hash_table[hash_value][index][1] = value
                    return
            # 해시 값이 같고, key값이 다른경우
            # 해당 해시 값을 인덱스로 [key, value] 연결 리스트 추가
            self.hash_table[hash_value].append([key, value])
            
        # 해시 값이 다른 경우
        else:
            # [key, value]를 요소로 하는 연결 리스트 추가
            self.hash_table[hash_value] = [[key,value]]
            
    # 데이터 조회 함수
    def read(self, data):
        # 키 생성
        key = self.get_key(data)
        # 생성된 키를 해시 함수에 넣음
        hash_value = self.hash_function(key)
        # 해시 값이 있을 경우
        if self.hash_table[hash_value] != 0:
            # 해당 해시값에 연결된 연결리스트 순회
            for index in range(len(self.hash_table[hash_value])):
                # key 를 찾았다면 해당 리스트의 [1] -> value 반환
                if self.hash_table[hash_value][index][0] == key:
                    return self.hash_table[hash_value][index][1]
                # key를 못찾았다면 None 반환
            return None
        # 해시 키도 없다면 바로 None 반환
        else:
            return None