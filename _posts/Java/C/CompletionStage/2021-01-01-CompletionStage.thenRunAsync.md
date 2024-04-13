---
title: CompletionStage.thenRunAsync()
permalink: /Java/CompletionStage/thenRunAsync/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="thenRunAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletionStage<Void> thenRunAsync(Runnable action)
CompletionStage<Void> thenRunAsync(Runnable action, Executor executor)
~~~

## Parámetros
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}
* **Runnable action**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable action" %}

## Clase Padre
[CompletionStage](/Java/CompletionStage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
