---
title: DescriptorKey
permalink: Java/DescriptorKey
date: 2021-01-04
key: JavaJava.D.DescriptorKey
category: java
tags: ['java se', 'javax.management', 'java.management', 'anotacion java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DescriptorKey.description }}

## Sintaxis
~~~java
@Documented @Retention(RUNTIME) @Target(METHOD) public @interface DescriptorKey
~~~

## Ejemplo
~~~java
{{ site.data.Java.D.DescriptorKey.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DescriptorKey.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
