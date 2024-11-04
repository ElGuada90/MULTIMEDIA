const video = document.querySelector('video');

        function playPause() {
            if (video.paused) {
                video.play();
            } else {
                video.pause();
            }
        }

        function makeBig() {
            video.style.width = '150%';
            video.style.margin = '0';
        }

        function makeSmall() {
            video.style.width = '50%';
            video.style.margin = '0 auto';
        }

        function makeNormal() {
            video.style.width = '100%';
            video.style.margin = '0';
        }


        const headers = document.querySelectorAll('.accordion-header');

        headers.forEach(header => {
            header.addEventListener('click', function() {
                const content = this.nextElementSibling;

                // Alternar el contenido
                content.style.display = content.style.display === "block" ? "none" : "block";
            });
        });