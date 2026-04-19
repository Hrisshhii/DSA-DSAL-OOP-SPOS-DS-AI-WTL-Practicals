var app = angular.module("authApp", []);

app.controller("AuthController", function($scope) {

    $scope.isRegister = true;
    $scope.isLogin = false;
    $scope.isLoggedIn = false;

    $scope.user = {};
    $scope.loginData = {};
    $scope.currentUser = {};

    // Toggle
    $scope.showRegister = function() {
        $scope.isRegister = true;
        $scope.isLogin = false;
    };

    $scope.showLogin = function() {
        $scope.isRegister = false;
        $scope.isLogin = true;
    };

    // Register
    $scope.register = function() {
        localStorage.setItem("user", JSON.stringify($scope.user));
        $scope.regMessage = "✅ Registration successful!";
        $scope.user = {};
    };

    // Login
    $scope.login = function() {
        let storedUser = JSON.parse(localStorage.getItem("user"));

        if (storedUser &&
            storedUser.username === $scope.loginData.username &&
            storedUser.password === $scope.loginData.password) {

            $scope.loginMessage = "";
            $scope.isLoggedIn = true;
            $scope.currentUser = storedUser;

        } else {
            $scope.loginMessage = "❌ Invalid username or password!";
        }

        $scope.loginData = {};
    };

    // Logout
    $scope.logout = function() {
        $scope.isLoggedIn = false;
        $scope.currentUser = {};
        $scope.showLogin();
    };

});
