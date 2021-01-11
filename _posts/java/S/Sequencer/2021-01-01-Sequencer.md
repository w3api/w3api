---
title: Sequencer
permalink: Java/Sequencer
date: 2021-01-11
key: JavaJava.S.Sequencer
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.Sequencer.description }}

## Sintaxis
~~~java
public interface Sequencer extends MidiDevice
~~~

## Campos
* [LOOP_CONTINUOUSLY](/Java/Sequencer/LOOP_CONTINUOUSLY)

## Métodos
* [addControllerEventListener()](/Java/Sequencer/addControllerEventListener)
* [addMetaEventListener()](/Java/Sequencer/addMetaEventListener)
* [getLoopCount()](/Java/Sequencer/getLoopCount)
* [getLoopEndPoint()](/Java/Sequencer/getLoopEndPoint)
* [getLoopStartPoint()](/Java/Sequencer/getLoopStartPoint)
* [getMasterSyncMode()](/Java/Sequencer/getMasterSyncMode)
* [getMasterSyncModes()](/Java/Sequencer/getMasterSyncModes)
* [getMicrosecondLength()](/Java/Sequencer/getMicrosecondLength)
* [getMicrosecondPosition()](/Java/Sequencer/getMicrosecondPosition)
* [getSequence()](/Java/Sequencer/getSequence)
* [getSlaveSyncMode()](/Java/Sequencer/getSlaveSyncMode)
* [getSlaveSyncModes()](/Java/Sequencer/getSlaveSyncModes)
* [getTempoFactor()](/Java/Sequencer/getTempoFactor)
* [getTempoInBPM()](/Java/Sequencer/getTempoInBPM)
* [getTempoInMPQ()](/Java/Sequencer/getTempoInMPQ)
* [getTickLength()](/Java/Sequencer/getTickLength)
* [getTickPosition()](/Java/Sequencer/getTickPosition)
* [getTrackMute()](/Java/Sequencer/getTrackMute)
* [getTrackSolo()](/Java/Sequencer/getTrackSolo)
* [isRecording()](/Java/Sequencer/isRecording)
* [isRunning()](/Java/Sequencer/isRunning)
* [recordDisable()](/Java/Sequencer/recordDisable)
* [recordEnable()](/Java/Sequencer/recordEnable)
* [removeControllerEventListener()](/Java/Sequencer/removeControllerEventListener)
* [removeMetaEventListener()](/Java/Sequencer/removeMetaEventListener)
* [setLoopCount()](/Java/Sequencer/setLoopCount)
* [setLoopEndPoint()](/Java/Sequencer/setLoopEndPoint)
* [setLoopStartPoint()](/Java/Sequencer/setLoopStartPoint)
* [setMasterSyncMode()](/Java/Sequencer/setMasterSyncMode)
* [setMicrosecondPosition()](/Java/Sequencer/setMicrosecondPosition)
* [setSequence()](/Java/Sequencer/setSequence)
* [setSlaveSyncMode()](/Java/Sequencer/setSlaveSyncMode)
* [setTempoFactor()](/Java/Sequencer/setTempoFactor)
* [setTempoInBPM()](/Java/Sequencer/setTempoInBPM)
* [setTempoInMPQ()](/Java/Sequencer/setTempoInMPQ)
* [setTickPosition()](/Java/Sequencer/setTickPosition)
* [setTrackMute()](/Java/Sequencer/setTrackMute)
* [setTrackSolo()](/Java/Sequencer/setTrackSolo)
* [start()](/Java/Sequencer/start)
* [startRecording()](/Java/Sequencer/startRecording)
* [stop()](/Java/Sequencer/stop)
* [stopRecording()](/Java/Sequencer/stopRecording)

## Ejemplo
~~~java
{{ site.data.Java.S.Sequencer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Sequencer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
