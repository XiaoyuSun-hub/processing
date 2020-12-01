import os
import solaris as sol

path = os.getcwd()
dir = os.path.join(path, 'data')
os.chdir(path)

raster_tiler = sol.tile.raster_tile.RasterTiler(dest_dir='rio_chips',  # the directory to save images to
                                                src_tile_size=(500, 500),  # the size of the output chips
                                                verbose=True)
raster_bounds_crs = raster_tiler.tile(os.path.join(dir,'PS-RGB_mosaic_013022223133.tif'))

vector_tiler = sol.tile.vector_tile.VectorTiler(dest_dir='rio_labels',
                                                verbose=True)
vector_tiler.tile(os.path.join(dir, 'Rio_Buildings_Public_AOI_v2.geojson'),
                  tile_bounds=raster_tiler.tile_bounds,
                  tile_bounds_crs=raster_bounds_crs)
