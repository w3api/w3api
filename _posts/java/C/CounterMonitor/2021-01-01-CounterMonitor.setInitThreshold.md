---
title: CounterMonitor.setInitThreshold()
permalink: /Java/CounterMonitor/setInitThreshold/
date: 2021-01-11
key: Java.C.CounterMonitor
category: Java
tags: ['java se', 'javax.management.monitor', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CounterMonitor.metodos valor="setInitThreshold" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setInitThreshold(Number value) throws IllegalArgumentException
~~~

## Parámetros
* **Number value**,  {% include w3api/param_description.html metodo=_dato parametro="Number value" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CounterMonitor](/Java/CounterMonitor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
