---
title: FlightRecorderMXBean.cloneRecording()
permalink: /Java/FlightRecorderMXBean/cloneRecording/
date: 2021-01-11
key: Java.F.FlightRecorderMXBean
category: Java
tags: ['java se', 'jdk.management.jfr', 'jdk.management.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlightRecorderMXBean.metodos valor="cloneRecording" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long cloneRecording(long recordingId, boolean stop) throws IllegalArgumentException, SecurityException
~~~

## Parámetros
* **long recordingId**,  {% include w3api/param_description.html metodo=_dato parametro="long recordingId" %}
* **boolean stop**,  {% include w3api/param_description.html metodo=_dato parametro="boolean stop" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
