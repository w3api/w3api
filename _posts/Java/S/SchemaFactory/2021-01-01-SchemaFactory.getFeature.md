---
title: SchemaFactory.getFeature()
permalink: /Java/SchemaFactory/getFeature/
date: 2021-01-11
key: Java.S.SchemaFactory
category: Java
tags: ['java se', 'javax.xml.validation', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SchemaFactory.metodos valor="getFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean getFeature(String name) throws SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[SAXNotRecognizedException](/Java/SAXNotRecognizedException/), [SAXNotSupportedException](/Java/SAXNotSupportedException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SchemaFactory](/Java/SchemaFactory/)

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
