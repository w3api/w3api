---
title: CompletionStage.thenCombineAsync()
permalink: Java/CompletionStage/thenCombineAsync
date: 2021-01-04
key: JavaJava.C.CompletionStage
category: java
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
* **Executor executor**,  {% include w3api/param_description.html metodo=_data parametro="Executor executor" %}
* **CompletionStage&lt;? extends U&gt; other**,  {% include w3api/param_description.html metodo=_data parametro="CompletionStage<? extends U> other" %}
* **? super U**,  {% include w3api/param_description.html metodo=_data parametro="? super U" %}
* **? extends V&gt; fn**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> fn" %}
* **BiFunction&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<? super T" %}

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
