---
title: ConcurrentMap.replace()
permalink: Java/ConcurrentMap/replace
date: 2021-01-04
key: JavaJava.C.ConcurrentMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentMap.metodos valor="replace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
V replace(K key, V value)
boolean replace(K key, V oldValue, V newValue)
~~~

## Parámetros
* **V value**,  {% include w3api/param_description.html metodo=_data parametro="V value" %}
* **K key**,  {% include w3api/param_description.html metodo=_data parametro="K key" %}
* **V newValue**,  {% include w3api/param_description.html metodo=_data parametro="V newValue" %}
* **V oldValue**,  {% include w3api/param_description.html metodo=_data parametro="V oldValue" %}

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
