//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('formularioRegistroCtrl', ['$scope', function($scope){
	$scope.acepto = false;
	$scope.fechaValida = true;
	$scope.mayorEdad = true;
	$scope.nicknameValido = true;
	$scope.nicknamePrueba = 'holi crayholi';
	$scope.emailValido = true;
	$scope.emailPrueba = 'aaa@aaa.com';
	$scope.fecha_actual = new Date();
	$scope.this_year = parseInt($scope.fecha_actual.getYear()) + 1900;
	$scope.validarFecha = function(){
		date = new Date($scope.year,$scope.mes, '0');
		this_month = parseInt($scope.fecha_actual.getMonth() + 1);
		this_day = parseInt($scope.fecha_actual.getDate());
		resta_fechas = $scope.this_year - $scope.year;
		if(($scope.dia-0)>(date.getDate()-0)){
			$scope.fechaValida = false;
		}
		else{
			$scope.fechaValida = true;
		}
		if(this_month < $scope.mes){
			resta_fechas--;
		}
		if(($scope.mes == this_month) && (this_day < $scope.dia)){
			resta_fechas--;
		}
		if(resta_fechas > 1900){
			resta_fechas -= 1900;
		}
		if(resta_fechas >= 18){
			$scope.mayorEdad = true;
		}
		else{
			$scope.mayorEdad = false;
		}
	};
	$scope.verificarNickname = function(){
		if($scope.nickname == $scope.nicknamePrueba){
			$scope.nicknameValido = false;
		}
		else{
			$scope.nicknameValido = true;
		}
	};
	$scope.verificarEmail = function(){
		if($scope.email == $scope.emailPrueba){
			$scope.emailValido = false;
		}
		else{
			$scope.emailValido = true;
		}
	};
	$scope.validar = function(){
		return !(!$scope.fechaValida || !$scope.mayorEdad || !$scope.emailValido || !$scope.nicknameValido || $scope.registro.$invalid);
	};
}]);
//Los controladores de los menus podrían hacerse en una directiva
app.controller('menuIzquierdoCtrl', ['$scope', function($scope){
	$scope.visible = false;
	$scope.posicion1 = {
		'left' : '-305px'
	};
	$scope.posicion2 = {
		'left' : '0'
	};
	$scope.posicionIzquierda = $scope.posicion1;
	$scope.mostrarMenu= function(){
		if($scope.visible == true){
			$scope.posicionIzquierda = $scope.posicion1;
			$scope.visible = false;
		}
		else{
			$scope.posicionIzquierda = $scope.posicion2
			$scope.visible = true;
		}
	};
}]);

app.controller('menuDerechoCtrl', ['$scope', function($scope){
	$scope.visible = false;
	$scope.posicion1 = {
		'right' : '-305px'
	};
	$scope.posicion2 = {
		'right' : '0'
	};
	$scope.posicionDerecha = $scope.posicion1;
	$scope.mostrarMenu= function(){
		if($scope.visible == true){
			$scope.posicionDerecha = $scope.posicion1;
			$scope.visible = false;
		}
		else{
			$scope.posicionDerecha = $scope.posicion2
			$scope.visible = true;
		}
	};
}]);

app.controller('modalCtrl', function($scope) {
	$scope.modalShown = false;
	$scope.toggleModal = function() {
		$scope.modalShown = !$scope.modalShown;
	};
});
//Falta opcion de mostrar mensajes
app.controller('cargarObrasCtrl', ['$scope', '$routeParams', 'peticionObras', function($scope, $routeParams, peticionObras){
	$scope.cantidad = 5;
	$scope.categoria = $routeParams.categoria;
	$scope.cargar = function(nuevaCantidad){
		peticionObras.get(
			function(obras) {
				$scope.obras = obras;
			},
			function(data, status) {
				alert('Ha fallado la petición. Estado HTTP:' + status);
			},
			'recientes',
			$scope.categoria,
			'todos',
			nuevaCantidad
		);
		$scope.cantidad += 4;
	};
	$scope.cargar($scope.cantidad);
	$scope.prueba = 'http://www.google.com';
}]);

app.controller('cargarPromotoresCtrl', ['$scope', '$routeParams', 'peticionPromotores', function($scope, $routeParams, peticionPromotores){
	$scope.cantidad = 2;
	$scope.inicial  = $routeParams.inicial;
	$scope.cargar = function(nuevaCantidad){
		peticionPromotores.get(
			function(promotores) {
				$scope.promotores = promotores;
			},
			function(data, status) {
				alert('Ha fallado la petición. Estado HTTP:' + status);
			},
			'alfabetico',
			$scope.inicial,
			nuevaCantidad
		);
		$scope.cantidad += 2;
	};
	$scope.cargar($scope.cantidad);
}]);

app.controller('errorCtrl', ['$scope', '$routeParams', 'peticionObras', function($scope, $routeParams, peticionObras){
	$scope.cantidad = 3;
	$scope.cargar = function(){
		peticionObras.get(
			function(obras) {
				$scope.obras = obras;
			},
			function(data, status) {
				alert('Ha fallado la petición. Estado HTTP:' + status);
			},
			'aleatorio',
			'todas',
			'todos',
			$scope.cantidad
		);
	};
	$scope.cargar();
}]);

