---
title: MediaPlayer.Status
permalink: Java/MediaPlayer/Status
date: 2021-01-04
key: JavaJava.M.MediaPlayer.Status
category: java
tags: ['java se', 'javafx.scene.media', 'javafx.media', 'enumerado java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MediaPlayer.Status.description }}

## Sintaxis
~~~java
public static enum MediaPlayer.Status extends Enum<MediaPlayer.Status>
~~~

## Enumerados
* [DISPOSED](/Java/MediaPlayer/Status/DISPOSED)
* [HALTED](/Java/MediaPlayer/Status/HALTED)
* [PAUSED](/Java/MediaPlayer/Status/PAUSED)
* [PLAYING](/Java/MediaPlayer/Status/PLAYING)
* [READY](/Java/MediaPlayer/Status/READY)
* [STALLED](/Java/MediaPlayer/Status/STALLED)
* [STOPPED](/Java/MediaPlayer/Status/STOPPED)
* [UNKNOWN](/Java/MediaPlayer/Status/UNKNOWN)

## Métodos
* [valueOf()](/Java/MediaPlayer/Status/valueOf)
* [values()](/Java/MediaPlayer/Status/values)

## Ejemplo
~~~java
{{ site.data.Java.M.MediaPlayer.Status.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MediaPlayer.Status.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
