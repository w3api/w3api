---
title: AtomicInteger.lazySet()
permalink: Java/AtomicInteger/lazySet
date: 2021-01-11
key: JavaJava.A.AtomicInteger
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicInteger.metodos valor="lazySet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void lazySet(int newValue)
~~~

## Parámetros
* **int newValue**,  {% include w3api/param_description.html metodo=_dato parametro="int newValue" %}

## Clase Padre
[AtomicInteger](/Java/AtomicInteger/)

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
