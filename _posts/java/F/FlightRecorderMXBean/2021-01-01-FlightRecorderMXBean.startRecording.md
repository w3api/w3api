---
title: FlightRecorderMXBean.startRecording()
permalink: Java/FlightRecorderMXBean/startRecording
date: 2021-01-11
key: JavaJava.F.FlightRecorderMXBean
category: java
tags: ['java se', 'jdk.management.jfr', 'jdk.management.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlightRecorderMXBean.metodos valor="startRecording" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void startRecording(long recordingId) throws IllegalStateException, SecurityException
~~~

## Parámetros
* **long recordingId**,  {% include w3api/param_description.html metodo=_dato parametro="long recordingId" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[FlightRecorderMXBean](/Java/FlightRecorderMXBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
