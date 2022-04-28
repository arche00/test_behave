Feature: 로그인
  Scenario: 이메일로 로그인 한다
    Given 나는 앱을 열고 로그인을 클릭한다
    When 로그인 선택에서 이메일로 로그인을 선택한다
    When teacher04@sharklasers.com 과 a1234567 를 입력하고 로그인한다
    Then 로그인이 완료되면 소식탭으로 포커스가 된다