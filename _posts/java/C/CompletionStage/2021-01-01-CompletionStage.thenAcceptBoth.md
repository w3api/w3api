---
title: CompletionStage.thenAcceptBoth()
permalink: Java/CompletionStage/thenAcceptBoth
date: 2021-01-11
key: JavaJava.C.CompletionStage
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="thenAcceptBoth" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> CompletionStage<Void> thenAcceptBoth(CompletionStage<? extends U> other, BiConsumer<? super T,? super U> action)
~~~

## Parámetros
* **CompletionStage&lt;? extends U&gt; other**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStage<? extends U> other" %}
* **? super U&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="? super U> action" %}
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
