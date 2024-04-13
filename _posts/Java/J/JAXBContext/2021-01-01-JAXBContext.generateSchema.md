---
title: JAXBContext.generateSchema()
permalink: /Java/JAXBContext/generateSchema/
date: 2021-01-11
key: Java.J.JAXBContext
category: Java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JAXBContext.metodos valor="generateSchema" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void generateSchema(SchemaOutputResolver outputResolver) throws IOException
~~~

## Parámetros
* **SchemaOutputResolver outputResolver**,  {% include w3api/param_description.html metodo=_dato parametro="SchemaOutputResolver outputResolver" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

## Clase Padre
[JAXBContext](/Java/JAXBContext/)

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
