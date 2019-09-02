import scadnano as sc

def main():
    width = 6
    width_h = width // 2
    helices = [sc.Helix(0, width), sc.Helix(1, width)]
    stap_left_ss1 = sc.Substrand(1, sc.forward, 0, width_h)
    stap_left_ss0 = sc.Substrand(0, sc.reverse, 0, width_h)
    stap_right_ss0 = sc.Substrand(0, sc.reverse, width_h, width)
    stap_right_ss1 = sc.Substrand(1, sc.forward, width_h, width)
    scaf_ss1_left = sc.Substrand(1, sc.reverse, 0, width_h)
    scaf_ss0 = sc.Substrand(0, sc.forward, 0, width)
    scaf_ss1_right = sc.Substrand(1, sc.reverse, width_h, width)
    stap_left = sc.Strand([stap_left_ss1, stap_left_ss0])
    stap_right = sc.Strand([stap_right_ss0, stap_right_ss1])
    scaf = sc.Strand([scaf_ss1_left, scaf_ss0, scaf_ss1_right], color=sc.default_scaffold_color)
    strands = [stap_left, stap_right, scaf]
    design = sc.DNADesign(helices=helices, strands=strands, grid=sc.square)
    design.add_deletion(helix_idx=0, offset=1)
    design.add_deletion(helix_idx=0, offset=4)
    design.add_deletion(helix_idx=1, offset=1)
    design.add_deletion(helix_idx=1, offset=4)
    design.assign_dna(scaf, 'AACATCGT')

    return design


if not sc.in_browser() and __name__ == '__main__':
    design = main()
    design.write_scadnano_file(directory='output_designs')
