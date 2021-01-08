---
title: JAXBResult.JAXBResult()
permalink: Java/JAXBResult/JAXBResult
date: 2021-01-04
key: JavaJava.J.JAXBResult
category: java
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
* **JAXBContext context**,  {% include w3api/param_description.html metodo=_data parametro="JAXBContext context" %}
* **Unmarshaller _unmarshaller**,  {% include w3api/param_description.html metodo=_data parametro="Unmarshaller _unmarshaller" %}

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
{%- for _ldc in site.data.Java.J.JAXBResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
