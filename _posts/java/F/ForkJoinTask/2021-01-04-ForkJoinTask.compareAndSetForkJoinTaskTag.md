---
title: ForkJoinTask.compareAndSetForkJoinTaskTag()
permalink: Java/ForkJoinTask/compareAndSetForkJoinTaskTag
date: 2021-01-04
key: JavaJava.F.ForkJoinTask
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinTask.metodos valor="compareAndSetForkJoinTaskTag" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean compareAndSetForkJoinTaskTag(short expect, short update)
~~~

## Parámetros
* **short expect**,  {% include w3api/param_description.html metodo=_data parametro="short expect" %}
* **short update**,  {% include w3api/param_description.html metodo=_data parametro="short update" %}

## Clase Padre
[ForkJoinTask](/Java/ForkJoinTask/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForkJoinTask.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
