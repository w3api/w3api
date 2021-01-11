---
title: JAXBSource.JAXBSource()
permalink: Java/JAXBSource/JAXBSource
date: 2021-01-11
key: JavaJava.J.JAXBSource
category: java
tags: ['java se', 'javax.xml.bind.util', 'java.xml.bind', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JAXBSource.constructores valor="JAXBSource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JAXBSource(JAXBContext context, Object contentObject) throws JAXBException
public JAXBSource(Marshaller marshaller, Object contentObject) throws JAXBException
~~~

## Parámetros
* **Object contentObject**,  {% include w3api/param_description.html metodo=_dato parametro="Object contentObject" %}
* **JAXBContext context**,  {% include w3api/param_description.html metodo=_dato parametro="JAXBContext context" %}
* **Marshaller marshaller**,  {% include w3api/param_description.html metodo=_dato parametro="Marshaller marshaller" %}

## Excepciones
[JAXBException](/Java/JAXBException/)

## Clase Padre
[JAXBSource](/Java/JAXBSource/)

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
