---
title: CompletionStage.handle()
permalink: Java/CompletionStage/handle
date: 2021-01-04
key: JavaJava.C.CompletionStage
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="handle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> CompletionStage<U> handle(BiFunction<? super T,Throwable,? extends U> fn)
~~~

## Parámetros
* **Throwable**,  {% include w3api/param_description.html metodo=_data parametro="Throwable" %}
* **BiFunction&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<? super T" %}
* **? extends U&gt; fn**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> fn" %}

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
