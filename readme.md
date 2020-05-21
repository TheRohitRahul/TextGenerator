Generates text using GRU in style of the text fed to it during training

### Training

All you need to do is specify a model name along with a text file that you want to use to train the model in the config.py file . 
After that run 

```
python main_code.py 
```
and the network will be trained 

### Inference

To use this model for inference you will have to run 
```
python test_code.py 
```
and a prompt will come up asking you to enter 5 words. Using these 5 words as initial words for a sentence it will generate the number of words that you have specified in the config.py file

Do note that the quality of the output starts to degrade rapidly if you have specified a large number in the number of words to generate parameter.

### Example input sentences : 

1. I am the one knocking

2. Everything before the word but

3. a lion doesn't concern himself

4. jon snow loves and he

### Output for the example sentences

i am the one knocking on the walls and the first men and the king in the north
i am the one knocking at the top of the wall the stone of the hall

everything before the word but it was a shade of the lannister the king's hand

a lion doesn't concern himself in the black of the night

jon snow loves and he could not watch the old one and the fat one