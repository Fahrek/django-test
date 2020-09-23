document.getElementById('form-demo-voice').addEventListener('click', function(event) {
   event.preventDefault();

   var spinner     = document.getElementsByClassName('spinner-wrapper')[0];
   var fieldLabels = [].slice.call(document.querySelectorAll('label'));
   var promise     = new Promise(function(resolve) {
      resolve();
   });

   var formData = function(i) {
      return promise.then(function() {
                 return Speech.speak(fieldLabels[i].dataset.question);
              })
              .then(function() {
                 spinner.classList.remove('hidden');
                 return Speech.recognize().then(function(text) {
                    spinner.classList.add('hidden');
                    document.getElementById(fieldLabels[i].getAttribute('for')).value = text;
                 });
              });
   };

   for(var i = 0; i < fieldLabels.length; i++) {
      promise = formData(i);
   }

   promise.then(function() {
      return Speech.speak('Gracias por rellenar el formulario!');
   })
   .catch(function(error) {
     spinner.classList.add('hidden');
     alert(error);
   });
});


/* SUPPORT OBJECT */
var Speech = {
   speak: function(text) {
      return new Promise(function(resolve, reject) {
         if (!SpeechSynthesisUtterance) {
            reject('API not supported');
         }

         var utterance = new SpeechSynthesisUtterance(text);

         utterance.addEventListener('end', function() {
            console.log('Synthesizing completed');
            resolve();
         });

         utterance.addEventListener('error', function (event) {
            console.log('Synthesizing error');
            reject('An error has occurred while speaking: ' + event.error);
         });

         console.log('Synthesizing the text: ' + text);
         speechSynthesis.speak(utterance);
      });
   },
   recognize: function() {
      return new Promise(function(resolve, reject) {
         var SpeechRecognition = SpeechRecognition        ||
                                 webkitSpeechRecognition  ||
                                 null;

         if (SpeechRecognition === null) {
            reject('API not supported');
         }

         var recognizer = new SpeechRecognition();

         recognizer.addEventListener('result', function (event) {
            console.log('Recognition completed');
            for (var i = event.resultIndex; i < event.results.length; i++) {
               if (event.results[i].isFinal) {
                  resolve(event.results[i][0].transcript);
               }
            }
         });

         recognizer.addEventListener('error', function (event) {
            console.log('Recognition error');
            reject('An error has occurred while recognizing: ' + event.error);
         });

         recognizer.addEventListener('nomatch', function (event) {
            console.log('Recognition ended because of nomatch');
            reject('Error: sorry but I could not find a match');
         });

         recognizer.addEventListener('end', function (event) {
            console.log('Recognition ended');
            // If the Promise isn't resolved or rejected at this point
            // the demo is running on Chrome and Windows 8.1 (issue #428873).
            reject('Error: sorry but I could not recognize your speech');
         });

         console.log('Recognition started');
         recognizer.start();
      });
   }
};