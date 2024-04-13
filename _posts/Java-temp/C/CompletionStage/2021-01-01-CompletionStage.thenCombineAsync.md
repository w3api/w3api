---
title: CompletionStage.thenCombineAsync()
permalink: /Java/CompletionStage/thenCombineAsync/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="thenCombineAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U,V> CompletionStage<V> thenCombineAsync(CompletionStage<? extends U> other, BiFunction<? super T,? super U,? extends V> fn)
<U,V> CompletionStage<V> thenCombineAsync(CompletionStage<? extends U> other, BiFunction<? super T,? super U,? extends V> fn, Executor executor)
~~~

## Parámetros
* **? extends V&gt; fn**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> fn" %}
* **CompletionStage&lt;? extends U&gt; other**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStage<? extends U> other" %}
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}
* **? super U**,  {% include w3api/param_description.html metodo=_dato parametro="? super U" %}
* **BiFunction&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super T" %}

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
