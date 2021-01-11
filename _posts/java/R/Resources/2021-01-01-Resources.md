---
title: Resources
permalink: Java/Resources
date: 2021-01-11
key: JavaJava.R.Resources
category: java
tags: ['java se', 'javax.annotation', 'java.xml.ws.annotation', 'anotacion java', 'Java 1.6', 'Common Annotations Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.Resources.description }}

## Sintaxis
~~~java
@Documented @Retention(RUNTIME) @Target(TYPE) public @interface Resources
~~~

## Ejemplo
~~~java
{{ site.data.Java.R.Resources.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.Resources.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
