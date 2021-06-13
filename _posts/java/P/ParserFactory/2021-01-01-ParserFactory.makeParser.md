---
title: ParserFactory.makeParser()
permalink: /Java/ParserFactory/makeParser/
date: 2021-01-11
key: Java.P.ParserFactory
category: Java
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
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [ClassNotFoundException](/Java/ClassNotFoundException/), [IllegalAccessException](/Java/IllegalAccessException/), [InstantiationException](/Java/InstantiationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ParserFactory](/Java/ParserFactory/)

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
