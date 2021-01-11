---
title: FlightRecorder.removeListener()
permalink: Java/FlightRecorder/removeListener
date: 2021-01-11
key: JavaJava.F.FlightRecorder
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlightRecorder.metodos valor="removeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean removeListener(FlightRecorderListener changeListener)
~~~

## Parámetros
* **FlightRecorderListener changeListener**,  {% include w3api/param_description.html metodo=_dato parametro="FlightRecorderListener changeListener" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[FlightRecorder](/Java/FlightRecorder/)

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