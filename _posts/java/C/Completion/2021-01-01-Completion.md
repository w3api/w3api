---
title: Completion
permalink: /Java/Completion/
date: 2021-01-11
key: Java.C.Completion
category: Java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Completion.description }}

## Sintaxis
~~~java
public interface Completion
~~~

## Métodos
* [getMessage()](/Java/Completion/getMessage)
* [getValue()](/Java/Completion/getValue)

## Ejemplo
~~~java
{{ site.data.Java.C.Completion.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Completion.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
