---
title: SupportedOptions
permalink: Java/SupportedOptions
date: 2021-01-11
key: JavaJava.S.SupportedOptions
category: java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'anotacion java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SupportedOptions.description }}

## Sintaxis
~~~java
@Documented @Target(TYPE) @Retention(RUNTIME) public @interface SupportedOptions
~~~

## Ejemplo
~~~java
{{ site.data.Java.S.SupportedOptions.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SupportedOptions.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
