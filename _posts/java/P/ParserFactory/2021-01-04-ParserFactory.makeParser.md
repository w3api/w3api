---
title: ParserFactory.makeParser()
permalink: Java/ParserFactory/makeParser
date: 2021-01-04
key: JavaJava.P.ParserFactory
category: java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ParserFactory.metodos valor="makeParser" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Parser makeParser() throws ClassNotFoundException, IllegalAccessException, InstantiationException, NullPointerException, ClassCastException
public static Parser makeParser(String className) throws ClassNotFoundException, IllegalAccessException, InstantiationException, ClassCastException
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}

## Excepciones
[IllegalAccessException](/Java/IllegalAccessException/), [InstantiationException](/Java/InstantiationException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [ClassNotFoundException](/Java/ClassNotFoundException/)

## Clase Padre
[ParserFactory](/Java/ParserFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ParserFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
