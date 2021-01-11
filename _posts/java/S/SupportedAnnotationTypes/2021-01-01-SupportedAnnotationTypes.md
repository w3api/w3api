---
title: SupportedAnnotationTypes
permalink: Java/SupportedAnnotationTypes
date: 2021-01-11
key: JavaJava.S.SupportedAnnotationTypes
category: java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'anotacion java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SupportedAnnotationTypes.description }}

## Sintaxis
~~~java
@Documented @Target(TYPE) @Retention(RUNTIME) public @interface SupportedAnnotationTypes
~~~

## Ejemplo
~~~java
{{ site.data.Java.S.SupportedAnnotationTypes.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SupportedAnnotationTypes.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
