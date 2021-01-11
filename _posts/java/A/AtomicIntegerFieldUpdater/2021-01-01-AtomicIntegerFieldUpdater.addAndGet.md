---
title: AtomicIntegerFieldUpdater.addAndGet()
permalink: Java/AtomicIntegerFieldUpdater/addAndGet
date: 2021-01-11
key: JavaJava.A.AtomicIntegerFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerFieldUpdater.metodos valor="addAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int addAndGet(T obj, int delta)
~~~

## Parámetros
* **T obj**,  {% include w3api/param_description.html metodo=_dato parametro="T obj" %}
* **int delta**,  {% include w3api/param_description.html metodo=_dato parametro="int delta" %}

## Clase Padre
[AtomicIntegerFieldUpdater](/Java/AtomicIntegerFieldUpdater/)

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
