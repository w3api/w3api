---
title: Configuration.create()
permalink: Java/Configuration-jdk-jfr/create
date: 2021-01-04
key: JavaJava.C.Configuration-jdk-jfr
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Configuration-jdk-jfr.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Configuration create(Reader reader) throws IOException, ParseException
public static Configuration create(Path path) throws IOException, ParseException
~~~

## Parámetros
* **Path path**,  {% include w3api/param_description.html metodo=_data parametro="Path path" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_data parametro="Reader reader" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [ParseException](/Java/ParseException/), [IOException](/Java/IOException/)

## Clase Padre
[Configuration](/Java/Configuration-jdk-jfr/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Configuration-jdk-jfr.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
