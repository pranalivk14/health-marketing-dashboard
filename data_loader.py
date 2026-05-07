import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)

    # Rename Kaggle columns to match the rest of the code
    df = df.rename(columns={
        'Date':             'date',
        'Channel_Used':     'channel',
        'Acquisition_Cost': 'spend',
        'Impressions':      'reach',
        'Clicks':           'conversions',
        'Campaign_Type':    'campaign',
        'Location':         'region',
        'Target_Audience':  'age_segment',
        'Conversion_Rate':  'conversion_rate',
    })

    # Clean the spend column — remove $ and commas, convert to number
    df['spend'] = df['spend'].replace('[\$,]', '', regex=True).astype(float)

    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Calculate CPA (cost per acquisition)
    df['cpa'] = (df['spend'] / df['conversions'].replace(0, 1)).round(2)

    # Drop rows missing key columns
    df = df.dropna(subset=['channel', 'spend', 'conversions'])

    return df


def get_summary_stats(df: pd.DataFrame) -> dict:
    return {
        'total_spend':       int(df['spend'].sum()),
        'total_reach':       int(df['reach'].sum()),
        'total_conversions': int(df['conversions'].sum()),
        'avg_cpa':           round(df['cpa'].mean(), 2),
        'best_channel':      df.groupby('channel')['conversions'].sum().idxmax(),
        'top_region':        df.groupby('region')['conversions'].sum().idxmax(),
        'date_range':        f"{df['date'].min().strftime('%b %Y')} – {df['date'].max().strftime('%b %Y')}",
        'channel_breakdown': df.groupby('channel')['spend'].sum().to_dict(),
    }