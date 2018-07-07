var app = angular.module('app', []);
app.controller('ctrl', function ($scope) {
    $scope.links = [
        {
            src: "http://www.conceptcarz.com/images/Suzuki/suzuki-concept-kizashi-3-2008-01-800.jpg",
            alt: "",
            caption: ""
        },
        {
            src: "http://www.conceptcarz.com/images/Volvo/2009_Volvo_S60_Concept-Image-01-800.jpg",
            alt: "",
            caption: ""
        },
        {
            src: "http://www.sleepzone.ie/uploads/images/PanelImages800x400/TheBurren/General/sleepzone_hostels_burren_800x400_14.jpg",
            alt: "",
            caption: ""
        },
    ];
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
