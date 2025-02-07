// import { useState } from 'react';
// import axios from 'axios';
// import {
//   Button,
//   Card,
//   TextField,
//   Typography,
//   Container,
//   Box,
// } from '@mui/material';

// export default function App() {
//   const [image, setImage] = useState(null);
//   const [threshold, setThreshold] = useState(60);
//   const [result, setResult] = useState(null);
//   const [processedImage, setProcessedImage] = useState(null);

//   const handleImageUpload = (event) => {
//     const file = event.target.files[0];
//     const reader = new FileReader();
//     reader.readAsDataURL(file);
//     reader.onload = () => {
//       setImage(reader.result);
//     };
//   };

//   const processImage = async () => {
//     try {
//       const base64Image = image.split(',')[1];
//       const response = await axios.post('http://localhost:5001/process_image', {
//         image: base64Image,
//         threshold: threshold,
//       });
//       setResult(response.data);
//       visualizeBugholes(response.data.locations);
//     } catch (error) {
//       console.error('Error processing image:', error);
//     }
//   };

//   const visualizeBugholes = (locations) => {
//     if (!image || !locations) return;
//     const img = new Image();
//     img.src = image;
//     img.onload = () => {
//       const canvas = document.createElement('canvas');
//       canvas.width = img.width;
//       canvas.height = img.height;
//       const ctx = canvas.getContext('2d');
//       ctx.drawImage(img, 0, 0);
//       ctx.strokeStyle = 'red';
//       ctx.lineWidth = 4;
//       locations.forEach(([y1, y2, x1, x2]) => {
//         ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);
//       });
//       setProcessedImage(canvas.toDataURL());
//     };
//   };

//   return (
//     <Container
//       maxWidth="md"
//       sx={{
//         p: 4,
//         bgcolor: '#121212',
//         color: 'white',
//         borderRadius: 4,
//         boxShadow: 5,
//       }}
//     >
//       <Typography
//         variant="h3"
//         align="center"
//         sx={{ fontWeight: 'bold', mb: 3, color: '#f50057' }}
//       >
//         Bughole Detector
//       </Typography>
//       <Box display="flex" flexDirection="column" alignItems="center" gap={2}>
//         <Button
//           variant="contained"
//           component="label"
//           sx={{ bgcolor: '#6200ea' }}
//         >
//           Upload Image
//           <input type="file" hidden onChange={handleImageUpload} />
//         </Button>
//         <TextField
//           type="number"
//           label="Threshold"
//           value={threshold}
//           onChange={(e) => setThreshold(Number(e.target.value))}
//           variant="filled"
//           sx={{ bgcolor: 'white', borderRadius: 1 }}
//         />
//         <Button
//           variant="contained"
//           color="secondary"
//           onClick={processImage}
//           sx={{ mt: 2, width: '50%' }}
//         >
//           Process Image
//         </Button>
//       </Box>
//       <Box display="flex" justifyContent="center" mt={4} gap={2}>
//         {image && (
//           <img
//             src={image}
//             alt="Uploaded"
//             style={{
//               width: 250,
//               height: 250,
//               borderRadius: 10,
//               boxShadow: '0px 4px 10px rgba(255,255,255,0.2)',
//             }}
//           />
//         )}
//         {processedImage && (
//           <img
//             src={processedImage}
//             alt="Processed"
//             style={{
//               width: 250,
//               height: 250,
//               borderRadius: 10,
//               border: '3px solid #f50057',
//               boxShadow: '0px 4px 10px rgba(255,255,255,0.5)',
//             }}
//           />
//         )}
//       </Box>
//       {result && (
//         <Card
//           sx={{
//             p: 3,
//             mt: 4,
//             bgcolor: '#212121',
//             color: 'white',
//             borderRadius: 2,
//             boxShadow: 3,
//           }}
//         >
//           <Typography variant="h5" sx={{ color: '#00e676' }}>
//             Bugholes Found: {result.num_bugholes}
//           </Typography>
//           <pre
//             style={{
//               background: '#333',
//               padding: '10px',
//               borderRadius: '5px',
//               overflow: 'auto',
//             }}
//           >
//             {JSON.stringify(result.locations, null, 2)}
//           </pre>
//         </Card>
//       )}
//     </Container>
//   );
// }
import { useState } from 'react';
import axios from 'axios';
import {
  Button,
  Card,
  TextField,
  Typography,
  Container,
  Box,
  List,
  ListItem,
  ListItemText,
} from '@mui/material';

