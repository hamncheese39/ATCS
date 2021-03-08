class Message:
    def __init__(self, username):
        self.text = ""
        self.get_input()

        self.user = username

        #set self.timestamp to the time at the creation of the message
        self.timestamp =

        self.comments = []

        self.reactions = []

    def show(self):
        #print the message, stylistically
        #print who posted it (username)
        #print what time it was posted from self.timestamp
        #print any reactions to it from self.reactions
        #print any comments and who posted them from self.comments
    
    def get_input(self):
        #gets input to be put in message and puts it in self.text
        pass

    def add_comment(self):
        #adds comment object to list of comment objects
        self.comments.append(input())
    
    def add_reaction(self):
        #adds reaction object to list of reaction objects
