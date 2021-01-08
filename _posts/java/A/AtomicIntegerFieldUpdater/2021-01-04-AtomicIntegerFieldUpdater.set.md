---
title: AtomicIntegerFieldUpdater.set()
permalink: Java/AtomicIntegerFieldUpdater/set
date: 2021-01-04
key: JavaJava.A.AtomicIntegerFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerFieldUpdater.metodos valor="set" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void set(T obj, int newValue)
~~~

## Parámetros
* **int newValue**,  {% include w3api/param_description.html metodo=_data parametro="int newValue" %}
* **T obj**,  {% include w3api/param_description.html metodo=_data parametro="T obj" %}

## Clase Padre
[AtomicIntegerFieldUpdater](/Java/AtomicIntegerFieldUpdater/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicIntegerFieldUpdater.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
