---
title: RecordingFile
permalink: /Java/RecordingFile/
date: 2021-01-11
key: Java.R.RecordingFile
category: Java
tags: ['java se', 'jdk.jfr.consumer', 'jdk.jfr', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RecordingFile.description }}

## Sintaxis
~~~java
public final class RecordingFile extends Object implements Closeable
~~~

## Constructores
* [RecordingFile()](/Java/RecordingFile/RecordingFile/)

## Métodos
* [close()](/Java/RecordingFile/close)
* [hasMoreEvents()](/Java/RecordingFile/hasMoreEvents)
* [readAllEvents()](/Java/RecordingFile/readAllEvents)
* [readEvent()](/Java/RecordingFile/readEvent)
* [readEventTypes()](/Java/RecordingFile/readEventTypes)

## Ejemplo
~~~java
{{ site.data.Java.R.RecordingFile.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RecordingFile.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
