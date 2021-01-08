---
title: XMLStreamWriter.setDefaultNamespace()
permalink: Java/XMLStreamWriter/setDefaultNamespace
date: 2021-01-04
key: JavaJava.X.XMLStreamWriter
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamWriter.metodos valor="setDefaultNamespace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setDefaultNamespace(String uri) throws XMLStreamException
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLStreamWriter](/Java/XMLStreamWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLStreamWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
