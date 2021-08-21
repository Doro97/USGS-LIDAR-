import pdal 
import json

data_path="https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
region="IA_FullState/"

bounds=([-10425171.940, -10423171.940], [5164494.710, 5166494.710])
access_data_path=data_path+region+"ept.json"

output_filename_laz="iowa.laz"
output_filename_tif="iowa.tif"

pipeline_path='iowa.json'


def get_raster_terrain(bounds:str,region:str,access_data_path:str=access_data_path,
                        output_filename_laz:str=output_filename_laz,output_filename_tif:str=output_filename_tif,
                        pipeline_path:str=pipeline_path)->None:
    """This function outputs the the raster file and dem file from a json script """                    

    with open(pipeline_path) as json_file:
        the_json=json.load(json_file)

    the_json['pipeline'][0]['bounds']=bounds
    the_json['pipeline'][0]['filename']=access_data_path
    the_json['pipeline'][3]['filename']=output_filename_laz
    the_json['pipeline'][4]['filename']=output_filename_tif

    pipeline=pdal.Pipeline(json.dumps(the_json))

    try:
        pipe_exec=pipeline.execute()
        metadata=pipeline.metadata

    except RuntimeError as e:
        print(e)
        print('Runtime Error, writing 0s and moving to the next bounds')  
        pass


    if __name__ =='__main__' :
        get_raster_terrain(bounds=bounds,region=region) 


