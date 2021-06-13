---
title: XMLStreamWriter.getProperty()
permalink: /Java/XMLStreamWriter/getProperty/
date: 2021-01-11
key: Java.X.XMLStreamWriter
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamWriter.metodos valor="getProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getProperty(String name) throws IllegalArgumentException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XMLStreamWriter](/Java/XMLStreamWriter/)

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
