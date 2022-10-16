def generate_table(dataframe: pd.DataFrame(), max_columns=10, max_rows=10):
    column_count = len(dataframe.columns)
    if column_count > max_columns:
        fith_last = column_count - 5
        columns_to_drop = dataframe.iloc[0:1, 6:fith_last].columns
        new_dataframe = dataframe.drop(labels=columns_to_drop, axis=1)
        new_dataframe["..."] = "..."
        cols = list(new_dataframe.columns)
        middle = len(cols) // 2
        print(cols[-1])
        print(cols)
        cols = cols[:middle] + cols[-1:] + cols[middle:-1]
        print(cols)
        new_dataframe = new_dataframe[cols]
    else:
        new_dataframe = dataframe    
    return html.Table([
        html.Thead(
            html.Tr(
                [html.Th(col) for col in new_dataframe.columns],
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            )
        ),
        html.Tbody([
            html.Tr([
                html.Td(
                    new_dataframe.iloc[i][col],
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }
                    ) for col in new_dataframe.columns
                ]) for i in range(min(len(new_dataframe), max_rows))
                
            ])

        ])
