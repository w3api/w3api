---
title: ConfigurationInfo.from()
permalink: Java/ConfigurationInfo/from
date: 2021-01-11
key: JavaJava.C.ConfigurationInfo
category: java
tags: ['java se', 'jdk.management.jfr', 'jdk.management.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConfigurationInfo.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ConfigurationInfo from(CompositeData cd)
~~~

## Parámetros
* **CompositeData cd**,  {% include w3api/param_description.html metodo=_dato parametro="CompositeData cd" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ConfigurationInfo](/Java/ConfigurationInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
