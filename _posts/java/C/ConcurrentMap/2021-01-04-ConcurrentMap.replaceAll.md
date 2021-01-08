---
title: ConcurrentMap.replaceAll()
permalink: Java/ConcurrentMap/replaceAll
date: 2021-01-04
key: JavaJava.C.ConcurrentMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentMap.metodos valor="replaceAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void replaceAll(BiFunction<? super K,? super V,? extends V> function)
~~~

## Parámetros
* **? super V**,  {% include w3api/param_description.html metodo=_data parametro="? super V" %}
* **BiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<? super K" %}
* **? extends V&gt; function**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> function" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ConcurrentMap](/Java/ConcurrentMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
