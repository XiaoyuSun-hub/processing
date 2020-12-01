import os
import solaris as sol

path = os.getcwd()
dir=r"C:\xiaoyu\study_extent"
os.chdir(path)

raster_tiler = sol.tile.raster_tile.RasterTiler(dest_dir='images',  # the directory to save images to
                                                src_tile_size=(512, 512),  # the size of the output chips
                                                verbose=True)
raster_bounds_crs = raster_tiler.tile(os.path.join(dir, 'ENS.tif'))

# vector_tiler = sol.tile.vector_tile.VectorTiler(dest_dir='brt',
#                                                 verbose=True)
# vector_tiler.tile(os.path.join(dir, 'top10enschede.geojson'),
#                   tile_bounds=raster_tiler.tile_bounds,
#                   tile_bounds_crs=raster_bounds_crs)
#
# vector_tilerbag = sol.tile.vector_tile.VectorTiler(dest_dir='bag',
#                                                    verbose=True)
# vector_tilerbag.tile(os.path.join(dir, 'BAGmerge.geojson'),
#                      tile_bounds=raster_tiler.tile_bounds,
#                      tile_bounds_crs=raster_bounds_crs)
