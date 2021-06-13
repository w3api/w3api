---
title: SynchronousQueue.take()
permalink: Java/SynchronousQueue/take
date: 2021-01-11
key: JavaJava.S.SynchronousQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SynchronousQueue.metodos valor="take" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public E take() throws InterruptedException
~~~

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[SynchronousQueue](/Java/SynchronousQueue/)

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