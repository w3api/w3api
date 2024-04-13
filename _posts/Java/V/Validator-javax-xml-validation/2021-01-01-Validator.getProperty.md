---
title: Validator.getProperty()
permalink: /Java/Validator-javax-xml-validation/getProperty/
date: 2021-01-11
key: Java.V.Validator-javax-xml-validation
category: Java
tags: ['java se', 'javax.xml.validation', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.Validator-javax-xml-validation.metodos valor="getProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getProperty(String name) throws SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[SAXNotRecognizedException](/Java/SAXNotRecognizedException/), [SAXNotSupportedException](/Java/SAXNotSupportedException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Validator](/Java/Validator-javax-xml-validation/)

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
