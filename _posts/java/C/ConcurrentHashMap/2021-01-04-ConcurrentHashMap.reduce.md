---
title: ConcurrentHashMap.reduce()
permalink: Java/ConcurrentHashMap/reduce
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduce" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> U reduce(long parallelismThreshold, BiFunction<? super K,? super V,? extends U> transformer, BiFunction<? super U,? super U,? extends U> reducer)
~~~

## Parámetros
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_data parametro="long parallelismThreshold" %}
* **? super U**,  {% include w3api/param_description.html metodo=_data parametro="? super U" %}
* **? super V**,  {% include w3api/param_description.html metodo=_data parametro="? super V" %}
* **? extends U&gt; reducer**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> reducer" %}
* **BiFunction&lt;? super U**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<? super U" %}
* **? extends U&gt; transformer**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> transformer" %}
* **BiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<? super K" %}

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
