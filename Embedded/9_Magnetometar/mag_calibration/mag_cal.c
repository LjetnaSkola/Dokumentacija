double soft_matrix[3][3] = {{1.0151, 0 ,0}, {0, 1.0321, 0} , {0 , 0, 0.9561}};
double hard_matrix[3] = {49.7109, 25.8281, -18.7131};  

void magcalMPU9250(uint8_t MPU9250Mmode)
{
    // https://github.com/kriswiner/MPU6050/wiki/Simple-and-Effective-Magnetometer-Calibration
    // https://github.com/adafruit/Adafruit_SensorLab/blob/master/notebooks/Mag_Gyro_Calibration.ipynb
    uint16_t ii = 0, sample_count = 0;
    uint8_t temp_data_mag[7];
    double MPU9250mRes = 0.15;
    double mx_temp, my_temp, mz_temp;
    int32_t mag_bias[3] = {0, 0, 0}, mag_scale[3] = {0, 0, 0};
    int16_t mag_max[3] = {-32767, -32767, -32767}, mag_min[3] = {32767, 32767, 32767}, mag_temp[3] = {0, 0, 0};

    str_len = sprintf((char*)str, "Mag Calibration: Wave device in a figure eight until done!\n\r");
    printf("%s",str);

    HAL_Delay(2000);
    
    str_len = sprintf((char*)str, "StartMagCalibrate \n");                  // start signal for python app!
    printf("%s",str);
    HAL_Delay(20);

    // shoot for ~fifteen seconds of mag data
    if(MPU9250Mmode == 0x02) sample_count = 128;  // at 8 Hz ODR, new mag data is available every 125 ms
    if(MPU9250Mmode == 0x06) sample_count = 1500;  // at 100 Hz ODR, new mag data is available every 10 ms

    for(ii = 0; ii < sample_count; ii++)
    {
        // Read the mag data
        ak8963_read_reg(AK8963_HXL, temp_data_mag, 7);              // reading magnetometer data and overflow
        ak8963_read_reg(0x02, &check, 1);                               // checking whether everything has been read

        if((temp_data_mag[6] & 0x08) !=8 && ((check & 0x02) == 0) )      // 0 normal | 1 data overrun
        {
            mag_temp[0] = ((uint16_t)temp_data_mag[1]<<8 | temp_data_mag[0]);           // low byte in the sensor goes first
            mag_temp[1] = ((uint16_t)temp_data_mag[3]<<8 | temp_data_mag[2]);
            mag_temp[2] = ((uint16_t)temp_data_mag[5]<<8 | temp_data_mag[4]);

            mx_temp = (int16_t)(temp_data_mag[1]<<8 | temp_data_mag[0])*d_asax * MPU9250mRes;
            my_temp = (int16_t)(temp_data_mag[3]<<8 | temp_data_mag[2])*d_asay * MPU9250mRes;
            mz_temp = (int16_t)(temp_data_mag[5]<<8 | temp_data_mag[4])*d_asaz * MPU9250mRes;

            str_len = sprintf((char*)str, "%.4lf %.4lf %.4lf\n", mx_temp, my_temp, mz_temp);  // for display in the python app
            printf("%s",str);
            HAL_Delay(10);                                              // it has to wait because of the python app (rate 20ms) 

        }
        for (int jj = 0; jj < 3; jj++)
        {
            if(mag_temp[jj] > mag_max[jj]) mag_max[jj] = mag_temp[jj];
            if(mag_temp[jj] < mag_min[jj]) mag_min[jj] = mag_temp[jj];
        }
        if(MPU9250Mmode == 0x02) HAL_Delay(135);  // at 8 Hz ODR, new mag data is available every 125 ms
        if(MPU9250Mmode == 0x06) HAL_Delay(12);   // at 100 Hz ODR, new mag data is available every 10 ms
    }

    // Get hard iron correction
    mag_bias[0]  = (mag_max[0] + mag_min[0])/2;  // get average x mag bias in counts
    mag_bias[1]  = (mag_max[1] + mag_min[1])/2;  // get average y mag bias in counts
    mag_bias[2]  = (mag_max[2] + mag_min[2])/2;  // get average z mag bias in counts

    MX_offset = (double) mag_bias[0]*MPU9250mRes*d_asax;  // save mag biases in uT for main program
    MY_offset = (double) mag_bias[1]*MPU9250mRes*d_asay;
    MZ_offset = (double) mag_bias[2]*MPU9250mRes*d_asaz;

    // Get soft iron correction estimate
    mag_scale[0]  = (mag_max[0] - mag_min[0])/2;  // get average x axis max chord length in counts
    mag_scale[1]  = (mag_max[1] - mag_min[1])/2;  // get average y axis max chord length in counts
    mag_scale[2]  = (mag_max[2] - mag_min[2])/2;  // get average z axis max chord length in counts

    double avg_rad = mag_scale[0] + mag_scale[1] + mag_scale[2];
    avg_rad /= 3.0;

    MX_offset_soft_iron = avg_rad/((double)mag_scale[0]);
    MY_offset_soft_iron = avg_rad/((double)mag_scale[1]);
    MZ_offset_soft_iron = avg_rad/((double)mag_scale[2]);
    
    soft_matrix[0][0] = MX_offset_soft_iron;
    soft_matrix[1][1] = MY_offset_soft_iron;
    soft_matrix[2][2] = MZ_offset_soft_iron;
    
    hard_matrix[0] = MX_offset;
    hard_matrix[1] = MY_offset;
    hard_matrix[2] = MZ_offset;

    str_len = sprintf((char*)str, "MagCalibrated \n");                  // end signal for python app!
    printf("%s",str);
    HAL_Delay(20);
    str_len = sprintf((char*)str, "Mag Calibration done! Hard iron: %.4lf %.4lf %.4lf\n\r", MX_offset, MY_offset, MZ_offset);
    printf("%s",str);
    HAL_Delay(20);
    str_len = sprintf((char*)str, "Mag Calibration done! Soft iron: %.4lf %.4lf %.4lf\n\r", MX_offset_soft_iron, MY_offset_soft_iron, MZ_offset_soft_iron);
    printf("%s",str);
  
}