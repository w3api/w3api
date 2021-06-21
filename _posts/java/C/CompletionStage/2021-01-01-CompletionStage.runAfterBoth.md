---
title: CompletionStage.runAfterBoth()
permalink: /Java/CompletionStage/runAfterBoth/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="runAfterBoth" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletionStage<Void> runAfterBoth(CompletionStage<?> other, Runnable action)
~~~

## Parámetros
* **CompletionStage&lt;?&gt; other**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStage<?> other" %}
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
