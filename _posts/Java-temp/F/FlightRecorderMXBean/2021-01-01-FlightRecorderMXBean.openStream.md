---
title: FlightRecorderMXBean.openStream()
permalink: /Java/FlightRecorderMXBean/openStream/
date: 2021-01-11
key: Java.F.FlightRecorderMXBean
category: Java
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
* **String&gt; streamOptions**,  {% include w3api/param_description.html metodo=_dato parametro="String> streamOptions" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **long recordingId**,  {% include w3api/param_description.html metodo=_dato parametro="long recordingId" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

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
