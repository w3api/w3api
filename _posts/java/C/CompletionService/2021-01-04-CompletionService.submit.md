---
title: CompletionService.submit()
permalink: Java/CompletionService/submit
date: 2021-01-04
key: JavaJava.C.CompletionService
category: java
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
* **Runnable task**,  {% include w3api/param_description.html metodo=_data parametro="Runnable task" %}
* **Callable&lt;V&gt; task**,  {% include w3api/param_description.html metodo=_data parametro="Callable<V> task" %}
* **V result**,  {% include w3api/param_description.html metodo=_data parametro="V result" %}

## Excepciones
[RejectedExecutionException](/Java/RejectedExecutionException/), [NullPointerException](/Java/NullPointerException/)

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
