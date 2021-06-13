---
title: CompletionService.submit()
permalink: /Java/CompletionService/submit/
date: 2021-01-11
key: Java.C.CompletionService
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionService.metodos valor="submit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Future<V> submit(Runnable task, V result)
Future<V> submit(Callable<V> task)
~~~

## Parámetros
* **V result**,  {% include w3api/param_description.html metodo=_dato parametro="V result" %}
* **Callable&lt;V&gt; task**,  {% include w3api/param_description.html metodo=_dato parametro="Callable<V> task" %}
* **Runnable task**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable task" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [RejectedExecutionException](/Java/RejectedExecutionException/)

## Clase Padre
[CompletionService](/Java/CompletionService/)

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
