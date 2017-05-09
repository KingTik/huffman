from tree import Tree
from collections import OrderedDict
import operator


#text = "Pok pok disrupt austin prism, skateboard pug wolf echo park. XOXO twee cornhole YOLO. Disrupt asymmetrical tbh fixie. Cronut tumeric vinyl polaroid, shoreditch artisan selvage tote bag fap iceland pug thundercats art party drinking vinegar. Sriracha distillery leggings intelligentsia freegan meh. Intelligentsia bitters put a bird on it locavore, next level beard irony whatever ethical. Hashtag chia air plant, green juice mustache prism taxidermy pork belly lumbersexual bushwick try-hard. Mixtape af pickled, sartorial hashtag biodiesel heirloom occupy readymade roof party green juice thundercats. Pinterest everyday carry leggings, kale chips post-ironic pok pok semiotics echo park enamel pin activated charcoal poke put a bird on it. Narwhal knausgaard cold-pressed poutine, coloring book hot chicken meh stumptown microdosing VHS swag kombucha. Hella cray jean shorts you probably haven't heard of them synth. Yuccie succulents organic brunch, portland enamel pin man bun disrupt fanny pack. Swag ramps church-key, jean shorts everyday carry art party la croix pickled iPhone listicle. Pitchfork deep v franzen, godard tbh humblebrag man bun blog poutine ennui biodiesel. Authentic raw denim slow-carb echo park four dollar toast meggings cold-pressed, godard williamsburg art party activated charcoal. Cold-pressed photo booth drinking vinegar marfa shoreditch. Echo park biodiesel gochujang fanny pack jianbing banh mi. Wolf vexillologist chartreuse brunch, seitan jean shorts shoreditch gastropub. Green juice butcher jianbing thundercats, chartreuse wolf shoreditch. Mumblecore retro disrupt, selvage messenger bag pitchfork etsy glossier literally try-hard gochujang cold-pressed 8-bit chartreuse prism. Pop-up hammock prism, raclette celiac squid small batch vice DIY chartreuse. Forage sartorial truffaut, cornhole hammock whatever paleo prism twee chambray chia humblebrag. Yuccie hoodie cornhole, vinyl af helvetica activated charcoal. Tacos cred meh 8-bit cold-pressed, iPhone chartreuse. Subway tile salvia gochujang twee listicle next level. Shabby chic keytar forage next level neutra, chartreuse salvia hell of. Ugh austin brunch asymmetrical selfies cliche forage. Brooklyn poutine la croix church-key."



class huffman:



    def __init__(self, text):
        self.text = text
        self.slownik = {}
        self.len = len(text)
        self.treeTable = []
        self.drzewokodowe = None


    def coutnProb(self):
        for letter in self.text:
            if self.slownik.has_key(letter) is False:
                self.slownik[letter] = 1
            else:
                self.slownik[letter] = self.slownik[letter] +1


        self.slownik = sorted(self.slownik.items(), key=operator.itemgetter(1))



    def createTreeTable(self):

        for element in self.slownik:
            tmp = Tree(int(element[1]), str(element[0]))
            self.treeTable.append(tmp)


    def buildTree(self):

        while len(self.treeTable) >= 2:
            
            tmp1 = self.treeTable.pop(0)
            tmp2 = self.treeTable.pop(0)
            newTree = Tree(tmp1.key + tmp2.key, tmp1.key + tmp2.key)
            newTree.left = tmp1
            newTree.right = tmp2
            self.treeTable.insert(0, newTree)
        
        self.drzewokodowe = self.treeTable[0]

    def letterCode(self, letter,node=None, code = ""):
        
        if node is None:
            node = self.drzewokodowe

        if node.getValue() == letter:
            return code
        if node.checkLeft() is True:
            tmp = self.letterCode(letter,node.left, code+'0')
            if tmp is not None:
                return tmp    
        if node.checkRight() is True:
            tmp = self.letterCode(letter,node.right, code+'1')
            if tmp is not None:
                return tmp
        



text = "Pok pok disrupt austin prism"
text = text.lower()

kod = huffman(text)
kod.coutnProb()
kod.createTreeTable()


kod.buildTree()

kod.drzewokodowe.display()

#print kod.letterCode('m')




'''
to do:
- znajdowanie sciezki do elementu?
- ulepszyc wyswietlanie
- huffman.encode() i huffman.decode()
- testy


'''