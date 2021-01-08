---
title: CompletionStage.thenRun()
permalink: Java/CompletionStage/thenRun
date: 2021-01-04
key: JavaJava.C.CompletionStage
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="thenRun" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletionStage<Void> thenRun(Runnable action)
~~~

## Parámetros
* **Runnable action**,  {% include w3api/param_description.html metodo=_data parametro="Runnable action" %}

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
