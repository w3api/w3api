---
title: CyclicBarrier.CyclicBarrier()
permalink: Java/CyclicBarrier/CyclicBarrier
date: 2021-01-04
key: JavaJava.C.CyclicBarrier
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CyclicBarrier.constructores valor="CyclicBarrier" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CyclicBarrier(int parties)
public CyclicBarrier(int parties, Runnable barrierAction)
~~~

## Parámetros
* **int parties**,  {% include w3api/param_description.html metodo=_data parametro="int parties" %}
* **Runnable barrierAction**,  {% include w3api/param_description.html metodo=_data parametro="Runnable barrierAction" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CyclicBarrier](/Java/CyclicBarrier/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CyclicBarrier.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
