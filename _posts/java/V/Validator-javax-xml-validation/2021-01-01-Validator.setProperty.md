---
title: Validator.setProperty()
permalink: /Java/Validator-javax-xml-validation/setProperty/
date: 2021-01-11
key: Java.V.Validator-javax-xml-validation
category: Java
tags: ['java se', 'javax.xml.validation', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.Validator-javax-xml-validation.metodos valor="setProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setProperty(String name, Object object) throws SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Object object**,  {% include w3api/param_description.html metodo=_dato parametro="Object object" %}

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
