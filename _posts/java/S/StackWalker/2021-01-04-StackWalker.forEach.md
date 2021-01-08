---
title: StackWalker.forEach()
permalink: Java/StackWalker/forEach
date: 2021-01-04
key: JavaJava.S.StackWalker
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackWalker.metodos valor="forEach" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void forEach(Consumer<? super StackWalker.StackFrame> action)
~~~

## Parámetros
* **Consumer&lt;? super StackWalker.StackFrame&gt; action**,  {% include w3api/param_description.html metodo=_data parametro="Consumer<? super StackWalker.StackFrame> action" %}

## Clase Padre
[StackWalker](/Java/StackWalker/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StackWalker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
