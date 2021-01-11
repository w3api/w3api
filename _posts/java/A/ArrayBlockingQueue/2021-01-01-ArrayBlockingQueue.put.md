---
title: ArrayBlockingQueue.put()
permalink: Java/ArrayBlockingQueue/put
date: 2021-01-11
key: JavaJava.A.ArrayBlockingQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayBlockingQueue.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void put(E e) throws InterruptedException
~~~

## Parámetros
* **E e**,  {% include w3api/param_description.html metodo=_dato parametro="E e" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ArrayBlockingQueue](/Java/ArrayBlockingQueue/)

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
