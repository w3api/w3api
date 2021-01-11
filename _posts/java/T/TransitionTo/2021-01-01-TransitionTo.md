---
title: TransitionTo
permalink: Java/TransitionTo
date: 2021-01-11
key: JavaJava.T.TransitionTo
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TransitionTo.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(FIELD) public @interface TransitionTo
~~~

## Ejemplo
~~~java
{{ site.data.Java.T.TransitionTo.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransitionTo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
