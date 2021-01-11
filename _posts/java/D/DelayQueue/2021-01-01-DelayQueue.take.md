---
title: DelayQueue.take()
permalink: Java/DelayQueue/take
date: 2021-01-11
key: JavaJava.D.DelayQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DelayQueue.metodos valor="take" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public E take() throws InterruptedException
~~~

## Excepciones
[InterruptedException](/Java/InterruptedException/)

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
