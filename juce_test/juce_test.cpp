


void playTestSound()
{
    AudioDeviceManager deviceManager;
    deviceManager.initialise(255,255,NULL, true);
    deviceManager.playTestSound();
    Thread::sleep(5000);
}

//==============================================================================
int main (int argc, char* argv[])
{
    ScopedJuceInitialiser_GUI plattform;
    playTestSound();
    return 0;
}