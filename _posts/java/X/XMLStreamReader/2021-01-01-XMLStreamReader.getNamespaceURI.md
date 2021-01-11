---
title: XMLStreamReader.getNamespaceURI()
permalink: Java/XMLStreamReader/getNamespaceURI
date: 2021-01-11
key: JavaJava.X.XMLStreamReader
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamReader.metodos valor="getNamespaceURI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getNamespaceURI()
String getNamespaceURI(int index)
String getNamespaceURI(String prefix)
~~~

## Parámetros
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[XMLStreamReader](/Java/XMLStreamReader/)

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
