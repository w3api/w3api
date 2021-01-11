---
title: Validator.getProperty()
permalink: Java/Validator-javax-xml-bind/getProperty
date: 2021-01-11
key: JavaJava.V.Validator-javax-xml-bind
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.Validator-javax-xml-bind.metodos valor="getProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getProperty(String name) throws PropertyException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [PropertyException](/Java/PropertyException/)

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
