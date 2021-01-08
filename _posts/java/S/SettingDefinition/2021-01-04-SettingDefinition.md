---
title: SettingDefinition
permalink: Java/SettingDefinition
date: 2021-01-04
key: JavaJava.S.SettingDefinition
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SettingDefinition.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(METHOD) public @interface SettingDefinition
~~~

## Ejemplo
~~~java
{{ site.data.Java.S.SettingDefinition.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SettingDefinition.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
