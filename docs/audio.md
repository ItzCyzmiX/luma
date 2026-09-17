# Audio

Luma initializes SDL audio and the mixer when you create an engine. Load an
audio file through `engine.Audio`:

```python
from luma import Luma


engine = Luma()
sound = engine.Audio.loadSound("assets/music.mp3")
```

`loadSound(path)` returns a sound object. The path is loaded immediately, and
an unreadable or unsupported file raises `Luma_Error` with SDL's error message.
The mixer supports the audio formats provided by the installed SDL mixer
library.

## Playback

Use `play()`, `pause()`, and `stop()` to control a sound:

```python
sound.play()
sound.pause()
sound.play()  # resumes a paused sound
sound.stop()
```

The `playing` and `paused` properties report the current state. Calling
`play()` on a stopped sound starts it from its current position; `stop()`
resets the position to zero.

Set `loop` before starting playback to restart the sound whenever it reaches
the end:

```python
sound.loop = True
sound.play()
```

Set `on_finish` to a no-argument callable to react when a non-looping sound
finishes:

```python
def finished():
    print("sound finished")


sound.on_finish = finished
```

## Volume and seeking

`volume` is a floating-point gain. It defaults to `1.0`; values below zero are
clamped to zero.

`position` and `duration` are integer milliseconds. Assigning `position` clamps
it to the range from zero through `duration`:

```python
sound.volume = 0.5
sound.position = 2_000
print(sound.position, sound.duration)
```

The current playback position can be read while the sound is playing. Seeking
is also useful for restarting a sound explicitly:

```python
sound.stop()
sound.position = 0
sound.play()
```

## Changing files and releasing sounds

Assigning a new `path` reloads the sound on the same sound object:

```python
sound.path = "assets/another-effect.wav"
```

Call `kill()` when a sound will no longer be used. Sounds loaded by
`engine.Audio` are also released automatically when the engine shuts down.

## Example

Run the complete interactive example from the repository root:

```bash
python examples/audio.py
```

It uses `examples/fx.mp3` and demonstrates playback, pause/resume, seeking,
volume, looping, and the finish callback.

Controls:

| Key | Action |
| --- | --- |
| `P` | Play or resume the sound |
| `SPACE` | Pause or resume the sound |
| `S` | Stop and reset the sound |
| `R` | Seek to the beginning |
| `LEFT` / `RIGHT` | Seek backward or forward by one second |
| `DOWN` / `UP` | Decrease or increase volume by `0.5` |
| `L` | Toggle looping |
