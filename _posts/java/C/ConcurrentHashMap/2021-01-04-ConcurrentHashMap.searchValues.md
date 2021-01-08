---
title: ConcurrentHashMap.searchValues()
permalink: Java/ConcurrentHashMap/searchValues
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="searchValues" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> U searchValues(long parallelismThreshold, Function<? super V,? extends U> searchFunction)
~~~

## Parámetros
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_data parametro="long parallelismThreshold" %}
* **? extends U&gt; searchFunction**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> searchFunction" %}
* **Function&lt;? super V**,  {% include w3api/param_description.html metodo=_data parametro="Function<? super V" %}

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
