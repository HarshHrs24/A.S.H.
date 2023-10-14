class Chatbox {
    constructor() {
        this.args ={
        openButton: document.querySelector('.chatbox__button'),
        chatBox: document.querySelector('.chatbox__support'),
        sendButton: document.querySelector('.send__button')
        }

    
    this.state = false;
    this.messages = []
    }



display(){
    const {openButton, chatBox, sendButton} = this.args;

    openButton.addEventListener('click' , () => this.toggleState(chatBox))
    sendButton.addEventListener('click' , () => this.onSendButton(chatBox))
    const node = chatBox.querySelector('input');
    node.addEventListener('keyup' , ({key}) => {
        if (key=="Enter"){
            this.onSendButton(chatBox)
        }

    })
    
}



toggleState(chatbox){
    this.state = !this.state;

    // show or hides the box 
    if(this.state){
        chatbox.classList.add('chatbox--active')

    } else{
        chatbox.classList.remove('chatbox--active')
    }

}

onSendButton(chatbox){
    var textField = chatbox.querySelector('input');
    let text1 = textField.value
    if (text1===""){
        return;
    }

    let msg1 = {name:"User", message: text1}
    this.messages.push(msg1);

    // 'http://127.0.0.1:5000/predict

    fetch($SCRIPT_ROOT + '/predict', {
        method: 'POST',
        body: JSON.stringify({message: text1}),
        mode:'cors',
        headers: {
            'Content-Type': 'application/json'
        
        },

    })

    .then(r=> r.json())
    .then(r => {
        
        if (r.type=="string"){
            console.log("string")
            let msg2 = {name:"Shivansh", message: r.answer};
            this.messages.push(msg2)
            this.updateChatText(chatbox)
        }else{
            console.log("-------")
           console.log(typeof r.answer)
           let msg3 = {name:"Shivansh", message: "Here are few suggested questions related to given topic. To copy any question just click on it"};
           this.messages.push(msg3)
           this.updateChatText(chatbox)
           for(let i=0;i<(r.answer).length;i++){
            let msg2 = {name:"Shivansh", message: r.answer[i]};
            this.messages.push(msg2)
            this.updateChatText(chatbox)
           }
        }
        
        textField.value =''
    

}).catch((error) => {
    console.error('Error', error);
    this.updateChatText(chatbox)
    textField.value = ''

  });
}

updateChatText(chatbox){
    var html='';
    this.messages.slice().reverse().forEach(function(item){
        if (item.name==="Shivansh")
        {
            html+= '<div class= "messages__item messages__item--visitor"  onclick="copyToClipboard(this)">' + item.message + '</div>'

        }

        else 
        {
            html+= '<div class= "messages__item messages__item--operator"  onclick="copyToClipboard(this)">' + item.message + '</div>'  
        }

    });

    const chatmessage = chatbox.querySelector('.chatbox__messages');
    chatmessage.innerHTML = html;


    }

}

const chatbox =  new Chatbox();
chatbox.display()

function submitForm() {
    // const selectedOption = document.getElementById('caviarChoice').value;
    const textContent = document.getElementById('textContent').value;

    const data = {
        // option: selectedOption,
        text: textContent
    };

    fetch($SCRIPT_ROOT +'/insert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function copyToClipboard(element) {
    const textToCopy = element.innerText || element.textContent;
    
    if (window.navigator && window.navigator.clipboard) {
        window.navigator.clipboard.writeText(textToCopy).then(function() {
            console.log('Text successfully copied!');
        }).catch(function(err) {
            console.error('Unable to copy text: ', err);
        });
    } else {
        // Fallback for older browsers
        const textArea = document.createElement("textarea");
        textArea.value = textToCopy;
        document.body.appendChild(textArea);
        textArea.select();
        try {
            document.execCommand('copy');
            console.log('Text successfully copied!');
        } catch (err) {
            console.error('Unable to copy text: ', err);
        }
        document.body.removeChild(textArea);
    }
}

function showChat() {
    document.querySelector(".chat-page").style.display = "block";
    document.querySelector(".experience-page").style.display = "none";
    document.querySelector(".navbar").style.margin = "50px auto";
}

function showExperience() {
    document.querySelector(".chat-page").style.display = "none";
    document.querySelector(".experience-page").style.display = "block";
    document.querySelector(".navbar").style.margin = "0px auto";
}
