---
title: Configuration.getConfiguration()
permalink: /Java/Configuration-jdk-jfr/getConfiguration/
date: 2021-01-11
key: Java.C.Configuration-jdk-jfr
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Configuration-jdk-jfr.metodos valor="getConfiguration" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Configuration getConfiguration(String name) throws IOException, ParseException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[ParseException](/Java/ParseException/), [IOException](/Java/IOException/)

## Clase Padre
[Configuration](/Java/Configuration-jdk-jfr/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
