---
title: FlightRecorder.addPeriodicEvent()
permalink: /Java/FlightRecorder/addPeriodicEvent/
date: 2021-01-11
key: Java.F.FlightRecorder
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FlightRecorder.metodos valor="addPeriodicEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void addPeriodicEvent(Class<? extends Event> eventClass, Runnable hook) throws SecurityException
~~~

## Parámetros
* **Runnable hook**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable hook" %}
* **Class&lt;? extends Event&gt; eventClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends Event> eventClass" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

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
