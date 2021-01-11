---
title: PostConstruct
permalink: Java/PostConstruct
date: 2021-01-11
key: JavaJava.P.PostConstruct
category: java
tags: ['java se', 'javax.annotation', 'java.xml.ws.annotation', 'anotacion java', 'Java 1.6', 'Common Annotations Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PostConstruct.description }}

## Sintaxis
~~~java
@Documented @Retention(RUNTIME) @Target(METHOD) public @interface PostConstruct
~~~

## Ejemplo
~~~java
{{ site.data.Java.P.PostConstruct.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PostConstruct.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
