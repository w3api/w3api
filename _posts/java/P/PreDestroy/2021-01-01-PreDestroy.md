---
title: PreDestroy
permalink: /Java/PreDestroy/
date: 2021-01-11
key: Java.P.PreDestroy
category: Java
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

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PreDestroy.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
