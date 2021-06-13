---
title: DelayQueue.drainTo()
permalink: /Java/DelayQueue/drainTo/
date: 2021-01-11
key: Java.D.DelayQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DelayQueue.metodos valor="drainTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int drainTo(Collection<? super E> c)
public int drainTo(Collection<? super E> c, int maxElements)
~~~

## Parámetros
* **int maxElements**,  {% include w3api/param_description.html metodo=_dato parametro="int maxElements" %}
* **Collection&lt;? super E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? super E> c" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[DelayQueue](/Java/DelayQueue/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
