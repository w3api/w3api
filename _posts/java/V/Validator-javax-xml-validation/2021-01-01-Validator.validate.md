---
title: Validator.validate()
permalink: Java/Validator-javax-xml-validation/validate
date: 2021-01-11
key: JavaJava.V.Validator-javax-xml-validation
category: java
tags: ['java se', 'javax.xml.validation', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.Validator-javax-xml-validation.metodos valor="validate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void validate(Source source) throws SAXException, IOException
public abstract void validate(Source source, Result result) throws SAXException, IOException
~~~

## Parámetros
* **Source source**,  {% include w3api/param_description.html metodo=_dato parametro="Source source" %}
* **Result result**,  {% include w3api/param_description.html metodo=_dato parametro="Result result" %}

## Excepciones
[SAXException](/Java/SAXException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

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
