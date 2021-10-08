from typing import List
import shutil
import click
import os


class CompressorError(Exception):
    def __init__(self, message: str, code: int) -> None:
        self.message = message
        self.code = code

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.code}): {self.message}"


class NotADirectoryError(CompressorError):
    pass


@click.command()
@click.option("--dir", type=click.STRING)
@click.option("--output_name", type=click.STRING)
def kompress(
    dir: str,
    output_name: str,
    files_to_skip: List[str] = [".DS_Store"],
    file_types_to_skip: List[str] = [],
):
    valid_directory = os.path.isdir(dir)
    if not valid_directory:
        raise NotADirectoryError(message="디렉토리를 찾을 수 없습니다", code=500)

    input_fils = [
        os.path.join(dir, file) for file in os.listdir(dir) if file not in files_to_skip
    ]

    if not output_name:
        output_name = f"{dir}"
    
    shutil.make_archive(output_name, 'zip', dir)

    # with ZipFile(output_name, mode="w") as zf:
    #     for f in input_files:
    #         zf.write(f)  # TODO(humphrey): add file recursive file copy


if __name__ == "__main__":
    kompress()
