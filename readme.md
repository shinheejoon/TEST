아이콘 과제
=========

테스트 방법
--

<pre>
python test.py
</pre>

테스트 케이스 생성방법
--
test.py -> assign_test 클래스에 메소드생성후 코드 작성

아래샘플 코드 참고
<pre>

    def test_assign_case1(self):
        res = assign.traverse_TCP_states(테스트 케이스 리스트)
        self.assertEqual(res,결과물)

</pre>

문제 풀이 방법
--
1. Trans.in파일 일 읽어온다
2. 입력 형식에 맞게 데이터를 파싱한다. 이전 상태 ->(명령어) 새로운 상태 식
3. make_transit의 메소드는 각 state클래스를 가지고 있으면 state클래스는 state의 이름과 어떠한 명령어에 의해 새로운 상태로 변이 돼는지 나타내는 그래프가 들어있다.
4. move_state의 메소드를 통하여 이전에 입력으로 구성해놓은 유한 오토마타를 이용해 상태를 변이 시킨다.
5. traverse_TCP_states함수를 통하여 상태를 변이 시킨다.

그래프를 구성할 때 파이써느이 딕셔너리를 사용하여 인접리스트 방법을 사용하였다.

 
