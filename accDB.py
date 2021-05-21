import sys
import os
import requests
import base64
import json
import logging
import time
import pymysql
import pandas as pd
import csv
import RDSinfo

# RDS info
host = RDSinfo.getHost()
port = RDSinfo.getPort()
username = RDSinfo.getUsername()
database = RDSinfo.getDatabase()
password = RDSinfo.getPassword()


def connect_RDS(host, port, username, password, database):  # DB와 연결
    try:
        # connect 함수를 사용하여 MySQL host 내 DB와 직접 연결
        conn = pymysql.connect(host=host, user=username, password=password, db=database, charset="utf8")

        # cursor 는 DB 와 SQL 문을 주고받는 역할
        cursor = conn.cursor()  # connect 로 연결한 DB와 상호작용하기 위한 cursor 객체

    except SystemExit:
        logging.error("RDS 에 연결되지 않았습니다.")
        sys.exit(1)

    return conn, cursor


# 가장 처음에 데이터베이스 생성할 때 한번만 수행, 지금은 데이터베이스를 만들었으니 더 이상 할 필요 x
def create_database():  # create DataBase

    # call RDS
    conn = pymysql.connect(host=host, user=username, password=password, charset="utf8")
    cursor = conn.cursor(())
    sql = "CREATE DATABASE ReadingBird"
    cursor.execute(sql)

    conn.commit()  # commit 을 날림으로서, execute() 한 결과를 DB에 반영
    conn.close()  # 연결 해제


# 가장 처음에 필요한 테이블을 생성할 때 한번만 수행, 지금은 테이블을 만들었으니 더 이상 할 필요 x
def create_table():  # crate Table
    conn, cursor = connect_RDS(host, port, username, password, database)

    sql = '''
    CREATE TABLE Quiz_Answer (
    bid int, 
    qid int,
    stage int,
    answer text,
    create_date datetime,
    correct tinyint,
    PRIMARY KEY (bid, qid, stage),
    FOREIGN KEY (bid, qid, stage) REFERENCES Quiz_Question(bid, qid, stage)
    )
    '''

    cursor.execute(sql)  # 작성한 sql 문을 실행
    conn.commit()  # commit 을 날림으로서, execute() 한 결과를 DB에 반영
    print("Query Success!")
    conn.close()


# data 삽입
def create_data():
    conn, cursor = connect_RDS(host, port, username, password, database)
    sql = "INSERT INTO Book VALUES (%s, %s)"

    cursor.execute(sql, ("1", "성냥팔이 소녀"))
    cursor.execute(sql, ("2", "라푼젤"))

    conn.commit()
    conn.close()


# data 조회
def read_data():
    conn, cursor = connect_RDS(host, port, username, password, database)
    sql = "SELECT * FROM Book where bid = %s"  # bid 가 %s 인 데이터 가져오기

    cursor.execute(sql, ("0"))  # %s 에 해당하는 값은 execute(sql)에서 매개변수로 전달한다.
    res = cursor.fetchall()  # 해당하는 모든 정보 가져오기
    # res = cursor.fetchone()  # 하나의 데이터만 가져오기

    for data in res:
        print(data)

    conn.commit()
    conn.close()


# data 수정
def update_data():
    conn, cursor = connect_RDS(host, port, username, password, database)
    cursor = conn.cursor()

    sql = "UPDATE Book SET bname = %s WHERE bid = %s"
    cursor.execute(sql, ("나의 라임 오렌지나무", "0"))

    conn.commit()
    conn.close()


# data 삭제
def delete_data():
    conn, cursor = connect_RDS(host, port, username, password, database)
    cursor = conn.cursor()

    sql = "DELETE FROM Book WHERE bid = %s"
    cursor.execute(sql, ("2"))
    conn.commit()

    conn.close()

read_data()