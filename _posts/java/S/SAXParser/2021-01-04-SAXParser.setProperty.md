---
title: SAXParser.setProperty()
permalink: Java/SAXParser/setProperty
date: 2021-01-04
key: JavaJava.S.SAXParser
category: java
tags: ['java se', 'javax.xml.parsers', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SAXParser.metodos valor="setProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setProperty(String name, Object value) throws SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

## Excepciones
[SAXNotSupportedException](/Java/SAXNotSupportedException/), [SAXNotRecognizedException](/Java/SAXNotRecognizedException/)

## Clase Padre
[SAXParser](/Java/SAXParser/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SAXParser.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
