---
title: CompletionStage.thenCombine()
permalink: Java/CompletionStage/thenCombine
date: 2021-01-11
key: JavaJava.C.CompletionStage
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="thenCombine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U,V> CompletionStage<V> thenCombine(CompletionStage<? extends U> other, BiFunction<? super T,? super U,? extends V> fn)
~~~

## Parámetros
* **CompletionStage&lt;? extends U&gt; other**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStage<? extends U> other" %}
* **? super U**,  {% include w3api/param_description.html metodo=_dato parametro="? super U" %}
* **BiFunction&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super T" %}
* **? extends V&gt; fn**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> fn" %}

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
