#coding : utf-8

stop_words=['', "'ll", "'ve", 'I', 'a', "a's", 'able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 
'add', 'added', 'address', 'adj', 'affected', 'affecting', 'affects', 'afraid', 'after', 'afterwards', 'again', 'against', 'age', 'ago', 'agree', 'ah', 
'ain', "ain't", 'air', 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 
'anger', 'animal', 'announce', 'another', 'answer', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 
'apparently', 'appear', 'apple', 'appreciate', 'appropriate', 'approximately', 'are', 'area', 'aren', 'arent', 'arise', 'arm', 'around', 'arrange', 'arrive', 
'art', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'atom', 'auth', 'available', 'away', 'awfully', 'b', 'baby', 'back', 'bad', 'ball', 'band', 'bank', 
'bar', 'base', 'basic', 'bat', 'be', 'bear', 'beat', 'beauty', 'became', 'because', 'becomes', 'becoming', 'bed', 'been', 'before', 'beforehand', 'began', 
'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe', 'bell', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'big', 
'biol', 'bird', 'bit', 'black', 'block', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 'bone', 'book', 'born', 'both', 'bottom', 'bought', 'box', 'boy', 
'branch', 'bread', 'break', 'brief', 'briefly', 'bright', 'bring', 'broad', 'broke', 'brother', 'brought', 'brown', 'build', 'burn', 'busy', 'but', 'buy', 'by', 
'c', "c'mon", "c's", 'ca', 'call', 'came', 'camp', 'can', "can't", 'cannot', 'cant', 'capital', 'captain', 'car', 'card', 'care', 'carry', 'case', 'cat', 
'catch', 'caught', 'cause', 'causes', 'cell', 'cent', 'center', 'century', 'certain', 'certainly', 'chair', 'chance', 'change', 'changes', 'character', 
'charge', 'chart', 'check', 'chick', 'chief', 'child', 'children', 'choose', 'chord', 'circle', 'city', 'claim', 'class', 'clean', 'clear', 'clearly', 
'climb', 'clock', 'close', 'clothe', 'cloud', 'co', 'coast', 'coat', 'cold', 'collect', 'colony', 'color', 'column', 'com', 'come', 'comes', 'common', 
'company', 'compare', 'complete', 'concerning', 'condition', 'connect', 'consequently', 'consider', 'considering', 'consonant', 'contain', 'containing', 
'contains', 'continent', 'continue', 'control', 'cook', 'cool', 'copy', 'corn', 'corner', 'correct', 'corresponding', 'cost', 'cotton', 'could', 'could', 
'couldn', "couldn't", 'count', 'country', 'course', 'cover', 'cow', 'crease', 'create', 'crop', 'cross', 'crowd', 'cry', 'current', 'currently', 'cut', 'd', 
'dad', 'dance', 'danger', 'dark', 'date', 'day', 'dead', 'deal', 'dear', 'death', 'decide', 'decimal', 'deep', 'definitely', 'degree', 'depend', 'describe', 
'described', 'desert', 'design', 'despite', 'determine', 'develop', 'dictionary', 'did', 'didn', "didn't", 'die', 'differ', 'different', 'difficult', 'direct', 
'discuss', 'distant', 'divide', 'division', 'do', 'doctor', 'does', 'doesn', "doesn't", 'dog', 'doing', 'dollar', 'don', "don't", 'done', 'door', 
'double', 'down', 'downwards', 'draw', 'dream', 'dress', 'drink', 'drive', 'drop', 'dry', 'duck', 'due', 'during', 'e', 'each', 'ear', 'early', 'earth', 
'ease', 'east', 'eat', 'ed', 'edge', 'edu', 'effect', 'effect', 'eg', 'egg', 'eight', 'eighty', 'either', 'electric', 'element', 'else', 'elsewhere', 'end', 
'ending', 'enemy', 'energy', 'engine', 'enough', 'enter', 'entirely', 'equal', 'equate', 'especially', 'et', 'etc', 'even', 'evening', 'event', 'ever', 'every', 
'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exact', 'exactly', 'example', 'except', 'excite', 'exercise', 'expect', 'experience', 'experiment', 
'eye', 'f', 'face', 'fact', 'fair', 'fall', 'family', 'famous', 'far', 'farm', 'fast', 'fat', 'father', 'favor', 'fear', 'feed', 'feel', 'feet', 'fell', 'felt', 
'few', 'ff', 'field', 'fifth', 'fig', 'fight', 'figure', 'fill', 'final', 'find', 'fine', 'finger', 'finish', 'fire', 'first', 'fish', 'fit', 'five', 'fix', 
'flat', 'floor', 'flow', 'flower', 'fly', 'follow', 'followed', 'following', 'follows', 'food', 'foot', 'for', 'force', 'forest', 'form', 'former', 'formerly', 
'forth', 'forward', 'found', 'four', 'fraction', 'free', 'fresh', 'friend', 'from', 'front', 'fruit', 'full', 'fun', 'further', 'furthermore', 'g', 'game', 
'garden', 'gas', 'gather', 'gave', 'general', 'gentle', 'get', 'gets', 'getting', 'girl', 'give', 'given', 'gives', 'giving', 'glad', 'glass', 'go', 'goes', 
'going', 'gold', 'gone', 'good', 'got', 'gotten', 'govern', 'grand', 'grandpy', 'grass', 'gray', 'great', 'green', 'greetings', 'grew', 'ground', 'group', 
'grow', 'guess', 'guide', 'gun', 'h', 'had', 'hadn', "hadn't", 'hair', 'half', 'hand', 'happen', 'happens', 'happy', 'hard', 'hardly', 'has', 'hasn', "hasn't", 
'hat', 'have', 'haven', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'head', 'hear', 'heard', 'heart', 'heat', 'heavy', 'hed', 'held', 'hello', 'help', 
'hence', 'her', 'her', 'here', 'here', "here's", 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'hid', 'high', 'hill', 
'him', 'himself', 'his', 'history', 'hit', 'hither', 'hold', 'hole', 'home', 'hope', 'hopefully', 'horse', 'hot', 'hour', 'house', 'how', "how's", 'howbeit', 
'however', 'huge', 'human', 'hundred', 'hunt', 'hurry', 'i', "i'd", "i'll", "i'm", "i've", 'ice', 'id', 'idea', 'ie', 'if', 'ignored', 'im', 'imagine', 
'immediate', 'immediately', 'importance', 'important', 'in', 'inasmuch', 'inc', 'inch', 'include', 'indeed', 'index', 'indicate', 'indicated', 'indicates', 
'industry', 'information', 'inner', 'insect', 'insofar', 'instant', 'instead', 'instrument', 'interest', 'into', 'invent', 'invention', 'inward', 'iron', 
'is', 'island', 'isn', "isn't", 'it', "it'd", "it'll", "it's", 'itd', 'its', 'itself', 'j', 'job', 'join', 'joy', 'jump', 'just', 'k', 'keep', 'keeps', 'kept', 
'key', 'kg', 'kill', 'kind', 'king', 'km', 'knew', 'know', 'known', 'knows', 'l', 'lady', 'lake', 'land', 'language', 'large', 'largely', 'last', 'late', 
'lately', 'later', 'latter', 'latterly', 'laugh', 'law', 'lay', 'lead', 'learn', 'least', 'leave', 'led', 'left', 'leg', 'length', 'less', 'lest', 'let', 
"let's", 'lets', 'letter', 'level', 'lie', 'life', 'lift', 'light', 'like', 'liked', 'likely', 'line', 'liquid', 'list', 'listen', 'little', 'live', 'll', 
'locate', 'log', 'lone', 'long', 'look', 'looking', 'looks', 'lost', 'lot', 'loud', 'love', 'low', 'ltd', 'm', 'ma', 'machine', 'made', 'magnet', 'main', 
'mainly', 'major', 'make', 'makes', 'man', 'many', 'map', 'mark', 'market', 'mass', 'master', 'match', 'material', 'matter', 'may', 'maybe', 'me', 'mean', 
'means', 'meant', 'meantime', 'meanwhile', 'measure', 'meat', 'meet', 'melody', 'men', 'merely', 'metal', 'method', 'mg', 'middle', 'might', 'mightn', 
"mightn't", 'mile', 'milk', 'million', 'mind', 'mine', 'minute', 'miss', 'mix', 'ml', 'modern', 'molecule', 'moment', 'money', 'month', 'moon', 'more', 
'moreover', 'morning', 'most', 'mostly', 'mother', 'motion', 'mount', 'mountain', 'mouth', 'move', 'mr', 'mrs', 'much', 'mug', 'multiply', 'music', 'must', 
'mustn', "mustn't", 'my', 'myself', 'n', 'na', 'name', 'namely', 'nation', 'natural', 'nature', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 
'neck', 'need', 'needn', "needn't", 'needs', 'neighbor', 'neither', 'never', 'nevertheless', 'next', 'night', 'nine', 'ninety', 'no', 'nobody', 
'noise', 'non', 'nonetheless', 'noon', 'noone', 'nor', 'normally', 'north', 'nos', 'nose', 'not', 'note', 'noted', 'nothing', 'notice', 'noun', 'novel', 
'now', 'nowhere', 'number', 'numeral', 'o', 'object', 'observe', 'obtain', 'obtained', 'obviously', 'occur', 'ocean', 'of', 'off', 'offer', 'office', 
'often', 'oh', 'oil', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'open', 'operate', 'opposite', 'or', 'ord', 'order', 
'organ', 'original', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'oxygen', 
'p', 'page', 'pages', 'paint', 'pair', 'paper', 'paragraph', 'parent', 'part', 'particular', 'particularly', 'party', 'pass', 'past', 'path', 'pattern', 
'pay', 'people', 'per', 'perhaps', 'period', 'person', 'phrase', 'pick', 'picture', 'piece', 'pitch', 'place', 'placed', 'plain', 'plan', 'plane', 'planet', 
'plant', 'play', 'please', 'plural', 'plus', 'poem', 'point', 'poor', 'poorly', 'populate', 'port', 'pose', 'position', 'possible', 'possibly', 'post', 
'potentially', 'pound', 'power', 'pp', 'practice', 'predominantly', 'prepare', 'present', 'press', 'presumably', 'pretty', 'previously', 'primarily', 
'print', 'probable', 'probably', 'problem', 'process', 'produce', 'product', 'promptly', 'proper', 'property', 'protect', 'proud', 'prove', 'provide', 
'provides', 'pull', 'push', 'put', 'q', 'quart', 'que', 'question', 'quick', 'quickly', 'quiet', 'quotient', 'qv', 'r', 'race', 'radio', 'rail', 'rain', 
'raise', 'ran', 'range', 'rather', 'rd', 're', 'reach', 'read', 'readily', 'ready', 'real', 'really', 'reason', 'reasonably', 'receive', 'recent', 
'recently', 'record', 'red', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'region', 'related', 'relatively', 'remember', 'repeat', 'reply', 
'represent', 'require', 'research', 'respectively', 'rest', 'result', 'resulted', 'resulting', 'results', 'rich', 'ride', 'right', 'ring', 'rise', 
'river', 'road', 'rock', 'roll', 'room', 'root', 'rope', 'rose', 'round', 'row', 'rub', 'rule', 'run', 's', 'safe', 'said', 'sail', 'salt', 'same', 
'sand', 'sat', 'save', 'saw', 'say', 'saying', 'says', 'scale', 'school', 'science', 'score', 'sea', 'search', 'season', 'seat', 'sec', 'second', 
'secondly', 'section', 'see', 'seed', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'segment', 'select', 'self', 'sell', 'selves', 'send', 
'sense', 'sensible', 'sent', 'sentence', 'separate', 'serious', 'seriously', 'serve', 'set', 'settle', 'seven', 'several', 'shall', 'shan', "shan't", 
'shape', 'share', 'sharp', 'she', "she'd", "she'll", "she's", 'shed', 'sheet', 'shell', 'shes', 'shine', 'ship', 'shoe', 'shop', 'shore', 'short', 
'should', 'should', "should've", 'shoulder', 'shouldn', "shouldn't", 'shout', 'show', 'showed', 'shown', 'showns', 'shows', 'side', 'sight', 'sign', 
'significant', 'significantly', 'silent', 'silver', 'similar', 'similarly', 'simple', 'since', 'sing', 'single', 'sister', 'sit', 'six', 'size', 
'skill', 'skin', 'sky', 'slave', 'sleep', 'slightly', 'slip', 'slow', 'small', 'smell', 'smile', 'snow', 'so', 'soft', 'soil', 'soldier', 'solution', 
'solve', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'son', 'song', 'soon', 
'sorry', 'sound', 'south', 'space', 'speak', 'special', 'specifically', 'specified', 'specify', 'specifying', 'speech', 'speed', 'spell', 'spend', 
'spoke', 'spot', 'spread', 'spring', 'square', 'stand', 'star', 'start', 'state', 'station', 'stay', 'stead', 'steam', 'steel', 'step', 'stick', 
'still', 'stone', 'stood', 'stop', 'store', 'story', 'straight', 'strange', 'stream', 'street', 'stretch', 'string', 'strong', 'strongly', 'student', 
'study', 'sub', 'subject', 'substance', 'substantially', 'subtract', 'success', 'successfully', 'such', 'sudden', 'sufficiently', 'suffix', 'sugar', 
'suggest', 'suit', 'summer', 'sun', 'sup', 'supply', 'support', 'sure', 'surface', 'surprise', 'swim', 'syllable', 'symbol', 'system', 't', "t's", 
'table', 'tail', 'take', 'taken', 'taking', 'talk', 'tall', 'teach', 'team', 'teeth', 'tell', 'temperature', 'ten', 'tends', 'term', 'test', 'th', 
'than', 'thank', 'thanks', 'thanx', 'that', "that'll", "that's", "that've", 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 
'there', "there'll", "there's", "there've", 'thereafter', 'thereby', 'thered', 'therefore', 'therein', 'thereof', 'therere', 'theres', 'thereto', 
'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'theyd', 'theyre', 'thick', 'thin', 'thing', 'think', 'third', 'this', 
'thorough', 'thoroughly', 'those', 'thou', 'though', 'thoughh', 'thought', 'thousand', 'three', 'throug', 'through', 'throughout', 'throw', 'thru', 
'thus', 'tie', 'til', 'time', 'tiny', 'tip', 'tire', 'to', 'together', 'told', 'tone', 'too', 'took', 'tool', 'top', 'total', 'touch', 'toward', 
'towards', 'town', 'track', 'trade', 'train', 'travel', 'tree', 'triangle', 'tried', 'tries', 'trip', 'trouble', 'truck', 'true', 'truly', 'try', 
'trying', 'ts', 'tube', 'turn', 'twenty', 'twice', 'two', 'type', 'u', 'un', 'under', 'unfortunately', 'unit', 'unless', 'unlike', 'unlikely', 
'until', 'unto', 'up', 'upon', 'ups', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usual', 'usually', 'v', 'valley', 
'value', 'various', 'vary', 've', 'verb', 'very', 'via', 'view', 'village', 'visit', 'viz', 'voice', 'vol', 'vols', 'vowel', 'vs', 'w', 'wait', 
'walk', 'wall', 'want', 'wants', 'war', 'warm', 'was', 'wash', "wasn't", 'wasnt', 'watch', 'water', 'wave', 'way', 'we', "we'd", "we'll", "we're", 
"we've", 'wear', 'weather', 'wed', 'week', 'weight', 'welcome', 'well', 'went', 'were', 'weren', "weren't", 'werent', 'west', 'what', "what'll", 
"what's", 'whatever', 'whats', 'wheel', 'when', "when's", 'whence', 'whenever', 'where', "where's", 'whereafter', 'whereas', 'whereby', 'wherein', 
'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'white', 'whither', 'who', "who'll", "who's", 'whod', 'whoever', 'whole', 
'whom', 'whomever', 'whos', 'whose', 'why', "why's", 'wide', 'widely', 'wife', 'wild', 'will', 'willing', 'win', 'wind', 'window', 'wing', 'winter', 
'wire', 'wish', 'with', 'within', 'without', 'woman', 'women', 'won', "won't", "won't", 'wonder', 'wont', 'wood', 'word', 'words', 'work', 'world', 
'would', 'wouldn', "wouldn't", 'wouldnt', 'write', 'written', 'wrong', 'wrote', 'www', 'x', 'y', 'yard', 'year', 'yellow', 'yes', 'yet', 'you', "you'd", 
"you'll", "you're", "you've", 'youd', 'young', 'your', 'youre', 'yours', 'yourself', 'yourselves', 'z', 'zero', 'grandma']