import {
    Card,
    Input,
    Checkbox,
    Button,
    Typography,
    Select, Option 
  } from "@material-tailwind/react";
   
  import {useState, useEffect} from "react"
  import {getShows} from "../../../api/hitsAPI"

  export const HorseSearchForm = ({SearchHorseShow}) => {
    const [shows, setShows] = useState([])
    const [showNames, setShowNames] = useState([])
    const [showNamesComponents, setShowNamesComponents] = useState([])
    const [horseName, setHorseName] = useState("")
    const [riderName, setRiderName] = useState("")
    const [selectedShow, setSelectedShow] = useState("")
    useEffect(() => {
      if(shows.length > 0) return;
      getShows().then((res) => {
        setShows(res);
        setShowNames(res.map((show) => show.name));
        setShowNamesComponents(res.map((show) => <Option value={show.name}>{show.name}</Option>));
      })
    }, [shows])

    const searchValueChanged = (e) => {
      const val = e.target.value;
      if(val != ""){
      let match = "";
      for(let i = 0; i < showNames.length; i++) {
        if(showNames[i].toLowerCase().includes(e.target.value.toLowerCase())) {
          match = showNames[i];
          break;
        }
      }
      const filteredShows = showNames.filter((show) => show.toLowerCase().includes(e.target.value.toLowerCase()));
      setShowNamesComponents(filteredShows.map((show) => <Option value={show}>{show}</Option>));
      setSelectedShow(filteredShows[0]);
    }else{
      setShowNamesComponents(shows.map((show) => <Option value={show.name}>{show.name}</Option>));
      setSelectedShow(shows[0].name);
    }
    }

    const selectedShowSet = (e) => {
      setSelectedShow(e);
    }

    const StartSearchHorse = () =>{
      console.log("Starting Search for: " + selectedShow);
      SearchHorseShow({"selectedShow":selectedShow, "horseName":horseName, "riderName":riderName});

    }



    return (
       <Card  className="w-auto" color="white" shadow={true} children={
      <div className="p-10">
<Typography variant="h4" color="blue-gray">
          Horse Search
        </Typography>
        <Typography color="gray" className="mt-1 font-normal">
          Search for a horse and see its details.
        </Typography>


        
        <form className="mt-8 mb-2 w-80 max-w-screen-lg sm:w-96">
          <div className="mb-1 flex flex-col gap-6">

          <Typography variant="h6" color="blue-gray" className="-mb-3">
              Show
            </Typography>
            <Input label="Search Shows" onChange={searchValueChanged} icon={<i className="fas fa-heart" />} />

          <Select variant="outlined" id="showSelect" label="Show" onChange={selectedShowSet}>
                  {showNamesComponents}
                </Select>


            
                <Typography variant="h6" color="blue-gray" className="-mb-3">
              Rider Last Name
            </Typography>
            <Input
              size="lg"
              placeholder="Jessup"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
              onChange={(e) => setRiderName(e.target.value)}
            />



            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Horse Name
            </Typography>
            <Input
              size="lg"
              placeholder="Horsimo"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
              onChange={(e) => setHorseName(e.target.value)}

            />




          </div>
          <Button className="mt-6" fullWidth onClick={StartSearchHorse}>
            Search
          </Button>
        </form>
</div>

       }/>
        
   
    );
  }