---
title: Validator.validate()
permalink: Java/Validator-javax-xml-bind/validate
date: 2021-01-11
key: JavaJava.V.Validator-javax-xml-bind
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.Validator-javax-xml-bind.metodos valor="validate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean validate(Object subrootObj) throws JAXBException
~~~

## Parámetros
* **Object subrootObj**,  {% include w3api/param_description.html metodo=_dato parametro="Object subrootObj" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [JAXBException](/Java/JAXBException/), [ValidationException](/Java/ValidationException/)

## Clase Padre
[Validator](/Java/Validator-javax-xml-bind/)

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
