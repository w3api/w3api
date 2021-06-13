---
title: CompletionStage.thenApply()
permalink: /Java/CompletionStage/thenApply/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="thenApply" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> CompletionStage<U> thenApply(Function<? super T,? extends U> fn)
~~~

## Parámetros
* **? extends U&gt; fn**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> fn" %}
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
