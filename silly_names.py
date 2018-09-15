import pandas as pd


def silly_names(df):
    """Replaces copyrighted names with fake names."""

    def random_names():
        """Concatenates a list of names."""

        animals = list(pd.read_fwf('resources/animals.txt').values)
        adjectives = list(pd.read_fwf('resources/adjectives.txt').values)
        names = []
        for i in range(0, len(animals)):
            names.append(str(adjectives[i][0] + ' ' + animals[i][0]))
        return names

    silly_names = random_names()
    for original, silly in zip(df['ride_name'].unique(), random_names()):
        df['ride_name'] = df['ride_name'].replace(original, silly)

    return df
 
