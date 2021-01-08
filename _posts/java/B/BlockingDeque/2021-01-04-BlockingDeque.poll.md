---
title: BlockingDeque.poll()
permalink: Java/BlockingDeque/poll
date: 2021-01-04
key: JavaJava.B.BlockingDeque
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BlockingDeque.metodos valor="poll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
E poll()
E poll(long timeout, TimeUnit unit) throws InterruptedException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[BlockingDeque](/Java/BlockingDeque/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BlockingDeque.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
