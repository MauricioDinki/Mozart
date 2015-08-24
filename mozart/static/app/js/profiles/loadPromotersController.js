(function () {
    'use strict';

    function loadPromotersController($scope, baseController, promotersRequest, profileUrl) {
        function extraFunction(user) {
            user.picture = (user.profile_picture !== null) ? user.profile_picture : '/static/img/default.png';
            user.userUrl = profileUrl(user.user);
            return user;
        }
        $scope = baseController.getController($scope, 'promoters', 'getUsers', promotersRequest.get, promotersRequest.checkRepeatedUser,
                'user', [extraFunction], []);
        $scope.getUsers();
    }

    loadPromotersController.$inject = ['$scope', 'baseController', 'promotersRequest', 'profileUrl'];

    angular.module('mozArtApp')
        .controller('loadPromotersCtrl', loadPromotersController);
}());