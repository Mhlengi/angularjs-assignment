var app = angular.module('app', ['ui.router', 'ngSanitize']);
app.constant('BASE_URL', 'http://localhost:8000/api/carousels/');
app.config(function ($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('home', {
            url: '/',
            controller: 'MainCtrl'
        })
        .state('about', {
            url: '/about',
            controller: 'MainCtrl'
        })
        .state('contact', {
            url: '/contact',
            controller: 'MainCtrl'
        })
        .state('carousel', {
            url: '/carousel',
            controller: 'MainCtrl'
        });
    $urlRouterProvider.otherwise('/');
});
app.controller('MainCtrl', function ($scope, Todos, $state, $http, BASE_URL) {
    $scope.about_us_text = "ABOUT US";
    $http.get('static/json/data.json')
        .success(function (response) {
            $scope.about_us_message = response.AboutUs;
        })
        .error(function (data) {
            console.log("Could not find data.json");
        });
    $scope.newTodo = {};
    $http.get(BASE_URL + '?format=json').success(function (data) {
        $scope.links = data;
    });
    $scope.isEditVisible = false;
    $scope.addTodo = function () {
        Todos.addOne($scope.newTodo)
            .then(function (res) {
                $state.go('home');
            });
        $scope.isEditVisible = true;
        $http.get(BASE_URL + '?format=json').success(function (data) {
            $scope.todos = data;
        });
    };
    $scope.toggleCompleted = function (todo) {
        Todos.update(todo);
    };
    $scope.deleteTodo = function (id) {
        Todos.delete(id);
        $scope.todos = $scope.todos.filter(function (todo) {
            return todo.id !== id;
        });
    };
    Todos.all().then(function (res) {
        $scope.todos = res.data;
    });
});
app.service('Todos', function ($http, BASE_URL) {
    var Todos = {};
    Todos.all = function () {
        return $http.get(BASE_URL + '?format=json');
    };

    Todos.update = function (updatedTodo) {
        return $http.put(BASE_URL + updatedTodo.id, updatedTodo);
    };

    Todos.delete = function (id) {
        return $http.delete(BASE_URL + id + '/');
    };

    Todos.addOne = function (newTodo) {
        return $http.post(BASE_URL, newTodo)
    };
    return Todos;
});
app.directive('carousel', function ($timeout) {
    return {
        restrict: 'E',
        scope: {
            links: '='
        },
        templateUrl: '/static/templates/carousel.html',
        link: function (scope, element) {
            $timeout(function () {
                $('.carousel-indicators li', element).first().addClass('active');
                $('.carousel-inner .item', element).first().addClass('active');
            });
        }
    }
});
