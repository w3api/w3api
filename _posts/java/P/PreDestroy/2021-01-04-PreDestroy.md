---
title: PreDestroy
permalink: Java/PreDestroy
date: 2021-01-04
key: JavaJava.P.PreDestroy
category: java
tags: ['java se', 'javax.annotation', 'java.xml.ws.annotation', 'anotacion java', 'Java 1.6', 'Common Annotations Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PreDestroy.description }}

## Sintaxis
~~~java
@Documented @Retention(RUNTIME) @Target(METHOD) public @interface PreDestroy
~~~

## Ejemplo
~~~java
{{ site.data.Java.P.PreDestroy.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PreDestroy.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
