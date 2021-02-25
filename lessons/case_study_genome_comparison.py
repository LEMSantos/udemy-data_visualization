import matplotlib.pyplot as plt
from itertools import product
from collections import defaultdict

dinucleotides = 'ATCG'

dinucleotides_perm = [
    ''.join(perm) for perm in product(dinucleotides, repeat=2)
]

genome_file_names = [
    'bacteria',
    'human',
]

for name in genome_file_names:
    with open(f'../data/{name}.fasta') as genome_file:
        genome = genome_file.read()

    counter = defaultdict(int)

    for perm in dinucleotides_perm:
        counter[perm] += genome.count(perm)

    html_template = """
    <div
        style="width:100px;
            border:1px solid #111;
            height:100px;
            float:left;
            color:#fff;
            background-color:rgba(0, 0, 0, {transparence})"
    >
        {dinucleotide}
    </div>
    """

    output_file_path = f'../html/{name}.html'

    with open(output_file_path, 'w') as output_file:
        i = 1

        for key, value in counter.items():
            transparence = value / max(counter.values())
            output_file.write(html_template.format(
                transparence=transparence,
                dinucleotide=key,
            ))

            if i%4 == 0:
                output_file.write('<div style="clear:both"></div>')

            i += 1
