---
title: SupportedSourceVersion
permalink: Java/SupportedSourceVersion
date: 2021-01-11
key: JavaJava.S.SupportedSourceVersion
category: java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'anotacion java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SupportedSourceVersion.description }}

## Sintaxis
~~~java
@Documented @Target(TYPE) @Retention(RUNTIME) public @interface SupportedSourceVersion
~~~

## Ejemplo
~~~java
{{ site.data.Java.S.SupportedSourceVersion.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SupportedSourceVersion.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
