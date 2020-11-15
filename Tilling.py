import os
raster_tiler = sol.tile.raster_tile.RasterTiler(dest_dir='rio_chips',  # the directory to save images to
                                                src_tile_size=(500, 500),  # the size of the output chips
                                                verbose=True)