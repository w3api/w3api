---
title: FlightRecorderMXBean.setPredefinedConfiguration()
permalink: Java/FlightRecorderMXBean/setPredefinedConfiguration
date: 2021-01-04
key: JavaJava.F.FlightRecorderMXBean
category: java
tags: ['java se', 'jdk.management.jfr', 'jdk.management.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlightRecorderMXBean.metodos valor="setPredefinedConfiguration" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setPredefinedConfiguration(long recordingId, String configurationName) throws IllegalArgumentException
~~~

## Parámetros
* **String configurationName**,  {% include w3api/param_description.html metodo=_data parametro="String configurationName" %}
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
