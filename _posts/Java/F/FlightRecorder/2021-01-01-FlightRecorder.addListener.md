---
title: FlightRecorder.addListener()
permalink: /Java/FlightRecorder/addListener/
date: 2021-01-11
key: Java.F.FlightRecorder
category: Java
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
