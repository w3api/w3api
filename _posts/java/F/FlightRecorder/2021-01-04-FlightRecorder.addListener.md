---
title: FlightRecorder.addListener()
permalink: Java/FlightRecorder/addListener
date: 2021-01-04
key: JavaJava.F.FlightRecorder
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlightRecorder.metodos valor="addListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void addListener(FlightRecorderListener changeListener)
~~~

## Parámetros
* **FlightRecorderListener changeListener**,  {% include w3api/param_description.html metodo=_data parametro="FlightRecorderListener changeListener" %}

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
{%- for _ldc in site.data.Java.F.FlightRecorder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
