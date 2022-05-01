Feature: 로그아웃
  Scenario: 로그아웃을 한다
    Background: 로그인
    Given 나는 앱을 열고 MY탭을 클릭한다
    When 설정으로 이동한다
    When 로그아웃을 클릭한다
    Then 로그아웃이 완료되면 메인화면으로 이동한다

