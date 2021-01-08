---
title: SchemaFactory.newSchema()
permalink: Java/SchemaFactory/newSchema
date: 2021-01-04
key: JavaJava.S.SchemaFactory
category: java
tags: ['java se', 'javax.xml.validation', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SchemaFactory.metodos valor="newSchema" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Schema newSchema() throws SAXException
public Schema newSchema(File schema) throws SAXException
public Schema newSchema(URL schema) throws SAXException
public Schema newSchema(Source schema) throws SAXException
public abstract Schema newSchema(Source[] schemas) throws SAXException
~~~

## Parámetros
* **URL schema**,  {% include w3api/param_description.html metodo=_data parametro="URL schema" %}
* **Source schema**,  {% include w3api/param_description.html metodo=_data parametro="Source schema" %}
* **File schema**,  {% include w3api/param_description.html metodo=_data parametro="File schema" %}
* **Source[] schemas**,  {% include w3api/param_description.html metodo=_data parametro="Source[] schemas" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/), [SAXException](/Java/SAXException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SchemaFactory](/Java/SchemaFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SchemaFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
