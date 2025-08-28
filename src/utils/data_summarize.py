import pandas as pd

def data_summarize(df, head=10):
    """
    데이터프레임의 주요 정보를 요약하여 출력하고 딕셔너리 형태로 반환하는 함수입니다.

    Args:
        df (pd.DataFrame): 요약할 데이터프레임.
        head (int): head()로 출력할 행의 수. 기본값은 10.

    Returns:
        dict: 데이터 요약 정보를 담은 딕셔너리.
    """
    #  1. 정보를 저장할 딕셔너리 초기화
    summary_dict = {}

    # 2. 정보 계산 및 딕셔너리에 추가
    summary_dict['shape'] = df.shape
    summary_dict['head'] = df.head(head)
    summary_dict['describe'] = df.describe()
    summary_dict['dtypes'] = df.dtypes
    summary_dict['nan_values'] = df.isnull().sum()

    # 3. 계산된 정보 출력
    print(f'<shape>{"-"*80}\n{summary_dict["shape"]}')
    print(f'\n<head({head})>{"-"*80}\n{summary_dict["head"]}')
    print(f'\n<describe>{"-"*80}\n{summary_dict["describe"]}')
    print(f'\n<dtypes>{"-"*80}\n{summary_dict["dtypes"]}')
    print(f'\n<NaN value>{"-"*80}\n{summary_dict["nan_values"]}')

    # 4. 딕셔너리 반환

    # return summary_dict


