# Import PCL module
import pcl

# Load Point Cloud file
cloud = pcl.load_XYZRGB('tabletop.pcd')


# Voxel Grid filter
vox = cloud.make_voxel_grid_filter()

LEAF_SIZE = 0.01

vox.set_leaf_size(LEAF_SIZE, LEAF_SIZE, LEAF_SIZE)

cloud_filtered = vox.filter()
#filename = 'voxel_downsampled.pcd'
#pcl.save(cloud_filtered, filename)

# PassThrough filter
passthrough = cloud_filtered.make_passthrough_filter()

passthrough.set_filter_field_name('z')
z_min = 0.6
z_max = 1.1
passthrough.set_filter_limits(z_min, z_max)

cloud_filtered = passthrough.filter()
filename = 'filtered.pcd'
pcl.save(cloud_filtered, filename)

# RANSAC plane segmentation


# Extract inliers

# Save pcd for table
# pcl.save(cloud, filename)


# Extract outliers


# Save pcd for tabletop objects


