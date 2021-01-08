---
title: ConcurrentHashMap.reduceToInt()
permalink: Java/ConcurrentHashMap/reduceToInt
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceToInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int reduceToInt(long parallelismThreshold, ToIntBiFunction<? super K,? super V> transformer, int basis, IntBinaryOperator reducer)
~~~

## Parámetros
* **ToIntBiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="ToIntBiFunction<? super K" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_data parametro="long parallelismThreshold" %}
* **int basis**,  {% include w3api/param_description.html metodo=_data parametro="int basis" %}
* **IntBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_data parametro="IntBinaryOperator reducer" %}
* **? super V&gt; transformer**,  {% include w3api/param_description.html metodo=_data parametro="? super V> transformer" %}

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
