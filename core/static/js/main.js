var app = angular.module('myAPP', [
    'ui.router'
]);

app.constant('BASE_URL', 'http://localhost:8000/api/carousels/');

app.config(function ($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('home', {
            url: '/',
            templateUrl: '/static/templates/home.html',
            controller: 'MainCtrl'
        })
        .state('about-us', {
            url: '/about-us',
            templateUrl: '/static/templates/about.html',
            controller: 'MainCtrl'
        })
        .state('contact', {
            url: '/contact',
            templateUrl: '/static/templates/contact.html',
            controller: 'MainCtrl'
        })
        .state('add-todo', {
            url: "/add",
            templateUrl: 'static/templates/add_todo.html',
            controller: 'MainCtrl'
        });

    $urlRouterProvider.otherwise('/');
});

app.controller('MainCtrl', function ($scope, Todos, $state, $http) {
    $scope.newTodo = {};
    // $scope.message = 'Mhlengi';

    $http.get('static/json/data.json')
        .success(function (response) {
            $scope.message = response.AboutUs;
        })
        .error(function (data) {
            console.log('Could not find data.json');
        });


    $scope.addTodo = function () {
        Todos.addOne($scope.newTodo)
            .then(function (res) {
                // redirect to homepage once added
                $state.go('home');
            });
    };

    $scope.toggleCompleted = function (todo) {
        Todos.update(todo);
    };

    $scope.deleteTodo = function (id) {
        Todos.delete(id);
        // update the list in ui
        $scope.todos = $scope.todos.filter(function (todo) {
            return todo.id !== id;
        })
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
