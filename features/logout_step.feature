Feature: 로그아웃
  Scenario: 로그아웃을 한다
    Given 나는 앱을 열고 MY탭을 클릭한다
    When 설정으로 이동한다
    And 로그아웃을 클릭힌다
    Then 로그아웃이 완료되면 메인화면으로 이동한다