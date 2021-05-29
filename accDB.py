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
from datetime import datetime

# RDS info
host = RDSinfo.getHost()
port = RDSinfo.getPort()
username = RDSinfo.getUsername()
database = RDSinfo.getDatabase()
password = RDSinfo.getPassword()


def connect_RDS(Host, Port, Username, Password, Database):  # DB와 연결
    try:
        # connect 함수를 사용하여 MySQL host 내 DB와 직접 연결
        conn = pymysql.connect(host=host, user=Username, password=Password, db=Database, charset="utf8")

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
    sql1 = '''
    CREATE TABLE Book (
    bid int,
    bname varchar(255),
    PRIMARY KEY (bid)
    )
    '''

    sql2 = '''
    CREATE TABLE Report_Subject (
    bid int,
    contents text,
    create_date datetime,
    PRIMARY KEY (bid),
    FOREIGN KEY (bid) REFERENCES Book(bid)
    )
    '''

    sql3 = '''
    CREATE TABLE Quiz_Question (
    cid int,
    bid int,
    qid int,
    stage int,
    question text,
    mp varchar(255),
    PRIMARY KEY (cid, bid, qid, stage),
    FOREIGN KEY (bid) REFERENCES Book(bid)
    )
    '''

    sql4 = '''
    CREATE TABLE Quiz_Answer (
    cid int,
    bid int,
    qid int,
    stage int,
    answer text,
    create_date datetime,
    correct tinyint,
    PRIMARY KEY (cid, bid, qid, stage),
    FOREIGN KEY (bid, cid, qid, stage) REFERENCES Quiz_Question(bid, cid, qid, stage)
    )
    '''

    sql5 = '''
    CREATE TABLE Freetalk_Subject (
    sid int,
    situation varchar(255),
    PRIMARY KEY (sid)
    )
    '''

    sql6 = '''
    CREATE TABLE Freetalk_Speaker_Speech (
    sid int,
    pid int,
    stage int,
    speech text,
    mp varchar(255),
    PRIMARY KEY (sid, pid, stage),
    FOREIGN KEY (sid) REFERENCES Freetalk_Subject(sid)
    )
    '''

    sql7 = '''
    CREATE TABLE Freetalk_User_Speech (
    sid int,
    pid int,
    stage int,
    answer text,
    create_date datetime,
    correct int,
    PRIMARY KEY (sid, pid, stage),
    FOREIGN KEY (sid, pid, stage) REFERENCES Freetalk_Speaker_Speech(sid, pid, stage)
    )
    '''

    cursor.execute(sql)  # 작성한 sql 문을 실행

    conn.commit()  # commit 을 날림으로서, execute() 한 결과를 DB에 반영
    print("Query Success!")
    conn.close()


