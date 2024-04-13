---
title: ConcurrentHashMap.searchKeys()
permalink: /Java/ConcurrentHashMap/searchKeys/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="searchKeys" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> U searchKeys(long parallelismThreshold, Function<? super K,? extends U> searchFunction)
~~~

## Parámetros
* **? extends U&gt; searchFunction**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> searchFunction" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **Function&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super K" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

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
