---
title: CompletionStage.thenAcceptBothAsync()
permalink: /Java/CompletionStage/thenAcceptBothAsync/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="thenAcceptBothAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> CompletionStage<Void> thenAcceptBothAsync(CompletionStage<? extends U> other, BiConsumer<? super T,? super U> action)
<U> CompletionStage<Void> thenAcceptBothAsync(CompletionStage<? extends U> other, BiConsumer<? super T,? super U> action, Executor executor)
~~~

## Parámetros
* **CompletionStage&lt;? extends U&gt; other**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStage<? extends U> other" %}
* **? super U&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="? super U> action" %}
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}
* **BiConsumer&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="BiConsumer<? super T" %}

## Clase Padre
[CompletionStage](/Java/CompletionStage/)

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
