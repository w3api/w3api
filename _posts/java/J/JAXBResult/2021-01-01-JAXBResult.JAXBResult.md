---
title: JAXBResult.JAXBResult()
permalink: /Java/JAXBResult/JAXBResult/
date: 2021-01-11
key: Java.J.JAXBResult
category: Java
tags: ['java se', 'javax.xml.bind.util', 'java.xml.bind', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JAXBResult.constructores valor="JAXBResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JAXBResult(JAXBContext context) throws JAXBException
public JAXBResult(Unmarshaller _unmarshaller) throws JAXBException
~~~

## Parámetros
* **Unmarshaller _unmarshaller**,  {% include w3api/param_description.html metodo=_dato parametro="Unmarshaller _unmarshaller" %}
* **JAXBContext context**,  {% include w3api/param_description.html metodo=_dato parametro="JAXBContext context" %}

## Excepciones
[JAXBException](/Java/JAXBException/)

## Clase Padre
[JAXBResult](/Java/JAXBResult/)

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