//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('subirObraCtrl', ['$scope', function($scope){
	$scope.maxeti = 30;
	$scope.archivo = {
		name: ''
	};
	$scope.portada = {
		name: ''
	};
	$scope.formatoArchivo = '';
	$scope.formatoPortada = '';
	$scope.archivoImagen = true;
	$scope.archivoValido = false;
	$scope.portadaValida = false;

	$scope.$on('archivoPrincipal', function (event, args) {
		$scope.$apply(function () {
			$scope.archivo = args.file;
			divisiones = $scope.archivo.name.split('.');
			$scope.formatoArchivo = divisiones[divisiones.length - 1];
			$scope.archivoValido = $scope.verificarFormato();
		});
	});
	$scope.$on('archivoPortada', function (event, args) {
		$scope.$apply(function () {
			$scope.portada = args.file;
			divisiones = $scope.portada.name.split('.');
			$scope.formatoPortada = divisiones[divisiones.length - 1];
			$scope.portadaValida = $scope.verificarImagen($scope.formatoPortada);
		});
	});
	$scope.verificarFormato = function(){
		otrosFormatos = ['pdf', 'mp3', 'aac', 'wma', 'mp4', 'mpeg', 'avi', '3gp'];
		$scope.archivoImagen = $scope.verificarImagen($scope.formatoArchivo);
		if($scope.archivoImagen == true){
			$scope.portadaValida = true;
			return true;
		}
		else{
			$scope.portadaValida = $scope.verificarImagen($scope.formatoPortada);
			for(i = 0; i < otrosFormatos.length; i++){
				if($scope.formatoArchivo == otrosFormatos[i]){
					return true;
				}
			}
		}
		return false;
	};
	$scope.verificarImagen = function(formato){
		formatosImagen = ['png', 'gif', 'jpg', 'jpeg', 'bmp', 'tiff'];
		for(i = 0; i < formatosImagen.length; i++){
			if(formato == formatosImagen[i]){
				return true;
			}
		}
		return false;
	};
	$scope.validar = function(){
		return !(!$scope.archivoValido || !$scope.portadaValida || $scope.subirobra.$invalid);
	};
}]);

//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('editarInformacionCtrl', ['$scope', function($scope){
	$scope.videoValido = true;
	$scope.portadaValida = true;
	$scope.imagenValida = true;
	$scope.video = {
		name: ''
	};
	$scope.portada = {
		name: ''
	};
	$scope.imagen = {
		name: ''
	};
	$scope.$on('archivoVideo', function (event, args) {
		$scope.$apply(function () { //add the file object to the scope's files collection
			$scope.video = args.file;
			divisiones = $scope.video.name.split('.');
			$scope.formatoVideo = divisiones[divisiones.length - 1];
			$scope.videoValido = $scope.verificarVideo($scope.formatoVideo);
		});
	});
	$scope.$on('archivoPortada', function (event, args) {
		$scope.$apply(function () { //add the file object to the scope's files collection
			$scope.portada = args.file;
			divisiones = $scope.portada.name.split('.');
			$scope.formatoPortada = divisiones[divisiones.length - 1];
			$scope.portadaValida = $scope.verificarImagen($scope.formatoPortada);
		});
	});
	$scope.$on('archivoImagen', function (event, args) {
		$scope.$apply(function () { //add the file object to the scope's files collection
			$scope.imagen = args.file;
			divisiones = $scope.imagen.name.split('.');
			$scope.formatoImagen = divisiones[divisiones.length - 1];
			$scope.imagenValida = $scope.verificarImagen($scope.formatoImagen);
		});
	});
	$scope.verificarVideo = function(formato){
		formatosVideo = ['mp4', 'mpeg', 'avi', '3gp'];
		for(i = 0; i < formatosVideo.length; i++){
			if(formato == formatosVideo[i]){
				return true;
			}
		}
		return false;
	};
	$scope.verificarImagen = function(formato){
		formatosImagen = ['png', 'gif', 'jpg', 'jpeg', 'bmp', 'tiff'];
		for(i = 0; i < formatosImagen.length; i++){
			if(formato == formatosImagen[i]){
				return true;
			}
		}
		return false;
	};
}]);

//Este controlador aun no esta escrito
app.controller('perfilArtistaCtrl', ['$scope', '$log', function($scope, $log){
	$log.log('Hola');
}]);

//Este controlador aun no esta escrito
app.controller('perfilPromotorCtrl', ['$scope', '$log', function($scope, $log){
	$log.log('Hola');
}]);

//Este controlador aun no esta escrito
app.controller('informacionPerfilCtrl', ['$scope', '$log', function($scope, $log){
	$log.log('Hola');
}]);

//Este controlador aun no esta escrito
app.controller('configuracionesCtrl', ['$scope', function($scope){
	$scope.validar = function(){
		alert('Hola ' + $scope.email + '!');
	};
}]);

//Este controlador aun no esta escrito, es necesario agregar funciones para login con vinculacion
app.controller('loginCtrl', ['$scope', function($scope){
	$scope.validar = function(){
		alert('Hola ' + $scope.email + '!');
	};
}]);
