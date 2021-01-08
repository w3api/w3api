---
title: ConcurrentMap.remove()
permalink: Java/ConcurrentMap/remove
date: 2021-01-04
key: JavaJava.C.ConcurrentMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentMap.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean remove(Object key, Object value)
~~~

## Parámetros
* **Object key**,  {% include w3api/param_description.html metodo=_data parametro="Object key" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

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
