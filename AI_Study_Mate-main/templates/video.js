document.addEventListener('DOMContentLoaded', function () {
    const chatbox = document.querySelector('.chatbox');
    const textarea = document.querySelector('.chat-input textarea');
    const sendBtn = document.getElementById('send-btn');

    sendBtn.addEventListener('click', function () {
        const message = textarea.value;
        addOutgoingMessage(message);
        fetchVideoLink(message);
        textarea.value = '';
    });

    function addIncomingMessage(message) {
        const chat = document.createElement('li');
        chat.className = 'chat incoming';
        chat.innerHTML = `
            <span class="material-symbols-outlined">smart_toy</span>
            <p>${message}</p>
        `;
        chatbox.appendChild(chat);
    }

    function addOutgoingMessage(message) {
        const chat = document.createElement('li');
        chat.className = 'chat outgoing';
        chat.innerHTML = `<p>${message}</p>`;
        chatbox.appendChild(chat);
    }

    function fetchVideoLink(topic) {
        fetch(`/get_video_link?topic=${encodeURIComponent(topic)}`)
            .then(response => response.json())
            .then(data => {
                const videoLink = data.videoLink; // Adjust based on your response structure
                addIncomingMessage(`Here is the video link: ${videoLink}`);
            })
            .catch(error => console.error('Error fetching video link:', error));
    }
});