export default function App() {
  const [image, setImage] = useState(null);
  const [threshold, setThreshold] = useState(60);
  const [result, setResult] = useState(null);
  const [processedImage, setProcessedImage] = useState(null);

  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
      setImage(reader.result);
    };
  };

  const processImage = async () => {
    try {
      const base64Image = image.split(',')[1];
      const response = await axios.post('http://localhost:5001/process_image', {
        image: base64Image,
        threshold: threshold,
      });
      setResult(response.data);
      visualizeBugholes(response.data.locations);
    } catch (error) {
      console.error('Error processing image:', error);
    }
  };

  const visualizeBugholes = (locations) => {
    if (!image || !locations) return;
    const img = new Image();
    img.src = image;
    img.onload = () => {
      const canvas = document.createElement('canvas');
      canvas.width = img.width;
      canvas.height = img.height;
      const ctx = canvas.getContext('2d');
      ctx.drawImage(img, 0, 0);
      ctx.strokeStyle = 'red';
      ctx.lineWidth = 4;
      locations.forEach(([y1, y2, x1, x2], index) => {
        ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);
      });
      setProcessedImage(canvas.toDataURL());
    };
  };

  return (
    <Container
      maxWidth="md"
      sx={{
        p: 4,
        bgcolor: '#121212',
        color: 'white',
        borderRadius: 4,
        boxShadow: 5,
      }}
    >
      <Typography
        variant="h3"
        align="center"
        sx={{ fontWeight: 'bold', mb: 3, color: '#f50057' }}
      >
        Bughole Detector
      </Typography>
      <Box display="flex" flexDirection="column" alignItems="center" gap={2}>
        <Button
          variant="contained"
          component="label"
          sx={{ bgcolor: '#6200ea' }}
        >
          Upload Image
          <input type="file" hidden onChange={handleImageUpload} />
        </Button>
        <TextField
          type="number"
          label="Threshold"
          value={threshold}
          onChange={(e) => setThreshold(Number(e.target.value))}
          variant="filled"
          sx={{ bgcolor: 'white', borderRadius: 1 }}
        />
        <Button
          variant="contained"
          color="secondary"
          onClick={processImage}
          sx={{ mt: 2, width: '50%' }}
        >
          Process Image
        </Button>
      </Box>
      <Box display="flex" justifyContent="center" mt={4} gap={2}>
        {image && (
          <img
            src={image}
            alt="Uploaded"
            style={{
              width: 250,
              height: 250,
              borderRadius: 10,
              boxShadow: '0px 4px 10px rgba(255,255,255,0.2)',
            }}
          />
        )}
        {processedImage && (
          <img
            src={processedImage}
            alt="Processed"
            style={{
              width: 250,
              height: 250,
              borderRadius: 10,
              border: '3px solid #f50057',
              boxShadow: '0px 4px 10px rgba(255,255,255,0.5)',
            }}
          />
        )}
      </Box>
      {result && (
        <Card
          sx={{
            p: 3,
            mt: 4,
            bgcolor: '#212121',
            color: 'white',
            borderRadius: 2,
            boxShadow: 3,
          }}
        >
          <Typography variant="h5" sx={{ color: '#00e676' }}>
            Bugholes Found: {result.num_bugholes}
          </Typography>
          <List
            sx={{
              bgcolor: '#fff',
              p: 2,
              borderRadius: 1,
              maxHeight: 200,
              overflowY: 'auto',
            }}
          >
            {result.locations.map((loc, index) => (
              <ListItem key={index} divider>
                <ListItemText
                  primary={`Bughole ${index + 1}:`}
                  secondary={`Y: ${loc[0]}-${loc[1]}, X: ${loc[2]}-${loc[3]}`}
                  sx={{ color: '#00e676' }}
                />
              </ListItem>
            ))}
          </List>
        </Card>
      )}
    </Container>
  );
}
