---
title: ValidatorHandler.setFeature()
permalink: /Java/ValidatorHandler/setFeature/
date: 2021-01-11
key: Java.V.ValidatorHandler
category: Java
tags: ['java se', 'javax.xml.validation', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValidatorHandler.metodos valor="setFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFeature(String name, boolean value) throws SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **boolean value**,  {% include w3api/param_description.html metodo=_dato parametro="boolean value" %}

## Excepciones
[SAXNotRecognizedException](/Java/SAXNotRecognizedException/), [SAXNotSupportedException](/Java/SAXNotSupportedException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ValidatorHandler](/Java/ValidatorHandler/)

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
