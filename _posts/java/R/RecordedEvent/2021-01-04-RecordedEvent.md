---
title: RecordedEvent
permalink: Java/RecordedEvent
date: 2021-01-04
key: JavaJava.R.RecordedEvent
category: java
tags: ['java se', 'jdk.jfr.consumer', 'jdk.jfr', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RecordedEvent.description }}

## Sintaxis
~~~java
public final class RecordedEvent extends RecordedObject
~~~

## Métodos
* [getDuration()](/Java/RecordedEvent/getDuration)
* [getEndTime()](/Java/RecordedEvent/getEndTime)
* [getEventType()](/Java/RecordedEvent/getEventType)
* [getFields()](/Java/RecordedEvent/getFields)
* [getStackTrace()](/Java/RecordedEvent/getStackTrace)
* [getStartTime()](/Java/RecordedEvent/getStartTime)
* [getThread()](/Java/RecordedEvent/getThread)

## Ejemplo
~~~java
{{ site.data.Java.R.RecordedEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RecordedEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
