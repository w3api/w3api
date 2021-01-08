---
title: FlightRecorderMXBean.getRecordingOptions()
permalink: Java/FlightRecorderMXBean/getRecordingOptions
date: 2021-01-04
key: JavaJava.F.FlightRecorderMXBean
category: java
tags: ['java se', 'jdk.management.jfr', 'jdk.management.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlightRecorderMXBean.metodos valor="getRecordingOptions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Map<String,String> getRecordingOptions(long recordingId) throws IllegalArgumentException
~~~

## Parámetros
* **long recordingId**,  {% include w3api/param_description.html metodo=_data parametro="long recordingId" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FlightRecorderMXBean](/Java/FlightRecorderMXBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FlightRecorderMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
