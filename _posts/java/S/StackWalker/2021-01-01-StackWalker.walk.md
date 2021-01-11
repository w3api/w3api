---
title: StackWalker.walk()
permalink: Java/StackWalker/walk
date: 2021-01-11
key: JavaJava.S.StackWalker
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackWalker.metodos valor="walk" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> T walk(Function<? super Stream<StackWalker.StackFrame>,? extends T> function)
~~~

## Parámetros
* **? extends T&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="? extends T> function" %}
* **Function&lt;? super Stream&lt;StackWalker.StackFrame&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super Stream<StackWalker.StackFrame>" %}

## Clase Padre
[StackWalker](/Java/StackWalker/)

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
