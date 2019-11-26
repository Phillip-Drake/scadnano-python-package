import scadnano as sc


def main():
    length = 10
    helices = [sc.Helix(position3d=(sc.Position3D(x=0, y=0, z=0, pitch=0, roll=0, yaw=0)))]
    stap_ss = sc.Substrand(0, sc.forward, 0, length)
    scaf_ss = sc.Substrand(0, sc.reverse, 0, length)
    stap = sc.Strand([stap_ss])
    scaf = sc.Strand([scaf_ss], color=sc.default_scaffold_color)
    strands = [stap, scaf]
    design = sc.DNADesign(helices=helices, strands=strands, grid=sc.Grid.none)

    return design


if not sc.in_browser() and __name__ == '__main__':
    design = main()
    design.write_scadnano_file(directory='output_designs')
