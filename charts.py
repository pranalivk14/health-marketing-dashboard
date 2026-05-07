import plotly.express as px
import pandas as pd

# Consistent colour palette across all charts
PALETTE = ['#1a6b4a', '#2d9e72', '#b84c1a', '#1a4a8a', '#8a6b1a']


def channel_performance_chart(df):
    """Bar chart: conversions by marketing channel."""
    grouped = df.groupby('channel')['conversions'].sum().reset_index()
    grouped = grouped.sort_values('conversions', ascending=True)

    fig = px.bar(
        grouped, x='conversions', y='channel',
        orientation='h',
        title='Conversions by Channel',
        color='channel',
        color_discrete_sequence=PALETTE
    )
    fig.update_layout(showlegend=False, height=320)
    return fig


def spend_trend_chart(df):
    """Line chart: monthly spend over time by channel."""
    df['month'] = df['date'].dt.to_period('M').astype(str)
    monthly = df.groupby(['month', 'channel'])['spend'].sum().reset_index()

    fig = px.line(
        monthly, x='month', y='spend', color='channel',
        title='Monthly Spend by Channel',
        color_discrete_sequence=PALETTE,
        markers=True
    )
    fig.update_layout(height=320, xaxis_tickangle=-45)
    return fig


def cpa_by_segment_chart(df):
    """Box plot: cost per acquisition by age segment."""
    fig = px.box(
        df, x='age_segment', y='cpa',
        color='age_segment',
        title='Cost per Acquisition by Age Segment',
        color_discrete_sequence=PALETTE
    )
    fig.update_layout(showlegend=False, height=320)
    return fig


def region_heatmap(df):
    """Heatmap: conversion rate by region and campaign."""
    pivot = df.groupby(['region', 'campaign'])['conversion_rate'].mean().reset_index()
    pivot_wide = pivot.pivot(index='region', columns='campaign', values='conversion_rate')

    fig = px.imshow(
        pivot_wide,
        title='Avg Conversion Rate: Region × Campaign',
        color_continuous_scale='Greens',
        text_auto='.1f'
    )
    fig.update_layout(height=320)
    return fig