---
title: CountDownLatch.CountDownLatch()
permalink: Java/CountDownLatch/CountDownLatch
date: 2021-01-11
key: JavaJava.C.CountDownLatch
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CountDownLatch.constructores valor="CountDownLatch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CountDownLatch(int count)
~~~

## Parámetros
* **int count**,  {% include w3api/param_description.html metodo=_dato parametro="int count" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CountDownLatch](/Java/CountDownLatch/)

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
