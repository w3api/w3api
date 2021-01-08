---
title: CompletionStage.runAfterBothAsync()
permalink: Java/CompletionStage/runAfterBothAsync
date: 2021-01-04
key: JavaJava.C.CompletionStage
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="runAfterBothAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletionStage<Void> runAfterBothAsync(CompletionStage<?> other, Runnable action)
CompletionStage<Void> runAfterBothAsync(CompletionStage<?> other, Runnable action, Executor executor)
~~~

## Parámetros
* **Executor executor**,  {% include w3api/param_description.html metodo=_data parametro="Executor executor" %}
* **Runnable action**,  {% include w3api/param_description.html metodo=_data parametro="Runnable action" %}
* **CompletionStage&lt;?&gt; other**,  {% include w3api/param_description.html metodo=_data parametro="CompletionStage<?> other" %}

## Clase Padre
[CompletionStage](/Java/CompletionStage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompletionStage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
