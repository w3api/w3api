---
title: Validator.setFeature()
permalink: Java/Validator-javax-xml-validation/setFeature
date: 2021-01-04
key: JavaJava.V.Validator-javax-xml-validation
category: java
tags: ['java se', 'javax.xml.validation', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.Validator-javax-xml-validation.metodos valor="setFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFeature(String name, boolean value) throws SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **boolean value**,  {% include w3api/param_description.html metodo=_data parametro="boolean value" %}

## Excepciones
[SAXNotSupportedException](/Java/SAXNotSupportedException/), [NullPointerException](/Java/NullPointerException/), [SAXNotRecognizedException](/Java/SAXNotRecognizedException/)

## Clase Padre
[Validator](/Java/Validator-javax-xml-validation/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.Validator-javax-xml-validation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
