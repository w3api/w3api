---
title: CompletionService.poll()
permalink: Java/CompletionService/poll
date: 2021-01-04
key: JavaJava.C.CompletionService
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionService.metodos valor="poll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Future<V> poll()
Future<V> poll(long timeout, TimeUnit unit) throws InterruptedException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[CompletionService](/Java/CompletionService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompletionService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
