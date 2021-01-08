---
title: ConcurrentHashMap.forEach()
permalink: Java/ConcurrentHashMap/forEach
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
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
* **? super V&gt; action**,  {% include w3api/param_description.html metodo=_data parametro="? super V> action" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_data parametro="long parallelismThreshold" %}
* **Consumer&lt;? super U&gt; action**,  {% include w3api/param_description.html metodo=_data parametro="Consumer<? super U> action" %}
* **? super V**,  {% include w3api/param_description.html metodo=_data parametro="? super V" %}
* **BiConsumer&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="BiConsumer<? super K" %}
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
