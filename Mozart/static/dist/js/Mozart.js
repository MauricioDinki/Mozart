(function() {
	'use strict';

	function appConfig($interpolateProvider, $httpProvider) {
		$interpolateProvider.startSymbol('{$');
		$interpolateProvider.endSymbol('$}');
		$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	}

	appConfig.$inject = ['$interpolateProvider', '$httpProvider'];

	function getWorkUrl(username, workSlug) {
		return '/profiles/' + username + '/works/' + workSlug;
	}

	function getUserProfile(username) {
		return '/profiles/' + username;
	}

	function getMonthAbbreviation() {
        return function(monthNumber) {
        	var monthAbbreviations = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        		'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec' ];
        	return monthAbbreviations[monthNumber - 1];
        };
    }

    function getHoursMinutes() {
        return function(fullTime) {
        	var array = fullTime.split(':');
        	return array[0] + ':' + array[1];
        };
    }

	angular
		.module('mozArtApp', ['ng.django.forms', 'ngAnimate', 'offClick', 'matchmedia-ng', 'hmTouchEvents'])
		.config(appConfig)
		.value('workUrl', getWorkUrl)
		.value('profileUrl', getUserProfile)
		.filter('monthAbbreviation', getMonthAbbreviation)
		.filter('hoursMinutes', getHoursMinutes);
})();
(function() {
  'use strict';

  function createEventController($scope, fileProperties, validateDates){
    var eventCoverIsValid = false;
    $scope.validDuration = true;
    $scope.validDate = true;

    function onCoverFunction(args) {
      $scope.eventCover = args.file;
      var fileFormat = fileProperties.getExtension($scope.eventCover);
      eventCoverIsValid = fileProperties.isAnImage(fileFormat);
    }

    $scope.eventCover = {
      name:''
    };

    $scope.showText = function(){
      return $scope.eventCover.name !== '';
    };
    $scope.showMessage = function(){
      return !(eventCoverIsValid || $scope.eventCover.name === '');
    };

    $scope.$on('cover', function (event, args) {
      $scope.$apply(function() {
        onCoverFunction(args);
      });
    });

    $scope.validateDate = function() {
      $scope.validDate = validateDates.futureDate($scope.eventform.date.$viewValue);
    };

    $scope.validateDuration = function() {
      $scope.validDuration = validateDates.validDuration($scope.eventform.start_time, $scope.eventform.finish_time);
    };

    $scope.validate = function(){
      return !(!$scope.validDate || !$scope.validDuration || !eventCoverIsValid || $scope.eventform.name.$invalid || $scope.eventform.description.$invalid || $scope.eventform.place.$invalid);
    };
  }

  createEventController.$inject = ['$scope', 'fileProperties', 'validateDates'];

  angular.module('mozArtApp')
    .controller('createEventCtrl', createEventController);
})();(function() {
  'use strict';

  function eventsRequestService($http, $filter, validateDates) {
    /* jshint validthis:true */
    var apiBaseUrl = '/api/events/';
    this.get = function(fnOK,fnError, creator, pageNumber) {
        var requestUrl;
        if(creator==='all') {
          requestUrl = apiBaseUrl + '?page=' + pageNumber;
        }
        else {
          requestUrl = apiBaseUrl + '?user=' + creator + '&page=' + pageNumber;
        }
        $http({
          method: 'GET',
          url: requestUrl
        })
        .success(function(data, status, headers, config) {
          fnOK(data.results, data.next);
        })
        .error(function(data, status, headers, config) {
          fnError(data,status);
        });
    };
    this.checkRepeatedEvent = function(eventsArray, _event) {
      return $filter('filter')(
        eventsArray,
        _event,
        true
      )[0] ? true: false;
    };
    this.checkFinishedEvent = function(_event) {
      console.log(validateDates.futureDate(_event.date));
      return !validateDates.futureDate(_event.date);
    };
  }

  eventsRequestService.$inject = ['$http', '$filter', 'validateDates'];

  angular.module('mozArtApp')
    .service('eventsRequest', eventsRequestService);
})();(function() {
	'use strict';

	function loadEventsController($scope, $window, eventsRequest, profileUrl) {
		$scope.showMessage = false;
		$scope.events = [];
		$scope.pageNumber = 1;
		$scope.getEvents = function(){
			eventsRequest.get(
				function(events, nextPage) {
					var prevSize = $scope.events.length;
					for(var i in events) {
						var _event = events[i];
						var isRepeated = eventsRequest.checkRepeatedEvent($scope.events, {slug: _event.slug});
						var hasFinished = eventsRequest.checkFinishedEvent(_event);
						if(!isRepeated && !hasFinished) {
							_event.userUrl = profileUrl(_event.user);
							$scope.events.push(_event);
						}
					}
					if(nextPage !== null) {
						$scope.pageNumber++;
					}
					$scope.showMessage = (prevSize === $scope.events.length);
				},
				function(data, status) {
					$window.alert('Ha fallado la petición. Estado HTTP:' + status);
				},
				$scope.eventsCreator,
				$scope.pageNumber
			);
		};
		$scope.getEvents();
	}

	loadEventsController.$inject = ['$scope', '$window', 'eventsRequest', 'profileUrl'];

	angular.module('mozArtApp')
		.controller('loadEventsCtrl', loadEventsController);
})();(function() {
  'use strict'; 

  function errorController($scope, $window, worksRequest){
    var worksAmount = 3;
    (function() {
      worksRequest.randomWorks.get(
        function(works) {
          $scope.works = works;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        'aleatorio',
        'todas',
        'todos',
        worksAmount
      );
    })();
  }

  errorController.$inject = ['$scope', '$window', 'worksRequest'];

  angular.module('mozArtApp')
    .controller('errorCtrl', errorController);
})();(function() {
	'use strict';
	
	function fileUploadDirective() {
		return {
	    restrict: 'A',
			scope: {
				fileBind : '@'
			},
			link: function (scope, el, attrs) {
				el.bind('change', function (event) {
					var files = event.target.files;
					for (var i = 0;i<files.length;i++) {
						scope.$emit(scope.fileBind, { file: files[i] });
					}
				});
			}
		};
	}

	angular.module('mozArtApp')
		.directive('fileUpload', fileUploadDirective);
})();(function() {
  'use strict';
 
  function mozartFieldDirective() {
    return {
      restrict: 'A',
      scope: false,
      transclude: false,
      link: function(scope, elem, attrs){
        if(elem.val() !== '') {
          elem.prev('label').removeClass('initial-label');
          elem.removeClass('empty-initial-field'); 
          elem.prev('label').addClass('non-active-label');
          elem.addClass('active-field');
        }
        elem.focus(function(){
          if(elem.prev('label').hasClass('initial-label')) {
            elem.prev('label').removeClass('initial-label');
          }
          else {
            elem.prev('label').removeClass('non-active-label');
          }
          elem.prev('label').addClass('active-label');
          elem.removeClass('empty-initial-field'); 
          elem.addClass('active-field');
        });
        elem.blur(function(){
          elem.prev('label').removeClass('active-label');
          if(elem.val() === '' && !((elem.hasClass('ng-valid') && elem.hasClass('ng-dirty')) || (elem.hasClass('ng-invalid') && elem.hasClass('ng-dirty')))){
            elem.removeClass('active-field');
            elem.addClass('empty-initial-field');
            if(elem.prop('tagName') === 'SELECT') {
              elem.prev('label').addClass('non-active-label');
            }
            else{
              elem.prev('label').addClass('initial-label');
            }
          }
          else {
            elem.prev('label').addClass('non-active-label');
          }
          if(elem.hasClass('ng-valid') && elem.hasClass('ng-dirty')) {
            if(elem.prev('label').hasClass('invalid-state')) {
              elem.prev('label').removeClass('invalid-state');
            }
            elem.prev('label').addClass('valid-state');
          }
          if(elem.hasClass('ng-invalid') && elem.hasClass('ng-dirty')) {
            if(elem.prev('label').hasClass('valid-state')) {
              elem.prev('label').removeClass('valid-state');
            }
            elem.prev('label').addClass('invalid-state');
          }
        });
        elem.keyup(function() {
          if(elem.hasClass('ng-invalid') && elem.hasClass('ng-dirty')) {
            if(elem.prev('label').hasClass('valid-state')) {
              elem.prev('label').removeClass('valid-state');
            }
            elem.prev('label').addClass('invalid-state');
          }
          else if(elem.hasClass('ng-valid') && elem.hasClass('ng-dirty')) {
            if(elem.prev('label').hasClass('invalid-state')) {
              elem.prev('label').removeClass('invalid-state');
            }
            elem.prev('label').addClass('valid-state');
          }
        });
      }
    };
  }

  angular.module('mozArtApp')
    .directive('mzField', mozartFieldDirective);
})();(function() {
  'use strict';
 
  function mozartMatchDirective() {
    return {
      restrict: 'A',
      require: 'ngModel',
      scope: {
        mzMatch: '='
      },
      link: function(scope, elem, attrs, ctrl){
        function compare(){
          var valid = (scope.mzMatch === ctrl.$modelValue);
          if(valid && elem.val().length >= 6) {
            if(elem.prev('label').hasClass('invalid-state')) {
              elem.prev('label').removeClass('invalid-state');
            }
            elem.prev('label').addClass('valid-state');
          }
          else if(!elem.prev('label').hasClass('initial-label')){
            if(elem.prev('label').hasClass('valid-state')) {
              elem.prev('label').removeClass('valid-state');
            }
            elem.prev('label').addClass('invalid-state');
          }
          return valid;
        }
        scope.$watch(
          compare, 
          function(currentValue) {
            ctrl.$setValidity('match', currentValue);
          }
        );
      }
    };
  }

  angular.module('mozArtApp')
    .directive('mzMatch', mozartMatchDirective);
})();(function() {
  'use strict';

  function notTriggeredOkayModalDirective() {
    return {
      restrict: 'E',
      scope: {
        modalTitle: '@',
        okayText: '@'
      },
      transclude: true,
      link: function(scope, elem, attrs) {
        scope.show = true;
        scope.hide = function() {
          scope.show = false;
        };
      },
      template: '<div class="modal-dialog-shadow" ng-show="show">' +
    '<div class="modal-dialog-container">' +
      '<h2 ng-bind="modalTitle"></h2><hr/>' +
      '<div class="modal-dialog-content" ng-transclude>' +
      '</div>' +
      '<a class="button okay-button" ng-click="hide()" ng-bind="okayText"></a>' +
    '</div>' +
  '</div>'
    };
  }

  angular.module('mozArtApp')
    .directive('mzBasicOkayModal', notTriggeredOkayModalDirective);

  function notTriggeredDecisionModalDirective() {
    return {
      restrict: 'E',
      scope: {
        modalTitle: '@',
        okayText: '@',
        cancelText: '@',
        okayLink: '@'
      },
      transclude: true,
      link: function(scope, elem, attrs) {
        scope.show = true;
        scope.hide = function() {
          scope.show = false;
        };
      },
      template: '<div class="modal-dialog-shadow" ng-show="show">' +
    '<div class="modal-dialog-container">' +
      '<h2 ng-bind="modalTitle"></h2><hr/>' +
      '<div class="modal-dialog-content" ng-transclude>' +
      '</div>' +
      '<a class="button cancel-button" ng-href="{$okayLink$}" ng-bind="okayText"></a>' +
      '<a class="button okay-button" ng-click="hide()" ng-bind="cancelText"></a>' +
    '</div>' +
  '</div>'
    };
  }

  angular.module('mozArtApp')
    .directive('mzBasicDecisionModal', notTriggeredDecisionModalDirective);

  function triggeredOkayModalDirective() {
    return {
      restrict: 'E',
      scope: {
        modalTitle: '@',
        okayText: '@',
        triggerText: '@',
        triggerButtonClass: '@'
      },
      transclude: true,
      link: function(scope, elem, attrs) {
        scope.show = false;
        scope.toggle = function() {
          scope.show = !scope.show;
        };
      },
      template: '<a class="button {$triggerButtonClass$}-button" ng-click="toggle()" ng-bind="triggerText"></a>' + 
      '<div class="modal-dialog-shadow" ng-show="show">' +
    '<div class="modal-dialog-container">' +
      '<h2 ng-bind="modalTitle"></h2><hr/>' +
      '<div class="modal-dialog-content" ng-transclude>' +
      '</div>' +
      '<a class="button okay-button" ng-click="toggle()" ng-bind="okayText"></a>' +
    '</div>' +
  '</div>'
    };
  }

  angular.module('mozArtApp')
    .directive('mzTriggeredOkayModal', triggeredOkayModalDirective);

  function triggeredDecisionModalDirective() {
    return {
      restrict: 'E',
      scope: {
        modalTitle: '@',
        okayText: '@',
        cancelText: '@',
        okayLink: '@',
        triggerText: '@',
        triggerButtonClass: '@',
        triggerButtonWeight: '@'
      },
      transclude: true,
      link: function(scope, elem, attrs) {
        scope.show = false;
        scope.toggle = function() {
          scope.show = !scope.show;
        };
      },
      template: '<a class="{$triggerButtonWeight$} {$triggerButtonClass$}-button" ng-click="toggle()" ng-bind="triggerText"></a>' + 
      '<div class="modal-dialog-shadow" ng-show="show">' +
    '<div class="modal-dialog-container">' +
      '<h2 ng-bind="modalTitle"></h2><hr/>' +
      '<div class="modal-dialog-content" ng-transclude>' +
      '</div>' +
      '<a class="button cancel-button" ng-href="{$okayLink$}" ng-bind="okayText"></a>' +
      '<a class="button okay-button" ng-click="toggle()" ng-bind="cancelText"></a>' +
    '</div>' +
  '</div>'
    };
  }

  angular.module('mozArtApp')
    .directive('mzTriggeredDecisionModal', triggeredDecisionModalDirective);
})();(function() {
	'use strict';
	
	function toggleContainerDirective() {
		return {
			restrict: 'E',
			transclude: true,
			template: '<div class="toggle-menu" ng-controller="toggleCtrl">' +
				'<ng-transclude>' +
				'</ng-transclude>' + 
				'</div>'
		};
	}

	angular.module('mozArtApp')
		.directive('mzToggleContainer', toggleContainerDirective);

	function toggleMenuDirective(matchmedia) {
		return {
		    restrict: 'E',
		    require: '^mzToggleContainer',
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
			template: '<mz-toggle-visible>' +
			'</mz-toggle-visible>' + 
			'<div class="menu-list" ng-show="showMenu" ng-transclude>' +
			'</div>'
		};
	}

	toggleMenuDirective.$inject = ['matchmedia'];

	angular.module('mozArtApp')
		.directive('mzToggleMenu', toggleMenuDirective);

	function toggleVisibleDirective(matchmedia) {
		return {
	    restrict: 'E',
	    require: '^mzToggleMenu',
			template: '<div class="menu-option icons {$iconClassName$}">' + 
			'<span ng-show="!showMenu">{$currentOptionText$}</span>' +
			'<a class="toggle-menu-button white-background" ng-click="toggleMenu()">{$buttonText$}</a></div>'
		};
	}

	angular.module('mozArtApp')
		.directive('mzToggleVisible', toggleVisibleDirective);
})();(function() {
  'use strict';

  function searchResultsController($scope, profileUrl){
    $scope.results = {
      showWorks : true,
      showUsers : false,
      works : {},
      users : {},
      aciveOptionText : 'Obras',
      nonAciveOptionText : 'Usuarios',
      aciveOptionClass : 'left-option',
      nonAciveOptionClass : 'right-option'
    };

    $scope.results.alternateResults = function() {
      if($scope.results.showWorks === false) {
        $scope.results.aciveOptionText = 'Obras';
        $scope.results.nonAciveOptionText = 'Usuarios';
        $scope.results.aciveOptionClass = 'left-option';
        $scope.results.nonAciveOptionClass = 'right-option';
      }
      else {
        $scope.results.nonAciveOptionText = 'Obras';
        $scope.results.aciveOptionText = 'Usuarios';
        $scope.results.nonAciveOptionClass = 'left-option';
        $scope.results.aciveOptionClass = 'right-option';
      }
      $scope.results.showWorks = !$scope.results.showWorks;
      $scope.results.showUsers = !$scope.results.showUsers;
    };
  }

  searchResultsController.$inject = ['$scope'];

  angular.module('mozArtApp')
    .controller('searchResultsCtrl', searchResultsController);
})();(function() {
	'use strict';

	function toggleController($scope) {
	 	$scope.isVisible = false;
	 	$scope.symbol = '+';
	 	$scope.toggle = function() {
	    	if($scope.isVisible) {
	 			$scope.symbol = '+';
	    	}
	    	else {
	    		$scope.symbol = '-';
	    	}
	    	$scope.isVisible = !$scope.isVisible;
		};
	}

	toggleController.$inject =  ['$scope'];

	angular.module('mozArtApp')
		.controller('toggleCtrl', toggleController);
})();(function() {
  'use strict';
 
  function mozartWelcomeDirective($window) {
    return {
      restrict: 'A',
      scope: {
        baseDir : "@"
      },
      transclude: false,
      link: function(scope, elem, attrs){
        var images = [scope.baseDir + 'img/fondo1.jpg', 
                      scope.baseDir + 'img/fondo2.jpg', 
                      scope.baseDir + 'img/fondo3.jpg', 
                      scope.baseDir + 'img/fondo4.jpg', 
                      scope.baseDir + 'img/fondo5.jpg'];
        elem.css({'background-image':'url(' + images[0] + ')'});
        elem
          .scroll(function (event){
            var sectionHeight = elem.innerHeight();
            var height = angular.element(event.target).scrollTop();
            if(height < sectionHeight) {
              elem.css({'background-image':'url(' + images[0] + ')'});
            }
            else if(height < 2*(sectionHeight)) {
              elem.css({'background-image':'url(' + images[1] + ')'});
            }
            else if(height < 3*(sectionHeight)) {
              elem.css({'background-image':'url(' + images[2] + ')'});
            }
            else if(height < 4*(sectionHeight)) {
              elem.css({'background-image':'url(' + images[3] + ')'});
            }
            else {
              elem.css({'background-image':'url(' + images[4] + ')'});
            }
          });
      }
    };
  }

  mozartWelcomeDirective.$inject = ['$window'];

  angular.module('mozArtApp')
    .directive('mzWelcome', mozartWelcomeDirective);
})();(function() {
  'use strict';

  function editInformationController($scope, fileProperties){
    var validVideo = true;
    var validCover = true;
    var validImage = true;

    function onVideoFile(event, args) {
      $scope.$apply(function () { 
        $scope.video = args.file;
        var fileFormat = fileProperties.getExtension($scope.video);
        validVideo = fileProperties.isAnImage(fileFormat);
      });
    }
    function onCoverFile(event, args) {
      $scope.$apply(function () { 
        $scope.cover = args.file;
        var fileFormat = fileProperties.getExtension($scope.cover);
        validCover = fileProperties.isAnImage(fileFormat);
      });
    }
    function onProfilePictureFile(event, args) {
      $scope.$apply(function () { 
        $scope.image = args.file;
        var fileFormat = fileProperties.getExtension($scope.image);
        validImage = fileProperties.isAnImage(fileFormat);
      });
    }

    $scope.video = {
      name: ''
    };
    $scope.cover = {
      name: ''
    };
    $scope.image = {
      name: ''
    };
    $scope.showText = function(){
      return $scope.image.name !== '';
    };
    $scope.showMessage = function(){
      return !(validImage || $scope.image.name === '');
    };
    $scope.$on('videoFile', onVideoFile);
    $scope.$on('coverFile', onCoverFile);
    $scope.$on('profilePicture', onProfilePictureFile);

    $scope.validate = function(){
      return !(!validImage || !validVideo || !validCover || $scope.informationform.$invalid);
    };
  }

  editInformationController.$inject = ['$scope', 'fileProperties'];

  angular.module('mozArtApp')
    .controller('editInformationCtrl', editInformationController);
})();(function() {
	'use strict';

	function loadPromotersController($scope, $window, promotersRequest, profileUrl) {
		$scope.showMessage = false;
		$scope.promoters = [];
		$scope.pageNumber = 1;
		$scope.getUsers = function(){
			promotersRequest.get(
				function(promoters, nextPage) {
					var prevSize = $scope.promoters.length;
					for(var i in promoters) {
						var user = promoters[i];
						var isRepeated = promotersRequest.checkRepeatedUser($scope.promoters, {user: user.user});
						user.picture = (user.profile_picture !== null) ? user.profile_picture : '/static/img/default.png';
						if(!isRepeated) {
							user.userUrl = profileUrl(user.user);
							$scope.promoters.push(user);
						}
					}
					if(nextPage !== null) {
						$scope.pageNumber++;
					}
					$scope.showMessage = (prevSize === $scope.promoters.length);
				},
				function(data, status) {
					$window.alert('Ha fallado la petición. Estado HTTP:' + status);
				},
				$scope.pageNumber
			);
		};
		$scope.getUsers();
	}

	loadPromotersController.$inject = ['$scope', '$window', 'promotersRequest', 'profileUrl'];

	angular.module('mozArtApp')
		.controller('loadPromotersCtrl', loadPromotersController);
})();(function() { 
  'use strict';

  function mozartUserInformationController($scope, $window, userInformation){
    $scope.user = {};
    var mozart_user = {};
    (function(username) {
      userInformation.get(
        function(results) {
          mozart_user.username = results.user;
          mozart_user.profile_picture = 
            (results.profile_picture !== null) ? results.profile_picture : '/static/img/default.png';
          mozart_user.description = 
            (results.description === null || results.description === '') ? 'Sin descripción.' : results.description;
          mozart_user.sex = 
            (results.sex !== null) ? results.sex : 'No disponible.';
          mozart_user.countryCode =  results.nationality;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        username,
        'mozart'
      );
      userInformation.get(
        function(results) {
          var arr = results.date_joined.split('T');
          mozart_user.mozArtDate = arr[0];
          var names = results.first_name;
          var surnames = results.last_name;
          mozart_user.fullname = 
            !(names === '' || surnames === '' ) ? names + ' ' + surnames : 'No disponible.';
          mozart_user.email =  results.email;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        username,
        'users'
      );
      userInformation.get(
        function(results) {
          mozart_user.phoneNumber = 
            (results.phone_number !== null) ? results.phone_number : 'No disponible.';
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        username,
        'contact'
      );
      userInformation.get(
        function(results) {
          mozart_user.dateOfBirth = results.day + ' de ' + results.month + ' de ' + results.year;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        username,
        'birth'
      );
      userInformation.get(
        function(results) {
          mozart_user.address = results.address + ', ' + results.neighborhood + ', ' + results.city + ', ' + results.zip_code;
          if((results.address === null && results.city === null && results.zip_code === null && results.neighborhood === null)  || (results.address === '' && results.city === '' && results.zip_code === '' && results.neighborhood === '')){
            mozart_user.address = 'No disponible.';
          }
          else if((results.address === null || results.city === null || results.zip_code === null || results.neighborhood === null) || (results.address === '' || results.city === '' || results.zip_code === '' || results.neighborhood === '')){
            mozart_user.address += '(Domicilio incompleto)';
          }
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        username,
        'address'
      );
      $scope.user = mozart_user;
    })($scope.base_username);
  }

  mozartUserInformationController.$inject = ['$scope', '$window', 'userInformation'];

  angular.module('mozArtApp')
    .controller('mozartUserInformationCtrl', mozartUserInformationController);
})();(function() {
  'use strict';

  function promotersRequestService($http, $filter) {
    /* jshint validthis:true */
    var apiBaseUrl = '/api/mozart/?user_type=Promotor';
    // this.get=function(fnOK,fnError, nameFirstLetter, paginate) {
    //   $http({
    //     method: 'GET',
    //     url: apiBaseUrl + '?' + 'nameFirstLetter=' + nameFirstLetter +  '&paginate=' + paginate
    //   })
    this.get=function(fnOK,fnError, paginate) {
      $http({
        method: 'GET',
        url: apiBaseUrl + '&page=' + paginate
      })
      .success(function(data, status, headers, config) {
        fnOK(data.results, data.next);
      })
      .error(function(data, status, headers, config) {
        fnError(data,status);
      });
    };
    this.checkRepeatedUser = function(usersArray, user) {
      return $filter('filter')(
        usersArray,
        user,
        true
      )[0] ? true: false;
    };
  }

  promotersRequestService.$inject = ['$http', '$filter'];

  angular.module('mozArtApp')
    .service('promotersRequest', promotersRequestService);
})();(function() {
  'use strict';

  function userInformationService($http) {
    /* jshint validthis:true */
    this.get = function(fnOK,fnError, user, information_to_get) {
      var userParameterName = 'user';
      if(information_to_get === 'users') {
        userParameterName = 'username';
      }
      $http({
        method: 'GET',
        url: '/api/' + information_to_get + '/?' + userParameterName + '=' + user
      })
      .success(function(data, status, headers, config) {
        fnOK(data.results[0]);
      })
      .error(function(data, status, headers, config) {
        fnError(data,status);
      });
    };
  }

  userInformationService.$inject = ['$http'];

  angular.module('mozArtApp')
    .service('userInformation', userInformationService);
})();(function() {
  'use strict';

  function signupFormController($scope, validateDates) {
    $scope.agree = false;
    $scope.validDate = true;
    $scope.message = '';
    $scope.dateIsDirty = false;
    $scope.validateDate = function(){
      $scope.message = validateDates.validDate($scope.day_of_birth, $scope.month_of_birth, $scope.year_of_birth, 18);
      $scope.dateIsDirty = ($scope.signupform.day_of_birth.$dirty && $scope.signupform.month_of_birth.$dirty);
      $scope.validDate = ($scope.message === 'Ok');
    };
    $scope.validate = function(){
      return !(!$scope.validDate || $scope.signupform.$invalid);
    };
  }

  signupFormController.$inject = ['$scope', 'validateDates'];

  angular.module('mozArtApp')
    .controller('signupFormCtrl', signupFormController);
})();(function() {
  'use strict';

  function validateDatesService() {
    /* jshint validthis:true */
    this.full_current_date = new Date();
    this.current_year = parseInt(this.full_current_date.getYear()) + 1900;
    this.current_month = parseInt(this.full_current_date.getMonth()) + 1;
    this.current_day = parseInt(this.full_current_date.getDate());
    this.current_date = new Date(this.current_year, this.current_month - 1, this.current_day);
    this.validDate = function(day, monthName, year, age){
      var month;
      if(isNaN(monthName)){
        month = this.getMonthNumber(monthName);
      }
      else{
        month = monthName;
      }
      var newDate = new Date(year, month, '0');
      if((day-0) <= parseInt(newDate.getDate()-0)){
        return this.validAge(day, month, year, age);
      }
      else{
        return 'La fecha que introduciste no es valida.';
      }
    };
    this.validAge = function(day, month, year, age){
      var datesDifference = this.current_year - year;
      if(this.current_month < month){
        datesDifference--;
      }
      if((month === this.current_month) && (this.current_day < day)){
        datesDifference--;
      }
      if(datesDifference > 1900){
        datesDifference -= 1900;
      }
      if(datesDifference >= age){
        return 'Ok';
      }
      else{
        return 'Lo sentimos, debes ser mayor de edad';
      }
    };
    this.futureDate = function(date) {
      var date_elements = date.split('-');
      var new_date = new Date(date_elements[0], date_elements[1] - 1, date_elements[2]);
      return new_date.getTime() - this.current_date.getTime() >= 86400000;
    };
    this.validDuration = function(start_time, finish_time) {
      var start_time_elements = String(start_time.$modelValue).split(':');
      var finish_time_elements = String(finish_time.$modelValue).split(':');

      var absolute_start_time = (parseInt(start_time_elements[0]) * 60) + parseInt(start_time_elements[1]);
      var absolute_finish_time = (parseInt(finish_time_elements[0]) * 60) + parseInt(finish_time_elements[1]);

      return absolute_finish_time >= absolute_start_time + 30;
    };
    this.getMonthNumber = function(monthName){
      if(monthName === 'Enero'){
        return 1;
      }
      else if(monthName === 'Febrero'){
        return 2;
      }
      else if(monthName === 'Marzo'){
        return 3;
      }
      else if(monthName === 'Abril'){
        return 4;
      }
      else if(monthName === 'Mayo'){
        return 5;
      }
      else if(monthName === 'Junio'){
        return 6;
      }
      else if(monthName === 'Julio'){
        return 7;
      }
      else if(monthName === 'Agosto'){
        return 8;
      }
      else if(monthName === 'Septiembre'){
        return 9;
      }
      else if(monthName === 'Octubre'){
        return 10;
      }
      else if(monthName === 'Noviembre'){
        return 11;
      }
      else if(monthName === 'Diciembre'){
        return 1;
      }
      else{
        return 0;
      }
    };
  }

  angular.module('mozArtApp')
    .service('validateDates', validateDatesService);
})();(function() {
	'use strict';

	function editWorkController($scope) {
		$scope.validate = function(){
	    return $scope.editworkform.$valid;
	  };
	}

	editWorkController.$inject = ['$scope'];

	angular.module('mozArtApp')
		.controller('editWorkCtrl', editWorkController);
})();(function() {
  'use strict';

  function filePropertiesService() {
    /* jshint validthis:true */
    this.getExtension = function(file){
      var divisions = file.name.split('.');
      var fileExtension = divisions[divisions.length -1];
      return fileExtension.toLowerCase();
    };
    this.validateFormat = function(fileExtension){
      // var validFormats = ['pdf', 'mp3', 'aac', 'wma', 'mp4', 'mpeg', 'avi', '3gp'];  Future valid formats
      var validFormats = ['mp3'];
      for(var i = 0; i < validFormats.length; i++){
        if(fileExtension == validFormats[i]){
          return true;
        }
      }
      return false;
    };
    this.isAnImage = function(fileExtension){
      var imageFormats = ['png', 'jpg', 'jpeg'];
      for(var i = 0; i < imageFormats.length; i++){
        if(fileExtension == imageFormats[i]){
          return true;
        }
      }
      return false;
    };
    this.isAVideo = function(fileExtension){
      videoFormats = ['mp4', 'mpeg', 'avi', '3gp'];
      for(var i = 0; i < videoFormats.length; i++){
        if(fileExtension == videoFormats[i]){
          return true;
        }
      }
      return false;
    };
    this.getFileSize = function(file){
      var fileSize = file.size/1024;
      return fileSize.toFixed(1);
    };
  }

  angular.module('mozArtApp')
    .service('fileProperties', filePropertiesService);
})();(function() {
	'use strict';

	function loadWorksController($scope, $window, worksRequest, workUrl, profileUrl) {
		$scope.showMessage = false;
		$scope.works = [];
		$scope.pageNumber = 1;
		$scope.getWorks = function(){
			worksRequest.recentWorks.get(
				function(works, nextPage) {
					var prevSize = $scope.works.length;
					for(var i in works) {
						var work = works[i];
						var isRepeated = worksRequest.checkRepeatedWork($scope.works, {slug: work.slug});
						if(!isRepeated) {
							work.workUrl = workUrl(work.user, work.slug);
							work.userUrl = profileUrl(work.user);
							$scope.works.push(work);
						}
					}
					if(nextPage !== null) {
						$scope.pageNumber++;
					}
					$scope.showMessage = (prevSize === $scope.works.length);
				},
				function(data, status) {
					$window.alert('Ha fallado la petición. Estado HTTP:' + status);
				},
				$scope.worksCategory,
				$scope.worksAuthor,
				$scope.pageNumber
			);
		};
		$scope.getWorks();
	}

	loadWorksController.$inject = ['$scope', '$window', 'worksRequest', 'workUrl', 'profileUrl'];

	angular.module('mozArtApp')
		.controller('loadWorksCtrl', loadWorksController);
})();(function() {
  'use strict';

  function uploadWorkController($scope, fileProperties){
    var workIsAnImage = true;
    var workFileIsValid = false;
    var workCoverIsValid = false;

    function onArchiveFunction(args) {
      $scope.workFile = args.file;
      var fileFormat = fileProperties.getExtension($scope.workFile);
      workIsAnImage = fileProperties.isAnImage(fileFormat);
      if(workIsAnImage){
        workFileIsValid = true;
        workCoverIsValid = true;
      }
      else{
        workFileIsValid = fileProperties.validateFormat(fileFormat);
        workCoverIsValid = false;
      }
    }

    function onCoverFunction(args) {
      $scope.workCover = args.file;
      var fileFormat = fileProperties.getExtension($scope.workCover);
      workCoverIsValid = fileProperties.isAnImage(fileFormat);
    }

    $scope.workFile = {
      name:''
    };
    $scope.workCover = {
      name:''
    };

    $scope.showText1 = function(){
      return $scope.workFile.name !== '';
    };
    $scope.showText2 = function(){
      return $scope.workCover.name !== '';
    };
    $scope.showMessage1 = function(){
      return !(workFileIsValid || $scope.workFile.name === '');
    };
    $scope.showMessage2 = function(){
      return !(workCoverIsValid || $scope.workCover.name === '');
    };
    $scope.showButton2 = function(){
      return !(workIsAnImage || !workFileIsValid);
    };

    $scope.$on('archive', function (event, args) {
      $scope.$apply(function() {
        onArchiveFunction(args);
      });
    });

    $scope.$on('cover', function (event, args) {
      $scope.$apply(function() {
        onCoverFunction(args);
      });
    });

    $scope.validate = function(){
      return !(!workFileIsValid || !workCoverIsValid || $scope.workform.title.$invalid || $scope.workform.description.$invalid || $scope.workform.category.$invalid);
    };
  }

  uploadWorkController.$inject = ['$scope', 'fileProperties'];

  angular.module('mozArtApp')
    .controller('uploadWorkCtrl', uploadWorkController);
})();(function() {
  'use strict';

  function worksRequestService($http, $filter) {
    /* jshint validthis:true */
    var apiBaseUrl = '/api/worksets/';
    this.recentWorks = {
      get:function(fnOK,fnError, category, author, pageNumber) {
        var requestUrl;
        if(category === 'all' && author === 'all') {
          requestUrl = apiBaseUrl + '?page=' + pageNumber;
        }
        else if(category === 'all') {
          requestUrl = apiBaseUrl + '?user=' + author + '&page=' + pageNumber;
        }
        else if(author==='all') {
          requestUrl = apiBaseUrl + '?category=' + category + '&page=' + pageNumber;
        }
        else {
          requestUrl = apiBaseUrl + '?user=' + author +  '&category=' + category + '&page=' + pageNumber;
        }
        $http({
          method: 'GET',
          url: requestUrl
        })
        .success(function(data, status, headers, config) {
          fnOK(data.results, data.next);
        })
        .error(function(data, status, headers, config) {
          fnError(data,status);
        });
      }
    };
    this.randomWorks = {
      get:function(fnOK,fnError, category, author, pageNumber) {
        var requestUrl;
        if(category === 'all' && author === 'all') {
          requestUrl = apiBaseUrl + '?page=' + pageNumber;
        }
        else if(category === 'all') {
          requestUrl = apiBaseUrl + '?user=' + author + '&page=' + pageNumber;
        }
        else {
          requestUrl = apiBaseUrl + '?category=' + category + '&page=' + pageNumber;
        }
        $http({
          method: 'GET',
          url: requestUrl
        })
        .success(function(data, status, headers, config) {
          fnOK(data.results, data.next);
        })
        .error(function(data, status, headers, config) {
          fnError(data,status);
        });
      }
    };
    this.checkRepeatedWork = function(worksArray, work, ex) {
      return $filter('filter')(
        worksArray,
        work,
        true
      )[0] ? true: false;
    };
  }

  worksRequestService.$inject = ['$http', '$filter'];

  angular.module('mozArtApp')
    .service('worksRequest', worksRequestService);
})();