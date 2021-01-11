---
title: MetadataDefinition
permalink: Java/MetadataDefinition
date: 2021-01-11
key: JavaJava.M.MetadataDefinition
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MetadataDefinition.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(TYPE) public @interface MetadataDefinition
~~~

## Ejemplo
~~~java
{{ site.data.Java.M.MetadataDefinition.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MetadataDefinition.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
