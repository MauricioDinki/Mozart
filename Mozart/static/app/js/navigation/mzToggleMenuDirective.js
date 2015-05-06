(function() {
	'use strict';
	
	function toggleMenuDirective(matchmedia) {
		return {
		    restrict: 'E',
		    transclude: true,
		    scope: {
		    	iconClassName: '@',
		    	currentOptionText: '@'
		    },
			controller: function ($scope) {
				$scope.originalIconClassName = $scope.iconClassName;
				$scope.buttonText = '+';
				$scope.showMenu = true;
				matchmedia.on('screen and (min-width:620px)', function(mediaQueryList) {
					if(mediaQueryList.matches) {
						$scope.showMenu = true;
						angular.element('mz-toggle-visible').css('display','none');
					}
					else {
						$scope.showMenu = false;
						$scope.iconClassName = $scope.originalIconClassName;
						$scope.buttonText = '+';
						angular.element('mz-toggle-visible').css('display','block');
					}
				});
				$scope.toggleMenu = function() {
					if($scope.showMenu) {
						$scope.iconClassName = $scope.originalIconClassName;
						$scope.buttonText = '+';
					}
					else {
						$scope.iconClassName = '';
						$scope.buttonText = '-';
					}
					$scope.showMenu = !$scope.showMenu;
				};
			},
			template: '<div class="settings-menu" ng-controller="toggleCtrl">' +
			'<mz-toggle-visible>' +
			'</mz-toggle-visible>' + 
			'<ul class="menu-list" ng-show="showMenu" ng-transclude>' +
			'</ul>' +
			'</div>'
		};
	}

	toggleMenuDirective.$inject = ['matchmedia'];

	angular.module('mozArtApp')
		.directive('mzToggleMenu', toggleMenuDirective);

	function toggleVisibleDirective(matchmedia) {
		return {
	    restrict: 'E',
	    transclude: true,
	    require: '^mzToggleMenu',
			template: '<div class="menu-option icons {$iconClassName$}">' + 
			'<span ng-hide="showMenu">{$currentOptionText$}</span>' +
			'<a class="toggle-menu-button white-background" ng-click="toggleMenu()">{$buttonText$}</a></div>'
		};
	}

	angular.module('mozArtApp')
		.directive('mzToggleVisible', toggleVisibleDirective);
})();