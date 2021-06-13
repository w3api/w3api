---
title: RecordingState
permalink: Java/RecordingState
date: 2021-01-11
key: Java.R.RecordingState
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'enumerado java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RecordingState.description }}

## Sintaxis
~~~java
public enum RecordingState extends Enum<RecordingState>
~~~

## Enumerados
* [CLOSED](/Java/RecordingState/CLOSED)
* [DELAYED](/Java/RecordingState/DELAYED)
* [NEW](/Java/RecordingState/NEW)
* [RUNNING](/Java/RecordingState/RUNNING)
* [STOPPED](/Java/RecordingState/STOPPED)

## Métodos
* [valueOf()](/Java/RecordingState/valueOf)
* [values()](/Java/RecordingState/values)

## Ejemplo
~~~java
{{ site.data.Java.R.RecordingState.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RecordingState.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
