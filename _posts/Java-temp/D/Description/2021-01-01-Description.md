---
title: Description
permalink: /Java/Description/
date: 2021-01-11
key: Java.D.Description
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.Description.description }}

## Sintaxis
~~~java
@Target({TYPE,FIELD,METHOD}) @Retention(RUNTIME) public @interface Description
~~~

## Ejemplo
~~~java
{{ site.data.Java.D.Description.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.Description.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
