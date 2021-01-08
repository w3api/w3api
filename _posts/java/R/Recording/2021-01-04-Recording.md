---
title: Recording
permalink: Java/Recording
date: 2021-01-04
key: JavaJava.R.Recording
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.Recording.description }}

## Sintaxis
~~~java
public final class Recording extends Object implements Closeable
~~~

## Constructores
* [Recording()](/Java/Recording/Recording/)

## Métodos
* [close()](/Java/Recording/close)
* [copy()](/Java/Recording/copy)
* [disable()](/Java/Recording/disable)
* [dump()](/Java/Recording/dump)
* [enable()](/Java/Recording/enable)
* [getDestination()](/Java/Recording/getDestination)
* [getDumpOnExit()](/Java/Recording/getDumpOnExit)
* [getDuration()](/Java/Recording/getDuration)
* [getId()](/Java/Recording/getId)
* [getMaxAge()](/Java/Recording/getMaxAge)
* [getMaxSize()](/Java/Recording/getMaxSize)
* [getName()](/Java/Recording/getName)
* [getSettings()](/Java/Recording/getSettings)
* [getSize()](/Java/Recording/getSize)
* [getStartTime()](/Java/Recording/getStartTime)
* [getState()](/Java/Recording/getState)
* [getStopTime()](/Java/Recording/getStopTime)
* [getStream()](/Java/Recording/getStream)
* [isToDisk()](/Java/Recording/isToDisk)
* [scheduleStart()](/Java/Recording/scheduleStart)
* [setDestination()](/Java/Recording/setDestination)
* [setDumpOnExit()](/Java/Recording/setDumpOnExit)
* [setDuration()](/Java/Recording/setDuration)
* [setMaxAge()](/Java/Recording/setMaxAge)
* [setMaxSize()](/Java/Recording/setMaxSize)
* [setName()](/Java/Recording/setName)
* [setSettings()](/Java/Recording/setSettings)
* [setToDisk()](/Java/Recording/setToDisk)
* [start()](/Java/Recording/start)
* [stop()](/Java/Recording/stop)

## Ejemplo
~~~java
{{ site.data.Java.R.Recording.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.Recording.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
