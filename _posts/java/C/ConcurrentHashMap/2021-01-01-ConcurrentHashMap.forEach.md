---
title: ConcurrentHashMap.forEach()
permalink: /Java/ConcurrentHashMap/forEach/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="forEach" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void forEach(long parallelismThreshold, BiConsumer<? super K,? super V> action)
<U> void forEach(long parallelismThreshold, BiFunction<? super K,? super V,? extends U> transformer, Consumer<? super U> action)
~~~

## Parámetros
* **Consumer&lt;? super U&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super U> action" %}
* **BiConsumer&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="BiConsumer<? super K" %}
* **? super V**,  {% include w3api/param_description.html metodo=_dato parametro="? super V" %}
* **BiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super K" %}
* **? super V&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="? super V> action" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **? extends U&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> transformer" %}

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
