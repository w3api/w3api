---
title: ConcurrentHashMap.reduceToDouble()
permalink: Java/ConcurrentHashMap/reduceToDouble
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceToDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double reduceToDouble(long parallelismThreshold, ToDoubleBiFunction<? super K,? super V> transformer, double basis, DoubleBinaryOperator reducer)
~~~

## Parámetros
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_data parametro="long parallelismThreshold" %}
* **DoubleBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_data parametro="DoubleBinaryOperator reducer" %}
* **double basis**,  {% include w3api/param_description.html metodo=_data parametro="double basis" %}
* **? super V&gt; transformer**,  {% include w3api/param_description.html metodo=_data parametro="? super V> transformer" %}
* **ToDoubleBiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="ToDoubleBiFunction<? super K" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentHashMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
