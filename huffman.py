from tree import Tree


text = "Pok pok disrupt austin prism, skateboard pug wolf echo park. XOXO twee cornhole YOLO. Disrupt asymmetrical tbh fixie. Cronut tumeric vinyl polaroid, shoreditch artisan selvage tote bag fap iceland pug thundercats art party drinking vinegar. Sriracha distillery leggings intelligentsia freegan meh. Intelligentsia bitters put a bird on it locavore, next level beard irony whatever ethical. Hashtag chia air plant, green juice mustache prism taxidermy pork belly lumbersexual bushwick try-hard. Mixtape af pickled, sartorial hashtag biodiesel heirloom occupy readymade roof party green juice thundercats. Pinterest everyday carry leggings, kale chips post-ironic pok pok semiotics echo park enamel pin activated charcoal poke put a bird on it. Narwhal knausgaard cold-pressed poutine, coloring book hot chicken meh stumptown microdosing VHS swag kombucha. Hella cray jean shorts you probably haven't heard of them synth. Yuccie succulents organic brunch, portland enamel pin man bun disrupt fanny pack. Swag ramps church-key, jean shorts everyday carry art party la croix pickled iPhone listicle. Pitchfork deep v franzen, godard tbh humblebrag man bun blog poutine ennui biodiesel. Authentic raw denim slow-carb echo park four dollar toast meggings cold-pressed, godard williamsburg art party activated charcoal. Cold-pressed photo booth drinking vinegar marfa shoreditch. Echo park biodiesel gochujang fanny pack jianbing banh mi. Wolf vexillologist chartreuse brunch, seitan jean shorts shoreditch gastropub. Green juice butcher jianbing thundercats, chartreuse wolf shoreditch. Mumblecore retro disrupt, selvage messenger bag pitchfork etsy glossier literally try-hard gochujang cold-pressed 8-bit chartreuse prism. Pop-up hammock prism, raclette celiac squid small batch vice DIY chartreuse. Forage sartorial truffaut, cornhole hammock whatever paleo prism twee chambray chia humblebrag. Yuccie hoodie cornhole, vinyl af helvetica activated charcoal. Tacos cred meh 8-bit cold-pressed, iPhone chartreuse. Subway tile salvia gochujang twee listicle next level. Shabby chic keytar forage next level neutra, chartreuse salvia hell of. Ugh austin brunch asymmetrical selfies cliche forage. Brooklyn poutine la croix church-key."
text = text.lower()


class huffman:

    def __init__(self, text):
        self.text = text
        self.slownik = {}
        self.len = len(text)
        self.treeTable = []


    def coutnProb(self):
        for letter in self.text:
            if self.slownik.has_key(letter) == False:
                self.slownik[letter] = 1
            else:
                self.slownik[letter] = self.slownik[letter] +1

    def createTreeTable(self):

        for element in self.slownik:

            self.treeTable.append(Tree(self.slownik[element],element))



     