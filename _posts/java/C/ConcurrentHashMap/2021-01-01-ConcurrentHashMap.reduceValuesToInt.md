---
title: ConcurrentHashMap.reduceValuesToInt()
permalink: Java/ConcurrentHashMap/reduceValuesToInt
date: 2021-01-11
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceValuesToInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int reduceValuesToInt(long parallelismThreshold, ToIntFunction<? super V> transformer, int basis, IntBinaryOperator reducer)
~~~

## Parámetros
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **IntBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_dato parametro="IntBinaryOperator reducer" %}
* **int basis**,  {% include w3api/param_description.html metodo=_dato parametro="int basis" %}
* **ToIntFunction&lt;? super V&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="ToIntFunction<? super V> transformer" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

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
