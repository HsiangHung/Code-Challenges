'''
    pairingclass.py
    Module that cures something fantastic.
    @Author: Hsiang-Hsuan Hung
'''
class ArtistPairing(object):
    '''Pairing Artists class'''
    def __init__(self):
        self.artist_count = dict()
        self.num_users = 0
        self.artist_user_id = dict()
        self.filtered_artist_dict = dict()
        #self.pair_artist_dict = set()
        self.pair_artist_dict = list()


    def create_artist_dict(self, input_filename):
        '''classify how many artists in the file'''
        input_file = open(input_filename)
        for line in input_file:
            line = line.replace('\n', '').split(',')
            self.num_users += 1
            for artist in line:
                if artist not in self.artist_count:
                    self.artist_count[artist] = 1
                    self.artist_user_id[artist] = list()
                else:
                    self.artist_count[artist] += 1
                self.artist_user_id[artist].append(self.num_users)
        return self.artist_count


    def filter_artist_dict(self, value):
        ''' find out the dictionary for artists' names appearing >= 50 times '''
        for artist in self.artist_count:
            if self.artist_count[artist] > value:
                self.filtered_artist_dict[artist] = self.artist_user_id[artist]
        return self.filtered_artist_dict


    def find_pair_artist(self, value):
        ''' find paired artist which show together more than 50 times '''
        shown_artist = set()
        for artist1 in self.filtered_artist_dict:
            for artist2 in self.filtered_artist_dict:
                if artist2 != artist1 and artist2 not in shown_artist:
                    count = 0
                    for user2 in self.filtered_artist_dict[artist2]:
                        if user2 in self.filtered_artist_dict[artist1]: count += 1
                    if count > value or count == value:
                        #self.pair_artist_dict.add(artist1+', '+artist2+', '+str(count))
                        self.pair_artist_dict.append(artist1+', '+artist2+', '+str(count))

            shown_artist.add(artist1)
        return self.pair_artist_dict


    def get_artist_count(self):
        ''' Get the artist list dictionary '''
        return self.artist_count

    def get_num_users(self):
        ''' get the number of users '''
        return self.num_users

    def get_artist_user_id(self):
        ''' get the userID which mentions the artist '''
        return self.artist_user_id

    def get_filtered_artist_dict(self):
        ''' get the artist list whose names appear >= 50 times '''
        return self.filtered_artist_dict

    def get_paired_artist_dict(self):
        ''' get the paired artist list whose names together appear >= 50 times '''
        return self.pair_artist_dict

    def write_paired_artist(self, output_filename):
        '''classify how many artists in the file'''
        output_file = open(output_filename, 'w')
        for paired_artist in self.pair_artist_dict:
            print(paired_artist, file=output_file)


    def execute(self, input_filename, output_filename, value):
        '''executing through all methods to generate the paired artist file'''
        self.create_artist_dict(input_filename)
        #print(self.get_num_users())
        #print(len(self.get_artist_count()))
        self.filter_artist_dict(value)
        #for artist in self.get_filtered_artist_dict():
        #    print(artist,self.get_filtered_artist_dict()[artist])
        #print(len(self.get_filtered_artist_dict()))

        self.find_pair_artist(value)
        #print(len(self.pair_artist_dict))
        self.write_paired_artist(output_filename)


A = ArtistPairing()
#input_filename = 'ArtistList.csv'
#output_filename = 'artistPair_List.csv'
#criterion = 50
#A.execute(input_filename, output_filename, criterion)
A.execute('ArtistList.csv', 'artistPair_List.csv', 50)


