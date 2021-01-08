---
title: FlightRecorderMXBean.openStream()
permalink: Java/FlightRecorderMXBean/openStream
date: 2021-01-04
key: JavaJava.F.FlightRecorderMXBean
category: java
tags: ['java se', 'jdk.management.jfr', 'jdk.management.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlightRecorderMXBean.metodos valor="openStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long openStream(long recordingId, Map<String,String> streamOptions) throws IOException
~~~

## Parámetros
* **long recordingId**,  {% include w3api/param_description.html metodo=_data parametro="long recordingId" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **String&gt; streamOptions**,  {% include w3api/param_description.html metodo=_data parametro="String> streamOptions" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
