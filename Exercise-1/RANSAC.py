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
seg = cloud_filtered.make_segmenter()

# Set the model you wish to fit 
seg.set_model_type(pcl.SACMODEL_PLANE)
seg.set_method_type(pcl.SAC_RANSAC)

# Max distance for a point to be considered fitting the model
# Experiment with different values for max_distance 
# for segmenting the table
max_distance = 0.01
seg.set_distance_threshold(max_distance)

# Call the segment function to obtain set of inlier indices and model coefficients
inliers, coefficients = seg.segment()

# Extract outliers
extracted_outliers = cloud_filtered.extract(inliers, negative=True)
filename = 'extracted_outliers.pcd'
pcl.save(extracted_outliers, filename)

# Save pcd for tabletop objects


