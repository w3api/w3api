---
title: ConcurrentHashMap.KeySetView.addAll()
permalink: Java/ConcurrentHashMap/KeySetView/addAll
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap.KeySetView
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.KeySetView.metodos valor="addAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean addAll(Collection<? extends K> c)
~~~

## Parámetros
* **Collection&lt;? extends K&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? extends K> c" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentHashMap.KeySetView](/Java/ConcurrentHashMap/KeySetView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentHashMap.KeySetView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
