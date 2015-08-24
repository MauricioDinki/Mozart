(function () {
    'use strict';

    function mozartUserInformationController($scope, userInformation) {
        $scope.user = {};
        var mozart_user = {};
        (function (username) {
            userInformation.get(
                function (response) {
                    var results = response.results[0];
                    mozart_user.username = results.user;
                    mozart_user.profile_picture =
                        (results.profile_picture !== null) ? results.profile_picture : '/static/img/default.png';
                    mozart_user.description =
                        (results.description === null || results.description === '') ? 'Sin descripción.' : results.description;
                    mozart_user.sex =
                        (results.sex !== null) ? results.sex : 'No disponible.';
                    mozart_user.countryCode =  results.nationality;
                },
                username,
                'extendedusers'
            );
            userInformation.get(
                function (response) {
                    var arr, names, surnames, results;
                    results = response.results[0];
                    arr = results.date_joined.split('T');
                    mozart_user.mozArtDate = arr[0];
                    names = results.first_name;
                    surnames = results.last_name;
                    mozart_user.fullname =
                        !(names === '' || surnames === '') ? names + ' ' + surnames : 'No disponible.';
                    mozart_user.email =  results.email;
                },
                username,
                'users'
            );
            userInformation.get(
                function (response) {
                    var results = response.results[0];
                    mozart_user.phoneNumber =
                        (results.phone_number !== null) ? results.phone_number : 'No disponible.';
                },
                username,
                'contacts'
            );
            userInformation.get(
                function (response) {
                    var results = response.results[0];
                    mozart_user.dateOfBirth = results.day + ' de ' + results.month + ' de ' + results.year;
                },
                username,
                'birthdays'
            );
            userInformation.get(
                function (response) {
                    var results = response.results[0];
                    mozart_user.address = results.address + ', ' + results.neighborhood + ', ' + results.city + ', ' + results.zip_code;
                    if ((results.address === null && results.city === null && results.zip_code === null && results.neighborhood === null)  || (results.address === '' && results.city === '' && results.zip_code === '' && results.neighborhood === '')) {
                        mozart_user.address = 'No disponible.';
                    } else if ((results.address === null || results.city === null || results.zip_code === null || results.neighborhood === null) || (results.address === '' || results.city === '' || results.zip_code === '' || results.neighborhood === '')) {
                        mozart_user.address += ' (Domicilio incompleto)';
                    }
                },
                username,
                'addresses'
            );
            $scope.user = mozart_user;
        }($scope.base_username));
    }

    mozartUserInformationController.$inject = ['$scope', 'userInformation'];

    angular.module('mozArtApp')
        .controller('mozartUserInformationCtrl', mozartUserInformationController);
}());