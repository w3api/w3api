---
title: CompletionStage.applyToEither()
permalink: /Java/CompletionStage/applyToEither/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="applyToEither" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> CompletionStage<U> applyToEither(CompletionStage<? extends T> other, Function<? super T,U> fn)
~~~

## Parámetros
* **U&gt; fn**,  {% include w3api/param_description.html metodo=_dato parametro="U> fn" %}
* **CompletionStage&lt;? extends T&gt; other**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStage<? extends T> other" %}
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super T" %}

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
