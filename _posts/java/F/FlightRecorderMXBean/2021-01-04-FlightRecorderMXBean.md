---
title: FlightRecorderMXBean
permalink: Java/FlightRecorderMXBean
date: 2021-01-04
key: JavaJava.F.FlightRecorderMXBean
category: java
tags: ['java se', 'jdk.management.jfr', 'jdk.management.jfr', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FlightRecorderMXBean.description }}

## Sintaxis
~~~java
public interface FlightRecorderMXBean extends PlatformManagedObject
~~~

## Campos
* [MXBEAN_NAME](/Java/FlightRecorderMXBean/MXBEAN_NAME)

## Métodos
* [cloneRecording()](/Java/FlightRecorderMXBean/cloneRecording)
* [closeRecording()](/Java/FlightRecorderMXBean/closeRecording)
* [closeStream()](/Java/FlightRecorderMXBean/closeStream)
* [copyTo()](/Java/FlightRecorderMXBean/copyTo)
* [getConfigurations()](/Java/FlightRecorderMXBean/getConfigurations)
* [getEventTypes()](/Java/FlightRecorderMXBean/getEventTypes)
* [getRecordingOptions()](/Java/FlightRecorderMXBean/getRecordingOptions)
* [getRecordings()](/Java/FlightRecorderMXBean/getRecordings)
* [getRecordingSettings()](/Java/FlightRecorderMXBean/getRecordingSettings)
* [newRecording()](/Java/FlightRecorderMXBean/newRecording)
* [openStream()](/Java/FlightRecorderMXBean/openStream)
* [readStream()](/Java/FlightRecorderMXBean/readStream)
* [setConfiguration()](/Java/FlightRecorderMXBean/setConfiguration)
* [setPredefinedConfiguration()](/Java/FlightRecorderMXBean/setPredefinedConfiguration)
* [setRecordingOptions()](/Java/FlightRecorderMXBean/setRecordingOptions)
* [setRecordingSettings()](/Java/FlightRecorderMXBean/setRecordingSettings)
* [startRecording()](/Java/FlightRecorderMXBean/startRecording)
* [stopRecording()](/Java/FlightRecorderMXBean/stopRecording)
* [takeSnapshot()](/Java/FlightRecorderMXBean/takeSnapshot)

## Ejemplo
~~~java
{{ site.data.Java.F.FlightRecorderMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FlightRecorderMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
