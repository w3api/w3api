---
title: FlightRecorder.removePeriodicEvent()
permalink: /Java/FlightRecorder/removePeriodicEvent/
date: 2021-01-11
key: Java.F.FlightRecorder
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlightRecorder.metodos valor="removePeriodicEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean removePeriodicEvent(Runnable hook) throws SecurityException
~~~

## Parámetros
* **Runnable hook**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable hook" %}

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