# data 삽입
def create_data():
    conn, cursor = connect_RDS(host, port, username, password, database)
    sql = "INSERT INTO Quiz_Question VALUES (%s, %s, %s, %s, %s, %s)"
    now = datetime.now()
    # cid bid qid stage question MP
    cursor.execute(sql, ("0", "1", "1", "0", "성냥팔이 소녀가 성냥을 한 상자도 팔지 못했을 때 기분이 어땠을까요?", "두려,고려,무서,무섭,걱정"))
    cursor.execute(sql, ("0", "1", "1", "1", "왜 그렇게 생각했나요?", "아빠,아버지,화,분노,두려,무서,무섭"))
    cursor.execute(sql, ("0", "1", "2", "0", "소녀가 성냥에 불을 붙여 따뜻한 음식들과 난로를 보았을 때 기분이 어땠을까요?", "행복,기뻤,꿈,깁,집,지"))
    cursor.execute(sql, ("0", "1", "2", "1", "왜 그렇게 생각했나요?", "원했,갖고,희망,소망"))
    cursor.execute(sql, ("0", "1", "3", "0", "소녀가 할머니를 봤을 때 기분이 어땠을까요?", "행복,기뻤,꿈,깁,집,지"))
    cursor.execute(sql, ("0", "1", "3", "1", "왜 그렇게 생각했나요?", "그리워,보고싶"))
    cursor.execute(sql, ("0", "1", "4", "0", "길에서 성냥팔이 소녀를 발견한 사람들의 기분은 어땠을까요?", "안타까,불쌍,가엾,가여,됐다,없,엽"))
    cursor.execute(sql, ("0", "1", "4", "1", "왜 그렇게 생각했을까요?", "외로,외롭,혼자,안타까,불쌍,누워,누웠"))

    cursor.execute(sql, ("1", "1", "0", "0", "소녀는 무엇을 입고 있었나요?", "드레스,목도리"))
    cursor.execute(sql, ("1", "1", "0", "1", "왜 그런옷을 입고 있었을까요?", "돈,경제,여유,가난"))
    cursor.execute(sql, ("1", "1", "1", "0", "성냥을 다못팔면 아빠는 어떻게 행동할 것 같나요?", "화,혼"))
    cursor.execute(sql, ("1", "1", "1", "1", "왜 그렇게 행동할까요?", ""))
    cursor.execute(sql, ("1", "1", "2", "0", "성냥을 사용하지 않았다고 얘기한것은 거짓말인가요 아닌가요?", "거짓말"))
    cursor.execute(sql, ("1", "1", "2", "1", "왜 거짓말을 했을까요?", "성냥,사용,못"))
    cursor.execute(sql, ("1", "1", "3", "0", "음식은 진짜인가요?", "아니,가짜"))
    cursor.execute(sql, ("1", "1", "3", "1", "가짜인 음식이 왜 보였을까요?", "맛있는,배고파,먹고"))
    cursor.execute(sql, ("1", "1", "4", "0", "소녀는 무엇을 기도했을까요?", "행복,즐거움,기쁨,맛,따뜻"))
    cursor.execute(sql, ("1", "1", "4", "1", "왜 그렇게 생각했나요?", "힘들,배고,추워,슬픔,가난"))
    cursor.execute(sql, ("1", "1", "5", "1", "친구가 주인공이였다면 성냥에 불을 붙였을때 어떤것이 나타났을 것 같나요?", ""))
    cursor.execute(sql, ("1", "1", "6", "0", "성냥팔이 소녀가 가장 보고 싶었던 사람은 누구였을까요?", "할"))
    cursor.execute(sql, ("1", "1", "6", "1", "할머니를 보기위해 성냥팔이 소녀는 어떻게 했나요?", "성냥,하나,더"))
    cursor.execute(sql, ("1", "1", "6", "2", "성냥을 켰을 때 할머니가 어떻게 됐나요?", "사라,없어"))
    cursor.execute(sql, ("1", "1", "7", "0", "마지막에 성냥팔이 소녀는 어떻게 됐나요?", "죽어,죽었,사라"))
    cursor.execute(sql, ("1", "1", "7", "1", "그때 소녀는 어떤 기분이였을까요?", ""))

    cursor.execute(sql, ("2", "1", "0", "0", "What caused the girl's death?", "cold"))
    cursor.execute(sql, ("2", "1", "1", "0", "What did the girl want from the vision of the match?", "happiness"))
    cursor.execute(sql, ("2", "1", "2", "0", "What day did the story take place?", "one"))
    cursor.execute(sql, ("2", "1", "3", "0", "What caused the girl to use matches the most?", "grandmother,vision"))
    cursor.execute(sql, ("2", "1", "4", "0", "How the girl felt through matches?", "craving,longing,liberation"))
    cursor.execute(sql, (
    "2", "1", "5", "0", "What did the girl see through the match?", "burning,stove,food,christmas,tree,grand"))
    cursor.execute(sql, (
    "2", "1", "6", "0", "The reason why the girl didn't go home", "father,daddy,dad,angry,tell off,mathes"))

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


# data 조회
def select_question(cid, bid, qid, stage):
    conn, cursor = connect_RDS(host, port, username, password, database)
    sql = "SELECT question, mp FROM Quiz_Question where cid = %s and bid = %s and qid = %s and stage =%s"  # bid 가 %s 인 데이터 가져오기

    cursor.execute(sql, (cid, bid, qid, stage))  # %s 에 해당하는 값은 execute(sql)에서 매개변수로 전달한다.
    res = cursor.fetchall()  # 해당하는 모든 정보 가져오기
    # res = cursor.fetchone()  # 하나의 데이터만 가져오기

    for data in res:
        return data

    conn.commit()
    conn.close()


# data 수정
def update_data():
    conn, cursor = connect_RDS(host, port, username, password, database)
    cursor = conn.cursor()

    sql = "UPDATE Quiz_Question SET stage= %s WHERE cid = %s and bid = %s and qid = %s"
    cursor.execute(sql, ("0", "1", "1", "5"))

    conn.commit()
    conn.close()


# data 삭제
def delete_data():
    conn, cursor = connect_RDS(host, port, username, password, database)
    cursor = conn.cursor()

    sql = "DELETE FROM Report_Subject WHERE bid = %s"
    cursor.execute(sql, ("1"))
    conn.commit()

    conn.close()


# quiz answer 삽입
def insert_quiz_answer(bid, qid, stage, answer, correct):
    conn, cursor = connect_RDS(host, port, username, password, database)
    sql = "INSERT INTO Quiz_Answer VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (bid, qid, stage, answer, datetime.now(), correct))

    conn.commit()
    conn.close()


# book report 삽입
def insert_book_report(bid, contents):
    conn, cursor = connect_RDS(host, port, username, password, database)
    sql = "INSERT INTO Report_Subject VALUES (%s, %s, %s)"
    cursor.execute(sql, (bid, contents, datetime.now()))

    conn.commit()
    conn.close()