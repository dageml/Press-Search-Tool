def clean_articles(df):
    bad_outlets = ["crooksandliars.com","wnd.com","hyperallergic","common dreams"]
    #drop bad sources
    df = df[~df["source.name"].str.lower().isin([x.lower() for x in bad_outlets])]
    #drop missing authors
    df = df[df["author"].notna()] 
    if "source.id" in df.columns:
        #drop columns
        df.drop(columns=["urlToImage","publishedAt"], inplace=True)
        #rename column
        df = df.rename(columns={'source.id':'affiliation'})
        return df
    return df