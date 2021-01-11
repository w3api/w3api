---
title: ConstructorParameters
permalink: Java/ConstructorParameters
date: 2021-01-11
key: JavaJava.C.ConstructorParameters
category: java
tags: ['java se', 'javax.management', 'java.management', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConstructorParameters.description }}

## Sintaxis
~~~java
@Documented @Target(CONSTRUCTOR) @Retention(RUNTIME) public @interface ConstructorParameters
~~~

## Ejemplo
~~~java
{{ site.data.Java.C.ConstructorParameters.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConstructorParameters.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
